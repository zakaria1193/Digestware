"""Tests for deterministic outcome derivation."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from agents.models.base import Outcome
from agents.tools.outcome import derive_discussion_outcome


class TestDeriveDiscussionOutcome:
    def test_committed_tag(self):
        assert (
            derive_discussion_outcome(
                "[hurd,committed] mach: fix tst-default-domain link",
                "body",
                [],
            )
            == Outcome.COMMITTED
        )

    def test_nack(self):
        assert (
            derive_discussion_outcome(
                "[PATCH] risky", "proposal body", ["NACK this breaks bootstrap"]
            )
            == Outcome.NACKD
        )

    def test_nacked_by_trailer(self):
        assert (
            derive_discussion_outcome(
                "[PATCH] risky",
                "body\nNacked-by: Somebody <x@y>",
                [],
            )
            == Outcome.NACKD
        )

    def test_ack(self):
        assert (
            derive_discussion_outcome(
                "[PATCH] fine",
                "body",
                ["LGTM, thanks"],
            )
            == Outcome.READY
        )

    def test_needs_revision(self):
        assert (
            derive_discussion_outcome(
                "[PATCH] draft",
                "body",
                ["Please rework the error handling"],
            )
            == Outcome.NEEDS_REVISION
        )

    def test_stalled(self):
        old = datetime.now(timezone.utc) - timedelta(days=120)
        assert (
            derive_discussion_outcome(
                "[PATCH] cold", "body", [], last_activity=old
            )
            == Outcome.STALLED
        )

    def test_default_proposed(self):
        assert (
            derive_discussion_outcome(
                "[PATCH] new", "body with no review signals", []
            )
            == Outcome.PROPOSED
        )

    def test_nack_wins_over_ack(self):
        # If any reviewer NACKed, the thread is not ready regardless of ACKs.
        assert (
            derive_discussion_outcome(
                "[PATCH] split",
                "body",
                ["ACK from A", "NACK from B — breaks arm64"],
            )
            == Outcome.NACKD
        )
