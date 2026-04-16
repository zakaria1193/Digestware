"""DiscussionDigest — output model for the Lab (discussion) agent."""

from datetime import datetime

from pydantic import Field

from agents.models.base import BimodalBase, ConsensusStatus


class DiscussionDigest(BimodalBase):
    discussion_id: str        # adapter's natural key (PR#, message_id, …)
    source_type: str          # preserved from RawDiscussion
    title: str
    proposer: str
    consensus: ConsensusStatus
    sentiment_score: int = Field(..., ge=1, le=10)
    technical_tradeoffs: list[str]
    summary: str
    url: str
    # preserved from RawDiscussion — when the discussion happened
    date: datetime
    bugzilla_url: str | None = None
