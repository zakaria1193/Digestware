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


class GlossaryEntry(BaseModel):
    """One `{term, definition}` pair for the "For Context" glossary block."""

    term: str = Field(..., max_length=80)
    definition: str = Field(..., max_length=400)


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
    # - ``primer_glossary`` is the "For Context" block for a systems
    #   programmer who is NOT a toolchain expert. Rather than a prose
    #   paragraph, it's a series of `{term, definition}` entries — one per
    #   toolchain-specific concept used in the article that such a reader
    #   would not already know. It assumes general systems-programming
    #   literacy (pointers, processes, syscalls) and does not re-define
    #   that; it only unpacks the toolchain-specific jargon.
    primer_expert: str | None = Field(default=None, max_length=600)
    primer_glossary: list[GlossaryEntry] = Field(default_factory=list, max_length=10)
