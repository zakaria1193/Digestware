"""Tests for retro_noise — rescans on-disk markdown and stamps `is_stub`."""

from __future__ import annotations

from pathlib import Path

import yaml

from agents.tools.retro_noise import (
    matches_noise_rules,
    sweep_content_root,
)


def _write_md(path: Path, frontmatter: dict, body: str = "Body text.\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
    path.write_text(f"---\n{fm}---\n\n{body}", encoding="utf-8")


def _read_fm(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---", 2)[1])


class TestMatchesNoiseRules:
    def test_snapshot_release_title(self):
        assert (
            matches_noise_rules("gcc-16-20260509 is now available", None)
            == "title-noise"
        )

    def test_buildbot_title(self):
        assert (
            matches_noise_rules(
                "Buildbot (Sourceware): binutils-gdb failed test failure", None
            )
            == "title-noise"
        )

    def test_spam_title(self):
        assert matches_noise_rules("Dermatologist Contacts", None) == "spam"

    def test_bot_author(self):
        assert (
            matches_noise_rules("Anything", "builder@sourceware.org")
            == "bot-author"
        )

    def test_real_thread_kept(self):
        assert matches_noise_rules("[PATCH] gcc/ipa: improve inlining", "a@b") is None


class TestSweepContentRoot:
    def test_marks_existing_release_announcement(self, tmp_path: Path):
        root = tmp_path
        f = root / "discussions" / "2026-04-25-gcc-16-now.md"
        _write_md(
            f,
            {
                "project": "gcc",
                "title": "gcc-16-20260425 is now available",
                "proposer": "Jakub Jelinek",
                "is_stub": False,
            },
        )
        counts = sweep_content_root(root)
        assert counts["total"] == 1
        assert counts["title-noise"] == 1
        assert _read_fm(f)["is_stub"] is True

    def test_marks_bot_author(self, tmp_path: Path):
        root = tmp_path
        f = root / "discussions" / "ci-notice.md"
        _write_md(
            f,
            {
                "project": "binutils",
                # Title alone is benign — the bot author is what triggers
                # the rule.
                "title": "CI run notice",
                "proposer": "builder@sourceware.org",
                "is_stub": False,
            },
        )
        counts = sweep_content_root(root)
        assert counts["bot-author"] == 1
        assert _read_fm(f)["is_stub"] is True

    def test_marks_landing_by_author(self, tmp_path: Path):
        root = tmp_path
        f = root / "landings" / "spam.md"
        _write_md(
            f,
            {
                "project": "binutils",
                "headline": "Dermatologist Contacts",
                "author": "spam@x.com",
                "is_stub": False,
            },
        )
        counts = sweep_content_root(root)
        assert counts["spam"] == 1
        assert _read_fm(f)["is_stub"] is True

    def test_idempotent_on_already_stub(self, tmp_path: Path):
        root = tmp_path
        f = root / "discussions" / "already.md"
        _write_md(
            f,
            {
                "project": "gcc",
                "title": "gcc-16-20260425 is now available",
                "proposer": "x",
                "is_stub": True,
            },
        )
        before = f.read_text(encoding="utf-8")
        counts = sweep_content_root(root)
        assert counts["total"] == 0
        assert f.read_text(encoding="utf-8") == before

    def test_leaves_real_content_alone(self, tmp_path: Path):
        root = tmp_path
        f = root / "discussions" / "real.md"
        _write_md(
            f,
            {
                "project": "gcc",
                "title": "[PATCH] ipa: improve inlining",
                "proposer": "a@b",
                "is_stub": False,
            },
        )
        counts = sweep_content_root(root)
        assert counts["total"] == 0
        assert _read_fm(f)["is_stub"] is False
