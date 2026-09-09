"""Tests for the read-only source-tree navigator.

Two things matter here and neither is about happy-path output:

1. **Injection.** Everything reaching a git subprocess is attacker-adjacent —
   a repo URL or a path could carry a leading dash that git reads as an option
   (``--upload-pack=``). The validators are the guard.
2. **Cost.** ``grep_repo`` must refuse an unscoped search. On a blobless clone
   that would lazily fault in every blob in the repository.

Git itself is mocked; one integration test runs against a real clone and is
opt-in via RUN_GIT_TESTS because it needs network and hundreds of MB.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

from agents.tools import source_repo as sr
from agents.tools.source_repo import SourceRepo, load_source_repos


@pytest.fixture
def repo(tmp_path: Path) -> SourceRepo:
    return SourceRepo(
        project="gcc",
        repo_url="https://github.com/gcc-mirror/gcc.git",
        cache_dir=tmp_path,
    )


SHA = "a" * 40


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "url",
    [
        "--upload-pack=/bin/sh",       # git option, not a URL
        "-ext::sh -c whoami",
        "file:///etc/passwd",          # scheme not on the allowlist
        "",
    ],
)
def test_rejects_unsafe_repo_url(url: str, tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        SourceRepo(project="x", repo_url=url, cache_dir=tmp_path)


@pytest.mark.parametrize("branch", ["--upload-pack=x", "a b", "x" * 200, ""])
def test_rejects_unsafe_branch(branch: str, tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        SourceRepo(
            project="x",
            repo_url="https://example.com/r.git",
            branch=branch,
            cache_dir=tmp_path,
        )


@pytest.mark.parametrize(
    "sha", ["", "xyz", "abc", "g" * 40, "a" * 41, "--output=/tmp/x"]
)
def test_rejects_unsafe_sha(sha: str) -> None:
    with pytest.raises(ValueError):
        sr.validate_sha(sha)


@pytest.mark.parametrize("sha", ["a1b2c3d", SHA, "A1B2C3D4"])
def test_accepts_valid_sha(sha: str) -> None:
    sr.validate_sha(sha)  # does not raise


@pytest.mark.parametrize(
    "path",
    [
        "--output=/tmp/pwned",   # leading dash: git would read it as an option
        "-rf",
        "../../etc/passwd",
        "gcc/../../etc/passwd",
        "",
    ],
)
def test_rejects_unsafe_pathspec(path: str) -> None:
    with pytest.raises(ValueError):
        sr.validate_pathspec(path)


@pytest.mark.parametrize(
    "path", ["gcc", "gcc/ipa-sra.cc", "gcc/config/aarch64/", "gcc/*.cc"]
)
def test_accepts_valid_pathspec(path: str) -> None:
    sr.validate_pathspec(path)  # does not raise


# ---------------------------------------------------------------------------
# The cost guard
# ---------------------------------------------------------------------------

def test_grep_refuses_unscoped_search(repo: SourceRepo, monkeypatch) -> None:
    """An unscoped grep on a blobless clone would fetch every blob in the repo."""
    def _boom(*a, **kw):
        raise AssertionError("git must not run for an unscoped grep")

    monkeypatch.setattr(repo, "_git", _boom)
    out = repo.grep_repo(SHA, "pattern", [])
    assert "not permitted" in out
    assert "at least one path" in out


def test_grep_rejects_empty_pattern(repo: SourceRepo, monkeypatch) -> None:
    monkeypatch.setattr(repo, "_git", lambda *a, **kw: "")
    assert "non-empty pattern" in repo.grep_repo(SHA, "   ", ["gcc/"])


def test_grep_validates_paths(repo: SourceRepo, monkeypatch) -> None:
    monkeypatch.setattr(repo, "_git", lambda *a, **kw: "")
    with pytest.raises(ValueError):
        repo.grep_repo(SHA, "x", ["--output=/tmp/pwned"])


def test_grep_no_match_is_an_answer_not_an_error(
    repo: SourceRepo, monkeypatch
) -> None:
    """git grep exits 1 when nothing matched — that is a result, not a fault."""
    def _fail(*a, **kw):
        raise subprocess.CalledProcessError(1, ["git", "grep"])

    monkeypatch.setattr(repo, "_git", _fail)
    out = repo.grep_repo(SHA, "nope", ["gcc/"])
    assert "No matches" in out
    assert "error" not in out.lower()


def test_grep_strips_rev_prefix(repo: SourceRepo, monkeypatch) -> None:
    """`git grep <rev>` prefixes every hit with '<rev>:' — noise for a reader."""
    monkeypatch.setattr(
        repo, "_git", lambda *a, **kw: f"{SHA}:gcc/ipa-sra.cc:42:  hit\n"
    )
    assert repo.grep_repo(SHA, "hit", ["gcc/"]) == "gcc/ipa-sra.cc:42:  hit"


# ---------------------------------------------------------------------------
# Output caps
# ---------------------------------------------------------------------------

def test_output_is_capped(repo: SourceRepo, monkeypatch) -> None:
    """Content is capped at MAX_OUTPUT_BYTES; the marker is appended on top."""
    monkeypatch.setattr(repo, "_git", lambda *a, **kw: "x" * 100_000)
    out = repo.show_commit(SHA)
    marker_bytes = len(sr._TRUNCATION_MARKER.encode())
    assert len(out.encode()) <= sr.MAX_OUTPUT_BYTES + marker_bytes
    assert out.endswith(sr._TRUNCATION_MARKER)


def test_read_file_is_paged_and_numbered(repo: SourceRepo, monkeypatch) -> None:
    body = "\n".join(f"line{n}" for n in range(1, 1001))
    monkeypatch.setattr(repo, "_git", lambda *a, **kw: body)

    out = repo.read_file(SHA, "gcc/ipa-sra.cc", 10, 12)
    assert "lines 10-12 of 1000" in out
    assert "    10  line10" in out
    assert "line13" not in out


def test_read_file_caps_range_length(repo: SourceRepo, monkeypatch) -> None:
    """A caller asking for the whole file gets a window, not 40k lines."""
    body = "\n".join(f"line{n}" for n in range(1, 5001))
    monkeypatch.setattr(repo, "_git", lambda *a, **kw: body)
    out = repo.read_file(SHA, "gcc/big.cc", 1, 5000)
    assert f"lines 1-{sr.MAX_READ_LINES} of 5000" in out


def test_read_file_reports_missing_path(repo: SourceRepo, monkeypatch) -> None:
    def _fail(*a, **kw):
        raise subprocess.CalledProcessError(128, ["git", "show"])

    monkeypatch.setattr(repo, "_git", _fail)
    out = repo.read_file(SHA, "gcc/nope.cc")
    # The '[error]' prefix is load-bearing: _drop_unread_code_refs keys on it
    # to remove fabricated paths from a lesson's code tour.
    assert out.startswith("[error]")


def test_read_file_past_end(repo: SourceRepo, monkeypatch) -> None:
    monkeypatch.setattr(repo, "_git", lambda *a, **kw: "one\ntwo\n")
    assert "past the end" in repo.read_file(SHA, "gcc/x.cc", 900)


# ---------------------------------------------------------------------------
# resolve / changed_dirs
# ---------------------------------------------------------------------------

def test_resolve_false_for_missing_sha(repo: SourceRepo, monkeypatch) -> None:
    """Mirror lag is routine — a miss must be False, never an exception."""
    def _fail(*a, **kw):
        raise subprocess.CalledProcessError(1, ["git", "cat-file"])

    monkeypatch.setattr(repo, "_git", _fail)
    assert repo.resolve(SHA) is False


def test_resolve_false_for_malformed_sha(repo: SourceRepo) -> None:
    assert repo.resolve("not-a-sha") is False


def test_changed_dirs_dedups_preserving_order(
    repo: SourceRepo, monkeypatch
) -> None:
    monkeypatch.setattr(
        repo,
        "_git",
        lambda *a, **kw: "gcc/cobol/genapi.cc\ngcc/cobol/util.cc\ngcc/testsuite/x.c\n",
    )
    assert repo.changed_dirs(SHA) == ["gcc/cobol", "gcc/testsuite"]


def test_changed_paths_empty_on_git_failure(repo: SourceRepo, monkeypatch) -> None:
    def _fail(*a, **kw):
        raise subprocess.CalledProcessError(128, ["git", "diff-tree"])

    monkeypatch.setattr(repo, "_git", _fail)
    assert repo.changed_paths(SHA) == []


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

def test_load_source_repos(tmp_path: Path) -> None:
    repos = load_source_repos(
        {
            "source_repos": {
                "gcc": {"url": "https://github.com/gcc-mirror/gcc.git"},
                "binutils": {
                    "url": "https://github.com/bminor/binutils-gdb.git",
                    "branch": "master",
                },
            }
        },
        cache_dir=tmp_path,
    )
    assert set(repos) == {"gcc", "binutils"}
    assert repos["gcc"].path.name == "gcc.git"


def test_load_source_repos_skips_invalid_entries(tmp_path: Path) -> None:
    """One bad entry must not take the other project's lesson down with it."""
    repos = load_source_repos(
        {
            "source_repos": {
                "bad_url": {"url": "--upload-pack=/bin/sh"},
                "no_url": {"branch": "master"},
                "good": {"url": "https://example.com/r.git"},
            }
        },
        cache_dir=tmp_path,
    )
    assert set(repos) == {"good"}


def test_load_source_repos_absent_block() -> None:
    assert load_source_repos({}) == {}


# ---------------------------------------------------------------------------
# ensure(): missing vs stale
# ---------------------------------------------------------------------------
#
# The distinction is the whole point. An unreachable mirror must cost freshness,
# not the article: the clone on disk still holds the project's entire history up
# to the last successful fetch. Only a clone that is absent — or present but
# unreadable — is actually fatal.

def _fake_bare_clone(path: Path) -> None:
    """A directory that is genuinely a git repo, cheaply."""
    path.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "init", "--bare", "--quiet", str(path)],
        check=True,
        capture_output=True,
    )


def test_fetch_failure_leaves_a_usable_stale_clone(
    repo: SourceRepo, monkeypatch
) -> None:
    _fake_bare_clone(repo.path)

    def _git(args, cwd=...):
        if args[0] == "fetch":
            raise subprocess.CalledProcessError(128, "git fetch")
        return ""

    monkeypatch.setattr(repo, "_git", _git)

    repo.ensure()   # must NOT raise — there is a readable repo right here

    assert repo.is_stale is True
    assert repo.last_fetch_error


def test_successful_fetch_is_not_stale(repo: SourceRepo, monkeypatch) -> None:
    _fake_bare_clone(repo.path)
    monkeypatch.setattr(repo, "_git", lambda *a, **kw: "")

    repo.ensure()

    assert repo.is_stale is False
    assert repo.last_fetch_error is None


def test_corrupt_clone_is_discarded_and_recloned(
    repo: SourceRepo, monkeypatch
) -> None:
    """A directory that merely *looks* like a clone must not be trusted.

    An interrupted clone answers every read with an error. Serving that as
    "cached state" would hand the model a dossier of `[error]` strings and
    produce a confidently wrong article.
    """
    repo.path.mkdir(parents=True)
    (repo.path / "junk").write_text("not a git repo")

    calls: list[list[str]] = []

    def _git(args, cwd=...):
        calls.append(args)
        if args[0] == "rev-parse":
            raise subprocess.CalledProcessError(128, "git rev-parse")
        return ""

    monkeypatch.setattr(repo, "_git", _git)

    repo.ensure()

    assert any(a[0] == "clone" for a in calls), "should have re-cloned"
    assert not any(a[0] == "fetch" for a in calls), "must not fetch a broken repo"
    assert not (repo.path / "junk").exists(), "stale directory should be gone"


def test_missing_clone_that_cannot_be_cloned_raises(
    repo: SourceRepo, monkeypatch
) -> None:
    """No clone and no network is the one genuinely fatal case."""

    def _git(args, cwd=...):
        raise subprocess.CalledProcessError(128, "git clone")

    monkeypatch.setattr(repo, "_git", _git)

    with pytest.raises(sr.SourceRepoError):
        repo.ensure()


# ---------------------------------------------------------------------------
# Integration (opt-in: needs network and ~640 MB)
# ---------------------------------------------------------------------------

@pytest.mark.skipif(
    not os.environ.get("RUN_GIT_TESTS"),
    reason="set RUN_GIT_TESTS=1 to clone a real repo",
)
def test_real_clone_reads_a_file(tmp_path: Path) -> None:
    repo = SourceRepo(
        project="gcc",
        repo_url="https://github.com/gcc-mirror/gcc.git",
        cache_dir=tmp_path,
    )
    repo.ensure()
    head = repo._git(["rev-parse", "master"]).strip()
    assert repo.resolve(head)
    assert "lines 1-" in repo.read_file(head, "gcc/ipa-sra.cc", 1, 20)
