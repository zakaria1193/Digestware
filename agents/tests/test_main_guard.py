"""Tests for the main() entry-point guards.

Two invariants:
  1. Running without OPENROUTER_API_KEY in non-dry-run mode exits 2 before
     any LLM/network call or file write happens — so we never silently ship
     stub digests to disk when the secret is missing.
  2. When every LLM batch falls back to stub digests, main() exits 3 so the
     CI workflow fails instead of committing garbage.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from agents import discussion_agent as discussion_agent_module
from agents import landing_agent as landing_agent_module
from agents import main as main_module


@pytest.fixture
def no_key(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    # load_dotenv may still pick up a .env on the dev box — disarm it.
    monkeypatch.setattr(main_module, "load_dotenv", lambda: None)


class TestMissingKeyGuard:
    def test_exits_2_when_key_missing(self, no_key, monkeypatch, tmp_path: Path):
        monkeypatch.setattr(
            "sys.argv",
            ["agents.main", "--since-hours", "1", "--content-root", str(tmp_path)],
        )
        rc = main_module.main()
        assert rc == 2

    def test_writes_nothing_when_key_missing(
        self, no_key, monkeypatch, tmp_path: Path,
    ):
        monkeypatch.setattr(
            "sys.argv",
            ["agents.main", "--since-hours", "1", "--content-root", str(tmp_path)],
        )
        main_module.main()
        # tmp_path should stay empty — guard runs before IngestionEngine.
        assert list(tmp_path.iterdir()) == []

    def test_dry_run_bypasses_guard(self, no_key, monkeypatch, tmp_path: Path):
        # With --dry-run, the guard is skipped so the wiring can be exercised
        # offline. We don't care about the return code here, only that it's
        # not the guard's "2".
        monkeypatch.setattr(
            "sys.argv",
            [
                "agents.main",
                "--since-hours",
                "1",
                "--dry-run",
                "--content-root",
                str(tmp_path),
            ],
        )
        rc = main_module.main()
        assert rc != 2


class TestAllBatchesStubbedExit:
    """If every LLM batch fell back, main() must exit non-zero."""

    def test_exits_3_when_all_stubbed(self, monkeypatch, tmp_path: Path):
        monkeypatch.setenv("OPENROUTER_API_KEY", "dummy")
        monkeypatch.setattr(main_module, "load_dotenv", lambda: None)

        # Short-circuit the heavy machinery so we can isolate the exit-code
        # branch. The engine returns empty lists; the agents then report
        # "every batch fell back" via the module-level counters.
        class _FakeEngine:
            def __init__(self, *a, **kw):
                pass

            def run(self, since_hours: int):
                return {"discussions": [], "commits": []}

        monkeypatch.setattr(main_module, "IngestionEngine", _FakeEngine)
        monkeypatch.setattr(
            main_module, "_build_sources", lambda config: ([], [])
        )

        # Simulate that the agents actually ran batches and all fell back.
        def _fake_discussion_run(raws, dry_run=False):
            discussion_agent_module.batches_total += 2
            discussion_agent_module.batches_stubbed += 2
            return []

        def _fake_landing_run(raws, dry_run=False):
            landing_agent_module.batches_total += 1
            landing_agent_module.batches_stubbed += 1
            return []

        monkeypatch.setattr(main_module, "run_discussion_agent", _fake_discussion_run)
        monkeypatch.setattr(main_module, "run_landing_agent", _fake_landing_run)

        # Force the pipeline past the "nothing to process" guard by seeding
        # filter_noise and dedup to pass non-empty lists through.
        def _pass_noise(d, c):
            return d, c, 0, 0

        def _pass_dedup(d, c, *a, **kw):
            return d, c, 0, 0

        monkeypatch.setattr(main_module, "filter_noise", _pass_noise)
        monkeypatch.setattr(main_module, "filter_raw", _pass_dedup)
        monkeypatch.setattr(
            main_module, "build_seen_index", lambda root: (set(), set(), set())
        )

        # Seed raw data so the `nothing to process` short-circuit is skipped.
        class _FakeEngineWithData(_FakeEngine):
            def run(self, since_hours: int):
                # Shape only — the fake agents don't inspect contents.
                return {"discussions": [object()], "commits": [object()]}

        monkeypatch.setattr(main_module, "IngestionEngine", _FakeEngineWithData)

        monkeypatch.setattr(
            "sys.argv",
            ["agents.main", "--since-hours", "1", "--content-root", str(tmp_path)],
        )
        rc = main_module.main()
        assert rc == 3

    def test_exits_0_when_no_batches_ran(self, monkeypatch, tmp_path: Path):
        # Zero batches means nothing to ingest — that's success, not failure.
        monkeypatch.setenv("OPENROUTER_API_KEY", "dummy")
        monkeypatch.setattr(main_module, "load_dotenv", lambda: None)
        monkeypatch.setattr(main_module, "_build_sources", lambda cfg: ([], []))

        class _EmptyEngine:
            def __init__(self, *a, **kw):
                pass

            def run(self, since_hours: int):
                return {"discussions": [], "commits": []}

        monkeypatch.setattr(main_module, "IngestionEngine", _EmptyEngine)
        monkeypatch.setattr(
            "sys.argv",
            ["agents.main", "--since-hours", "1", "--content-root", str(tmp_path)],
        )
        rc = main_module.main()
        assert rc == 0


def teardown_module(module):
    # Counters are module-level; reset so other test files start clean.
    discussion_agent_module.batches_total = 0
    discussion_agent_module.batches_stubbed = 0
    landing_agent_module.batches_total = 0
    landing_agent_module.batches_stubbed = 0
    os.environ.pop("OPENROUTER_API_KEY", None)
