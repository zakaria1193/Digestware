"""Tests for month-to-date spend and the lesson budget guard.

The guard's whole value is that it fails *toward* the cap. Every test here that
looks paranoid — unknown model, null tokens, unreachable price listing — is
pinning that direction, because a budget guard that quietly prices something at
zero has stopped guarding without saying so.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from agents import budget

PRICES = {
    "cheap/model": (0.000001, 0.000002),      # $1 / $2 per M tokens
    "premium/model": (0.000005, 0.000025),    # $5 / $25 per M tokens
}


def _log(tmp_path: Path, records: list[dict]) -> Path:
    path = tmp_path / "usage.log"
    path.write_text(
        "\n".join(json.dumps(r) for r in records) + "\n", encoding="utf-8"
    )
    return path


def _rec(
    model: str = "cheap/model",
    ts: str = "2026-09-09T12:00:00+00:00",
    req: int | None = 1_000_000,
    resp: int | None = 1_000_000,
    **extra,
) -> dict:
    return {
        "agent": "lesson_research",
        "model": model,
        "ts": ts,
        "request_tokens": req,
        "response_tokens": resp,
        **extra,
    }


NOW = datetime(2026, 9, 9, tzinfo=timezone.utc)


def test_prices_tokens_at_the_model_rate(tmp_path: Path) -> None:
    path = _log(tmp_path, [_rec()])
    # 1M prompt @ $1 + 1M completion @ $2
    assert budget.month_to_date_usd(NOW, path, PRICES) == pytest.approx(3.0)


def test_sums_across_calls(tmp_path: Path) -> None:
    path = _log(tmp_path, [_rec(), _rec(model="premium/model")])
    assert budget.month_to_date_usd(NOW, path, PRICES) == pytest.approx(3.0 + 30.0)


def test_only_the_current_month_counts(tmp_path: Path) -> None:
    """A December record must not be charged to January."""
    path = _log(
        tmp_path,
        [
            _rec(ts="2026-08-31T23:59:59+00:00"),   # previous month
            _rec(ts="2026-09-01T00:00:00+00:00"),   # this month
            _rec(ts="2026-10-01T00:00:00+00:00"),   # next month
        ],
    )
    assert budget.month_to_date_usd(NOW, path, PRICES) == pytest.approx(3.0)


def test_year_boundary_is_not_confused_by_month_alone(tmp_path: Path) -> None:
    path = _log(tmp_path, [_rec(ts="2025-09-09T12:00:00+00:00")])
    assert budget.month_to_date_usd(NOW, path, PRICES) == 0.0


def test_unknown_model_is_priced_high_not_free(tmp_path: Path) -> None:
    """The failure mode that would silently disable the cap."""
    path = _log(tmp_path, [_rec(model="brand/new-model")])
    cost = budget.month_to_date_usd(NOW, path, PRICES)
    premium = 1_000_000 * PRICES["premium/model"][0] + 1_000_000 * PRICES[
        "premium/model"
    ][1]
    assert cost > 0
    assert cost >= premium, "an unpriced model must cost at least a known premium one"


def test_null_token_counts_are_not_free(tmp_path: Path) -> None:
    path = _log(tmp_path, [_rec(req=None, resp=None)])
    assert budget.month_to_date_usd(NOW, path, PRICES) > 0


def test_null_counts_use_total_tokens_when_present(tmp_path: Path) -> None:
    path = _log(tmp_path, [_rec(req=None, resp=None, total_tokens=1_000)])
    cost = budget.month_to_date_usd(NOW, path, PRICES)
    assert cost == pytest.approx(1_000 * PRICES["cheap/model"][1])


def test_missing_log_is_zero(tmp_path: Path) -> None:
    assert budget.month_to_date_usd(NOW, tmp_path / "nope.log", PRICES) == 0.0


def test_malformed_lines_are_skipped(tmp_path: Path) -> None:
    path = tmp_path / "usage.log"
    path.write_text(
        "not json\n"
        "[1,2,3]\n"
        '{"model":"cheap/model"}\n'          # no ts
        '{"model":"cheap/model","ts":"nonsense"}\n'
        "\n" + json.dumps(_rec()) + "\n",
        encoding="utf-8",
    )
    assert budget.month_to_date_usd(NOW, path, PRICES) == pytest.approx(3.0)


def test_naive_timestamps_are_treated_as_utc(tmp_path: Path) -> None:
    path = _log(tmp_path, [_rec(ts="2026-09-09T12:00:00")])
    assert budget.month_to_date_usd(NOW, path, PRICES) == pytest.approx(3.0)


# ---------------------------------------------------------------------------
# The decision
# ---------------------------------------------------------------------------

def test_can_afford_under_the_cap(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("MONTHLY_BUDGET_USD", "5.0")
    path = _log(tmp_path, [])
    ok, spent, cap = budget.can_afford(0.5, NOW, path, PRICES)
    assert ok and spent == 0.0 and cap == 5.0


def test_can_afford_is_false_once_the_estimate_would_exceed(
    tmp_path: Path, monkeypatch
) -> None:
    """Checked BEFORE spending — that is the point.

    Asking "are we over?" after the fact permits one unbounded overshoot, and
    the lesson is the most expensive call the project makes.
    """
    monkeypatch.setenv("MONTHLY_BUDGET_USD", "5.0")
    path = _log(tmp_path, [_rec()])          # $3.00 spent
    assert budget.can_afford(1.9, NOW, path, PRICES)[0] is True    # 4.90
    assert budget.can_afford(2.0, NOW, path, PRICES)[0] is True    # 5.00, exactly
    assert budget.can_afford(2.1, NOW, path, PRICES)[0] is False   # 5.10


def test_budget_override_is_read_from_the_environment(monkeypatch) -> None:
    monkeypatch.setenv("MONTHLY_BUDGET_USD", "1.25")
    assert budget.monthly_budget_usd() == 1.25


def test_a_junk_budget_override_falls_back_to_the_default(monkeypatch) -> None:
    monkeypatch.setenv("MONTHLY_BUDGET_USD", "five dollars")
    assert budget.monthly_budget_usd() == budget.DEFAULT_MONTHLY_BUDGET_USD


# ---------------------------------------------------------------------------
# Prices
# ---------------------------------------------------------------------------

def test_unreachable_listing_falls_back_to_the_static_table(monkeypatch) -> None:
    def _boom() -> list[dict]:
        raise RuntimeError("proxy said no")

    monkeypatch.setattr(budget, "fetch_models", _boom)
    prices = budget.load_prices()
    assert prices == budget.FALLBACK_PRICES
    assert prices, "the fallback table must not be empty"


def test_live_prices_are_merged_over_the_fallback(monkeypatch) -> None:
    """A listing that omits a model must not un-price it."""
    monkeypatch.setattr(
        budget,
        "fetch_models",
        lambda: [
            {"id": "cheap/model", "pricing": {"prompt": "0.000009", "completion": "0.000009"}},
            {"id": "no-pricing/model"},
            "junk",
        ],
    )
    prices = budget.load_prices()
    assert prices["cheap/model"] == (0.000009, 0.000009)
    for known in budget.FALLBACK_PRICES:
        assert known in prices


def test_every_configured_model_has_a_fallback_price() -> None:
    """A configured model with no offline price would be charged as unknown."""
    from agents import check_models

    for env_var, default in check_models.CONFIGURED:
        assert default in budget.FALLBACK_PRICES, (
            f"{env_var} defaults to {default}, which has no entry in "
            "budget.FALLBACK_PRICES"
        )
