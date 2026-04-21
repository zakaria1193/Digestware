"""Tiny exponential-backoff retry helper for flaky LLM calls.

Designed so a single 429/timeout/network blip doesn't degrade an entire batch
of 10-15 items to low-value stub digests.
"""
from __future__ import annotations

import json
import logging
import time
from collections.abc import Callable
from typing import TypeVar

from pydantic import ValidationError

logger = logging.getLogger(__name__)

T = TypeVar("T")

_DEFAULT_ATTEMPTS = 3
_DEFAULT_BASE_DELAY = 2.0  # seconds; 2, 4, 8 …

# Errors that won't be fixed by trying again with the same prompt. Retrying a
# schema mismatch or a truncated JSON response just burns OpenRouter budget
# until we land in the same stub path anyway.
_NON_RETRYABLE: tuple[type[BaseException], ...] = (
    ValidationError,
    json.JSONDecodeError,
)


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
        except _NON_RETRYABLE as exc:
            logger.warning(
                "%s failed with non-retryable %s on attempt %d — not retrying: %s",
                label, type(exc).__name__, attempt, exc,
            )
            raise
        except Exception as exc:
            last_exc = exc
            if attempt >= attempts:
                break
            delay = base_delay * (2 ** (attempt - 1))
            # openai.APIStatusError and similar expose the upstream response
            # body on exc.response.text; str(exc) often drops it. Surface it
            # so "401 Invalid API key" doesn't hide behind a generic repr.
            body = getattr(getattr(exc, "response", None), "text", None)
            body_hint = f" | body={body[:300]}" if body else ""
            logger.warning(
                "%s failed (attempt %d/%d: %s%s) — retrying in %.1fs",
                label, attempt, attempts, exc, body_hint, delay,
            )
            time.sleep(delay)
    assert last_exc is not None  # loop entered at least once
    raise last_exc
