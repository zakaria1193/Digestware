"""Shared base model and enums for all digest output types."""

from enum import Enum

from pydantic import BaseModel, Field


class ConsensusStatus(str, Enum):
    PROPOSED = "Proposed"
    UNDER_REVIEW = "Under Review"
    NEEDS_REVISION = "Needs Revision"
    NACKED = "NACK'd"
    READY_TO_LAND = "Ready to Land"
    COMMITTED = "Committed"


class Outcome(str, Enum):
    """Lifecycle state of a proposal or landed change.

    Richer than ConsensusStatus (kept for backward-compat frontmatter) — this
    is the field the UI uses to colour-code cards and filter the feed.
    """

    PROPOSED = "proposed"
    UNDER_REVIEW = "under_review"
    NEEDS_REVISION = "needs_revision"
    NACKD = "nackd"
    READY = "ready"
    COMMITTED = "committed"
    WITHDRAWN = "withdrawn"
    STALLED = "stalled"


class BimodalBase(BaseModel):
    project: str
    subsystem: str
    patch_id: str | None = None  # git patch-id --stable for cross-referencing
    tags: list[str] = Field(default_factory=list, max_length=5)
    # "What is this even about?" comes in two registers so readers of very
    # different backgrounds both get something useful. Both are populated via
    # grounded search and rendered at the end of each article in a faded
    # typographic register — context, not headline.
    #
    # - ``primer_expert`` is dense toolchain-insider prose. Assumes the reader
    #   already recognises compiler passes, ELF/DWARF, relocations, PIC, the
    #   usual subsystem vocabulary. It situates *this* subsystem inside that
    #   mental model and may name specific files, passes, or invariants.
    # - ``primer_general`` is for a competent software engineer who does not
    #   work on toolchains. It unpacks the jargon the expert version takes
    #   for granted, explains why the subsystem exists at all, and gives
    #   enough footing to follow the rest of the article.
    primer_expert: str | None = Field(default=None, max_length=600)
    primer_general: str | None = Field(default=None, max_length=1000)
