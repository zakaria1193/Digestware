"""Tests for writer body validation.

The writer must reject LLM-failure-mode summaries (truncated, quoted email
leakage, too short) and replace them with a visible fallback string.
"""

from __future__ import annotations

from datetime import datetime, timezone

import yaml

from agents.models.base import ConsensusStatus, Outcome
from agents.models.discussion import DiscussionDigest
from agents.models.landing import LandingDigest
from agents.writer import write_discussion, write_landing

_FALLBACK = "Summary unavailable — see source link."


def _make_discussion(summary: str) -> DiscussionDigest:
    return DiscussionDigest(
        project="gcc",
        subsystem="gcc/ipa",
        discussion_id="id-1",
        source_type="public_inbox",
        title="[PATCH] subject",
        headline="Subject",
        tldr="A short tldr.",
        stakes="Stakes statement.",
        proposer="a@b",
        consensus=ConsensusStatus.PROPOSED,
        outcome=Outcome.PROPOSED,
        sentiment_score=5,
        summary=summary,
        url="https://example.com/1",
        date=datetime(2026, 4, 14, tzinfo=timezone.utc),
    )


def _make_landing(summary: str) -> LandingDigest:
    return LandingDigest(
        project="gcc",
        subsystem="gcc/ipa",
        commit_hash="a" * 40,
        source_type="github",
        author="a@b",
        headline="Subject",
        tldr="A short tldr.",
        impact_score=5,
        summary=summary,
        url="https://example.com/1",
        date=datetime(2026, 4, 14, tzinfo=timezone.utc),
    )


def _body_of(path) -> str:
    text = path.read_text(encoding="utf-8")
    return text.split("---", 2)[2].strip()


class TestDiscussionBodyValidation:
    def test_quoted_email_replaced(self, tmp_output_dir):
        d = _make_discussion("On Thu Apr 16 2026, Alice wrote:\n> original message")
        path = write_discussion(d, output_dir=tmp_output_dir)
        assert _body_of(path) == _FALLBACK

    def test_truncated_mid_word_replaced(self, tmp_output_dir):
        d = _make_discussion(
            "This proposal introduces a new tunable for the malloc allocator "
            "which denote the signed"
        )
        path = write_discussion(d, output_dir=tmp_output_dir)
        assert _body_of(path) == _FALLBACK

    def test_dangling_bracket_replaced(self, tmp_output_dir):
        d = _make_discussion(
            "We currently accept invalid code here, per section [expr.prim.lam"
        )
        path = write_discussion(d, output_dir=tmp_output_dir)
        assert _body_of(path) == _FALLBACK

    def test_too_short_replaced(self, tmp_output_dir):
        d = _make_discussion("Daily bump.")
        path = write_discussion(d, output_dir=tmp_output_dir)
        assert _body_of(path) == _FALLBACK

    def test_good_body_kept(self, tmp_output_dir):
        good = (
            "The inliner now tracks call-site frequency via a new tunable "
            "flag, letting users tune code-size versus runtime trade-offs "
            "without recompiling."
        )
        d = _make_discussion(good)
        path = write_discussion(d, output_dir=tmp_output_dir)
        assert _body_of(path) == good


class TestLandingBodyValidation:
    def test_quoted_commit_replaced(self, tmp_output_dir):
        lg = _make_landing("> This is the commit message copied verbatim.")
        path = write_landing(lg, output_dir=tmp_output_dir)
        assert _body_of(path) == _FALLBACK

    def test_frontmatter_still_valid_on_fallback(self, tmp_output_dir):
        lg = _make_landing("")  # empty → fallback
        path = write_landing(lg, output_dir=tmp_output_dir)
        content = path.read_text(encoding="utf-8")
        fm = yaml.safe_load(content.split("---", 2)[1])
        assert fm["headline"] == "Subject"
        assert fm["outcome"] == "committed"
