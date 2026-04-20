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
    # "What is this even about?" primer for devs outside the subsystem.
    # Populated via Gemini grounded search so it carries real background, not
    # a rehash of the commit message. Rendered at the end of each article in a
    # faded typographic register — context, not headline.
    primer: str | None = Field(default=None, max_length=800)
