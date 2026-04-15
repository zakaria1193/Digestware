"""Tiny exponential-backoff retry helper for flaky LLM calls.

Designed so a single 429/timeout/network blip doesn't degrade an entire batch
of 10-15 items to low-value stub digests.
"""
from __future__ import annotations

import logging
import time
from collections.abc import Callable
from typing import TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")

_DEFAULT_ATTEMPTS = 3
_DEFAULT_BASE_DELAY = 2.0  # seconds; 2, 4, 8 …


def retry_with_backoff(
    fn: Callable[[], T],
    *,
    attempts: int = _DEFAULT_ATTEMPTS,
    base_delay: float = _DEFAULT_BASE_DELAY,
    label: str = "call",
) -> T:
    """Call *fn* up to *attempts* times with exponential backoff.

    The final failing exception is re-raised so the caller can fall back
    (e.g. to stub digests).
    """
    last_exc: BaseException | None = None
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except Exception as exc:
            last_exc = exc
            if attempt >= attempts:
                break
            delay = base_delay * (2 ** (attempt - 1))
            logger.warning(
                "%s failed (attempt %d/%d: %s) — retrying in %.1fs",
                label, attempt, attempts, exc, delay,
            )
            time.sleep(delay)
    assert last_exc is not None  # loop entered at least once
    raise last_exc
