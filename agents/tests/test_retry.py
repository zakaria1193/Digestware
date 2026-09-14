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


class _FakeHTTPError(Exception):
    """Stands in for pydantic_ai.exceptions.ModelHTTPError."""

    def __init__(self, status_code: int, message: str = "http error"):
        super().__init__(message)
        self.status_code = status_code


@pytest.mark.parametrize("status", [401, 402, 403, 404])
def test_permanent_http_statuses_are_not_retried(status, caplog):
    """A 402 from OpenRouter is a spent balance, not a blip.

    Run 197 of the nightly digest burned three attempts and six seconds of
    backoff on the same "requires more credits" refusal before stubbing the
    lesson. Nothing about the second and third call could have differed.
    """
    calls = {"n": 0}

    def fn():
        calls["n"] += 1
        raise _FakeHTTPError(status, "This request requires more credits")

    caplog.set_level(logging.WARNING, logger="agents._retry")
    with pytest.raises(_FakeHTTPError):
        retry_with_backoff(fn, attempts=3, base_delay=0.0)

    assert calls["n"] == 1
    assert any(
        "not retrying" in r.getMessage() for r in caplog.records
    ), "expected the refusal to be logged as non-retryable"


@pytest.mark.parametrize("status", [429, 500, 502, 503])
def test_transient_http_statuses_still_retry(status):
    """Rate limits and upstream 5xx are exactly what the backoff is for."""
    calls = {"n": 0}

    def fn():
        calls["n"] += 1
        raise _FakeHTTPError(status)

    with pytest.raises(_FakeHTTPError):
        retry_with_backoff(fn, attempts=3, base_delay=0.0)
    assert calls["n"] == 3


def test_structured_output_failure_is_not_retried(caplog):
    """PydanticAI has already reprompted the model by the time we see this.

    A retry here re-runs the entire agent loop. For the lesson's research
    stage that means resending every tool result collected so far — the most
    expensive call this project makes — to land in the same stub.
    """
    from pydantic_ai.exceptions import UnexpectedModelBehavior

    calls = {"n": 0}

    def fn():
        calls["n"] += 1
        raise UnexpectedModelBehavior("Exceeded maximum retries for output")

    with pytest.raises(UnexpectedModelBehavior):
        retry_with_backoff(fn, attempts=3, base_delay=0.0)

    assert calls["n"] == 1
