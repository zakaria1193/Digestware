"""Retro-apply the noise filter to already-published markdown.

The pre-ingestion `filter_noise` only gates fresh `RawDiscussion` /
`RawCommit` objects, so it can't fix entries that were published before a
new noise pattern was added. This module rescans every markdown file under
`web/src/content/{discussions,landings}/` and stamps `is_stub: true` on the
ones that today's rules would have dropped — the public site already
filters `is_stub`, so the entries become admin-only without disturbing
links or RSS history.
"""
from __future__ import annotations

import logging
import re
from pathlib import Path

import yaml

from agents.tools.noise_filter import (
    _NOISE_AUTHOR_RE,
    _NOISE_DISCUSSION_TITLE_RE,
    _SPAM_TITLE_RE,
)

logger = logging.getLogger(__name__)

# Mirrors the floor in main.py — keep in sync.
_MIN_LANDING_SCORE = 4

# Pre-compiled here so we don't rebuild it on every file.
_IS_STUB_LINE_RE = re.compile(r"^is_stub:.*$", re.MULTILINE)
_STUB_REASON_LINE_RE = re.compile(r"^stub_reason:.*$", re.MULTILINE)


def matches_noise_rules(title: str, author: str | None) -> str | None:
    """Return the rule name that matches, or None.

    Mirrors `is_noise_discussion` minus the short-body check (we never have
    the raw body once a digest has been written).
    """
    title = (title or "").strip()
    author = (author or "").strip()
    if title and _NOISE_DISCUSSION_TITLE_RE.search(title):
        return "title-noise"
    if title and _SPAM_TITLE_RE.search(title):
        return "spam"
    if author and _NOISE_AUTHOR_RE.search(author):
        return "bot-author"
    return None


def _set_stub_fields(frontmatter_text: str, reason: str) -> str:
    if _IS_STUB_LINE_RE.search(frontmatter_text):
        text = _IS_STUB_LINE_RE.sub("is_stub: true", frontmatter_text)
    else:
        text = frontmatter_text.rstrip("\n") + "\nis_stub: true\n"
    if _STUB_REASON_LINE_RE.search(text):
        return _STUB_REASON_LINE_RE.sub(f"stub_reason: {reason}", text)
    return text.rstrip("\n") + f"\nstub_reason: {reason}\n"


def _process_file(path: Path) -> str | None:
    """Mark a single file as stub when it matches a noise rule.

    Returns the matched rule name when the file was newly marked, else
    None (already stub, no match, or unparseable).
    """
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        logger.warning("retro_noise: skipping unparseable frontmatter in %s", path)
        return None
    if fm.get("is_stub"):
        return None

    title = fm.get("title") or fm.get("headline") or ""
    author = fm.get("proposer") or fm.get("author") or ""
    rule = matches_noise_rules(title, author)

    # Score floor for landings — retroactively suppress cosmetic/docs/typo
    # commits that slipped through before this threshold existed.
    if rule is None and path.parent.name == "landings":
        score = fm.get("impact_score")
        if score is not None and score < _MIN_LANDING_SCORE:
            rule = "low-score"

    if rule is None:
        return None
    new_fm = _set_stub_fields(parts[1], rule)
    path.write_text(f"---{new_fm}---{parts[2]}", encoding="utf-8")
    return rule


def sweep_content_root(content_root: Path) -> dict[str, int]:
    """Rescan content under `content_root` and mark new noise as stubs.

    Returns a counts dict keyed by rule name plus a ``total`` entry. The
    pass is idempotent — files already marked are skipped without rewrite.
    """
    counts: dict[str, int] = {"title-noise": 0, "spam": 0, "bot-author": 0, "low-score": 0}
    for subdir in ("discussions", "landings"):
        for path in sorted((content_root / subdir).glob("*.md")):
            rule = _process_file(path)
            if rule is not None:
                counts[rule] += 1
                logger.debug("retro_noise: marked %s (%s)", path, rule)
    counts["total"] = sum(counts.values())
    return counts
