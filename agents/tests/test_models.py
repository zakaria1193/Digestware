"""Tests for all Pydantic output models and enums."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from agents.models.base import BimodalBase, ConsensusStatus
from agents.models.discussion import DiscussionDigest
from agents.models.landing import LandingDigest

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
        assert 1 <= d.sentiment_score <= 10

    def test_sentiment_too_low(self):
        with pytest.raises(ValidationError):
            DiscussionDigest(
                project="gcc",
                subsystem="gcc/ipa",
                discussion_id="1",
                source_type="public_inbox",
                title="x",
                proposer="a",
                consensus=ConsensusStatus.PROPOSED,
                sentiment_score=0,  # invalid
                technical_tradeoffs=[],
                summary="s",
                url="https://example.com",
            )

    def test_sentiment_too_high(self):
        with pytest.raises(ValidationError):
            DiscussionDigest(
                project="gcc",
                subsystem="gcc/ipa",
                discussion_id="1",
                source_type="public_inbox",
                title="x",
                proposer="a",
                consensus=ConsensusStatus.PROPOSED,
                sentiment_score=11,  # invalid
                technical_tradeoffs=[],
                summary="s",
                url="https://example.com",
            )

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
        l = sample_landing_digest
        assert l.project == "binutils"
        assert 1 <= l.impact_score <= 10

    def test_impact_score_bounds(self):
        with pytest.raises(ValidationError):
            LandingDigest(
                project="gcc",
                subsystem="gcc/lto",
                commit_hash="abc",
                source_type="github",
                author="a",
                impact_score=0,  # invalid
                summary="s",
                url="https://example.com",
            )
        with pytest.raises(ValidationError):
            LandingDigest(
                project="gcc",
                subsystem="gcc/lto",
                commit_hash="abc",
                source_type="github",
                author="a",
                impact_score=11,  # invalid
                summary="s",
                url="https://example.com",
            )

    def test_boolean_defaults(self):
        l = LandingDigest(
            project="p",
            subsystem="s",
            commit_hash="c",
            source_type="github",
            author="a",
            impact_score=5,
            summary="s",
            url="https://example.com",
            date=_DUMMY_DATE,
        )
        assert l.performance_win is False
        assert l.breaking_change is False

    def test_serialisation_roundtrip(self, sample_landing_digest: LandingDigest):
        l = LandingDigest.model_validate(sample_landing_digest.model_dump())
        assert l == sample_landing_digest
