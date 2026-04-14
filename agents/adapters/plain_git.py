"""PlainGit adapter — bare-clone any public Git repo and iterate commits.

Implements CommitSource only (no PR/discussion concept for plain Git).

Security: repo_url and branch are validated against strict allowlists before
being passed to git subprocesses, preventing git-option injection attacks.
All subprocess calls carry an explicit timeout to prevent hangs on slow servers.
"""

import logging
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from agents.models.raw import RawCommit

logger = logging.getLogger(__name__)

_GIT_LOG_FORMAT = "%H\x1f%ae\x1f%aI\x1f%s\x1f%D"
_GIT_TIMEOUT = 120  # seconds

# Strict allowlists guard against git-option injection (e.g. --upload-pack=…)
_ALLOWED_URL_SCHEMES = ("https://", "http://", "git://", "ssh://")
_BRANCH_RE = re.compile(r"^[A-Za-z0-9._/-]{1,128}$")


def _validate_repo_url(url: str) -> None:
    if not any(url.startswith(s) for s in _ALLOWED_URL_SCHEMES):
        raise ValueError(
            f"Unsafe repo_url {url!r}: must start with one of {_ALLOWED_URL_SCHEMES}"
        )


def _validate_branch_name(branch: str) -> None:
    if not _BRANCH_RE.match(branch):
        raise ValueError(
            f"Unsafe branch name {branch!r}: must match {_BRANCH_RE.pattern}"
        )


class PlainGitAdapter:
    """Clones a bare repo once and fetches on every subsequent call."""

    def __init__(
        self,
        repo_url: str,
        branch: str = "master",
        cache_dir: Path | None = None,
    ) -> None:
        _validate_repo_url(repo_url)
        _validate_branch_name(branch)
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
                    self.branch,           # validated; placed before option flags
                    f"--since={since_dt}",
                    f"--format={_GIT_LOG_FORMAT}",
                    "--no-merges",
                    "--",                  # end of revision/option args; no path filter
                ],
                cwd=self._bare_path,
            )
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
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
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
                logger.warning("git fetch failed for %s: %s", self.repo_url, exc)
        else:
            logger.info("Cloning %s → %s", self.repo_url, self._bare_path)
            try:
                # `--` before URL prevents git from interpreting it as an option
                self._run(
                    ["git", "clone", "--bare", "--quiet", "--",
                     self.repo_url, str(self._bare_path)]
                )
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
                logger.error("git clone failed for %s: %s", self.repo_url, exc)
                raise

    def _get_diff_stat(self, sha: str) -> str:
        try:
            return self._run(
                ["git", "diff-tree", "--stat", "--no-commit-id", "-r", sha],
                cwd=self._bare_path,
            ).strip()
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return ""

    def _infer_url(self, sha: str) -> str:
        """Best-effort: convert known Git hosting URLs to web URLs."""
        url = self.repo_url.rstrip("/")
        if "git.kernel.org" in url:
            return f"{url}/commit/?id={sha}"
        if "github.com" in url:
            url = url.removesuffix(".git")
            return f"{url}/commit/{sha}"
        return f"{url}/commit/{sha}"

    @staticmethod
    def _run(cmd: list[str], cwd: Path | None = None) -> str:
        result = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, check=True,
            timeout=_GIT_TIMEOUT,
        )
        return result.stdout
