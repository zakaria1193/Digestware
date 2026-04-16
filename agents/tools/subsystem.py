"""Deterministic subsystem extraction.

We never want ``subsystem: unknown`` in published frontmatter — it's ugly in
URLs and kills discoverability. This module derives the subsystem from the
commit subject / discussion title first, then from the diff_stat, then falls
back to the project name. The LLM is only consulted as a last resort elsewhere
in the pipeline.
"""
from __future__ import annotations

import re

# Subject-line pattern: ``middle-end/124877 - …``, ``gcc/ipa: …``,
# ``tests: foo``, ``malloc: …``, ``[PATCH] gcc/c++: …``
_SUBJECT_PATTERNS = [
    # Strip leading [PATCH …] / [RFC …] brackets before matching.
    re.compile(r"^\s*(?P<sub>[a-z][a-z0-9/+_.-]{1,48})\s*[:/-]\s", re.IGNORECASE),
]

# Typical top-level directories per project. Order matters: more specific first.
_TOPDIR_KEYS = (
    "gcc",
    "libgcc",
    "libstdc++-v3",
    "gcc/ipa",
    "gcc/c-family",
    "gcc/c++",
    "gcc/cp",
    "gcc/fortran",
    "gcc/go",
    "gcc/testsuite",
    "binutils",
    "ld",
    "gas",
    "gold",
    "bfd",
    "libc",
    "malloc",
    "nptl",
    "elf",
    "stdio",
    "string",
    "sysdeps",
    "nss",
    "locale",
    "kernel",
    "mm",
    "net",
    "drivers",
    "fs",
    "arch",
    "tools",
    "tests",
)


def _strip_brackets(title: str) -> str:
    """Remove ``[PATCH v2 1/3]`` / ``[RFC]`` / ``Re:`` prefixes.

    Runs both strippers in a loop so ``"Re: [PATCH] …"`` reduces cleanly:
    strip Re:, see a leading bracket, strip it, loop again.
    """
    s = title
    while True:
        before = s
        # Drop leading "Re:" chains.
        s = re.sub(r"^(?:\s*re\s*:\s*)+", "", s, flags=re.IGNORECASE)
        # Drop leading bracketed blocks.
        m = re.match(r"^\s*\[[^\]]*\]\s*", s)
        if m:
            s = s[m.end():]
        if s == before:
            break
    return s.strip()


def _first_diffstat_path(diff_stat: str | None) -> str | None:
    """Return the first file path from a one-line-per-file diff_stat."""
    if not diff_stat:
        return None
    # diff_stat looks like "+45/-12 in 3 files" (one-liner) OR multi-line
    # "gcc/ipa-inline.cc | 10 +--\n gcc/cgraph.cc | 3 +\n". Try to pick a path.
    for line in diff_stat.splitlines():
        m = re.search(r"([a-zA-Z0-9_./+-]+\.[a-zA-Z0-9]+)", line)
        if m and "/" in m.group(1):
            return m.group(1)
    return None


def _from_top_dir(path: str) -> str | None:
    """Map a file path to a coarse subsystem via the top-level directory."""
    parts = path.split("/")
    if len(parts) < 2:
        return None
    top = parts[0].lower()
    if top in _TOPDIR_KEYS:
        # Use the two first segments if they're both meaningful (e.g. gcc/ipa).
        second = parts[1].lower()
        if f"{top}/{second}" in _TOPDIR_KEYS:
            return f"{top}/{second}"
        return top
    return None


def extract_subsystem(
    title: str,
    diff_stat: str | None = None,
    project: str = "unknown",
) -> str:
    """Best-effort deterministic subsystem label.

    Priority: subject-line prefix → first diff_stat path → project name.
    Never returns ``"unknown"`` if any signal is present; falls back to the
    project label, which is always known.
    """
    cleaned = _strip_brackets(title or "")
    for pat in _SUBJECT_PATTERNS:
        m = pat.match(cleaned)
        if m:
            sub = m.group("sub").lower().strip(" :/-")
            # ``middle-end/124877`` → ``middle-end``: trailing numeric segment
            # (a PR/bug number, not a real subdirectory) is dropped.
            parts = sub.split("/")
            if len(parts) >= 2 and parts[-1].isdigit():
                sub = "/".join(parts[:-1])
            # Guard against single-letter false positives.
            if len(sub) >= 2:
                return sub

    path = _first_diffstat_path(diff_stat)
    if path:
        td = _from_top_dir(path)
        if td:
            return td

    return project if project and project != "unknown" else "general"
