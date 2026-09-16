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

import json
from datetime import date
from typing import Any, cast

import pytest

from agents.lesson_agent import (
    _build_tools,
    _drop_unread_code_refs,
    _ExcerptLog,
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
        self.ranges: list[tuple[str, int, int | None]] = []

    def read_file(self, sha, path, start_line=1, end_line=None):
        self.calls.append(path)
        self.ranges.append((path, start_line, end_line))
        if path in self.present:
            return f"# {path} @ {sha[:12]} — lines 1-1 of 10\n     1  code"
        return f"[error] cannot read {path} at {sha[:12]}: no such path"

    def changed_dirs(self, sha):
        return ["gcc"]

    def changed_paths(self, sha):
        return ["gcc/ipa-sra.cc"]

    def show_commit(self, sha):
        return (
            "commit aaaa\n\n    ipa-sra: fix parameter liveness\n\n"
            " gcc/ipa-sra.cc | 2 +-\n\n"
            "diff --git a/gcc/ipa-sra.cc b/gcc/ipa-sra.cc\n"
            "--- a/gcc/ipa-sra.cc\n+++ b/gcc/ipa-sra.cc\n@@ -1 +1 @@\n-old\n+new\n"
        )

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
    tools = {t.__name__: t for t in _build_tools(repo, SHA, budget, _ExcerptLog())}

    assert "ipa-sra: fix parameter liveness" in tools["show_commit"]()
    assert tools["list_dir"]() == "ipa-sra.cc"
    for name in ("show_commit", "grep_repo", "find_symbol"):
        out = tools[name]("x") if name != "show_commit" else tools[name]()
        assert "[budget]" in str(out)


def test_grep_defaults_to_the_commits_own_directories():
    repo = _fake_repo()
    captured = {}
    repo.grep_repo = lambda sha, pattern, paths: captured.setdefault("paths", paths)
    tools = {t.__name__: t for t in _build_tools(repo, SHA, _ToolBudget(), _ExcerptLog())}

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
        "what_changed": "A parameter is now marked dead.",
        "how_it_works": "The pass re-runs liveness.",
        "why_it_matters": "Fewer spills.",
    }
    payload.update(overrides)
    return payload


#: What `note_excerpt` would have logged during the run.
_NOTED = [{"path": "gcc/ipa-sra.cc", "lines": "1-3", "symbol": "", "note": "why"}]


def _research_draft(**overrides):
    return LessonResearchDraft(**_research_json(**overrides))


def _finalised(subject, repo=None, excerpts=None, **overrides):
    from agents.lesson_agent import _finalise_research

    return _finalise_research(
        _research_draft(**overrides),
        subject,
        repo or _fake_repo(),
        _NOTED if excerpts is None else excerpts,
    )


def test_finalise_research_end_to_end(subject):
    research = _finalised(subject)

    assert research.what_changed == "A parameter is now marked dead."
    assert research.subsystem == "gcc/ipa"
    assert research.excerpts[0].path == "gcc/ipa-sra.cc"


def test_the_quotable_material_comes_from_git_not_the_model(subject):
    """The explorer names regions; the pipeline reads the bytes.

    Re-typing a 12k-char diff and several 6k-char excerpts into one tool call
    is what broke stage 1 on 2026-09-14 ("Exceeded maximum output retries"),
    and it risks a paraphrase where the article conventions demand exact bytes.
    """
    research = _finalised(subject)

    assert "ipa-sra: fix parameter liveness" in research.commit_message
    assert research.diff.startswith("diff --git")
    assert research.changed_files == ["gcc/ipa-sra.cc"]
    assert "code" in research.excerpts[0].code
    # …and the model is not even offered the fields it used to have to echo.
    assert {"commit_message", "diff", "changed_files", "excerpts"}.isdisjoint(
        LessonResearchDraft.model_fields
    )


def test_excerpt_line_ranges_are_passed_through_to_the_read(subject):
    repo = FakeRepo()
    _finalised(
        subject, cast(SourceRepo, repo),
        excerpts=[{"path": "gcc/ipa-sra.cc", "lines": "1204-1231", "note": "why"}],
    )

    assert ("gcc/ipa-sra.cc", 1204, 1231) in repo.ranges


def test_an_unreadable_excerpt_path_is_dropped(subject):
    """Same guard as the writer's citations, one stage earlier and free."""
    repo = _fake_repo(present={"gcc/ipa-sra.cc"})
    research = _finalised(
        subject, repo,
        excerpts=[
            {"path": "gcc/ipa-sra.cc", "note": "real"},
            {"path": "gcc/invented.cc", "note": "not there at this commit"},
        ],
    )

    assert [e.path for e in research.excerpts] == ["gcc/ipa-sra.cc"]


@pytest.mark.parametrize(
    "value,expected",
    [
        ("1204-1231", (1204, 1231)),
        ("1204–1231", (1204, 1231)),   # en dash
        ("1231-1204", (1204, 1231)),   # reversed
        ("1204", (1204, None)),
        ("the top of the file", (1, None)),
        (None, (1, None)),
        ("", (1, None)),
    ],
)
def test_line_range_parsing(value, expected):
    """A malformed range falls back to read_file's window, never an error.

    Losing the exact window of one excerpt is not worth failing a paid run.
    """
    from agents.lesson_agent import _parse_line_range

    assert _parse_line_range(value) == expected


def test_research_identity_is_forced_from_the_subject(subject):
    """A hallucinated SHA would attach the dossier to the wrong commit."""
    research = _finalised(subject, commit_hash="b" * 40, subsystem="")

    assert research.commit_hash == SHA
    assert research.subsystem == "gcc/ipa"


def test_null_is_read_as_nothing_to_report(subject):
    """``"external_context": null`` means "I found nothing", not a type error.

    Two of the four stubs on disk as of 2026-09-14 died on exactly this, and a
    ValidationError here is non-retryable — it costs the whole week's lesson.
    """
    research = _finalised(subject, external_context=None, open_questions=None)

    assert research.external_context == []
    assert research.open_questions == []


def test_too_many_excerpts_are_trimmed(subject):
    from agents.lesson_agent import _RESEARCH_LIST_CAPS

    cap = _RESEARCH_LIST_CAPS["excerpts"]
    paths = {f"f{i}.cc" for i in range(cap + 5)}
    research = _finalised(
        subject, _fake_repo(present=paths),
        excerpts=[{"path": f"f{i}.cc"} for i in range(cap + 5)],
    )
    assert len(research.excerpts) == cap


def test_over_long_prose_is_clamped(subject):
    from agents.lesson_agent import _RESEARCH_STR_CAPS

    cap = _RESEARCH_STR_CAPS["how_it_works"]
    research = _finalised(subject, how_it_works="z" * (cap + 500))
    assert len(research.how_it_works) == cap


def test_the_draft_carries_no_caps_of_its_own():
    """The caps are repairs, not requirements — the model must not hit them.

    Put them in the output schema and an over-long field comes back as a
    validation failure and a paid reprompt, instead of being quietly trimmed.
    """
    draft = cast(Any, _research_draft(how_it_works="z" * 99_000))

    assert len(draft.how_it_works) == 99_000


def test_research_draft_asks_only_for_what_the_model_can_supply():
    """The twin is derived, so it cannot drift — this fails if it ever does."""
    from agents.models.lesson import LESSON_RESEARCH_FROM_REPO

    asked = set(LessonResearchDraft.model_fields)
    strict = set(LessonResearch.model_fields)

    # Everything asked for exists on the strict model…
    assert asked <= strict
    # …minus what git supplies and what the agent counts itself.
    assert asked == strict - LESSON_RESEARCH_FROM_REPO - {"tool_calls_used"}


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


# ---------------------------------------------------------------------------
# An empty dossier is a failure, not an article
# ---------------------------------------------------------------------------
#
# The regression these guard against shipped and was caught in production on
# 2026-09-14: with every draft field nullable, the explorer answered with the
# two identity fields after one tool call and 53 tokens, and the writer — which
# never opens a file — spent $0.08 of Opus writing "No Dossier, No Lesson: Why
# This Week's Article Cannot Be Written". That article is `is_stub: false`, so
# it passed validation and was committed, one merge from the front page.

def test_dossier_without_excerpts_is_rejected(subject):
    with pytest.raises(ValueError, match="no source excerpts"):
        _finalised(subject, excerpts=[])


def test_dossier_whose_every_excerpt_was_dropped_is_rejected(subject):
    """Naming only paths that don't exist leaves the writer with nothing."""
    with pytest.raises(ValueError, match="no source excerpts"):
        _finalised(subject, _fake_repo(present=set()),
                   excerpts=[{"path": "gcc/invented.cc"}])


def test_dossier_without_diff_or_message_is_rejected(subject):
    """An empty `git show` means the clone cannot back the article up."""
    repo = _fake_repo()
    repo.show_commit = lambda sha: "   "          # type: ignore[method-assign]

    with pytest.raises(ValueError, match="neither a diff nor a commit message"):
        _finalised(subject, repo)


def test_the_evidence_fields_are_required_of_the_explorer():
    """A nullable-everything schema invites the empty answer that caused this.

    These carry defaults on `LessonResearch` so a stub can be constructed; the
    explorer is not free to use them.
    """
    required = set(LessonResearchDraft.model_json_schema()["required"])

    assert {"what_changed", "how_it_works", "why_it_matters"} <= required
    # …while the genuinely optional ones stay omittable.
    assert {"open_questions", "external_context"}.isdisjoint(required)


def test_the_writer_must_return_a_body():
    """A lesson with no sections is not a lesson."""
    required = set(LessonDraft.model_json_schema()["required"])

    assert {"sections", "takeaways"} <= required
    # `_drop_unread_code_refs` can legitimately empty the code tour, so
    # requiring it here would promise something the pipeline then removes.
    assert "code_tour" not in required


# ---------------------------------------------------------------------------
# Stage 1's schema has to be one Gemini can actually fill
# ---------------------------------------------------------------------------
#
# Three consecutive runs on 2026-09-14 stubbed with `UnexpectedModelBehavior:
# Exceeded maximum output retries` because the research output schema carried
# `$defs`/`$ref` (a nested excerpt object) and `anyOf: [..., null]`. Gemini's
# function-calling dialect supports neither, and because OpenRouter speaks the
# OpenAI-compatible API, pydantic-ai applies its OpenAI schema transformer
# rather than its Google one — whatever the schema says goes out verbatim.
#
# The tell was run 1: with nothing required but the two identity strings, the
# model answered instantly and validly, because it never had to construct the
# `$ref`'d object. Make that object required and it cannot answer at all.

def test_research_schema_is_flat_enough_for_gemini():
    schema = json.dumps(LessonResearchDraft.model_json_schema())

    assert "$ref" not in schema
    assert "$defs" not in schema
    assert "anyOf" not in schema
    assert '"null"' not in schema


def test_research_schema_is_only_strings_and_string_lists():
    """The shapes every function-calling implementation agrees on."""
    props = LessonResearchDraft.model_json_schema()["properties"]

    for name, spec in props.items():
        assert spec["type"] in ("string", "array"), f"{name} is {spec['type']}"
        if spec["type"] == "array":
            assert spec["items"] == {"type": "string"}, name


def test_note_excerpt_records_what_the_explorer_read():
    log = _ExcerptLog()
    tools = {t.__name__: t for t in _build_tools(_fake_repo(), SHA, _ToolBudget(), log)}

    tools["note_excerpt"]("gcc/ipa-sra.cc", "1204-1231", "isra", "the invariant")

    assert log.records == [{
        "path": "gcc/ipa-sra.cc", "lines": "1204-1231",
        "symbol": "isra", "note": "the invariant",
    }]


def test_note_excerpt_does_not_spend_the_read_budget():
    """Bookkeeping must not compete with reading files — that buys nothing."""
    budget = _ToolBudget(limit=3)
    tools = {t.__name__: t for t in _build_tools(_fake_repo(), SHA, budget, _ExcerptLog())}

    for _ in range(5):
        tools["note_excerpt"]("gcc/ipa-sra.cc")

    assert budget.used == 0


def test_note_excerpt_stops_at_the_cap():
    log = _ExcerptLog(limit=2)
    tools = {t.__name__: t for t in _build_tools(_fake_repo(), SHA, _ToolBudget(), log)}

    replies = [tools["note_excerpt"](f"f{i}.cc") for i in range(4)]

    assert len(log.records) == 2
    assert "[budget]" in replies[-1]


def test_note_excerpt_rejects_an_empty_path():
    log = _ExcerptLog()
    tools = {t.__name__: t for t in _build_tools(_fake_repo(), SHA, _ToolBudget(), log)}

    assert "[error]" in tools["note_excerpt"]("   ")
    assert log.records == []


def test_every_capped_list_is_trimmed_not_rejected(subject):
    """Derived from the model, because the hand-written list missed one.

    `primer_glossary` was absent from the old hardcoded caps, so when the
    writer followed its instruction to "err on the side of more entries" and
    produced 17 against a cap of 10, a finished and paid-for article died on
    `too_long`. Deriving the caps covers any capped list the model grows.
    """
    from agents.lesson_agent import _LESSON_LIST_CAPS

    assert "primer_glossary" in _LESSON_LIST_CAPS

    item = _writer_item(
        primer_glossary=[
            {"term": f"T{i}", "definition": f"Definition number {i}."}
            for i in range(17)
        ],
        prerequisites=[f"p{i}" for i in range(20)],
    )
    _repair_lesson_item(item, subject)

    for key, cap in _LESSON_LIST_CAPS.items():
        assert len(item.get(key) or []) <= cap, key
    # …and the whole thing still validates, which is the point.
    assert LessonDigest.model_validate(item).primer_glossary


def test_list_caps_match_the_model_exactly():
    """A drifting mirror of the schema is how the last failure happened."""
    from agents.lesson_agent import _LESSON_LIST_CAPS

    for name, field in LessonDigest.model_fields.items():
        caps = [getattr(m, "max_length", None) for m in field.metadata]
        caps = [c for c in caps if c is not None]
        origin = getattr(field.annotation, "__origin__", field.annotation)
        if caps and origin is list:
            assert _LESSON_LIST_CAPS.get(name) == caps[0], name


def test_an_oversized_read_is_clamped_not_rejected(subject):
    """`read_file` returns up to 8192 bytes; `SourceExcerpt.code` caps at 6000.

    The excerpt is read from the clone, so overrunning the cap is the normal
    case, not an edge one. `_read_excerpts` therefore hands back dicts and lets
    `_clamp_to_schema` trim them — building the strict model early validates
    before the clamp can run, which is exactly how a run was lost.
    """
    from agents.lesson_agent import _EXCERPT_STR_CAPS

    cap = _EXCERPT_STR_CAPS["code"]
    repo = FakeRepo()
    repo.read_file = (                                   # type: ignore[method-assign]
        lambda sha, path, start_line=1, end_line=None: "x" * (cap + 2192)
    )

    research = _finalised(subject, cast(SourceRepo, repo))

    assert len(research.excerpts[0].code) == cap


def test_every_nested_string_cap_is_repaired(subject):
    """`code_tour.path/symbol/lines` and `further_reading.title/url` had none.

    Each was a way to lose a finished, paid-for article to a mechanical
    overshoot. The repair is derived from the nested models so it cannot fall
    behind the schema the way the hand-written mirrors did.
    """
    item = _writer_item(
        sections=[{"heading": "H" * 400, "body": "B" * 9000}],
        code_tour=[{
            "path": "p" * 900, "symbol": "s" * 900,
            "lines": "l" * 900, "why": "w" * 900,
        }],
        further_reading=[{"title": "t" * 900, "url": "u" * 900}],
        primer_glossary=[{"term": "T" * 900, "definition": "D" * 900}],
    )
    _repair_lesson_item(item, subject)

    # Validation is the assertion: every cap above is enforced by the model.
    lesson = LessonDigest.model_validate(item)
    assert lesson.code_tour[0].path
    assert lesson.further_reading[0].url


def test_an_optional_nested_string_stays_absent_not_empty(subject):
    """`symbol: null` must not become `symbol: ""` in the frontmatter."""
    item = _writer_item(
        code_tour=[{"path": "gcc/ipa-sra.cc", "why": "because"}],
    )
    _repair_lesson_item(item, subject)

    assert "symbol" not in item["code_tour"][0]
    assert LessonDigest.model_validate(item).code_tour[0].symbol is None


def test_both_lesson_stages_reserve_an_explicit_max_tokens():
    """An uncapped call reserves the model's own ceiling against the balance.

    OpenRouter holds `max_tokens` worth of credit up front. With no cap that is
    whatever the model could theoretically emit — 65535 for gemini-2.5-flash —
    so on 2026-09-16 the nightly lost the lesson at research with "you
    requested up to 65535 tokens", before reading a single file. The writer has
    carried a cap since the identical failure; stage 1 was simply missed.
    """
    import inspect

    import agents.lesson_agent as la
    from agents._openrouter import (
        LESSON_RESEARCH_MAX_TOKENS,
        LESSON_WRITER_MAX_TOKENS,
    )

    source = inspect.getsource(la)
    assert "build_model(model_name)" not in source, (
        "a lesson stage builds its model without max_tokens — it will reserve "
        "the model's full ceiling against the key's balance"
    )
    # Both caps must clear what the stages actually produce: research has
    # measured 1202-2585 output tokens, a full article 7832.
    assert LESSON_RESEARCH_MAX_TOKENS > 2585 * 2
    assert LESSON_WRITER_MAX_TOKENS > 7832
