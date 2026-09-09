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
from typing import cast

import pytest

from agents.lesson_agent import (
    _build_tools,
    _drop_unread_code_refs,
    _parse_lesson,
    _render_dossier,
    _repair_lesson_item,
    _ToolBudget,
    stub_lesson,
)
from agents.lesson_picker import LessonSubject, previous_complete_week
from agents.models.lesson import LessonResearch, SourceExcerpt
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


def _writer_output(**overrides) -> str:
    item = {
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
    return json.dumps(item)


# ---------------------------------------------------------------------------
# Identity is forced, not trusted
# ---------------------------------------------------------------------------

def test_identity_fields_are_forced_from_the_subject(subject):
    """A model typo here would misattribute the article to the wrong commit."""
    item = json.loads(_writer_output())
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
    item = json.loads(_writer_output())
    _repair_lesson_item(item, subject)

    assert item["week_start"] == "2026-08-31"
    assert item["week_end"] == "2026-09-06"
    assert item["commit_date"] == "2026-09-02"
    # The article is dated by its week, not by the commit.
    assert item["date"] == "2026-09-06"


def test_unknown_subsystem_falls_back_to_the_landing(subject):
    for value in ("unknown", "general", "", None):
        item = json.loads(_writer_output())
        item["subsystem"] = value
        _repair_lesson_item(item, subject)
        assert item["subsystem"] == "gcc/ipa"


# ---------------------------------------------------------------------------
# Length repair
# ---------------------------------------------------------------------------

def test_overlong_fields_are_clipped_not_rejected(subject):
    """A ten-character overshoot should not cost the whole (paid) run."""
    item = json.loads(_writer_output(
        headline="x" * 400, hook="y" * 400, tldr="z" * 400, concept="c" * 900,
    ))
    _repair_lesson_item(item, subject)

    assert len(item["headline"]) <= 140
    assert len(item["hook"]) <= 200
    assert len(item["tldr"]) <= 160
    assert len(item["concept"]) <= 300
    assert item["headline"].endswith("…")


def test_overlong_lists_are_truncated(subject):
    item = json.loads(_writer_output(
        tags=[f"t{i}" for i in range(20)],
        takeaways=[f"take {i}" for i in range(20)],
    ))
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


def test_parse_lesson_end_to_end(subject):
    repo = _fake_repo()
    lesson = _parse_lesson(_writer_output(), subject, repo)

    assert lesson.lesson_id == "gcc:2026-W36"
    assert lesson.commit_hash == SHA
    assert lesson.week_start == date(2026, 8, 31)
    assert lesson.commit_date == date(2026, 9, 2)
    assert [r.path for r in lesson.code_tour] == ["gcc/ipa-sra.cc"]


def test_parse_lesson_strips_markdown_fences(subject):
    repo = _fake_repo()
    fenced = "```json\n" + _writer_output() + "\n```"
    assert _parse_lesson(fenced, subject, repo).commit_hash == SHA


def test_parse_lesson_unwraps_a_single_element_array(subject):
    """Models wrap a lone object in an array surprisingly often."""
    repo = _fake_repo()
    wrapped = "[" + _writer_output() + "]"
    assert _parse_lesson(wrapped, subject, repo).commit_hash == SHA


@pytest.mark.parametrize("bad", ["[]", '"a string"', "not json at all"])
def test_parse_lesson_rejects_unusable_output(subject, bad):
    repo = _fake_repo()
    with pytest.raises((ValueError, json.JSONDecodeError)):
        _parse_lesson(bad, subject, repo)


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
# Dossier parsing must survive a real model's output
# ---------------------------------------------------------------------------
#
# Both of the first two production runs failed at this stage, and the cost of a
# failure here is the whole article — every tool call in the research loop has
# already been paid for by the time the parse runs. It must be generous.

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


def test_parses_json_wrapped_in_prose(subject):
    """A reasoning model narrates. That must not cost the article."""
    import json as _json

    from agents.lesson_agent import _parse_research

    text = (
        "Sure! I explored the tree. Here is the dossier you asked for:\n\n"
        "```json\n" + _json.dumps(_research_json()) + "\n```\n\n"
        "Let me know if you'd like me to look at anything else."
    )
    research = _parse_research(text, subject)
    assert research.what_changed == "A parameter is now marked dead."


def test_parses_bare_json_with_a_trailing_remark(subject):
    import json as _json

    from agents.lesson_agent import _parse_research

    text = _json.dumps(_research_json()) + "\n\nHope that helps!"
    assert _parse_research(text, subject).subsystem == "gcc/ipa"


def test_braces_inside_strings_do_not_confuse_the_scan(subject):
    import json as _json

    from agents.lesson_agent import _parse_research

    payload = _research_json(
        what_changed='Handles the `struct { int a; }` case and a quote \\" too.'
    )
    text = "Preamble.\n" + _json.dumps(payload) + "\nTrailer."
    assert "struct { int a; }" in _parse_research(text, subject).what_changed


def test_oversized_excerpt_is_clamped_not_rejected(subject):
    """`read_file` returns up to 8192 bytes; SourceExcerpt.code caps at 6000.

    A model copying an excerpt verbatim — exactly as instructed — therefore
    produces a value pydantic rejects. Losing the tail of one excerpt beats
    losing the whole dossier.
    """
    import json as _json

    from agents.lesson_agent import _EXCERPT_STR_CAPS, _parse_research

    cap = _EXCERPT_STR_CAPS["code"]
    payload = _research_json(
        excerpts=[{"path": "gcc/ipa-sra.cc", "code": "x" * (cap + 2192)}]
    )
    research = _parse_research(_json.dumps(payload), subject)
    assert len(research.excerpts[0].code) == cap


def test_too_many_excerpts_are_trimmed(subject):
    import json as _json

    from agents.lesson_agent import _RESEARCH_LIST_CAPS, _parse_research

    cap = _RESEARCH_LIST_CAPS["excerpts"]
    payload = _research_json(
        excerpts=[{"path": f"f{i}.cc", "code": "y"} for i in range(cap + 5)]
    )
    research = _parse_research(_json.dumps(payload), subject)
    assert len(research.excerpts) == cap


def test_over_long_prose_is_clamped(subject):
    import json as _json

    from agents.lesson_agent import _RESEARCH_STR_CAPS, _parse_research

    cap = _RESEARCH_STR_CAPS["how_it_works"]
    payload = _research_json(how_it_works="z" * (cap + 500))
    research = _parse_research(_json.dumps(payload), subject)
    assert len(research.how_it_works) == cap


def test_output_with_no_json_still_raises(subject):
    """Generosity has a limit — nothing parseable is still a failure."""
    from agents.lesson_agent import _parse_research

    with pytest.raises(ValueError, match="no JSON object"):
        _parse_research("I was unable to complete this task.", subject)


def test_unterminated_json_raises(subject):
    from agents.lesson_agent import _parse_research

    with pytest.raises(ValueError, match="unterminated"):
        _parse_research('{"commit_message": "truncated mid', subject)


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
