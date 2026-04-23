"""Shared pytest fixtures for Phase 2 tests."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pytest

from agents.models.base import ConsensusStatus, Outcome
from agents.models.discussion import DiscussionDigest
from agents.models.landing import LandingDigest
from agents.models.raw import RawCommit, RawDiscussion


@pytest.fixture
def sample_raw_discussion() -> RawDiscussion:
    return RawDiscussion(
        id="42",
        title="[PATCH] gcc/ipa: improve inline heuristics for hot functions",
        body="This patch improves the inliner by tracking call frequency...",
        author="jane.doe@example.com",
        date=datetime(2026, 4, 14, 10, 0, 0, tzinfo=timezone.utc),
        url="https://gcc.gnu.org/ml/gcc-patches/2026-04/msg00042.html",
        replies=[
            {"body": "Looks good to me, ACK"},
            {"body": "NACK — this breaks bootstrap on arm64"},
        ],
        diff_text="diff --git a/gcc/ipa-inline.cc b/gcc/ipa-inline.cc\n"
                  "--- a/gcc/ipa-inline.cc\n"
                  "+++ b/gcc/ipa-inline.cc\n"
                  "@@ -100,7 +100,8 @@ inline_call\n"
                  "-  if (freq > 0)\n"
                  "+  if (freq > INLINE_THRESHOLD)\n",
        source_type="public_inbox",
        metadata={"list": "gcc"},
    )


@pytest.fixture
def sample_raw_commit() -> RawCommit:
    return RawCommit(
        sha="deadbeef" * 5,
        author="john.smith@example.com",
        date=datetime(2026, 4, 14, 9, 0, 0, tzinfo=timezone.utc),
        message="binutils/ld: fix relaxation loop for RISC-V compressed insns\n\n"
                "Closes #1234\nSigned-off-by: John Smith <john.smith@example.com>",
        diff_stat="+45/-12 in 3 files",
        url="https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=deadbeef",
        source_type="plain_git",
        metadata={"repo_url": "https://sourceware.org/git/binutils-gdb.git"},
    )


@pytest.fixture
def sample_discussion_digest() -> DiscussionDigest:
    return DiscussionDigest(
        project="gcc",
        subsystem="gcc/ipa",
        patch_id="abc123",
        tags=["optimization", "inliner"],
        discussion_id="42",
        source_type="public_inbox",
        title="[PATCH] gcc/ipa: improve inline heuristics for hot functions",
        headline="GCC inliner adds frequency-aware hot-function threshold",
        tldr="GCC's inliner gains a configurable threshold for hot functions.",
        stakes="Affects code-size vs runtime trade-offs on every GCC-compiled binary.",
        proposer="jane.doe@example.com",
        consensus=ConsensusStatus.UNDER_REVIEW,
        outcome=Outcome.UNDER_REVIEW,
        sentiment_score=7,
        sentiment_rationale="One ACK, one blocker on arm64.",
        summary="This patch refines GCC's inliner to better handle hot functions "
                "by introducing a configurable frequency threshold.",
        url="https://gcc.gnu.org/ml/gcc-patches/2026-04/msg00042.html",
        date=datetime(2026, 4, 14, 10, 0, 0, tzinfo=timezone.utc),
        bugzilla_url=None,
    )


@pytest.fixture
def sample_landing_digest() -> LandingDigest:
    return LandingDigest(
        project="binutils",
        subsystem="binutils/ld",
        patch_id="def456",
        tags=["risc-v", "bugfix"],
        commit_hash="deadbeef" * 5,
        source_type="plain_git",
        author="John Smith",
        headline="Binutils LD fixes RISC-V relaxation loop for compressed insns",
        tldr="LD no longer loops on RISC-V compressed instructions near section ends.",
        impact_score=6,
        performance_win=False,
        breaking_change=False,
        outcome=Outcome.COMMITTED,
        summary="Fixes an infinite loop in the RISC-V relaxation pass when "
                "compressed instructions are present near section boundaries.",
        discussion_id_link=None,
        bugzilla_pr=1234,
        url="https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=deadbeef",
        date=datetime(2026, 4, 14, 9, 0, 0, tzinfo=timezone.utc),
    )


@pytest.fixture
def tmp_output_dir(tmp_path: Path) -> Path:
    d = tmp_path / "output"
    d.mkdir()
    return d
