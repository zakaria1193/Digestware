"""Clean up mailing-list / commit subject lines into readable headlines.

The raw subjects we ingest are things like::

    [PATCH v3 4/8] tests: misc: Use new tunable handling
    Re: [RFC] redesigning callbacks for make_forwarder_block

These are unreadable in a feed UI. This module strips the cruft and produces
a deterministic fallback headline when the LLM doesn't supply one.
"""
from __future__ import annotations

import re

_BRACKET_RE = re.compile(r"^\s*\[[^\]]*\]\s*")
_RE_PREFIX_RE = re.compile(r"^(?:\s*re\s*:\s*)+", re.IGNORECASE)
_SERIES_MARK_RE = re.compile(r"\b\d+\s*/\s*\d+\b")


def clean_subject(title: str) -> str:
    """Strip bracketed tags and ``Re:`` prefixes from a subject line.

    Examples:
        ``"[PATCH v3 4/8] tests: misc: Use new tunable handling"``
          → ``"tests: misc: Use new tunable handling"``
        ``"Re: [RFC] redesign callbacks"`` → ``"redesign callbacks"``
    """
    s = title or ""
    # Strip leading "Re:" chains first so bracket removal doesn't leave them.
    s = _RE_PREFIX_RE.sub("", s)
    # Strip all leading bracketed tags (may be multiple).
    while True:
        m = _BRACKET_RE.match(s)
        if not m:
            break
        s = s[m.end():]
    # Re-strip "Re:" in case it was nested inside brackets.
    s = _RE_PREFIX_RE.sub("", s)
    # Collapse residual whitespace.
    s = re.sub(r"\s+", " ", s).strip()
    # Drop trailing " N/M" series markers if they leaked through.
    s = _SERIES_MARK_RE.sub("", s).strip(" -:")
    return s or (title or "").strip()
