"""Tests for the model-slug preflight.

The bug this guards against has bitten twice: a slug that looks right, is
wrong, and only says so at request time — after the run has paid for
everything leading up to it.
"""

from __future__ import annotations

import httpx
import pytest

from agents import check_models

AVAILABLE = {
    "google/gemini-2.5-flash",
    "google/gemini-2.5-flash-lite",
    "anthropic/claude-sonnet-4-5",
    "anthropic/claude-opus-4-1",
    "openai/gpt-4o",
}


def test_all_present_reports_nothing_missing(capsys: pytest.CaptureFixture) -> None:
    monkey = {
        "SUMMARISER_MODEL": "google/gemini-2.5-flash-lite",
        "BENTO_MODEL": "anthropic/claude-sonnet-4-5",
        "LESSON_RESEARCH_MODEL": "google/gemini-2.5-flash",
        "LESSON_WRITER_MODEL": "anthropic/claude-sonnet-4-5",
    }
    with pytest.MonkeyPatch.context() as mp:
        for key, value in monkey.items():
            mp.setenv(key, value)
        assert check_models.check(AVAILABLE) == []


def test_missing_slug_is_reported() -> None:
    with pytest.MonkeyPatch.context() as mp:
        mp.setenv("LESSON_WRITER_MODEL", "anthropic/claude-opus-5")
        mp.setenv("SUMMARISER_MODEL", "google/gemini-2.5-flash-lite")
        mp.setenv("BENTO_MODEL", "anthropic/claude-sonnet-4-5")
        mp.setenv("LESSON_RESEARCH_MODEL", "google/gemini-2.5-flash")
        missing = check_models.check(AVAILABLE)
    assert missing == ["anthropic/claude-opus-5"]


def test_suggestions_prefer_the_same_vendor() -> None:
    options = check_models.suggest("anthropic/claude-opus-5", AVAILABLE)
    assert options == ["anthropic/claude-opus-4-1", "anthropic/claude-sonnet-4-5"]
    assert all(o.startswith("anthropic/") for o in options)


def test_suggestions_fall_back_to_a_name_match() -> None:
    options = check_models.suggest("unknownvendor/gemini-9", AVAILABLE)
    assert options == ["google/gemini-2.5-flash", "google/gemini-2.5-flash-lite"]


def test_fetch_available_parses_the_listing() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={"data": [{"id": "a/b"}, {"id": "c/d"}, {"no_id": 1}, "junk"]},
        )

    client = httpx.Client(transport=httpx.MockTransport(handler))
    assert check_models.fetch_available(client) == {"a/b", "c/d"}


def test_unreachable_listing_does_not_block_the_run(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A network blip must not be worse than the bug this guards against."""

    def _boom() -> set[str]:
        raise httpx.ConnectError("proxy said no")

    monkeypatch.setattr(check_models, "fetch_available", _boom)
    assert check_models.main() == 0


def test_every_configured_model_is_covered() -> None:
    """CONFIGURED must not fall behind the defaults it is meant to check."""
    from agents import _openrouter

    defaults = {
        name
        for name in dir(_openrouter)
        if name.startswith("DEFAULT_") and name.endswith("_MODEL")
    }
    assert len(check_models.CONFIGURED) == len(defaults), (
        f"agents/_openrouter.py defines {len(defaults)} default model(s) but "
        f"check_models.CONFIGURED covers {len(check_models.CONFIGURED)}"
    )
