"""GitHub adapter — fetches PRs (discussions) and commits via GitHub REST API.

Implements both DiscussionSource and CommitSource protocols.

Improvements over v1:
- Persistent httpx.Client (one TLS handshake per adapter lifetime, not per request).
- Rate-limit awareness: reads X-RateLimit-Remaining / X-RateLimit-Reset / Retry-After.
- Backs off on 429 / 403-with-no-quota and retries up to _MAX_RETRIES times.
- Pagination uses the Link: rel="next" header — more reliable than len < per_page.
- Diff fetch capped at _MAX_DIFF_BYTES (32 KB); skips PRs with >500 changed files.
- Files list in commit metadata capped at 50 entries.
"""

import logging
import os
import time
from datetime import datetime, timezone

import httpx

from agents.models.raw import RawCommit, RawDiscussion

logger = logging.getLogger(__name__)

_GITHUB_API = "https://api.github.com"
_MAX_DIFF_BYTES = 32_768   # 32 KB — enough context for the LLM, avoids huge allocs
_MAX_FILES_IN_META = 50    # cap the files list stored in metadata
_RATE_LIMIT_WARN = 50      # log a warning when fewer than this many requests remain
_MAX_RETRIES = 3


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
        headers: dict[str, str] = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        # Persistent client — reuses the underlying TCP/TLS connection.
        self._client = httpx.Client(
            headers=headers,
            timeout=httpx.Timeout(30.0),
            follow_redirects=True,
        )

    def __del__(self) -> None:
        try:
            self._client.close()
        except Exception:
            pass

    # ------------------------------------------------------------------
    # Core HTTP helpers
    # ------------------------------------------------------------------

    def _request(
        self,
        path: str,
        params: dict | None = None,
        extra_headers: dict | None = None,
    ) -> httpx.Response:
        """Single GET with rate-limit awareness and retry on 429 / quota-403."""
        url = f"{_GITHUB_API}{path}"
        for attempt in range(_MAX_RETRIES):
            resp = self._client.get(url, params=params, headers=extra_headers)

            remaining = int(resp.headers.get("X-RateLimit-Remaining", "9999"))
            if remaining < _RATE_LIMIT_WARN:
                logger.warning("GitHub rate limit low: %d requests remaining", remaining)

            if resp.status_code == 429:
                wait = int(resp.headers.get("Retry-After", "60"))
                logger.warning(
                    "HTTP 429 Too Many Requests; sleeping %ds (attempt %d/%d)",
                    wait, attempt + 1, _MAX_RETRIES,
                )
                time.sleep(wait)
                continue

            if resp.status_code == 403 and remaining == 0:
                reset_ts = int(
                    resp.headers.get("X-RateLimit-Reset", str(int(time.time()) + 60))
                )
                wait = max(1, reset_ts - int(time.time()))
                logger.warning("GitHub quota exhausted; sleeping %ds", wait)
                time.sleep(wait)
                continue

            resp.raise_for_status()
            return resp

        # Last-chance attempt — will raise on failure
        resp = self._client.get(url, params=params, headers=extra_headers)
        resp.raise_for_status()
        return resp

    def _paginate(self, path: str, params: dict | None = None) -> list:
        """Fetch all pages using the Link: rel="next" header for reliability."""
        params = dict(params or {})
        params.setdefault("per_page", 100)
        results: list = []
        page = 1
        while True:
            params["page"] = page
            resp = self._request(path, params)
            data = resp.json()
            if not isinstance(data, list) or not data:
                break
            results.extend(data)
            if 'rel="next"' not in resp.headers.get("Link", ""):
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
                break  # sorted desc by updated_at — safe to stop here
            replies = self._fetch_pr_comments(pr["number"])
            diff_text = self._fetch_pr_diff(
                pr["number"], changed_files=pr.get("changed_files", 0)
            )
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
                        "changed_files": pr.get("changed_files", 0),
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

    def _fetch_pr_diff(self, pr_number: int, changed_files: int = 0) -> str | None:
        """Fetch unified diff, capped at _MAX_DIFF_BYTES. Skips massive PRs."""
        if changed_files > 500:
            logger.debug(
                "Skipping diff for PR %s (%d files > 500 threshold)",
                pr_number, changed_files,
            )
            return None
        path = f"/repos/{self.owner}/{self.repo}/pulls/{pr_number}"
        try:
            resp = self._request(
                path,
                extra_headers={"Accept": "application/vnd.github.diff"},
            )
            text = resp.text
            if len(text) > _MAX_DIFF_BYTES:
                logger.debug(
                    "Diff for PR %s truncated %d→%d bytes",
                    pr_number, len(text), _MAX_DIFF_BYTES,
                )
                return text[:_MAX_DIFF_BYTES]
            return text
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
                        # Cap at _MAX_FILES_IN_META to bound memory usage
                        "files": [
                            f["filename"]
                            for f in item.get("files", [])[:_MAX_FILES_IN_META]
                        ],
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
