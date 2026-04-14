"""GitHub adapter — fetches PRs (discussions) and commits via GitHub REST API.

Implements both DiscussionSource and CommitSource protocols.
Uses GITHUB_TOKEN env var when available (60 → 5 000 req/hr).
All HTTP is synchronous via httpx (async would require an event loop at the
call site; the ingestion engine is intentionally sync for simplicity).
"""

import logging
import os
from datetime import datetime, timezone

import httpx

from agents.models.raw import RawCommit, RawDiscussion

logger = logging.getLogger(__name__)

_GITHUB_API = "https://api.github.com"


class GitHubAdapter:
    """Fetches open PRs and recent commits for a single GitHub repository."""

    def __init__(
        self,
        owner: str,
        repo: str,
        token: str | None = None,
    ) -> None:
        self.owner = owner
        self.repo = repo
        self._token = token or os.getenv("GITHUB_TOKEN")
        self._headers: dict[str, str] = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self._token:
            self._headers["Authorization"] = f"Bearer {self._token}"

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get(self, path: str, params: dict | None = None) -> list | dict:
        url = f"{_GITHUB_API}{path}"
        with httpx.Client(headers=self._headers, timeout=30) as client:
            resp = client.get(url, params=params)
            resp.raise_for_status()
            return resp.json()

    def _paginate(self, path: str, params: dict | None = None) -> list:
        """Fetch all pages for a list endpoint."""
        params = dict(params or {})
        params.setdefault("per_page", 100)
        results: list = []
        page = 1
        while True:
            params["page"] = page
            data = self._get(path, params)
            if not isinstance(data, list) or not data:
                break
            results.extend(data)
            if len(data) < params["per_page"]:
                break
            page += 1
        return results

    @staticmethod
    def _parse_dt(s: str) -> datetime:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))

    # ------------------------------------------------------------------
    # DiscussionSource protocol
    # ------------------------------------------------------------------

    def fetch_discussions(self, since_hours: int = 24) -> list[RawDiscussion]:
        """Return recently-updated open PRs as RawDiscussion objects."""
        prs = self._paginate(
            f"/repos/{self.owner}/{self.repo}/pulls",
            {"state": "open", "sort": "updated", "direction": "desc"},
        )
        cutoff = datetime.now(tz=timezone.utc).timestamp() - since_hours * 3600
        discussions: list[RawDiscussion] = []
        for pr in prs:
            updated_at = self._parse_dt(pr["updated_at"])
            if updated_at.timestamp() < cutoff:
                break  # results are sorted by updated desc
            replies = self._fetch_pr_comments(pr["number"])
            diff_text = self._fetch_pr_diff(pr["number"])
            discussions.append(
                RawDiscussion(
                    id=str(pr["number"]),
                    title=pr["title"],
                    body=pr.get("body") or "",
                    author=pr["user"]["login"],
                    date=self._parse_dt(pr["created_at"]),
                    url=pr["html_url"],
                    replies=replies,
                    diff_text=diff_text,
                    source_type="github_pr",
                    metadata={
                        "state": pr["state"],
                        "draft": pr.get("draft", False),
                        "labels": [lb["name"] for lb in pr.get("labels", [])],
                    },
                )
            )
        return discussions

    def _fetch_pr_comments(self, pr_number: int) -> list[dict]:
        try:
            return self._paginate(
                f"/repos/{self.owner}/{self.repo}/pulls/{pr_number}/comments"
            )
        except httpx.HTTPError as exc:
            logger.warning("Could not fetch comments for PR %s: %s", pr_number, exc)
            return []

    def _fetch_pr_diff(self, pr_number: int) -> str | None:
        url = f"{_GITHUB_API}/repos/{self.owner}/{self.repo}/pulls/{pr_number}"
        with httpx.Client(
            headers={**self._headers, "Accept": "application/vnd.github.diff"},
            timeout=60,
        ) as client:
            try:
                resp = client.get(url)
                resp.raise_for_status()
                return resp.text
            except httpx.HTTPError as exc:
                logger.warning("Could not fetch diff for PR %s: %s", pr_number, exc)
                return None

    # ------------------------------------------------------------------
    # CommitSource protocol
    # ------------------------------------------------------------------

    def fetch_commits(self, since_hours: int = 24) -> list[RawCommit]:
        """Return commits pushed within the last *since_hours* hours."""
        since_dt = datetime.fromtimestamp(
            datetime.now(tz=timezone.utc).timestamp() - since_hours * 3600,
            tz=timezone.utc,
        ).isoformat()
        raw = self._paginate(
            f"/repos/{self.owner}/{self.repo}/commits",
            {"since": since_dt},
        )
        commits: list[RawCommit] = []
        for item in raw:
            commit_data = item["commit"]
            author_info = commit_data.get("author") or {}
            date_str = author_info.get("date", "1970-01-01T00:00:00Z")
            commits.append(
                RawCommit(
                    sha=item["sha"],
                    author=author_info.get("name", "unknown"),
                    date=self._parse_dt(date_str),
                    message=commit_data.get("message", ""),
                    diff_stat=self._format_diff_stat(item.get("stats")),
                    url=item["html_url"],
                    source_type="github",
                    metadata={
                        "files": [f["filename"] for f in item.get("files", [])],
                    },
                )
            )
        return commits

    @staticmethod
    def _format_diff_stat(stats: dict | None) -> str:
        if not stats:
            return ""
        return (
            f"+{stats.get('additions', 0)}/-{stats.get('deletions', 0)} "
            f"in {stats.get('total', 0)} changes"
        )
