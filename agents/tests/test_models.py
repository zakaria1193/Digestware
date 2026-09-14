"""Tests for all Pydantic output models and enums."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from agents.models.base import BimodalBase, ConsensusStatus
from agents.models.discussion import DiscussionDigest
from agents.models.landing import LandingDigest
from agents.models.lesson import LessonResearch

_DUMMY_DATE = datetime(2026, 4, 14, 12, 0, 0, tzinfo=timezone.utc)


# ---------------------------------------------------------------------------
# ConsensusStatus
# ---------------------------------------------------------------------------

class TestConsensusStatus:
    def test_all_values_are_strings(self):
        for member in ConsensusStatus:
            assert isinstance(member.value, str)

    def test_expected_members(self):
        names = {m.name for m in ConsensusStatus}
        assert names == {
            "PROPOSED", "UNDER_REVIEW", "NEEDS_REVISION",
            "NACKED", "READY_TO_LAND", "COMMITTED",
        }

    def test_round_trip(self):
        assert ConsensusStatus("Under Review") is ConsensusStatus.UNDER_REVIEW


# ---------------------------------------------------------------------------
# BimodalBase
# ---------------------------------------------------------------------------

class TestBimodalBase:
    def test_patch_id_optional(self):
        b = BimodalBase(project="gcc", subsystem="gcc/ipa")
        assert b.patch_id is None

    def test_patch_id_set(self):
        b = BimodalBase(project="gcc", subsystem="gcc/ipa", patch_id="abc")
        assert b.patch_id == "abc"


# ---------------------------------------------------------------------------
# DiscussionDigest
# ---------------------------------------------------------------------------

class TestDiscussionDigest:
    def test_valid(self, sample_discussion_digest: DiscussionDigest):
        d = sample_discussion_digest
        assert d.project == "gcc"
        assert d.subsystem == "gcc/ipa"
        assert d.sentiment_score is not None and 1 <= d.sentiment_score <= 10

    def _discussion(self, **overrides) -> dict:
        base: dict = dict(
            project="gcc",
            subsystem="gcc/ipa",
            discussion_id="1",
            source_type="public_inbox",
            title="x",
            headline="x",
            tldr="x",
            proposer="a",
            consensus=ConsensusStatus.PROPOSED,
            sentiment_score=5,
            technical_tradeoffs=[],
            summary="s",
            url="https://example.com",
            date=_DUMMY_DATE,
        )
        base.update(overrides)
        return base

    def test_sentiment_too_low(self):
        with pytest.raises(ValidationError):
            DiscussionDigest(**self._discussion(sentiment_score=0))

    def test_sentiment_too_high(self):
        with pytest.raises(ValidationError):
            DiscussionDigest(**self._discussion(sentiment_score=11))

    def test_sentiment_score_defaults_to_none(self):
        data = self._discussion()
        data.pop("sentiment_score")
        d = DiscussionDigest(**data)
        assert d.sentiment_score is None

    def test_sentiment_score_accepts_none(self):
        d = DiscussionDigest(**self._discussion(sentiment_score=None))
        assert d.sentiment_score is None

    def test_bugzilla_url_optional(self, sample_discussion_digest: DiscussionDigest):
        assert sample_discussion_digest.bugzilla_url is None

    def test_serialisation_roundtrip(self, sample_discussion_digest: DiscussionDigest):
        d = DiscussionDigest.model_validate(
            sample_discussion_digest.model_dump()
        )
        assert d == sample_discussion_digest


# ---------------------------------------------------------------------------
# LandingDigest
# ---------------------------------------------------------------------------

class TestLandingDigest:
    def test_valid(self, sample_landing_digest: LandingDigest):
        landing = sample_landing_digest
        assert landing.project == "binutils"
        assert landing.impact_score is None or 1 <= landing.impact_score <= 10

    def _landing(self, **overrides) -> dict:
        base: dict = dict(
            project="gcc",
            subsystem="gcc/lto",
            commit_hash="abc",
            source_type="github",
            author="a",
            headline="x",
            tldr="x",
            impact_score=5,
            summary="s",
            url="https://example.com",
            date=_DUMMY_DATE,
        )
        base.update(overrides)
        return base

    def test_impact_score_bounds(self):
        with pytest.raises(ValidationError):
            LandingDigest(**self._landing(impact_score=0))
        with pytest.raises(ValidationError):
            LandingDigest(**self._landing(impact_score=11))

    def test_impact_score_defaults_to_none(self):
        data = self._landing()
        data.pop("impact_score")
        d = LandingDigest(**data)
        assert d.impact_score is None

    def test_impact_score_accepts_none(self):
        d = LandingDigest(**self._landing(impact_score=None))
        assert d.impact_score is None

    def test_boolean_defaults(self):
        landing = LandingDigest(**self._landing())
        assert landing.performance_win is False
        assert landing.breaking_change is False

    def test_serialisation_roundtrip(self, sample_landing_digest: LandingDigest):
        landing = LandingDigest.model_validate(sample_landing_digest.model_dump())
        assert landing == sample_landing_digest


# ---------------------------------------------------------------------------
# LessonResearch — an explicit null must not cost the whole lesson
# ---------------------------------------------------------------------------


def test_lesson_research_accepts_null_for_optional_fields():
    """``"external_context": null`` means "found nothing", not a type error.

    A ValidationError here is non-retryable and drops straight to a stub, so
    this one null used to cost the entire week's lesson — twice in the stubs
    on disk as of 2026-09-14.
    """
    research = LessonResearch.model_validate(
        {
            "commit_hash": "83998f47450c",
            "subsystem": "rs6000",
            "external_context": None,
            "open_questions": None,
            "excerpts": None,
            "changed_files": None,
            "what_changed": None,
            "diff": None,
            "tool_calls_used": None,
        }
    )

    assert research.external_context == []
    assert research.open_questions == []
    assert research.excerpts == []
    assert research.changed_files == []
    assert research.what_changed == ""
    assert research.diff == ""
    assert research.tool_calls_used == 0


def test_lesson_research_still_requires_its_identity_fields():
    """Nulling a required field must stay an error, not an empty article."""
    with pytest.raises(ValidationError, match="commit_hash"):
        LessonResearch.model_validate({"commit_hash": None, "subsystem": "rs6000"})
