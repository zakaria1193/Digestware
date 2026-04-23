"""DiscussionDigest — output model for the Lab (discussion) agent."""

from datetime import datetime
from typing import Literal

from pydantic import Field

from agents.models.base import BimodalBase, ConsensusStatus, Outcome


class DiscussionDigest(BimodalBase):
    discussion_id: str        # adapter's natural key (PR#, message_id, …)
    source_type: str          # preserved from RawDiscussion
    title: str                # original subject line (kept for reference)
    headline: str             # translated, human-readable title
    tldr: str = Field(..., max_length=160)
    stakes: str               # why the proposal matters, for a working dev
    proposer: str
    consensus: ConsensusStatus                 # legacy single status
    outcome: Outcome = Outcome.PROPOSED        # richer lifecycle state
    sentiment_score: int = Field(..., ge=1, le=10)
    sentiment_rationale: str = ""
    summary: str
    series_id: str | None = None
    series_role: Literal["cover", "reply", "standalone"] | None = None
    series_parts: list[dict] = Field(default_factory=list)
    url: str
    # preserved from RawDiscussion — when the discussion happened
    date: datetime
    bugzilla_url: str | None = None
