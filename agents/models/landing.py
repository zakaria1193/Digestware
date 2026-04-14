"""LandingDigest — output model for the Factory (landing) agent."""

from pydantic import Field

from agents.models.base import BimodalBase


class LandingDigest(BimodalBase):
    commit_hash: str
    source_type: str          # preserved from RawCommit
    author: str
    impact_score: int = Field(..., ge=1, le=10)
    performance_win: bool = False
    breaking_change: bool = False
    summary: str
    discussion_id_link: str | None = None  # cross-ref back to DiscussionDigest
    bugzilla_pr: int | None = None
    url: str
