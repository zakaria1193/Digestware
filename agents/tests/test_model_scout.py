"""Tests for the weekly model scout: when does it propose a switch?"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from agents import model_scout
from agents.model_scout import Stage, scout, split_slug

TOOLS = ["tools", "structured_outputs"]


def entry(slug: str, prompt_per_m: float, completion_per_m: float, params: list[str] | None = None,
          created: int = 0) -> dict:
    return {
        "id": slug,
        "created": created,
        "pricing": {"prompt": str(prompt_per_m / 1e6), "completion": str(completion_per_m / 1e6)},
        "supported_parameters": TOOLS if params is None else params,
    }


def catalogue(*entries: dict) -> dict[str, dict]:
    return {e["id"]: e for e in entries}


@pytest.fixture
def log(tmp_path: Path) -> Path:
    path = tmp_path / "usage.log"
    rows = [
        # research: almost all input
        {"agent": "lesson_research", "model": "x", "request_tokens": 980, "response_tokens": 20},
        # writer: half and half
        {"agent": "lesson_writer", "model": "x", "request_tokens": 500, "response_tokens": 500},
    ]
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\nnot json\n", encoding="utf-8")
    return path


def stage(default: str, agent: str = "lesson_writer", needs_tools: bool = True) -> Stage:
    return Stage("SCOUT_TEST_MODEL", default, (agent,), needs_tools)


def test_split_slug_separates_family_from_version() -> None:
    assert split_slug("anthropic/claude-sonnet-5.5") == ("anthropic", "claude-sonnet", (5, 5))
    assert split_slug("anthropic/claude-3.5-haiku") == ("anthropic", "claude-haiku", (3, 5))
    assert split_slug("google/gemini-2.5-flash-lite")[1] == "gemini-flash-lite"
    assert split_slug("google/gemini-2.5-flash")[1] == "gemini-flash"


def test_newer_and_cheaper_same_family_is_proposed(log: Path) -> None:
    cat = catalogue(entry("anthropic/claude-opus-5.5", 4, 20), entry("anthropic/claude-opus-6", 3, 15))
    r = scout(stage("anthropic/claude-opus-5.5"), cat, log)
    assert r.status == "switch"
    assert r.proposal is not None and r.proposal.slug == "anthropic/claude-opus-6"
    assert r.proposal.saving_pct == 25.0


def test_older_cheaper_model_is_never_proposed(log: Path) -> None:
    cat = catalogue(entry("anthropic/claude-opus-5.5", 4, 20), entry("anthropic/claude-opus-4.1", 1, 5))
    r = scout(stage("anthropic/claude-opus-5.5"), cat, log)
    assert r.status == "keep" and r.proposal is None


def test_other_family_is_listed_not_proposed(log: Path) -> None:
    cat = catalogue(entry("anthropic/claude-opus-5.5", 4, 20), entry("anthropic/claude-sonnet-6", 2, 10))
    r = scout(stage("anthropic/claude-opus-5.5"), cat, log)
    assert r.status == "keep"
    assert [o.slug for o in r.cheaper_alternatives] == ["anthropic/claude-sonnet-6"]


def test_other_vendors_are_listed_too(log: Path) -> None:
    """Chinese and other vendors are alternatives like any other family."""
    cat = catalogue(
        entry("anthropic/claude-opus-5.5", 4, 20, created=200),
        entry("deepseek/deepseek-v4", 0.5, 2, created=300),
        entry("qwen/qwen4-max", 1, 4, created=200),
        entry("moonshotai/kimi-k3", 6, 30, created=300),       # dearer
        entry("meta-llama/llama-3-8b", 0.01, 0.01, created=100),  # older than today's pick
    )
    r = scout(stage("anthropic/claude-opus-5.5"), cat, log)
    assert r.status == "keep"
    assert [o.slug for o in r.cheaper_alternatives] == ["deepseek/deepseek-v4", "qwen/qwen4-max"]


def test_newer_but_dearer_is_reported_not_proposed(log: Path) -> None:
    cat = catalogue(entry("anthropic/claude-opus-5.5", 4, 20), entry("anthropic/claude-opus-6", 5, 25))
    r = scout(stage("anthropic/claude-opus-5.5"), cat, log)
    assert r.status == "keep"
    assert [o.slug for o in r.newer_but_dearer] == ["anthropic/claude-opus-6"]


def test_the_stage_mix_decides_cheaper(log: Path) -> None:
    """Cheaper input, dearer output: a win for input-heavy research only."""
    cat = catalogue(entry("anthropic/claude-haiku-5.5", 0.10, 0.50), entry("anthropic/claude-haiku-6", 0.05, 1.00))
    research = scout(stage("anthropic/claude-haiku-5.5", "lesson_research"), cat, log)
    writer = scout(stage("anthropic/claude-haiku-5.5", "lesson_writer"), cat, log)
    assert research.status == "switch"
    assert writer.status == "keep"


def test_variants_previews_and_snapshots_are_skipped(log: Path) -> None:
    cat = catalogue(
        entry("anthropic/claude-opus-5.5", 4, 20),
        entry("anthropic/claude-opus-6:free", 0, 0),
        entry("anthropic/claude-opus-6:thinking", 1, 1),
        entry("anthropic/claude-opus-6-preview", 1, 1),
        entry("anthropic/claude-opus-6-20270101", 1, 1),
    )
    assert scout(stage("anthropic/claude-opus-5.5"), cat, log).status == "keep"


def test_tool_stages_require_tool_support(log: Path) -> None:
    cat = catalogue(entry("anthropic/claude-opus-5.5", 4, 20), entry("anthropic/claude-opus-6", 1, 5, params=[]))
    assert scout(stage("anthropic/claude-opus-5.5"), cat, log).status == "keep"
    no_tools = stage("anthropic/claude-opus-5.5", needs_tools=False)
    assert scout(no_tools, cat, log).status == "switch"


def test_newest_cheaper_version_wins(log: Path) -> None:
    cat = catalogue(
        entry("anthropic/claude-opus-5.5", 4, 20),
        entry("anthropic/claude-opus-6", 2, 10),
        entry("anthropic/claude-opus-6.1", 3, 15),
    )
    r = scout(stage("anthropic/claude-opus-5.5"), cat, log)
    assert r.proposal is not None and r.proposal.slug == "anthropic/claude-opus-6.1"


def test_missing_current_model(log: Path) -> None:
    r = scout(stage("anthropic/claude-opus-5.5"), {}, log)
    assert r.status == "missing"


def test_env_override_is_flagged(log: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SCOUT_TEST_MODEL", "anthropic/claude-opus-6")
    cat = catalogue(entry("anthropic/claude-opus-6", 4, 20))
    r = scout(stage("anthropic/claude-opus-5.5"), cat, log)
    assert r.current == "anthropic/claude-opus-6" and r.overridden


def test_no_logged_calls_falls_back_to_default_mix(tmp_path: Path) -> None:
    r = scout(stage("anthropic/claude-opus-5.5", "nobody"), catalogue(entry("anthropic/claude-opus-5.5", 4, 20)),
              tmp_path / "absent.log")
    assert r.sample_calls == 0 and r.input_share == model_scout.DEFAULT_INPUT_SHARE


def test_main_survives_an_unreachable_listing(monkeypatch: pytest.MonkeyPatch, capsys) -> None:
    def boom(*_a, **_k):
        raise OSError("no network")

    monkeypatch.setattr(model_scout, "fetch_models", boom)
    assert model_scout.main([]) == 0
    assert "could not reach" in capsys.readouterr().out


def test_main_renders_every_stage(monkeypatch: pytest.MonkeyPatch, capsys) -> None:
    for name in ("SUMMARISER_MODEL", "BENTO_MODEL", "LESSON_RESEARCH_MODEL", "LESSON_WRITER_MODEL"):
        monkeypatch.delenv(name, raising=False)
    entries = [entry(s.default, 1, 2) for s in model_scout.STAGES]
    monkeypatch.setattr(model_scout, "fetch_models", lambda *_a, **_k: entries)
    assert model_scout.main([]) == 0
    out = capsys.readouterr().out
    for s in model_scout.STAGES:
        assert s.env_var in out
