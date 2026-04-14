"""Source-agnostic intermediate structs.

All adapters normalise their platform-specific data into RawDiscussion or
RawCommit before anything else in the pipeline sees them.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class RawDiscussion:
    id: str               # PR number, Message-ID, issue URL — source's natural key
    title: str
    body: str
    author: str
    date: datetime
    url: str
    replies: list[dict]   # comments, review threads, email replies
    diff_text: str | None  # patch/diff if attached
    source_type: str      # "github_pr" | "gitlab_mr" | "public_inbox"
    metadata: dict = field(default_factory=dict)  # source-specific pass-through


@dataclass
class RawCommit:
    sha: str
    author: str
    date: datetime
    message: str
    diff_stat: str
    url: str
    source_type: str      # "github" | "gitlab" | "public_inbox" | "plain_git"
    metadata: dict = field(default_factory=dict)
