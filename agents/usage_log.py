"""Shared structured-token usage logger.

Writes one JSON line per LLM call to ``agents/output/usage.log`` — the sole
audit trail for €5/month budget enforcement.

Schema (stable; both agents emit the same keys):

    {
        "agent":            "discussion_agent" | "landing_agent" | "landing_agent_premium",
        "model":            "<model-id>",
        "ts":               "<ISO-8601 UTC>",
        "request_tokens":   <int | null>,
        "response_tokens":  <int | null>,
        "total_tokens":     <int | null>,
        "usage_repr":       "<str(usage)>"       # fallback for unparseable shapes
    }

Path is anchored at ``agents/output/usage.log`` relative to this file, so it
works regardless of the process CWD.
"""
from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

# Anchored to the agents package root — independent of cwd.
_AGENTS_ROOT = Path(__file__).resolve().parent
USAGE_LOG = _AGENTS_ROOT / "output" / "usage.log"
_MAX_USAGE_LOG_BYTES = 10 * 1024 * 1024  # 10 MB — rotate when exceeded


def _maybe_rotate_log(path: Path) -> None:
    """Rotate the usage log when it exceeds the size cap (one backup kept)."""
    if path.exists() and path.stat().st_size > _MAX_USAGE_LOG_BYTES:
        backup = path.with_suffix(".log.1")
        backup.unlink(missing_ok=True)
        path.rename(backup)
        logger.info("Rotated usage log → %s", backup)


def _token_counts(usage: object) -> tuple[int | None, int | None, int | None]:
    """Extract (request, response, total) token counts from a usage object.

    Tries several attribute names to accommodate pydantic-ai's ``RunUsage``,
    OpenAI SDK ``Usage``, and similar shapes. Unknown shapes fall through to
    ``(None, None, None)`` — the ``usage_repr`` string remains as evidence.
    """
    def _pick(*names: str) -> int | None:
        for n in names:
            v = getattr(usage, n, None)
            if isinstance(v, int):
                return v
        return None

    req = _pick("request_tokens", "input_tokens", "prompt_tokens")
    resp = _pick("response_tokens", "output_tokens", "completion_tokens")
    total = _pick("total_tokens")
    if total is None and req is not None and resp is not None:
        total = req + resp
    return req, resp, total


def append_usage(agent_name: str, model: str, usage: object) -> None:
    """Append one structured JSON record describing an LLM call."""
    USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
    _maybe_rotate_log(USAGE_LOG)
    req, resp, total = _token_counts(usage)
    record = {
        "agent": agent_name,
        "model": model,
        "ts": datetime.now(tz=timezone.utc).isoformat(),
        "request_tokens": req,
        "response_tokens": resp,
        "total_tokens": total,
        "usage_repr": str(usage),
    }
    with USAGE_LOG.open("a") as fh:
        fh.write(json.dumps(record) + "\n")
