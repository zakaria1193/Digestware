"""Tests for the writer module."""

from __future__ import annotations

import re

import yaml

from agents.writer import _slugify, write_discussion, write_landing

# ---------------------------------------------------------------------------
# Slug sanitisation
# ---------------------------------------------------------------------------

class TestSlugify:
    def test_basic(self):
        assert _slugify("Hello World") == "hello-world"

    def test_special_chars(self):
        slug = _slugify("[PATCH v2] gcc/ipa: improve inline!")
        assert re.fullmatch(r"[a-z0-9-]+", slug)

    def test_leading_trailing_hyphens_stripped(self):
        slug = _slugify("---title---")
        assert not slug.startswith("-")
        assert not slug.endswith("-")

    def test_max_length(self):
        long_title = "a" * 200
        assert len(_slugify(long_title)) <= 80


# ---------------------------------------------------------------------------
# write_discussion
# ---------------------------------------------------------------------------

class TestWriteDiscussion:
    def test_file_created(self, sample_discussion_digest, tmp_output_dir):
        path = write_discussion(sample_discussion_digest, output_dir=tmp_output_dir)
        assert path.exists()

    def test_file_path_pattern(self, sample_discussion_digest, tmp_output_dir):
        path = write_discussion(sample_discussion_digest, output_dir=tmp_output_dir)
        # Format: YYYY-MM-DD-<slug>-<6-char-id-hash>.md
        assert re.match(r"\d{4}-\d{2}-\d{2}-.+-[0-9a-f]{6}\.md$", path.name)

    def test_same_title_different_ids_no_collision(self, tmp_output_dir):
        """Two discussions with identical titles on the same day must produce
        distinct files thanks to the id_hash suffix."""
        from datetime import datetime, timezone

        from agents.models.base import ConsensusStatus
        from agents.models.discussion import DiscussionDigest

        def _make(discussion_id: str) -> DiscussionDigest:
            return DiscussionDigest(
                project="gcc",
                subsystem="gcc/ipa",
                discussion_id=discussion_id,
                source_type="public_inbox",
                title="[PATCH] same title",
                headline="Same title",
                tldr="Same title tldr.",
                proposer="a@example.com",
                consensus=ConsensusStatus.PROPOSED,
                sentiment_score=5,
                technical_tradeoffs=[],
                summary=(
                    "Some enough text here that passes the writer body "
                    "validator so the fallback message is not used instead."
                ),
                url=f"https://example.com/{discussion_id}",
                date=datetime(2026, 4, 14, tzinfo=timezone.utc),
            )

        p1 = write_discussion(_make("id-001"), output_dir=tmp_output_dir)
        p2 = write_discussion(_make("id-002"), output_dir=tmp_output_dir)
        assert p1 != p2

    def test_frontmatter_has_required_keys(
        self, sample_discussion_digest, tmp_output_dir,
    ):
        path = write_discussion(sample_discussion_digest, output_dir=tmp_output_dir)
        content = path.read_text(encoding="utf-8")
        # Strip fences
        fm_text = content.split("---")[1]
        fm = yaml.safe_load(fm_text)
        required = {
            "project", "subsystem", "discussion_id", "source_type",
            "title", "proposer", "consensus", "impact_score", "sentiment_score",
            "technical_tradeoffs", "url", "date",
        }
        assert required.issubset(fm.keys())

    def test_body_contains_summary(self, sample_discussion_digest, tmp_output_dir):
        path = write_discussion(sample_discussion_digest, output_dir=tmp_output_dir)
        content = path.read_text(encoding="utf-8")
        assert sample_discussion_digest.summary in content

    def test_consensus_is_string_in_frontmatter(
        self, sample_discussion_digest, tmp_output_dir
    ):
        path = write_discussion(sample_discussion_digest, output_dir=tmp_output_dir)
        content = path.read_text(encoding="utf-8")
        fm = yaml.safe_load(content.split("---")[1])
        assert isinstance(fm["consensus"], str)


# ---------------------------------------------------------------------------
# write_landing
# ---------------------------------------------------------------------------

class TestWriteLanding:
    def test_file_created(self, sample_landing_digest, tmp_output_dir):
        path = write_landing(sample_landing_digest, output_dir=tmp_output_dir)
        assert path.exists()

    def test_file_path_pattern(self, sample_landing_digest, tmp_output_dir):
        path = write_landing(sample_landing_digest, output_dir=tmp_output_dir)
        assert re.match(r"\d{4}-\d{2}-\d{2}-", path.name)
        assert path.suffix == ".md"

    def test_frontmatter_has_required_keys(self, sample_landing_digest, tmp_output_dir):
        path = write_landing(sample_landing_digest, output_dir=tmp_output_dir)
        content = path.read_text(encoding="utf-8")
        fm = yaml.safe_load(content.split("---")[1])
        required = {
            "project", "subsystem", "commit_hash", "source_type",
            "author", "impact_score", "performance_win",
            "breaking_change", "url", "date",
        }
        assert required.issubset(fm.keys())

    def test_body_contains_summary(self, sample_landing_digest, tmp_output_dir):
        path = write_landing(sample_landing_digest, output_dir=tmp_output_dir)
        content = path.read_text(encoding="utf-8")
        assert sample_landing_digest.summary in content

    def test_is_stub_default_false(self, sample_landing_digest, tmp_output_dir):
        path = write_landing(sample_landing_digest, output_dir=tmp_output_dir)
        fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---")[1])
        assert fm["is_stub"] is False

    def test_is_stub_emitted_when_true(self, sample_landing_digest, tmp_output_dir):
        sample_landing_digest = sample_landing_digest.model_copy(
            update={"is_stub": True}
        )
        path = write_landing(sample_landing_digest, output_dir=tmp_output_dir)
        fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---")[1])
        assert fm["is_stub"] is True
