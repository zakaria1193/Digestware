"""Model-name resolution from the environment.

This exists because of a real outage, not a hypothetical. The workflow passes
`LESSON_RESEARCH_MODEL: ${{ vars.LESSON_RESEARCH_MODEL }}`; when that repo
variable is unset, GitHub exports the name as **present and empty** rather than
omitting it. `os.environ.get(key, default)` then returns `""`, every OpenRouter
call fails on an empty model slug, and the first real Lesson of the Week run
produced two `research_failed` stubs that looked like a green build.
"""

from __future__ import annotations

import pytest

from agents._openrouter import model_from_env

KEY = "TEST_MODEL_SLUG"


def test_absent_falls_back(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(KEY, raising=False)
    assert model_from_env(KEY, "vendor/default") == "vendor/default"


def test_empty_string_falls_back(monkeypatch: pytest.MonkeyPatch) -> None:
    """The regression: set-but-empty is what GitHub Actions actually sends."""
    monkeypatch.setenv(KEY, "")
    assert model_from_env(KEY, "vendor/default") == "vendor/default"


def test_whitespace_falls_back(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(KEY, "   ")
    assert model_from_env(KEY, "vendor/default") == "vendor/default"


def test_real_value_wins(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(KEY, "vendor/override")
    assert model_from_env(KEY, "vendor/default") == "vendor/override"


def test_value_is_stripped(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(KEY, "  vendor/override\n")
    assert model_from_env(KEY, "vendor/default") == "vendor/override"


def test_no_call_site_uses_the_unsafe_form() -> None:
    """Guard the whole class of bug, not just the two lines that bit us."""
    import pathlib
    import re

    root = pathlib.Path(__file__).resolve().parents[1]
    bad = re.compile(r"os\.environ\.get\(\s*\"[A-Z_]*MODEL\"")
    offenders = [
        p.name for p in root.glob("*.py") if bad.search(p.read_text(encoding="utf-8"))
    ]
    assert not offenders, (
        f"{offenders} resolve a model name with os.environ.get, which returns "
        "'' for a set-but-empty var. Use model_from_env instead."
    )
