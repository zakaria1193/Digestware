"""IngestionEngine — fans out fetch calls across all registered adapters.

Deduplicates results by `id` (discussions) or `sha` (commits) so the same
item ingested from two sources only appears once in the pipeline.
"""

import logging

from agents.adapters import CommitSource, DiscussionSource
from agents.models.raw import RawCommit, RawDiscussion
from agents.tools.noise_filter import filter_noise

logger = logging.getLogger(__name__)


class IngestionEngine:
    def __init__(
        self,
        discussion_sources: list[DiscussionSource],
        commit_sources: list[CommitSource],
    ) -> None:
        self.discussion_sources = discussion_sources
        self.commit_sources = commit_sources

    def run(self, since_hours: int = 24) -> dict[str, list]:
        """Fetch from all sources and return deduplicated lists.

        Returns:
            {"discussions": list[RawDiscussion], "commits": list[RawCommit]}
        """
        raw_discussions: list[RawDiscussion] = []
        for src in self.discussion_sources:
            try:
                items = src.fetch_discussions(since_hours)
                logger.info(
                    "%s yielded %d discussions", type(src).__name__, len(items)
                )
                raw_discussions.extend(items)
            except Exception as exc:
                logger.warning(
                    "%s.fetch_discussions raised: %s — skipping",
                    type(src).__name__,
                    exc,
                )

        raw_commits: list[RawCommit] = []
        for src in self.commit_sources:
            try:
                items = src.fetch_commits(since_hours)
                logger.info(
                    "%s yielded %d commits", type(src).__name__, len(items)
                )
                raw_commits.extend(items)
            except Exception as exc:
                logger.warning(
                    "%s.fetch_commits raised: %s — skipping",
                    type(src).__name__,
                    exc,
                )

        discussions = self._dedup_discussions(raw_discussions)
        commits = self._dedup_commits(raw_commits)

        discussions, commits, dropped_d, dropped_c = filter_noise(discussions, commits)
        if dropped_d or dropped_c:
            logger.info(
                "Noise filter dropped %d discussions, %d commits",
                dropped_d,
                dropped_c,
            )

        logger.info(
            "Ingestion complete: %d discussions, %d commits (after dedup + noise filter)",
            len(discussions),
            len(commits),
        )
        return {"discussions": discussions, "commits": commits}

    # ------------------------------------------------------------------
    # Deduplication helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _dedup_discussions(items: list[RawDiscussion]) -> list[RawDiscussion]:
        """Dedup by (source_type, project, id) — bare PR number "123" on
        project A must not collide with message-id "123" or PR "123" on
        project B. Namespacing the key keeps the guarantee explicit.
        """
        seen: set[tuple[str, str, str]] = set()
        result: list[RawDiscussion] = []
        for item in items:
            key = (item.source_type, item.project, item.id)
            if key not in seen:
                seen.add(key)
                result.append(item)
        return result

    @staticmethod
    def _dedup_commits(items: list[RawCommit]) -> list[RawCommit]:
        """Commit SHAs are globally unique (git is content-addressed) but we
        still namespace by source_type so a plain-git mirror + its GitHub
        twin don't produce double digests for the same sha.
        """
        seen: set[tuple[str, str]] = set()
        result: list[RawCommit] = []
        for item in items:
            key = (item.source_type, item.sha)
            if key not in seen:
                seen.add(key)
                result.append(item)
        return result
