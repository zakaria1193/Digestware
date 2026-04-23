"""LandingDigest — output model for the Factory (landing) agent."""

from datetime import datetime

from pydantic import Field

from agents.models.base import BimodalBase, Outcome


class LandingDigest(BimodalBase):
    commit_hash: str
    source_type: str          # preserved from RawCommit
    author: str
    headline: str             # human-readable title (not the raw commit subject)
    tldr: str = Field(..., max_length=160)   # one sentence, ≤ 160 chars
    why_it_matters: str       # 1–2 sentences, dev-facing stakes
    impact_score: int | None = Field(default=None, ge=1, le=10)
    impact_rationale: str = ""  # one-line justification for the score
    performance_win: bool = False
    breaking_change: bool = False
    outcome: Outcome = Outcome.COMMITTED  # landed commits default to committed
    summary: str
    discussion_id_link: str | None = None  # cross-ref back to DiscussionDigest
    bugzilla_pr: int | None = None
    series_id: str | None = None   # set when this commit is part of a series
    series_parts: list[dict] = Field(default_factory=list)  # [{title, url}, …]
    url: str
    date: datetime            # preserved from RawCommit — when the commit landed
