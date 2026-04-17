"""Detect and collapse ``[PATCH N/M]`` series into a single canonical story.

A patch series on a mailing list arrives as many separate emails:

    [PATCH 0/5] malloc: introduce ifuncs for malloc functions   ← cover letter
    [PATCH 1/5] …
    [PATCH 2/5] …
    …

Without collapsing, each email becomes its own article — readers see 6 near-
duplicate cards in the feed. This module:

1. Builds a stable ``series_id`` from the subject so all parts of a series
   group together.
2. Picks a *canonical* item (the cover letter, else the first part) to
   represent the series in the feed.
3. Returns the non-canonical parts as ``{title, url}`` dicts so the canonical
   item can link to them.
"""
from __future__ import annotations

import re
from collections.abc import Callable
from typing import TypeVar

from agents.tools.headline import clean_subject

T = TypeVar("T")


# Captures (version, n, total) from ``[PATCH v3 4/8] …``. ``v`` and the number
# within the series are optional to cover ``[PATCH 4/8]`` and bare ``[PATCH]``.
_PATCH_TAG_RE = re.compile(
    r"\[\s*(?:RFC\s+)?PATCH"
    r"(?:\s+v(?P<ver>\d+))?"
    r"(?:\s+(?P<n>\d+)\s*/\s*(?P<total>\d+))?"
    r"\s*\]",
    re.IGNORECASE,
)


def parse_patch_tag(title: str) -> dict | None:
    """Return ``{version, n, total}`` if title has a ``[PATCH …]`` tag."""
    if not title:
        return None
    m = _PATCH_TAG_RE.search(title)
    if not m:
        return None
    return {
        "version": int(m.group("ver")) if m.group("ver") else 1,
        "n": int(m.group("n")) if m.group("n") else None,
        "total": int(m.group("total")) if m.group("total") else None,
    }


def series_id_for(title: str, project: str = "") -> str | None:
    """Stable id shared by every part of the same series.

    Returned value is ``project:<cleaned-subject>`` (no version, no N/M).
    Two items with the same returned id belong to the same series. Returns
    ``None`` if the title doesn't look like a patch series part.
    """
    tag = parse_patch_tag(title or "")
    if not tag or tag.get("total") is None:
        return None
    cleaned = clean_subject(title).lower()
    # Normalise whitespace and strip trailing punctuation.
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" -:.,")
    if not cleaned:
        return None
    return f"{project or 'unknown'}:{cleaned}"


def split_canonical(
    items: list[T],
    title_of: Callable[[T], str],
    project_of: Callable[[T], str],
    url_of: Callable[[T], str],
) -> tuple[list[T], dict[int, list[dict]]]:
    """Keep one canonical item per series; return the remainders as pointers.

    Returns:
        (canonical_items, parts_by_index) where parts_by_index maps the index
        of the canonical item **in the returned list** to a list of
        ``{title, url, n, total}`` dicts for the non-canonical parts.

    The canonical choice prefers:
      1. The cover letter (``n == 0``), newest version wins.
      2. Otherwise the first part seen, newest version wins.
      3. Standalone items (no series_id) are always canonical and have no
         parts entry.
    """
    by_series: dict[str, list[tuple[int, T, dict]]] = {}
    standalone: list[T] = []
    order: list[str] = []

    for i, item in enumerate(items):
        title = title_of(item)
        sid = series_id_for(title, project_of(item))
        if sid is None:
            standalone.append(item)
            continue
        tag = parse_patch_tag(title) or {}
        if sid not in by_series:
            by_series[sid] = []
            order.append(sid)
        by_series[sid].append((i, item, tag))

    canonical: list[T] = list(standalone)
    parts_by_index: dict[int, list[dict]] = {}

    for sid in order:
        group = by_series[sid]
        group.sort(
            key=lambda t: (
                -(t[2].get("version") or 1),   # newest version first
                0 if (t[2].get("n") == 0) else 1,   # cover letter first
                t[2].get("n") or 9999,         # then by N ascending
                t[0],                          # then by original order
            )
        )
        chosen_idx, chosen_item, _ = group[0]
        canonical_index = len(canonical)
        canonical.append(chosen_item)
        if len(group) > 1:
            parts_by_index[canonical_index] = [
                {
                    "title": clean_subject(title_of(it)),
                    "url": url_of(it),
                    "n": tg.get("n"),
                    "total": tg.get("total"),
                }
                for (_, it, tg) in group[1:]
            ]

    return canonical, parts_by_index
