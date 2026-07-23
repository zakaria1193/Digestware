"""Deterministic exclusions for the ``primer_glossary`` ("For Context") block.

The glossary targets a systems programmer who isn't a toolchain specialist,
but every reader of this digest already knows which top-level project it's
about — the digest's own ``project``/``subsystem`` fields say "gcc" or
"binutils" on every article. The cheap model still defines those names as if
they were subsystem jargon; filter them out post-hoc rather than trusting
the prompt alone.
"""
from __future__ import annotations

import re

# Project / toolchain names a systems-programmer reader is assumed to
# already know, so they should never appear as a defined glossary entry.
EXCLUDED_TERMS = frozenset({
    "gcc",
    "g++",
    "binutils",
    "gnu binutils",
    "glibc",
    "gdb",
    "gnu",
    "llvm",
    "clang",
    "linux",
    "linux kernel",
    "newlib",
})

_EXCLUDED_RE = re.compile(
    r"^\s*(the\s+)?("
    + "|".join(re.escape(t) for t in sorted(EXCLUDED_TERMS, key=len, reverse=True))
    + r")\s*$",
    re.IGNORECASE,
)


def is_excluded_term(term: str) -> bool:
    """True when ``term`` is a top-level project name that needs no definition."""
    if not term:
        return False
    return bool(_EXCLUDED_RE.match(term.strip()))


def filter_glossary(entries: list) -> list:
    """Drop glossary entries whose ``term`` is a top-level project name."""
    return [
        e for e in entries
        if not (isinstance(e, dict) and is_excluded_term(e.get("term", "")))
    ]
