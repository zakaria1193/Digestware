"""DiscussionDigest — output model for the Lab (discussion) agent."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from agents.models.base import BimodalBase, ConsensusStatus, Outcome


class Exchange(BaseModel):
    """One participant's contribution to a discussion thread.

    A discussion is NEVER collapsed into a single narrator voice. Each
    participant who weighed in gets their own entry so readers can see who
    said what — "the contributor suggests X, Y responded with Z, …".
    """

    author: str                       # human name or email-style handle
    role: Literal[
        "proposer", "reviewer", "maintainer", "contributor", "other"
    ] | None = None
    # One- or two-sentence paraphrase of this participant's stance / point.
    position: str = Field(..., max_length=320)
    # Optional verbatim excerpt to anchor the paraphrase. Kept short —
    # not a transcript, just a pull-quote.
    quote: str | None = Field(default=None, max_length=400)


class DiscussionDigest(BimodalBase):
    discussion_id: str        # adapter's natural key (PR#, message_id, …)
    source_type: str          # preserved from RawDiscussion
    title: str                # original subject line (kept for reference)
    headline: str             # translated, human-readable title
    tldr: str = Field(..., max_length=160)
    proposer: str
    consensus: ConsensusStatus                 # legacy single status
    outcome: Outcome = Outcome.PROPOSED        # richer lifecycle state
    # 1–10. Same rubric as LandingDigest.impact_score but applied to the
    # *proposed* change: how significant would this be if it landed?
    # Never guess — set null when there is not enough information.
    impact_score: int | None = Field(default=None, ge=1, le=10)
    # None when the community has not responded yet — we must not fabricate a
    # sentiment when no one has weighed in. Only set 1..10 once there is at
    # least one reply to judge.
    sentiment_score: int | None = Field(default=None, ge=1, le=10)
    technical_tradeoffs: list[str]
    # Per-participant breakdown of the thread. Empty list when the thread has
    # only the proposer and no replies. The narrator-voice ``summary`` below
    # still exists as a fallback and for meta/index views.
    exchanges: list[Exchange] = Field(default_factory=list)
    summary: str
    series_id: str | None = None
    series_role: Literal["cover", "reply", "standalone"] | None = None
    series_parts: list[dict] = Field(default_factory=list)
    url: str
    # preserved from RawDiscussion — when the discussion happened
    date: datetime
    bugzilla_url: str | None = None
    # True when the digest is an agent-side placeholder (LLM batch failed or
    # omitted the item). Stubs are written to disk so admin can inspect them,
    # but the public site filters them out.
    is_stub: bool = False
