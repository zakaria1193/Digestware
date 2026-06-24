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
      | Automatic\ date\ update.*       # binutils/BFD version.h date bump
      | Update\ copyright\ years?.*
      | Update\ .*version.*header.*     # generic "Update * version header" bumps
      | Regenerate\ .*
      | Bump\ version.*
      | Merge\ (branch|tag|pull|remote-tracking).*
      | Revert\ ".*"                    # pure reverts with no extra context
      | Fix\ typo.*
    )\s*$
    """,
    re.IGNORECASE | re.VERBOSE | re.DOTALL,
)

# Discussion subjects that are bot- or release-management chatter — they
# carry no technical content even with a long body.
_NOISE_DISCUSSION_TITLE_RE = re.compile(
    r"""
    (
        # Snapshot / point-release announcements:
        #   "gcc-16-20260509 is now available", "binutils-2.46 is now available"
        ^[\s☝]*(re:\s*)?(gcc|binutils|glibc|gdb|newlib)
        -\d+(\.\d+)*(-\d{8})?\ is\ now\ available
        # Release-candidate announcements: "Second GCC 16.1 Release Candidate available …"
      | (first|second|third|fourth|fifth|\d+(st|nd|rd|th))?\s*
        (gcc|binutils|glibc|gdb|newlib)\s+\d+(\.\d+)*\s+release\s+candidate
        # Buildbot mails: "Buildbot (Sourceware): …" or "☝ Buildbot: …"
      | ^[\s☝]*(re:\s*)?buildbot\b
    )
    """,
    re.IGNORECASE | re.VERBOSE,
)

# Authors / senders that are bots. Match the recognisable prefix; bot accounts
# vary in their full email but the local-part is stable.
_NOISE_AUTHOR_RE = re.compile(
    r"""
    \b(
        builder@sourceware\.org
      | buildbot@
      | sourceware-builder@
      | builder@[\w.-]*sourceware
    )\b
    """,
    re.IGNORECASE | re.VERBOSE,
)

# Obvious off-topic / commercial spam. Real toolchain threads never contain
# these terms; matching any one of them in the title is sufficient.
_SPAM_TITLE_RE = re.compile(
    r"""
    \b(
        dermatologist
      | ultrasonic\ transducer
      | guangzhou\ fair
      | overseas\ property
      | study\ abroad
      | immigration\ expo
      | crypto(currency)?\ invest
      | loan\ offer
      | sex(ual)?\ enhance
      | weight\ loss
      | viagra
      | casino
      | bitcoin\ giveaway
    )\b
    """,
    re.IGNORECASE | re.VERBOSE,
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
    """True for bots, release/buildbot chatter, spam, or trivial pings.

    A discussion with a diff attached is exempt from the short-body rule —
    the diff itself is the content. Bot/spam/release rules still apply
    regardless of body length or diff presence.
    """
    title = (d.title or "").strip()
    if _NOISE_DISCUSSION_TITLE_RE.search(title):
        return True
    if _SPAM_TITLE_RE.search(title):
        return True
    author = (d.author or "").strip()
    if author and _NOISE_AUTHOR_RE.search(author):
        return True
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
