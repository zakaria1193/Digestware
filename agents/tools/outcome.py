"""Deterministic outcome derivation for discussions and landings.

The LLM is terrible at this — it reads an RFC, sees "proposed" sounds
generic, and tags everything ``proposed`` regardless of what happened in the
thread. Signals like ``NACK``, ``Reviewed-by:``, ``[committed]`` are already
in the raw data; we extract them with regex and hand the outcome to the LLM
as an input hint.
"""
from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone

from agents.models.base import Outcome

_NACK_RE = re.compile(r"\b(NACK|Nacked-by\s*:)", re.IGNORECASE)
_ACK_RE = re.compile(r"\b(ACK\b|Acked-by\s*:|LGTM\b|Reviewed-by\s*:)", re.IGNORECASE)
_COMMITTED_TAG_RE = re.compile(
    r"\[[^\]]*\b(?:committed|commited|pushed|merged)\b[^\]]*\]",
    re.IGNORECASE,
)
_NEEDS_REV_RE = re.compile(
    r"\b(needs? (?:revision|rework)|please (?:fix|rework)|changes? requested)\b",
    re.IGNORECASE,
)
_WITHDRAWN_RE = re.compile(r"\b(withdrawn|retracted)\b", re.IGNORECASE)

_STALE_AFTER = timedelta(days=60)


def derive_discussion_outcome(
    title: str,
    body: str,
    replies_bodies: list[str],
    last_activity: datetime | None = None,
    now: datetime | None = None,
) -> Outcome:
    """Pick an ``Outcome`` from signals in the thread.

    Precedence (highest first):
        1. ``[committed]`` / ``[merged]`` tag in title → COMMITTED
        2. ``NACK`` / ``Nacked-by:`` anywhere → NACKD
        3. ``withdrawn`` in any body → WITHDRAWN
        4. ``needs revision`` / "changes requested" → NEEDS_REVISION
        5. ``ACK`` / ``LGTM`` / ``Reviewed-by:`` with no NACK → READY
        6. Inactive > 60d with no decision → STALLED
        7. Else → PROPOSED
    """
    title = title or ""
    if _COMMITTED_TAG_RE.search(title):
        return Outcome.COMMITTED

    all_text = "\n".join([title, body or "", *replies_bodies])

    if _NACK_RE.search(all_text):
        return Outcome.NACKD
    if _WITHDRAWN_RE.search(all_text):
        return Outcome.WITHDRAWN
    if _NEEDS_REV_RE.search(all_text):
        return Outcome.NEEDS_REVISION
    if _ACK_RE.search(all_text):
        return Outcome.READY

    if last_activity is not None:
        reference = now or datetime.now(timezone.utc)
        if last_activity.tzinfo is None:
            last_activity = last_activity.replace(tzinfo=timezone.utc)
        if reference - last_activity > _STALE_AFTER:
            return Outcome.STALLED

    return Outcome.PROPOSED
