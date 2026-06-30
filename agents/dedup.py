"""Skip items whose output Markdown already exists on disk.

Re-runs of ``python -m agents.main`` overlap (``--since-hours 24`` called
daily, manual retries, backfills). Without this filter every overlapping item
goes back through the LLM batch, burning tokens.

The filesystem under ``web/src/content/`` is the source of truth (per root
CLAUDE.md); we don't keep a separate cache/DB because it would drift from the
on-disk Markdown. At daily-digest scale the scan is <10 ms.

We index by ``discussion_id`` / ``commit_hash`` read from YAML frontmatter
rather than parsing filenames — robust to filename-scheme changes and handles
the LLM-generated ``subsystem`` component of landing filenames.
"""

from __future__ import annotations

import logging
from datetime import date, datetime
from pathlib import Path

import yaml

from agents.models.raw import RawCommit, RawDiscussion
from agents.tools.series import series_id_for

logger = logging.getLogger(__name__)


def _read_frontmatter(path: Path) -> dict | None:
    """Return the YAML frontmatter dict, or None if unparseable."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        logger.debug("dedup: cannot read %s: %s", path, exc)
        return None

    # Frontmatter convention: file starts with `---\n`, fences a YAML block,
    # then another `---\n`, then the body.
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        logger.debug("dedup: malformed frontmatter in %s: %s", path, exc)
        return None
    return fm if isinstance(fm, dict) else None


def _coerce_date(value: object) -> date | None:
    """Best-effort parse of a frontmatter ``date`` value into a ``date``.

    Frontmatter dates are written day-granular (``YYYY-MM-DD``), which
    ``yaml.safe_load`` already returns as a ``datetime.date``. We still accept
    ``datetime`` and ISO-ish strings so older or hand-edited files don't break
    the scan.
    """
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value.strip()[:10])
        except ValueError:
            return None
    return None


def latest_content_date(content_root: Path) -> date | None:
    """Return the newest ``date`` across all on-disk digests, or ``None``.

    Deterministic (no LLM): reads the ``date`` frontmatter field of every
    ``discussions/*.md`` and ``landings/*.md`` file and returns the maximum.
    Used to bound how far back ingestion reaches — there is no point pulling
    history older than the newest article we already have, since dedup would
    drop it anyway. Returns ``None`` when there is no dated content yet (e.g.
    a first run or a purged tree), which callers treat as "no cap".
    """
    latest: date | None = None
    for subdir in ("discussions", "landings"):
        for path in (content_root / subdir).glob("*.md"):
            fm = _read_frontmatter(path)
            if not fm:
                continue
            d = _coerce_date(fm.get("date"))
            if d is not None and (latest is None or d > latest):
                latest = d
    return latest


def build_seen_index(
    content_root: Path,
) -> tuple[set[str], set[str], set[str]]:
    """Scan ``content_root`` for already-processed items.

    Returns ``(seen_discussion_ids, seen_commit_hashes, seen_series_ids)``.
    Missing subdirs are treated as empty — useful for first runs and for
    tests with clean dirs.

    The ``seen_series_ids`` set captures ``series_id`` values already
    represented by a canonical digest on disk; new incoming parts of the
    same series are skipped (they collapse into the existing canonical
    article rather than producing duplicates).
    """
    seen_ids: set[str] = set()
    seen_shas: set[str] = set()
    seen_series: set[str] = set()

    discussions_dir = content_root / "discussions"
    for path in discussions_dir.glob("*.md"):
        fm = _read_frontmatter(path)
        if not fm:
            continue
        if did := fm.get("discussion_id"):
            seen_ids.add(str(did))
        if sid := fm.get("series_id"):
            seen_series.add(str(sid))

    landings_dir = content_root / "landings"
    for path in landings_dir.glob("*.md"):
        fm = _read_frontmatter(path)
        if not fm:
            continue
        if sha := fm.get("commit_hash"):
            seen_shas.add(str(sha))
        if sid := fm.get("series_id"):
            seen_series.add(str(sid))

    return seen_ids, seen_shas, seen_series


def filter_raw(
    raw_discussions: list[RawDiscussion],
    raw_commits: list[RawCommit],
    seen_ids: set[str],
    seen_shas: set[str],
    seen_series: set[str] | None = None,
) -> tuple[list[RawDiscussion], list[RawCommit], int, int]:
    """Drop raw items whose digest already exists. Returns filtered lists +
    counts of skipped items.

    Skip rules:
      - Discussions whose ``id`` is already on disk.
      - Discussions whose ``series_id`` (derived from the subject) matches a
        canonical digest on disk — a later part of a seen series.
      - Commits whose ``sha`` is already on disk.
    """
    seen_series = seen_series or set()

    def _skip_discussion(d: RawDiscussion) -> bool:
        if d.id in seen_ids:
            return True
        sid = series_id_for(d.title, d.project)
        if sid and sid in seen_series:
            return True
        return False

    kept_discussions = [d for d in raw_discussions if not _skip_discussion(d)]
    kept_commits = [c for c in raw_commits if c.sha not in seen_shas]
    skipped_discussions = len(raw_discussions) - len(kept_discussions)
    skipped_commits = len(raw_commits) - len(kept_commits)
    return kept_discussions, kept_commits, skipped_discussions, skipped_commits
