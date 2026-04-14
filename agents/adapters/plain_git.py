"""PlainGit adapter — bare-clone any public Git repo and iterate commits.

Implements CommitSource only (no PR/discussion concept for plain Git).
"""

import logging
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from agents.models.raw import RawCommit

logger = logging.getLogger(__name__)

_GIT_LOG_FORMAT = "%H\x1f%ae\x1f%aI\x1f%s\x1f%D"


class PlainGitAdapter:
    """Clones a bare repo once and fetches on every subsequent call."""

    def __init__(
        self,
        repo_url: str,
        branch: str = "master",
        cache_dir: Path | None = None,
    ) -> None:
        self.repo_url = repo_url
        self.branch = branch
        self._cache_dir = Path(cache_dir) if cache_dir else Path("agents/cache")
        # Derive a safe directory name from the URL
        safe_name = repo_url.rstrip("/").split("/")[-1]
        if not safe_name.endswith(".git"):
            safe_name += ".git"
        self._bare_path = self._cache_dir / safe_name

    # ------------------------------------------------------------------
    # CommitSource protocol
    # ------------------------------------------------------------------

    def fetch_commits(self, since_hours: int = 24) -> list[RawCommit]:
        self._ensure_repo()
        since_dt = datetime.fromtimestamp(
            datetime.now(tz=timezone.utc).timestamp() - since_hours * 3600,
            tz=timezone.utc,
        ).isoformat()
        try:
            raw_log = self._run(
                [
                    "git",
                    "log",
                    self.branch,
                    f"--since={since_dt}",
                    f"--format={_GIT_LOG_FORMAT}",
                    "--no-merges",
                ],
                cwd=self._bare_path,
            )
        except subprocess.CalledProcessError as exc:
            logger.warning(
                "git log failed for %s/%s: %s", self.repo_url, self.branch, exc
            )
            return []

        commits: list[RawCommit] = []
        for line in raw_log.splitlines():
            line = line.strip()
            if not line:
                continue
            parts = line.split("\x1f")
            if len(parts) < 5:
                continue
            sha, email_addr, date_str, subject, refs = parts
            try:
                commit_date = datetime.fromisoformat(date_str)
            except ValueError:
                commit_date = datetime.now(tz=timezone.utc)
            commits.append(
                RawCommit(
                    sha=sha,
                    author=email_addr,
                    date=commit_date,
                    message=subject,
                    diff_stat=self._get_diff_stat(sha),
                    url=self._infer_url(sha),
                    source_type="plain_git",
                    metadata={"refs": refs, "repo_url": self.repo_url},
                )
            )
        return commits

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _ensure_repo(self) -> None:
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        if self._bare_path.exists():
            try:
                self._run(["git", "fetch", "--quiet", "origin"], cwd=self._bare_path)
                logger.debug("Fetched %s", self.repo_url)
            except subprocess.CalledProcessError as exc:
                logger.warning("git fetch failed for %s: %s", self.repo_url, exc)
        else:
            logger.info("Cloning %s → %s", self.repo_url, self._bare_path)
            try:
                self._run(
                    ["git", "clone", "--bare", "--quiet", self.repo_url,
                     str(self._bare_path)]
                )
            except subprocess.CalledProcessError as exc:
                logger.error("git clone failed for %s: %s", self.repo_url, exc)
                raise

    def _get_diff_stat(self, sha: str) -> str:
        try:
            return self._run(
                ["git", "diff-tree", "--stat", "--no-commit-id", "-r", sha],
                cwd=self._bare_path,
            ).strip()
        except subprocess.CalledProcessError:
            return ""

    def _infer_url(self, sha: str) -> str:
        """Best-effort: convert known Git hosting URLs to web URLs."""
        url = self.repo_url.rstrip("/")
        # kernel.org
        if "git.kernel.org" in url:
            return f"{url}/commit/?id={sha}"
        # GitHub
        if "github.com" in url:
            url = url.removesuffix(".git")
            return f"{url}/commit/{sha}"
        return f"{url}/commit/{sha}"

    @staticmethod
    def _run(cmd: list[str], cwd: Path | None = None) -> str:
        result = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, check=True
        )
        return result.stdout
