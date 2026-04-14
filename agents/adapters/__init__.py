"""Adapter protocols for discussion and commit sources.

Any object that satisfies DiscussionSource or CommitSource can be fed into
IngestionEngine without the engine knowing anything about the underlying
platform.
"""

from typing import Protocol

from agents.models.raw import RawCommit, RawDiscussion


class DiscussionSource(Protocol):
    def fetch_discussions(self, since_hours: int = 24) -> list[RawDiscussion]: ...


class CommitSource(Protocol):
    def fetch_commits(self, since_hours: int = 24) -> list[RawCommit]: ...
