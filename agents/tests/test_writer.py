"""Tests for the writer module."""

from __future__ import annotations

import re
from pathlib import Path

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
        assert re.match(r"\d{4}-\d{2}-\d{2}-", path.name)
        assert path.suffix == ".md"

    def test_frontmatter_has_required_keys(self, sample_discussion_digest, tmp_output_dir):
        path = write_discussion(sample_discussion_digest, output_dir=tmp_output_dir)
        content = path.read_text(encoding="utf-8")
        # Strip fences
        fm_text = content.split("---")[1]
        fm = yaml.safe_load(fm_text)
        required = {
            "project", "subsystem", "discussion_id", "source_type",
            "title", "proposer", "consensus", "sentiment_score",
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
