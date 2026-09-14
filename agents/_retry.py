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

# HTTP statuses that mean "this will fail identically until a human changes
# something". 401/403 is a bad or unauthorised key; 402 is OpenRouter refusing
# because the key's remaining balance cannot cover the request's max_tokens
# reservation; 404 is a model slug that doesn't exist. None of these get better
# in 2, 4, or 8 seconds — the three attempts just push the real cause 40 lines
# further up a log that CI truncates from the front.
_NON_RETRYABLE_STATUS = frozenset({401, 402, 403, 404})


def _is_permanent(exc: BaseException) -> bool:
    """True when *exc* carries an HTTP status that retrying cannot fix."""
    status = getattr(exc, "status_code", None)
    return isinstance(status, int) and status in _NON_RETRYABLE_STATUS


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
            if _is_permanent(exc):
                logger.warning(
                    "%s failed with non-retryable HTTP %s on attempt %d — "
                    "not retrying: %s",
                    label, getattr(exc, "status_code", "?"), attempt, exc,
                )
                raise
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
