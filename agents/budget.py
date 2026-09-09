"""Month-to-date spend, and the guard that stops a lesson exceeding the cap.

The project ceiling is **€5/month**, and until now that was a comment. Tokens
were logged; money was never counted. This module closes that gap:

    usage.log (tokens, per call)  ×  OpenRouter /models (price per token)
        →  month-to-date USD  →  "can we afford another lesson?"

Two design choices carry the safety of the whole thing.

**Unknowns are expensive.** A model missing from the price listing, or a record
whose token counts came back null, is charged at ``UNKNOWN_*_USD_PER_TOKEN``
— deliberately above anything we actually use. A budget guard that silently
skips what it cannot price is a budget guard that stops guarding; the failure
has to push *toward* the cap, never away from it.

**The check happens before spending, not after.** Asking "have we exceeded the
cap?" once the bill is in permits exactly one unbounded overshoot — and the
lesson, at Opus rates, is the single most expensive call the project makes.
``can_afford()`` therefore takes the estimated cost of the work being
considered and asks whether it *would* exceed.

Spend is only visible if ``output/usage.log`` survives between runs, which is
why that file is committed rather than ignored — see the note in `.gitignore`.
"""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path

from agents._openrouter import fetch_models
from agents.usage_log import USAGE_LOG

logger = logging.getLogger(__name__)

# The cap is EUR 5/month and OpenRouter bills in USD. USD 5 is below EUR 5 at
# any plausible rate, so treating the cap as $5 needs no exchange rate and errs
# on the safe side of the real limit.
DEFAULT_MONTHLY_BUDGET_USD = 5.0

# What one lesson is expected to cost: a cheap multi-turn research pass plus a
# single premium writing call. This is still an ESTIMATE — no lesson has ever
# completed — so it is deliberately generous. Replace it with the measured
# figure from the `lesson_research` / `lesson_writer` rows of usage.log once a
# real run lands.
DEFAULT_LESSON_COST_USD = 0.50

# Charged when a model has no price we can look up. Above Opus input/output
# rates on purpose: see the module docstring.
UNKNOWN_PROMPT_USD_PER_TOKEN = 0.000015
UNKNOWN_COMPLETION_USD_PER_TOKEN = 0.000075

# Charged for a call whose token counts are null — we know it happened and that
# it cost something, so it must not count as free.
ASSUMED_TOKENS_WHEN_UNKNOWN = 20_000

# Fallback prices (USD per token) for the models this repo configures, used
# only when /models is unreachable. Captured 2026-09; refresh alongside the
# slugs in _openrouter.py. Rounded UP, per the "unknowns are expensive" rule.
FALLBACK_PRICES: dict[str, tuple[float, float]] = {
    "google/gemini-2.5-flash-lite": (0.0000002, 0.0000010),
    "google/gemini-2.5-flash": (0.0000004, 0.0000025),
    "anthropic/claude-sonnet-4.5": (0.0000030, 0.0000150),
    "anthropic/claude-opus-5": (0.0000050, 0.0000250),
}


def monthly_budget_usd() -> float:
    """The cap, overridable via ``MONTHLY_BUDGET_USD`` for testing."""
    raw = (os.environ.get("MONTHLY_BUDGET_USD") or "").strip()
    if not raw:
        return DEFAULT_MONTHLY_BUDGET_USD
    try:
        return float(raw)
    except ValueError:
        logger.warning(
            "MONTHLY_BUDGET_USD=%r is not a number — using the default $%.2f",
            raw, DEFAULT_MONTHLY_BUDGET_USD,
        )
        return DEFAULT_MONTHLY_BUDGET_USD


def lesson_cost_estimate_usd() -> float:
    raw = (os.environ.get("LESSON_COST_ESTIMATE_USD") or "").strip()
    if not raw:
        return DEFAULT_LESSON_COST_USD
    try:
        return float(raw)
    except ValueError:
        return DEFAULT_LESSON_COST_USD


def load_prices() -> dict[str, tuple[float, float]]:
    """``{model: (usd_per_prompt_token, usd_per_completion_token)}``.

    Live from OpenRouter when reachable, the static table otherwise. A partial
    listing is merged over the fallback rather than replacing it, so a model
    the listing omits still has a price.
    """
    prices = dict(FALLBACK_PRICES)
    try:
        entries = fetch_models()
    except Exception as exc:                     # noqa: BLE001
        logger.warning(
            "budget: could not fetch live prices (%s) — using the %d-model "
            "fallback table",
            exc, len(FALLBACK_PRICES),
        )
        return prices

    for entry in entries:
        if not isinstance(entry, dict):
            continue
        model_id = entry.get("id")
        pricing = entry.get("pricing")
        if not isinstance(model_id, str) or not isinstance(pricing, dict):
            continue
        try:
            prompt = float(pricing.get("prompt", "0") or 0)
            completion = float(pricing.get("completion", "0") or 0)
        except (TypeError, ValueError):
            continue
        prices[model_id] = (prompt, completion)
    return prices


def _record_cost(record: dict, prices: dict[str, tuple[float, float]]) -> float:
    model = record.get("model")
    prompt_rate, completion_rate = prices.get(
        model if isinstance(model, str) else "",
        (UNKNOWN_PROMPT_USD_PER_TOKEN, UNKNOWN_COMPLETION_USD_PER_TOKEN),
    )

    req = record.get("request_tokens")
    resp = record.get("response_tokens")
    if not isinstance(req, int) and not isinstance(resp, int):
        # The call happened and cost something; refusing to guess would price
        # it at zero, which is the one answer that is certainly wrong.
        total = record.get("total_tokens")
        assumed = total if isinstance(total, int) else ASSUMED_TOKENS_WHEN_UNKNOWN
        return assumed * completion_rate

    return (req or 0) * prompt_rate + (resp or 0) * completion_rate


def month_to_date_usd(
    now: datetime | None = None,
    log_path: Path | None = None,
    prices: dict[str, tuple[float, float]] | None = None,
) -> float:
    """Total USD spent so far in *now*'s UTC calendar month."""
    now = now or datetime.now(tz=timezone.utc)
    path = log_path or USAGE_LOG
    if not path.exists():
        return 0.0

    prices = prices if prices is not None else load_prices()
    total = 0.0
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(record, dict):
            continue

        ts = record.get("ts")
        if not isinstance(ts, str):
            continue
        try:
            when = datetime.fromisoformat(ts)
        except ValueError:
            continue
        if when.tzinfo is None:
            when = when.replace(tzinfo=timezone.utc)
        when = when.astimezone(timezone.utc)
        if (when.year, when.month) != (now.year, now.month):
            continue

        total += _record_cost(record, prices)
    return total


def can_afford(
    estimate_usd: float,
    now: datetime | None = None,
    log_path: Path | None = None,
    prices: dict[str, tuple[float, float]] | None = None,
) -> tuple[bool, float, float]:
    """Would spending *estimate_usd* more this month stay within the cap?

    Returns ``(affordable, month_to_date, cap)`` so the caller can log real
    numbers rather than just "no".
    """
    cap = monthly_budget_usd()
    spent = month_to_date_usd(now=now, log_path=log_path, prices=prices)
    return (spent + estimate_usd <= cap), spent, cap
