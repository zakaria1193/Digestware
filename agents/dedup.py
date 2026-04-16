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
from pathlib import Path

import yaml

from agents.models.raw import RawCommit, RawDiscussion

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


def build_seen_index(content_root: Path) -> tuple[set[str], set[str]]:
    """Scan ``content_root`` for already-processed items.

    Returns ``(seen_discussion_ids, seen_commit_hashes)``. Missing subdirs are
    treated as empty — useful for first runs and for tests with clean dirs.
    """
    seen_ids: set[str] = set()
    seen_shas: set[str] = set()

    discussions_dir = content_root / "discussions"
    for path in discussions_dir.glob("*.md"):
        fm = _read_frontmatter(path)
        if fm and (did := fm.get("discussion_id")):
            seen_ids.add(str(did))

    landings_dir = content_root / "landings"
    for path in landings_dir.glob("*.md"):
        fm = _read_frontmatter(path)
        if fm and (sha := fm.get("commit_hash")):
            seen_shas.add(str(sha))

    return seen_ids, seen_shas


def filter_raw(
    raw_discussions: list[RawDiscussion],
    raw_commits: list[RawCommit],
    seen_ids: set[str],
    seen_shas: set[str],
) -> tuple[list[RawDiscussion], list[RawCommit], int, int]:
    """Drop raw items whose digest already exists. Returns filtered lists +
    counts of skipped items."""
    kept_discussions = [d for d in raw_discussions if d.id not in seen_ids]
    kept_commits = [c for c in raw_commits if c.sha not in seen_shas]
    skipped_discussions = len(raw_discussions) - len(kept_discussions)
    skipped_commits = len(raw_commits) - len(kept_commits)
    return kept_discussions, kept_commits, skipped_discussions, skipped_commits
