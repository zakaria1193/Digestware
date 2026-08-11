"""Tests for the pre-commit content validator."""

from __future__ import annotations

from pathlib import Path

import yaml

from agents.tools.validate_content import validate_content_root, validate_file

_GOOD_LANDING = {
    "project": "binutils",
    "subsystem": "binutils/ld",
    "source_type": "public_inbox",
    "headline": "Fix a thing.",
    "tldr": "It fixes the thing.",
    "url": "https://example.com/a",
    "date": "2026-07-28",
}

_LANDING_FIELDS = (
    "project", "subsystem", "source_type", "headline", "tldr", "url", "date",
)


def _write_md(path: Path, frontmatter: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
    path.write_text(f"---\n{fm}---\n\nBody.\n", encoding="utf-8")
    return path


class TestValidateFile:
    def test_valid_file_has_no_problems(self, tmp_path: Path):
        f = _write_md(tmp_path / "ok.md", _GOOD_LANDING)
        assert validate_file(f, _LANDING_FIELDS) == []

    def test_unquoted_date_is_accepted(self, tmp_path: Path):
        # yaml.safe_load turns this into a datetime.date rather than a string.
        f = _write_md(tmp_path / "d.md", {**_GOOD_LANDING, "date": "2026-07-28"})
        f.write_text(f.read_text().replace("'2026-07-28'", "2026-07-28"))
        assert validate_file(f, _LANDING_FIELDS) == []

    def test_missing_url_is_reported(self, tmp_path: Path):
        fm = {k: v for k, v in _GOOD_LANDING.items() if k != "url"}
        f = _write_md(tmp_path / "no-url.md", fm)
        assert "missing required field `url`" in validate_file(f, _LANDING_FIELDS)

    def test_relative_url_is_reported(self, tmp_path: Path):
        f = _write_md(tmp_path / "rel.md", {**_GOOD_LANDING, "url": "/local/path"})
        problems = validate_file(f, _LANDING_FIELDS)
        assert any("not an absolute URL" in p for p in problems)

    def test_unparseable_date_is_reported(self, tmp_path: Path):
        f = _write_md(tmp_path / "bad-date.md", {**_GOOD_LANDING, "date": "someday"})
        problems = validate_file(f, _LANDING_FIELDS)
        assert any("not a valid date" in p for p in problems)

    def test_missing_frontmatter_is_reported(self, tmp_path: Path):
        f = tmp_path / "plain.md"
        f.write_text("Just a body.\n", encoding="utf-8")
        assert validate_file(f, _LANDING_FIELDS) == [
            "missing or malformed YAML frontmatter"
        ]

    def test_truncated_frontmatter_is_reported(self, tmp_path: Path):
        """The exact corruption shape that broke the Pages build."""
        f = tmp_path / "truncated.md"
        f.write_text(
            "---\n"
            "project: binutils\n"
            "subsystem: binutils/pre-commit\n"
            "source_type: public_inbox\n"
            "headline: Fix yamllint errors.\n"
            "tldr: Corrects YAML formatting.\n"
            "primer_expert: markers (`\n"
            "is_stub: true\n"
            "stub_reason: low-score\n"
            "---`), and fixing whitespace.\n"
            "url: https://example.com/a\n"
            "date: 2026-07-28\n"
            "---\n\nBody.\n",
            encoding="utf-8",
        )
        problems = validate_file(f, _LANDING_FIELDS)
        assert "missing required field `url`" in problems
        assert "missing required field `date`" in problems


class TestValidateContentRoot:
    def test_clean_tree_passes(self, tmp_path: Path):
        _write_md(tmp_path / "landings" / "a.md", _GOOD_LANDING)
        assert validate_content_root(tmp_path) == {}

    def test_offender_is_returned(self, tmp_path: Path):
        _write_md(tmp_path / "landings" / "good.md", _GOOD_LANDING)
        bad = _write_md(
            tmp_path / "landings" / "bad.md",
            {k: v for k, v in _GOOD_LANDING.items() if k != "url"},
        )
        failures = validate_content_root(tmp_path)
        assert list(failures) == [bad]

    def test_missing_subdir_is_tolerated(self, tmp_path: Path):
        assert validate_content_root(tmp_path) == {}
