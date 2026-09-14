"""Tests for the two-stage lesson agent.

No LLM is called. What is worth testing here is the plumbing either side of
the model:

- **Identity is forced, not trusted.** The writer echoes several fields back;
  a hallucinated commit hash or week would mislabel the whole article, so they
  are overwritten from the subject regardless of what came back.
- **Cited paths are verified.** The writing model never opens a file — it works
  entirely from the dossier — so every `code_tour` path is re-checked against
  the real tree. This is the guard that keeps a fabricated file reference off
  the page.
- **The tool budget actually stops.** It is the dominant cost lever, and a
  budget that only *mostly* holds is a budget overrun.
"""

from __future__ import annotations

from datetime import date
from typing import Any, cast

import pytest

from agents.lesson_agent import (
    _build_tools,
    _drop_unread_code_refs,
    _finalise_lesson,
    _render_dossier,
    _repair_lesson_item,
    _ToolBudget,
    stub_lesson,
)
from agents.lesson_picker import LessonSubject, previous_complete_week
from agents.models.lesson import (
    LessonDigest,
    LessonDraft,
    LessonResearch,
    LessonResearchDraft,
    SourceExcerpt,
)
from agents.tools.source_repo import SourceRepo

WEEK = previous_complete_week(date(2026, 9, 9))     # 2026-W36, Aug 31 – Sep 6
SHA = "a" * 40


@pytest.fixture
def subject() -> LessonSubject:
    return LessonSubject(
        commit_hash=SHA,
        project="gcc",
        subsystem="gcc/ipa",
        headline="ipa-sra: fix parameter liveness",
        tldr="Liveness was computed wrong.",
        url="https://github.com/gcc-mirror/gcc/commit/" + SHA,
        source_type="github",
        commit_date=date(2026, 9, 2),
        week=WEEK,
        impact_score=9,
        landing_slug="2026-09-02-ipa-aaaaaaaa",
    )


class FakeRepo:
    """Stands in for SourceRepo: only the paths in `present` exist."""

    def __init__(self, present: set[str] | None = None) -> None:
        self.present = present if present is not None else {"gcc/ipa-sra.cc"}
        self.calls: list[str] = []

    def read_file(self, sha, path, start_line=1, end_line=None):
        self.calls.append(path)
        if path in self.present:
            return f"# {path} @ {sha[:12]} — lines 1-1 of 10\n     1  code"
        return f"[error] cannot read {path} at {sha[:12]}: no such path"

    def changed_dirs(self, sha):
        return ["gcc"]

    def changed_paths(self, sha):
        return ["gcc/ipa-sra.cc"]

    def show_commit(self, sha):
        return "commit body"

    def list_dir(self, sha, path="."):
        return "ipa-sra.cc"

    def grep_repo(self, sha, pattern, paths):
        return "hit"

    def find_symbol(self, sha, name, paths):
        return "hit"


def _fake_repo(present: set[str] | None = None) -> SourceRepo:
    """A FakeRepo typed as SourceRepo.

    The functions under test only ever call `read_file` / `changed_dirs`, so a
    stand-in is enough at runtime; the cast is what tells the type checker
    that. One cast here beats eight suppressions at the call sites.
    """
    return cast(SourceRepo, FakeRepo(present))


def _writer_item(**overrides) -> dict:
    item: dict = {
        "headline": "How IPA-SRA decides a parameter is dead",
        "hook": "A short fix, a long idea.",
        "tldr": "Liveness, corrected.",
        "concept": "Interprocedural passes must agree on what a parameter means.",
        "subsystem": "gcc/ipa",
        "sections": [{"heading": "Background", "body": "Prose."}],
        "code_tour": [
            {"path": "gcc/ipa-sra.cc", "symbol": "isra", "lines": "1-10",
             "why": "Where liveness is decided."},
        ],
        "takeaways": ["Check both directions."],
        "tags": ["ipa"],
    }
    item.update(overrides)
    return item


# ---------------------------------------------------------------------------
# Identity is forced, not trusted
# ---------------------------------------------------------------------------

def test_identity_fields_are_forced_from_the_subject(subject):
    """A model typo here would misattribute the article to the wrong commit."""
    item = _writer_item()
    item["commit_hash"] = "b" * 40          # wrong
    item["project"] = "binutils"            # wrong
    item["url"] = "https://evil.example/x"  # wrong

    _repair_lesson_item(item, subject)

    assert item["commit_hash"] == SHA
    assert item["project"] == "gcc"
    assert item["url"] == subject.url
    assert item["lesson_id"] == "gcc:2026-W36"
    assert item["landing_slug"] == "2026-09-02-ipa-aaaaaaaa"


def test_week_fields_come_from_the_subject(subject):
    item = _writer_item()
    _repair_lesson_item(item, subject)

    assert item["week_start"] == "2026-08-31"
    assert item["week_end"] == "2026-09-06"
    assert item["commit_date"] == "2026-09-02"
    # The article is dated by its week, not by the commit.
    assert item["date"] == "2026-09-06"


def test_unknown_subsystem_falls_back_to_the_landing(subject):
    for value in ("unknown", "general", "", None):
        item = _writer_item()
        item["subsystem"] = value
        _repair_lesson_item(item, subject)
        assert item["subsystem"] == "gcc/ipa"


# ---------------------------------------------------------------------------
# Length repair
# ---------------------------------------------------------------------------

def test_overlong_fields_are_clipped_not_rejected(subject):
    """A ten-character overshoot should not cost the whole (paid) run."""
    item = _writer_item(
        headline="x" * 400, hook="y" * 400, tldr="z" * 400, concept="c" * 900,
    )
    _repair_lesson_item(item, subject)

    assert len(item["headline"]) <= 140
    assert len(item["hook"]) <= 200
    assert len(item["tldr"]) <= 160
    assert len(item["concept"]) <= 300
    assert item["headline"].endswith("…")


def test_overlong_lists_are_truncated(subject):
    item = _writer_item(
        tags=[f"t{i}" for i in range(20)],
        takeaways=[f"take {i}" for i in range(20)],
    )
    _repair_lesson_item(item, subject)
    assert len(item["tags"]) == 5
    assert len(item["takeaways"]) == 6


# ---------------------------------------------------------------------------
# The evidence guard
# ---------------------------------------------------------------------------

def test_fabricated_paths_are_dropped():
    """The writer never opened a file, so its citations are verified, not trusted."""
    repo = _fake_repo(present={"gcc/ipa-sra.cc"})
    item = {"code_tour": [
        {"path": "gcc/ipa-sra.cc", "why": "real"},
        {"path": "gcc/totally-made-up.cc", "why": "invented"},
    ]}
    _drop_unread_code_refs(item, repo, SHA)

    assert [r["path"] for r in item["code_tour"]] == ["gcc/ipa-sra.cc"]


def test_malformed_code_refs_are_dropped():
    repo = _fake_repo()
    item = {"code_tour": [{"why": "no path"}, "not-a-dict", {"path": ""}]}
    _drop_unread_code_refs(item, repo, SHA)
    assert item["code_tour"] == []


def test_finalise_lesson_end_to_end(subject):
    repo = _fake_repo()
    lesson = _finalise_lesson(LessonDraft(**_writer_item()), subject, repo)

    assert lesson.lesson_id == "gcc:2026-W36"
    assert lesson.commit_hash == SHA
    assert lesson.week_start == date(2026, 8, 31)
    assert lesson.commit_date == date(2026, 9, 2)
    assert [r.path for r in lesson.code_tour] == ["gcc/ipa-sra.cc"]


def test_lesson_draft_omits_the_fields_the_pipeline_injects():
    """The writer is not asked to echo identity it cannot get right.

    Every name below is forced from the subject in ``_repair_lesson_item``, so
    carrying it in the draft schema only spends tokens and invites a typo in
    the values that decide which commit the article is about.
    """
    authored = set(LessonDraft.model_fields)

    assert {"commit_hash", "project", "url", "week_start"}.isdisjoint(authored)
    assert "headline" in authored and "sections" in authored
    # …and nothing the strict model doesn't know about.
    assert authored <= set(LessonDigest.model_fields)


def test_finalise_lesson_reads_null_as_nothing_to_add(subject):
    """A model answering ``"further_reading": null`` means it found none."""
    repo = _fake_repo()
    draft = LessonDraft(**_writer_item(further_reading=None, primer_glossary=None))

    lesson = _finalise_lesson(draft, subject, repo)

    assert lesson.further_reading == []
    assert lesson.primer_glossary == []


# ---------------------------------------------------------------------------
# Tool budget
# ---------------------------------------------------------------------------

def test_budget_stops_at_the_limit():
    budget = _ToolBudget(limit=3)
    assert [budget.spend() for _ in range(5)] == [True, True, True, False, False]
    assert budget.used == 3


def test_tools_refuse_to_run_once_the_budget_is_spent():
    """The cap is the dominant cost lever — it has to actually bind."""
    repo = _fake_repo()
    budget = _ToolBudget(limit=2)
    tools = {t.__name__: t for t in _build_tools(repo, SHA, budget)}

    assert tools["show_commit"]() == "commit body"
    assert tools["list_dir"]() == "ipa-sra.cc"
    for name in ("show_commit", "grep_repo", "find_symbol"):
        out = tools[name]("x") if name != "show_commit" else tools[name]()
        assert "[budget]" in str(out)


def test_grep_defaults_to_the_commits_own_directories():
    repo = _fake_repo()
    captured = {}
    repo.grep_repo = lambda sha, pattern, paths: captured.setdefault("paths", paths)
    tools = {t.__name__: t for t in _build_tools(repo, SHA, _ToolBudget())}

    tools["grep_repo"]("pattern")
    assert captured["paths"] == ["gcc"]


# ---------------------------------------------------------------------------
# Dossier rendering
# ---------------------------------------------------------------------------

def test_dossier_carries_excerpts_verbatim(subject):
    code = "  if (!isra_track_scalar_value_p (p))\n    return false;"
    research = LessonResearch(
        commit_hash=SHA,
        subsystem="gcc/ipa",
        commit_message="ipa-sra: fix liveness",
        diff="--- a/gcc/ipa-sra.cc",
        changed_files=["gcc/ipa-sra.cc"],
        excerpts=[SourceExcerpt(
            path="gcc/ipa-sra.cc", lines="1204-1231", symbol="isra_call_summary",
            code=code, note="Where liveness is decided.",
        )],
        what_changed="Corrects the liveness test.",
        how_it_works="IPA-SRA walks call summaries.",
        why_it_matters="Wrong code at -O2.",
    )
    out = _render_dossier(research, subject)

    # The writer's only view of the source — it must arrive unmangled.
    assert code in out
    assert "gcc/ipa-sra.cc  lines 1204-1231  [isra_call_summary]" in out
    assert "IPA-SRA walks call summaries." in out
    assert "2026-08-31 to 2026-09-06" in out


def test_dossier_flags_open_questions_as_off_limits(subject):
    research = LessonResearch(
        commit_hash=SHA,
        subsystem="gcc/ipa",
        open_questions=["Whether the ABI changed."],
    )
    out = _render_dossier(research, subject)
    assert "Whether the ABI changed." in out
    # The writer must be told these are gaps, not facts to assert.
    assert "do not assert" in out


# ---------------------------------------------------------------------------
# Stub
# ---------------------------------------------------------------------------

def test_stub_lesson_is_valid_and_marked(subject):
    lesson = stub_lesson(subject, reason="research_failed")

    assert lesson.is_stub is True
    assert lesson.stub_reason == "research_failed"
    assert lesson.lesson_id == "gcc:2026-W36"
    assert lesson.week_end == date(2026, 9, 6)
    assert lesson.code_tour == []


# ---------------------------------------------------------------------------
# The dossier must survive a real model's output
# ---------------------------------------------------------------------------
#
# Every lesson on disk as of 2026-09-14 is a stub and all four died here, where
# a failure costs the whole article — every tool call in the research loop has
# already been paid for by the time the dossier is assembled.
#
# JSON *encoding* is the provider's job now: the dossier arrives as structured
# output rather than prose the pipeline parses. What is left to prove is the
# repair either side of it — caps trimmed rather than enforced, a null read as
# "nothing to report", identity taken from the subject and not the model.

def _research_json(**overrides) -> dict:
    payload: dict = {
        "commit_hash": "a" * 40,
        "subsystem": "gcc/ipa",
        "commit_message": "Fix the thing",
        "diff": "--- a\n+++ b\n",
        "changed_files": ["gcc/ipa-sra.cc"],
        "excerpts": [
            {"path": "gcc/ipa-sra.cc", "lines": "1-3", "code": "int x;", "note": "why"}
        ],
        "what_changed": "A parameter is now marked dead.",
        "how_it_works": "The pass re-runs liveness.",
        "why_it_matters": "Fewer spills.",
    }
    payload.update(overrides)
    return payload


def _research_draft(**overrides):
    return LessonResearchDraft(**_research_json(**overrides))


def test_finalise_research_end_to_end(subject):
    from agents.lesson_agent import _finalise_research

    research = _finalise_research(_research_draft(), subject)

    assert research.what_changed == "A parameter is now marked dead."
    assert research.subsystem == "gcc/ipa"
    assert research.excerpts[0].code == "int x;"


def test_research_identity_is_forced_from_the_subject(subject):
    """A hallucinated SHA would attach the dossier to the wrong commit."""
    from agents.lesson_agent import _finalise_research

    research = _finalise_research(
        _research_draft(commit_hash="b" * 40, subsystem=""), subject
    )

    assert research.commit_hash == SHA
    assert research.subsystem == "gcc/ipa"


def test_null_is_read_as_nothing_to_report(subject):
    """``"external_context": null`` means "I found nothing", not a type error.

    Two of the four stubs on disk as of 2026-09-14 died on exactly this, and a
    ValidationError here is non-retryable — it costs the whole week's lesson.
    """
    from agents.lesson_agent import _finalise_research

    research = _finalise_research(
        _research_draft(external_context=None, open_questions=None), subject
    )

    assert research.external_context == []
    assert research.open_questions == []


def test_oversized_excerpt_is_clamped_not_rejected(subject):
    """`read_file` returns up to 8192 bytes; SourceExcerpt.code caps at 6000.

    A model copying an excerpt verbatim — exactly as instructed — therefore
    produces a value pydantic rejects. Losing the tail of one excerpt beats
    losing the whole dossier.
    """
    from agents.lesson_agent import _EXCERPT_STR_CAPS, _finalise_research

    cap = _EXCERPT_STR_CAPS["code"]
    draft = _research_draft(
        excerpts=[{"path": "gcc/ipa-sra.cc", "code": "x" * (cap + 2192)}]
    )
    assert len(_finalise_research(draft, subject).excerpts[0].code) == cap


def test_too_many_excerpts_are_trimmed(subject):
    from agents.lesson_agent import _RESEARCH_LIST_CAPS, _finalise_research

    cap = _RESEARCH_LIST_CAPS["excerpts"]
    draft = _research_draft(
        excerpts=[{"path": f"f{i}.cc", "code": "y"} for i in range(cap + 5)]
    )
    assert len(_finalise_research(draft, subject).excerpts) == cap


def test_over_long_prose_is_clamped(subject):
    from agents.lesson_agent import _RESEARCH_STR_CAPS, _finalise_research

    cap = _RESEARCH_STR_CAPS["how_it_works"]
    draft = _research_draft(how_it_works="z" * (cap + 500))
    assert len(_finalise_research(draft, subject).how_it_works) == cap


def test_the_draft_carries_no_caps_of_its_own():
    """The caps are repairs, not requirements — the model must not hit them.

    Put them in the output schema and an over-long excerpt comes back as a
    validation failure and a paid reprompt, instead of being quietly trimmed.
    """
    # `cast` because the twin is generated at import time: pyright sees a
    # plain BaseModel, which is exactly why the drift test below exists.
    draft = cast(Any, _research_draft(
        how_it_works="z" * 99_000,
        excerpts=[{"path": "f.cc", "code": "y" * 99_000}],
    ))

    assert len(draft.how_it_works) == 99_000
    assert len(draft.excerpts[0].code) == 99_000


def test_research_draft_mirrors_the_strict_model():
    """The twin is derived, so it cannot drift — this fails if it ever does.

    ``tool_calls_used`` is the one deliberate omission: the explorer cannot
    count its own budget, so the agent fills it in from the real counter.
    """
    assert set(LessonResearchDraft.model_fields) | {"tool_calls_used"} == set(
        LessonResearch.model_fields
    )


# ---------------------------------------------------------------------------
# A stub must say why
# ---------------------------------------------------------------------------

def test_stage_reason_carries_the_exception_text():
    from agents.lesson_agent import _MAX_STUB_REASON, _stage_reason

    reason = _stage_reason("research_failed", ValueError("no JSON object found"))
    assert reason.startswith("research_failed: ValueError: no JSON object found")
    assert len(reason) <= _MAX_STUB_REASON


def test_stage_reason_includes_an_api_response_body():
    """`str(exc)` drops the upstream body; that body is usually the answer."""
    from agents.lesson_agent import _stage_reason

    class _Resp:
        text = '{"error":{"message":"No endpoints found for model"}}'

    class _ApiError(Exception):
        response = _Resp()

    assert "No endpoints found" in _stage_reason("research_failed", _ApiError("404"))


def test_stage_reason_is_single_line_and_bounded():
    """It goes into YAML frontmatter, so it must not carry newlines."""
    from agents.lesson_agent import _MAX_STUB_REASON, _stage_reason

    reason = _stage_reason("writer_failed", ValueError("line one\nline two\n" + "q" * 500))
    assert "\n" not in reason
    assert len(reason) == _MAX_STUB_REASON


# ---------------------------------------------------------------------------
# Both stages run against a real Agent
# ---------------------------------------------------------------------------
#
# The tests above exercise the code either side of the model. This one builds
# the actual `pydantic_ai.Agent` — with the real `output_type`, the real tools
# and PydanticAI's own structured-output machinery — against `TestModel`, which
# synthesises a reply from the output schema and calls every tool once.
#
# It is here because the unit tests cannot see a constructor argument that
# PydanticAI doesn't accept, or an `output_type` a version bump stops
# supporting. Both fail the whole lesson at runtime, in the nightly job, after
# the research loop has been paid for.

def _agent_repo() -> SourceRepo:
    """A repo stub that answers every navigation tool."""
    class _Repo:
        def changed_dirs(self, sha): return ["gcc/ipa"]
        def changed_paths(self, sha): return ["gcc/ipa-sra.cc"]
        def show_commit(self, sha): return "Fix the thing\n\n--- a\n+++ b\n"
        def read_file(self, sha, path, start_line=1, end_line=None): return "int x;"
        def list_dir(self, sha, path): return "ipa-sra.cc"
        def grep_repo(self, sha, pattern, paths): return "gcc/ipa-sra.cc:1:int x;"
        def find_symbol(self, sha, name, paths): return "gcc/ipa-sra.cc:1:int x;"

    return cast(SourceRepo, _Repo())


@pytest.fixture
def offline_models(monkeypatch):
    """Both stages on TestModel, with the network and the ledger stubbed out."""
    from pydantic_ai.models.test import TestModel

    import agents.lesson_agent as la

    monkeypatch.setattr(la, "build_model", lambda *a, **k: TestModel())
    monkeypatch.setattr(la, "append_usage", lambda *a, **k: None)
    monkeypatch.setattr(la, "search_context", lambda query: ["offline"])
    return la


def test_research_stage_wires_up_and_returns_a_dossier(subject, offline_models):
    errors: list[str] = []

    research = offline_models.run_research(subject, _agent_repo(), errors=errors)

    assert errors == []
    assert isinstance(research, LessonResearch)
    assert research.commit_hash == SHA          # forced, not echoed
    assert research.tool_calls_used > 0         # counted by us, not the model


def test_writer_stage_wires_up_and_returns_a_lesson(subject, offline_models):
    errors: list[str] = []
    research = offline_models.run_research(subject, _agent_repo(), errors=errors)

    lesson = offline_models.run_writer(
        subject, research, _agent_repo(), errors=errors
    )

    assert errors == []
    assert isinstance(lesson, LessonDigest)
    assert lesson.lesson_id == "gcc:2026-W36"
    assert lesson.url == subject.url
    assert lesson.is_stub is False
