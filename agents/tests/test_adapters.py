"""Tests for the source adapters.

Uses:
- respx  — mock httpx calls for GitHubAdapter
- unittest.mock — mock subprocess for PlainGitAdapter and PublicInboxAdapter
"""

from __future__ import annotations

import json
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
            import httpx
        except ImportError:
            pytest.skip("respx not installed")

        adapter = GitHubAdapter("gcc-mirror", "gcc", token="fake-token")
        pr = self._make_pr()

        with respx.mock(base_url="https://api.github.com") as mock:
            mock.get(
                "/repos/gcc-mirror/gcc/pulls",
            ).respond(200, json=[pr])
            mock.get(
                "/repos/gcc-mirror/gcc/pulls/101/comments",
            ).respond(200, json=[])
            # PR diff
            mock.get(
                "/repos/gcc-mirror/gcc/pulls/101",
            ).respond(200, text="diff --git a/gcc/ipa-inline.cc b/gcc/ipa-inline.cc\n")

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
            import httpx
        except ImportError:
            pytest.skip("respx not installed")

        adapter = GitHubAdapter("gcc-mirror", "gcc", token="fake-token")
        commit = self._make_commit("deadbeef")

        with respx.mock(base_url="https://api.github.com") as mock:
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
            import httpx
        except ImportError:
            pytest.skip("respx not installed")

        adapter = GitHubAdapter("gcc-mirror", "gcc", token="fake-token")
        pr = self._make_pr(200)

        with respx.mock(base_url="https://api.github.com") as mock:
            mock.get("/repos/gcc-mirror/gcc/pulls").respond(200, json=[pr])
            mock.get("/repos/gcc-mirror/gcc/pulls/200/comments").respond(500, json={})
            mock.get("/repos/gcc-mirror/gcc/pulls/200").respond(200, text="")

            discussions = adapter.fetch_discussions(since_hours=24)

        assert discussions[0].replies == []


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
            use_nntp=False,
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

        with (
            patch("agents.adapters.public_inbox._mirror_list", return_value=mock_mirror),
            patch("agents.adapters.public_inbox.subprocess.run", side_effect=fake_run),
        ):
            discussions = adapter.fetch_discussions(since_hours=999)

        assert len(discussions) == 1
        d = discussions[0]
        assert d.source_type == "public_inbox"
        assert "inline" in d.title.lower()

    def test_nntp_fallback_on_mirror_failure(self, tmp_path: Path):
        from agents.adapters.public_inbox import PublicInboxAdapter

        adapter = PublicInboxAdapter(
            discussion_lists=["gcc"],
            cvs_lists=[],
            cache_dir=tmp_path,
            use_nntp=True,
        )

        with (
            patch(
                "agents.adapters.public_inbox._mirror_list",
                side_effect=RuntimeError("network error"),
            ),
            patch(
                "agents.adapters.public_inbox.nntplib.NNTP",
                side_effect=ConnectionRefusedError("NNTP down"),
            ),
        ):
            result = adapter.fetch_discussions(since_hours=24)

        assert result == []


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
                return MagicMock(
                    returncode=0, stdout=_GIT_LOG_LINE + "\n", stderr=""
                )
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


# ---------------------------------------------------------------------------
# IngestionEngine — deduplication
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

    def test_nntp_fallback_test(self):
        """Adapter errors must not propagate — engine returns empty lists."""
        class BrokenSource:
            def fetch_discussions(self, since_hours=24):
                raise RuntimeError("adapter exploded")

            def fetch_commits(self, since_hours=24):
                raise RuntimeError("adapter exploded")

        engine = IngestionEngine([BrokenSource()], [BrokenSource()])
        result = engine.run()
        assert result["discussions"] == []
        assert result["commits"] == []
