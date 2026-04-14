"""PublicInbox adapter — mirrors Sourceware mailing lists and parses mbox emails.

Implements both DiscussionSource (discussion lists) and CommitSource (CVS lists).

Strategy:
1. `git clone --mirror https://inbox.sourceware.org/{list}/0` on first run.
2. `git fetch` on subsequent runs (fast incremental sync).
3. Epochs /0, /1, /2 … are discovered automatically (up to _MAX_EPOCH_ATTEMPTS).
4. ALL epoch paths are iterated — not just epoch 0.
5. On mirror failure → returns [] + warning log (never raises to caller).

Note: NNTP (nntplib) has been removed — news.gmane.io shut down in 2020 and
nntplib is removed in Python 3.13. Future real-time fallback can be implemented
via the lore.kernel.org/{list}/latest.atom HTTP feed.

Raw mbox bytes are cached to agents/cache/raw/{message_id}.mbox with a TTL
of _MBOX_TTL_DAYS days to cap disk usage.
"""

import email
import email.policy
import logging
import re
import subprocess
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

from agents.models.raw import RawCommit, RawDiscussion

logger = logging.getLogger(__name__)

_SOURCEWARE_INBOX = "https://inbox.sourceware.org"
_MAX_EPOCH_ATTEMPTS = 10
_GIT_TIMEOUT = 120                           # seconds — clone/fetch may be slow
_MBOX_TTL_DAYS = 30                          # delete cached mbox after this many days
_LIST_NAME_RE = re.compile(r"^[a-z][a-z0-9-]{0,63}$")  # strict allowlist


def _validate_list_name(name: str) -> None:
    """Raise ValueError if *name* could cause git-option injection."""
    if not _LIST_NAME_RE.match(name):
        raise ValueError(
            f"Invalid list name {name!r}: must match {_LIST_NAME_RE.pattern}"
        )


def _since_iso(since_hours: int) -> str:
    """Return an ISO-8601 timestamp *since_hours* ago."""
    ts = datetime.now(tz=timezone.utc).timestamp() - since_hours * 3600
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def _run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> str:
    """Run a subprocess with a timeout and return stdout as a string."""
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=check,
        timeout=_GIT_TIMEOUT,
    )
    return result.stdout


def _mirror_list(list_name: str, base_cache: Path) -> list[Path]:
    """Clone or fetch all public-inbox epochs for *list_name*.

    Iterates epochs /0, /1, /2 … up to _MAX_EPOCH_ATTEMPTS and returns a
    list of ALL successfully-mirrored bare-clone paths.  Returns [] only when
    every epoch fails.
    """
    _validate_list_name(list_name)
    epoch_paths: list[Path] = []
    for epoch in range(_MAX_EPOCH_ATTEMPTS):
        url = f"{_SOURCEWARE_INBOX}/{list_name}/{epoch}"
        dest = base_cache / f"{list_name}.{epoch}.git"
        if dest.exists():
            try:
                _run(["git", "fetch", "--quiet"], cwd=dest)
                logger.debug("Fetched %s epoch %d", list_name, epoch)
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
                logger.warning("git fetch failed for %s/%d: %s", list_name, epoch, exc)
            epoch_paths.append(dest)
        else:
            result = subprocess.run(
                ["git", "clone", "--mirror", "--quiet", "--", url, str(dest)],
                capture_output=True,
                text=True,
                timeout=_GIT_TIMEOUT,
            )
            if result.returncode != 0:
                # No more epochs exist — stop probing
                break
            logger.info("Cloned %s epoch %d → %s", list_name, epoch, dest)
            epoch_paths.append(dest)
    return epoch_paths


class PublicInboxAdapter:
    """Mirrors public-inbox lists and parses mbox messages."""

    def __init__(
        self,
        discussion_lists: list[str],
        cvs_lists: list[str],
        cache_dir: Path,
        use_nntp: bool = True,  # accepted for API compatibility; NNTP not implemented
    ) -> None:
        for name in discussion_lists + cvs_lists:
            _validate_list_name(name)
        self.discussion_lists = discussion_lists
        self.cvs_lists = cvs_lists
        self.cache_dir = Path(cache_dir)
        self._raw_cache = self.cache_dir / "raw"
        self._raw_cache.mkdir(parents=True, exist_ok=True)
        self._prune_mbox_cache()

    # ------------------------------------------------------------------
    # DiscussionSource protocol
    # ------------------------------------------------------------------

    def fetch_discussions(self, since_hours: int = 24) -> list[RawDiscussion]:
        discussions: list[RawDiscussion] = []
        for list_name in self.discussion_lists:
            discussions.extend(self._fetch_list_discussions(list_name, since_hours))
        return discussions

    def _fetch_list_discussions(
        self, list_name: str, since_hours: int
    ) -> list[RawDiscussion]:
        epoch_paths = _mirror_list(list_name, self.cache_dir)
        if not epoch_paths:
            logger.warning("Could not mirror any epoch for %s — skipping", list_name)
            return []

        since_dt = _since_iso(since_hours)
        seen_ids: set[str] = set()
        discussions: list[RawDiscussion] = []
        for mirror in epoch_paths:
            for d in self._parse_epoch_discussions(mirror, list_name, since_dt):
                if d.id not in seen_ids:
                    seen_ids.add(d.id)
                    discussions.append(d)
        return discussions

    def _parse_epoch_discussions(
        self, mirror: Path, list_name: str, since_dt: str
    ) -> list[RawDiscussion]:
        """Yield RawDiscussion objects from a single epoch mirror."""
        try:
            # Use --since= to avoid walking the entire repo history
            shas = _run(
                ["git", "log", f"--since={since_dt}", "--format=%H"],
                cwd=mirror,
            ).splitlines()
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
            logger.warning("git log failed for %s: %s", mirror, exc)
            return []

        results: list[RawDiscussion] = []
        for sha in shas:
            raw = self._get_mbox(sha, mirror)
            if raw is None:
                continue
            msg = email.message_from_bytes(raw, policy=email.policy.default)
            message_id = msg.get("Message-ID", sha).strip("<>")
            self._cache_mbox(message_id, raw)
            msg_date = self._parse_date(msg.get("Date", ""))
            results.append(
                RawDiscussion(
                    id=message_id,
                    title=str(msg.get("Subject", "(no subject)")),
                    body=self._get_body(msg),
                    author=str(msg.get("From", "unknown")),
                    date=msg_date or datetime.now(tz=timezone.utc),
                    url=f"{_SOURCEWARE_INBOX}/{list_name}/{message_id}",
                    replies=[],
                    diff_text=self._extract_diff(msg),
                    source_type="public_inbox",
                    metadata={"list": list_name, "sha": sha},
                )
            )
        return results

    # ------------------------------------------------------------------
    # CommitSource protocol
    # ------------------------------------------------------------------

    def fetch_commits(self, since_hours: int = 24) -> list[RawCommit]:
        commits: list[RawCommit] = []
        for list_name in self.cvs_lists:
            commits.extend(self._fetch_list_commits(list_name, since_hours))
        return commits

    def _fetch_list_commits(
        self, list_name: str, since_hours: int
    ) -> list[RawCommit]:
        epoch_paths = _mirror_list(list_name, self.cache_dir)
        if not epoch_paths:
            logger.warning(
                "Could not mirror any epoch for CVS list %s — skipping", list_name
            )
            return []

        since_dt = _since_iso(since_hours)
        seen_shas: set[str] = set()
        commits: list[RawCommit] = []
        for mirror in epoch_paths:
            for c in self._parse_epoch_commits(mirror, list_name, since_dt):
                if c.sha not in seen_shas:
                    seen_shas.add(c.sha)
                    commits.append(c)
        return commits

    def _parse_epoch_commits(
        self, mirror: Path, list_name: str, since_dt: str
    ) -> list[RawCommit]:
        """Yield RawCommit objects from a single CVS-list epoch mirror."""
        try:
            shas = _run(
                ["git", "log", f"--since={since_dt}", "--format=%H"],
                cwd=mirror,
            ).splitlines()
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
            logger.warning("git log failed for %s: %s", mirror, exc)
            return []

        results: list[RawCommit] = []
        for sha in shas:
            raw = self._get_mbox(sha, mirror)
            if raw is None:
                continue
            msg = email.message_from_bytes(raw, policy=email.policy.default)
            message_id = msg.get("Message-ID", sha).strip("<>")
            commit_sha = self._extract_commit_sha(msg)
            self._cache_mbox(message_id, raw)
            msg_date = self._parse_date(msg.get("Date", ""))
            results.append(
                RawCommit(
                    sha=commit_sha or sha,
                    author=str(msg.get("From", "unknown")),
                    date=msg_date or datetime.now(tz=timezone.utc),
                    message=str(msg.get("Subject", "")),
                    diff_stat=self._extract_diff_stat(msg),
                    url=f"{_SOURCEWARE_INBOX}/{list_name}/{message_id}",
                    source_type="public_inbox",
                    metadata={"list": list_name, "message_id": message_id},
                )
            )
        return results

    # ------------------------------------------------------------------
    # Cache management
    # ------------------------------------------------------------------

    def _prune_mbox_cache(self) -> None:
        """Delete mbox files older than _MBOX_TTL_DAYS to prevent unbounded growth."""
        cutoff = datetime.now(tz=timezone.utc).timestamp() - _MBOX_TTL_DAYS * 86400
        pruned = 0
        for f in self._raw_cache.glob("*.mbox"):
            try:
                if f.stat().st_mtime < cutoff:
                    f.unlink()
                    pruned += 1
            except OSError:
                pass
        if pruned:
            logger.info("Pruned %d stale mbox files from %s", pruned, self._raw_cache)

    def _get_mbox(self, sha: str, mirror: Path) -> bytes | None:
        try:
            result = subprocess.run(
                ["git", "show", f"{sha}:m"],
                cwd=mirror,
                capture_output=True,
                check=True,
                timeout=_GIT_TIMEOUT,
            )
            return result.stdout
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return None

    def _cache_mbox(self, message_id: str, raw: bytes) -> None:
        safe_id = re.sub(r"[^\w@.-]", "_", message_id)
        path = self._raw_cache / f"{safe_id}.mbox"
        try:
            path.write_bytes(raw)
        except OSError as exc:
            logger.debug("Could not cache mbox %s: %s", message_id, exc)

    # ------------------------------------------------------------------
    # Email parsing helpers (static — no state needed)
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_date(date_str: str) -> datetime | None:
        if not date_str:
            return None
        try:
            return parsedate_to_datetime(date_str)
        except Exception:
            return None

    @staticmethod
    def _get_body(msg: email.message.Message) -> str:
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    payload = part.get_payload(decode=True)
                    if isinstance(payload, bytes):
                        return payload.decode("utf-8", errors="replace")
        payload = msg.get_payload(decode=True)
        if isinstance(payload, bytes):
            return payload.decode("utf-8", errors="replace")
        return str(payload or "")

    @staticmethod
    def _extract_diff(msg: email.message.Message) -> str | None:
        body = PublicInboxAdapter._get_body(msg)
        if "--- a/" in body and "+++ b/" in body:
            return body
        return None

    @staticmethod
    def _extract_diff_stat(msg: email.message.Message) -> str:
        body = PublicInboxAdapter._get_body(msg)
        lines = [ln for ln in body.splitlines() if re.search(r"\|\s+\d+", ln)]
        return "\n".join(lines[:20]) if lines else ""

    @staticmethod
    def _extract_commit_sha(msg: email.message.Message) -> str | None:
        body = PublicInboxAdapter._get_body(msg)
        match = re.search(r"\b([0-9a-f]{40})\b", body)
        return match.group(1) if match else None
