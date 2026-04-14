"""PublicInbox adapter — mirrors Sourceware mailing lists and parses mbox emails.

Implements both DiscussionSource (discussion lists) and CommitSource (CVS lists).

Strategy:
1. `git clone --mirror https://inbox.sourceware.org/{list}/0` on first run.
2. `git fetch` on subsequent runs (fast incremental sync).
3. Epochs /0, /1, /2 … are discovered automatically.
4. Falls back to NNTP (stdlib nntplib) for near-real-time messages when
   `use_nntp=True` and the NNTP server is reachable.
5. On any error → returns [] + warning log (never raises to caller).

Raw mbox bytes are cached to agents/cache/raw/{message_id}.mbox.
"""

import email
import email.policy
import logging
import nntplib
import re
import subprocess
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

from agents.models.raw import RawCommit, RawDiscussion

logger = logging.getLogger(__name__)

_SOURCEWARE_INBOX = "https://inbox.sourceware.org"
_NNTP_HOST = "news.gmane.io"


def _run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> str:
    """Run a subprocess and return stdout as a string."""
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=check,
    )
    return result.stdout


def _mirror_list(list_name: str, base_cache: Path) -> Path:
    """Clone or fetch a public-inbox mirror for *list_name*.

    Tries epochs /0, /1, /2 until the server returns a non-zero exit code.
    Returns the path of the primary (epoch 0) bare clone.
    """
    epoch = 0
    primary: Path | None = None
    while True:
        url = f"{_SOURCEWARE_INBOX}/{list_name}/{epoch}"
        dest = base_cache / f"{list_name}.{epoch}.git"
        if dest.exists():
            try:
                _run(["git", "fetch", "--quiet"], cwd=dest)
                logger.debug("Fetched %s epoch %d", list_name, epoch)
            except subprocess.CalledProcessError as exc:
                logger.warning("git fetch failed for %s/%d: %s", list_name, epoch, exc)
        else:
            result = subprocess.run(
                ["git", "clone", "--mirror", "--quiet", url, str(dest)],
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                # No more epochs
                break
            logger.info("Cloned %s epoch %d → %s", list_name, epoch, dest)
        if primary is None:
            primary = dest
        epoch += 1
    if primary is None:
        raise RuntimeError(f"Could not mirror {list_name} from {_SOURCEWARE_INBOX}")
    return primary


class PublicInboxAdapter:
    """Mirrors public-inbox lists and parses mbox messages."""

    def __init__(
        self,
        discussion_lists: list[str],
        cvs_lists: list[str],
        cache_dir: Path,
        use_nntp: bool = True,
    ) -> None:
        self.discussion_lists = discussion_lists
        self.cvs_lists = cvs_lists
        self.cache_dir = Path(cache_dir)
        self.use_nntp = use_nntp
        self._raw_cache = self.cache_dir / "raw"
        self._raw_cache.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # DiscussionSource protocol
    # ------------------------------------------------------------------

    def fetch_discussions(self, since_hours: int = 24) -> list[RawDiscussion]:
        discussions: list[RawDiscussion] = []
        for list_name in self.discussion_lists:
            discussions.extend(
                self._fetch_list_discussions(list_name, since_hours)
            )
        return discussions

    def _fetch_list_discussions(
        self, list_name: str, since_hours: int
    ) -> list[RawDiscussion]:
        try:
            mirror = _mirror_list(list_name, self.cache_dir)
        except Exception as exc:
            logger.warning("Could not mirror %s: %s — skipping", list_name, exc)
            if self.use_nntp:
                return self._nntp_fetch_discussions(list_name, since_hours)
            return []

        shas = _run(["git", "log", "--format=%H"], cwd=mirror).splitlines()
        cutoff = datetime.now(tz=timezone.utc).timestamp() - since_hours * 3600
        discussions: list[RawDiscussion] = []
        for sha in shas:
            raw = self._get_mbox(sha, mirror)
            if raw is None:
                continue
            msg = email.message_from_bytes(raw, policy=email.policy.default)
            msg_date = self._parse_date(msg.get("Date", ""))
            if msg_date and msg_date.timestamp() < cutoff:
                continue
            message_id = msg.get("Message-ID", sha).strip("<>")
            self._cache_mbox(message_id, raw)
            discussions.append(
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
        return discussions

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
        try:
            mirror = _mirror_list(list_name, self.cache_dir)
        except Exception as exc:
            logger.warning(
                "Could not mirror CVS list %s: %s — skipping", list_name, exc
            )
            return []

        shas = _run(["git", "log", "--format=%H"], cwd=mirror).splitlines()
        cutoff = datetime.now(tz=timezone.utc).timestamp() - since_hours * 3600
        commits: list[RawCommit] = []
        for sha in shas:
            raw = self._get_mbox(sha, mirror)
            if raw is None:
                continue
            msg = email.message_from_bytes(raw, policy=email.policy.default)
            msg_date = self._parse_date(msg.get("Date", ""))
            if msg_date and msg_date.timestamp() < cutoff:
                continue
            message_id = msg.get("Message-ID", sha).strip("<>")
            commit_sha = self._extract_commit_sha(msg)
            self._cache_mbox(message_id, raw)
            commits.append(
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
        return commits

    # ------------------------------------------------------------------
    # NNTP fallback
    # ------------------------------------------------------------------

    def _nntp_fetch_discussions(
        self, list_name: str, since_hours: int
    ) -> list[RawDiscussion]:
        if not self.use_nntp:
            return []
        group = f"gmane.{list_name.replace('-', '.')}"
        try:
            server = nntplib.NNTP(_NNTP_HOST, timeout=10)
            _, _, first, last, _ = server.group(group)
            start = max(int(first), int(last) - 200)
            _, overviews = server.over((start, int(last)))
            discussions: list[RawDiscussion] = []
            cutoff = datetime.now(tz=timezone.utc).timestamp() - since_hours * 3600
            for art_num, overview in overviews:
                subject = overview.get("subject", "")
                date_str = overview.get("date", "")
                msg_date = self._parse_date(date_str)
                if msg_date and msg_date.timestamp() < cutoff:
                    continue
                message_id = overview.get("message-id", str(art_num)).strip("<>")
                discussions.append(
                    RawDiscussion(
                        id=message_id,
                        title=subject,
                        body="",
                        author=overview.get("from", "unknown"),
                        date=msg_date or datetime.now(tz=timezone.utc),
                        url=f"{_SOURCEWARE_INBOX}/{list_name}/{message_id}",
                        replies=[],
                        diff_text=None,
                        source_type="public_inbox",
                        metadata={"list": list_name, "nntp": True},
                    )
                )
            server.quit()
            return discussions
        except Exception as exc:
            logger.warning("NNTP fallback failed for %s: %s", list_name, exc)
            return []

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _get_mbox(self, sha: str, mirror: Path) -> bytes | None:
        try:
            result = subprocess.run(
                ["git", "show", f"{sha}:m"],
                cwd=mirror,
                capture_output=True,
                check=True,
            )
            return result.stdout
        except subprocess.CalledProcessError:
            return None

    def _cache_mbox(self, message_id: str, raw: bytes) -> None:
        safe_id = re.sub(r"[^\w@.-]", "_", message_id)
        path = self._raw_cache / f"{safe_id}.mbox"
        try:
            path.write_bytes(raw)
        except OSError as exc:
            logger.debug("Could not cache mbox %s: %s", message_id, exc)

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
