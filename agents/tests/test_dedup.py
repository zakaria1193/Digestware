"""Tests for the dedup module."""

from __future__ import annotations

from datetime import date, datetime, timezone
from pathlib import Path

from agents.dedup import build_seen_index, filter_raw, latest_content_date
from agents.models.raw import RawCommit, RawDiscussion
from agents.writer import write_discussion, write_landing


def _content_root(base: Path) -> Path:
    """Create a ``<base>/content`` layout with empty discussions/ and landings/."""
    root = base / "content"
    (root / "discussions").mkdir(parents=True)
    (root / "landings").mkdir(parents=True)
    return root


class TestBuildSeenIndex:
    def test_empty_dirs(self, tmp_path):
        root = _content_root(tmp_path)
        ids, shas, series = build_seen_index(root)
        assert ids == set()
        assert shas == set()
        assert series == set()

    def test_missing_dirs(self, tmp_path):
        # Fresh deploys may not have the content subdirs yet.
        ids, shas, series = build_seen_index(tmp_path / "does-not-exist")
        assert ids == set()
        assert shas == set()
        assert series == set()

    def test_reads_frontmatter(
        self, tmp_path, sample_discussion_digest, sample_landing_digest,
    ):
        root = _content_root(tmp_path)
        write_discussion(sample_discussion_digest, output_dir=root / "discussions")
        write_landing(sample_landing_digest, output_dir=root / "landings")

        ids, shas, _series = build_seen_index(root)
        assert ids == {sample_discussion_digest.discussion_id}
        assert shas == {sample_landing_digest.commit_hash}

    def test_skips_malformed(self, tmp_path):
        root = _content_root(tmp_path)
        # No frontmatter at all
        (root / "discussions" / "bad.md").write_text("just a body\n")
        # Unclosed frontmatter
        (root / "landings" / "bad.md").write_text("---\nkey: value\nstill yaml\n")
        # Valid but missing expected keys
        (root / "discussions" / "ok.md").write_text(
            "---\ntitle: hello\n---\n\nbody\n"
        )

        ids, shas, series = build_seen_index(root)
        assert ids == set()
        assert shas == set()
        assert series == set()


class TestLatestContentDate:
    def test_none_when_empty(self, tmp_path):
        root = _content_root(tmp_path)
        assert latest_content_date(root) is None

    def test_none_when_dirs_missing(self, tmp_path):
        assert latest_content_date(tmp_path / "nope") is None

    def test_returns_max_across_subdirs(self, tmp_path):
        root = _content_root(tmp_path)
        (root / "discussions" / "a.md").write_text(
            "---\ndiscussion_id: a\ndate: 2026-06-20\n---\n\nbody\n"
        )
        (root / "landings" / "b.md").write_text(
            "---\ncommit_hash: b\ndate: 2026-06-27\n---\n\nbody\n"
        )
        (root / "landings" / "c.md").write_text(
            "---\ncommit_hash: c\ndate: 2026-06-24\n---\n\nbody\n"
        )
        assert latest_content_date(root) == date(2026, 6, 27)

    def test_accepts_datetime_strings(self, tmp_path):
        root = _content_root(tmp_path)
        (root / "landings" / "b.md").write_text(
            '---\ncommit_hash: b\ndate: "2026-06-29T12:34:56+00:00"\n---\n\nbody\n'
        )
        assert latest_content_date(root) == date(2026, 6, 29)

    def test_ignores_undated_and_malformed(self, tmp_path):
        root = _content_root(tmp_path)
        (root / "discussions" / "no-date.md").write_text(
            "---\ndiscussion_id: a\n---\n\nbody\n"
        )
        (root / "landings" / "bad-date.md").write_text(
            "---\ncommit_hash: b\ndate: not-a-date\n---\n\nbody\n"
        )
        (root / "landings" / "ok.md").write_text(
            "---\ncommit_hash: c\ndate: 2026-06-15\n---\n\nbody\n"
        )
        assert latest_content_date(root) == date(2026, 6, 15)


class TestFilterRaw:
    def _raw_discussion(self, did: str) -> RawDiscussion:
        return RawDiscussion(
            id=did,
            title=f"t-{did}",
            body="",
            author="a",
            date=datetime(2026, 4, 14, tzinfo=timezone.utc),
            url=f"https://example.com/{did}",
            replies=[],
            diff_text=None,
            source_type="public_inbox",
        )

    def _raw_commit(self, sha: str) -> RawCommit:
        return RawCommit(
            sha=sha,
            author="a",
            date=datetime(2026, 4, 14, tzinfo=timezone.utc),
            message="msg",
            diff_stat="",
            url=f"https://example.com/{sha}",
            source_type="plain_git",
        )

    def test_drops_seen_items(self):
        discussions = [self._raw_discussion(x) for x in ("a", "b", "c")]
        commits = [self._raw_commit(x) for x in ("1", "2")]
        kept_d, kept_c, skip_d, skip_c = filter_raw(
            discussions, commits, seen_ids={"b"}, seen_shas={"2"},
        )
        assert [d.id for d in kept_d] == ["a", "c"]
        assert [c.sha for c in kept_c] == ["1"]
        assert skip_d == 1
        assert skip_c == 1

    def test_keeps_all_when_seen_empty(self):
        discussions = [self._raw_discussion("a")]
        commits = [self._raw_commit("1")]
        kept_d, kept_c, skip_d, skip_c = filter_raw(
            discussions, commits, seen_ids=set(), seen_shas=set(),
        )
        assert kept_d == discussions
        assert kept_c == commits
        assert skip_d == 0
        assert skip_c == 0

    def test_roundtrip_with_writer(
        self, tmp_path, sample_raw_discussion, sample_discussion_digest,
    ):
        """After writing a digest, its raw twin is filtered out."""
        root = _content_root(tmp_path)
        write_discussion(sample_discussion_digest, output_dir=root / "discussions")

        seen_ids, seen_shas, seen_series = build_seen_index(root)
        kept_d, _, skip_d, _ = filter_raw(
            [sample_raw_discussion], [], seen_ids, seen_shas, seen_series,
        )
        assert kept_d == []
        assert skip_d == 1
