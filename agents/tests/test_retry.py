"""Tests for retry_with_backoff.

The important behaviour we care about is that when an exception carries a
``.response.text`` attribute (openai.APIStatusError shape), the intermediate
warning log surfaces that body so "401 Invalid API key" isn't hidden behind
a generic ``str(exc)`` repr.
"""

from __future__ import annotations

import logging

import pytest

from agents._retry import retry_with_backoff


class _FakeResponse:
    def __init__(self, text: str):
        self.text = text


class _FakeAPIError(Exception):
    """Mimics the relevant surface of openai.APIStatusError."""

    def __init__(self, msg: str, body: str):
        super().__init__(msg)
        self.response = _FakeResponse(body)


def test_success_first_try(monkeypatch):
    calls = {"n": 0}

    def fn():
        calls["n"] += 1
        return "ok"

    assert retry_with_backoff(fn, attempts=3, base_delay=0.0) == "ok"
    assert calls["n"] == 1


def test_reraises_after_attempts(monkeypatch):
    calls = {"n": 0}

    def fn():
        calls["n"] += 1
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError, match="boom"):
        retry_with_backoff(fn, attempts=3, base_delay=0.0)
    assert calls["n"] == 3


def test_logs_response_body_on_api_error(monkeypatch, caplog):
    calls = {"n": 0}

    def fn():
        calls["n"] += 1
        raise _FakeAPIError(
            "Error code: 401",
            '{"error":{"message":"Invalid API key","code":"invalid_api_key"}}',
        )

    caplog.set_level(logging.WARNING, logger="agents._retry")
    with pytest.raises(_FakeAPIError):
        retry_with_backoff(fn, attempts=2, base_delay=0.0)

    # One warning emitted between attempt 1 and attempt 2 (no warning after
    # the final attempt, since that one re-raises).
    warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
    assert warnings, "expected at least one WARNING from retry_with_backoff"
    assert any("Invalid API key" in r.getMessage() for r in warnings), (
        "expected the response body to be surfaced in the warning line"
    )


def test_no_body_log_when_exception_has_none(monkeypatch, caplog):
    def fn():
        raise ValueError("plain")

    caplog.set_level(logging.WARNING, logger="agents._retry")
    with pytest.raises(ValueError):
        retry_with_backoff(fn, attempts=2, base_delay=0.0)

    # Ensure we don't crash or print ``body=None`` when there's no response.
    warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
    assert warnings
    assert all("body=" not in r.getMessage() for r in warnings)
