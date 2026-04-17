"""Drop low-value items before we pay the LLM to digest them.

Cheap, deterministic rules only. If a rule is ambiguous it should err on the
side of *keeping* the item — the LLM can handle ambiguity, the feed reader
can't handle "Daily bump." showing up as a headline.
"""
from __future__ import annotations

import re

from agents.models.raw import RawCommit, RawDiscussion

# Commit messages that are noise by policy.
_NOISE_COMMIT_RE = re.compile(
    r"""
    ^(
        Daily\ bump\.?
      | Update\ copyright\ years?.*
      | Regenerate\ .*
      | Bump\ version.*
      | Merge\ (branch|tag|pull|remote-tracking).*
      | Revert\ ".*"                    # pure reverts with no extra context
      | Fix\ typo.*
    )\s*$
    """,
    re.IGNORECASE | re.VERBOSE | re.DOTALL,
)


def is_noise_commit(c: RawCommit) -> bool:
    """True when the commit is routine maintenance we shouldn't publish."""
    msg = (c.message or "").strip()
    if not msg:
        return True
    first_line = msg.splitlines()[0]
    if _NOISE_COMMIT_RE.match(first_line):
        return True
    return False


def is_noise_discussion(d: RawDiscussion) -> bool:
    """True for empty pings, ``+1`` replies, or trivially short bodies.

    A discussion with a diff attached is never noise even if the body is short
    — the diff itself is the content.
    """
    if d.diff_text:
        return False
    body = (d.body or "").strip()
    if len(body) < 200:
        return True
    return False


def filter_noise(
    discussions: list[RawDiscussion],
    commits: list[RawCommit],
) -> tuple[list[RawDiscussion], list[RawCommit], int, int]:
    """Return ``(kept_discussions, kept_commits, dropped_d, dropped_c)``."""
    kept_d = [d for d in discussions if not is_noise_discussion(d)]
    kept_c = [c for c in commits if not is_noise_commit(c)]
    return kept_d, kept_c, len(discussions) - len(kept_d), len(commits) - len(kept_c)
