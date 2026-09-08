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

import pytest

from agents.lesson_agent import (
    _ToolBudget,
    _build_tools,
    _drop_unread_code_refs,
    _parse_lesson,
    _render_dossier,
    _repair_lesson_item,
    stub_lesson,
)
from agents.lesson_picker import LessonSubject, previous_complete_week
from agents.models.lesson import LessonResearch, SourceExcerpt

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
    repo = FakeRepo(present={"gcc/ipa-sra.cc"})
    item = {"code_tour": [
        {"path": "gcc/ipa-sra.cc", "why": "real"},
        {"path": "gcc/totally-made-up.cc", "why": "invented"},
    ]}
    _drop_unread_code_refs(item, repo, SHA)

    assert [r["path"] for r in item["code_tour"]] == ["gcc/ipa-sra.cc"]


def test_malformed_code_refs_are_dropped():
    repo = FakeRepo()
    item = {"code_tour": [{"why": "no path"}, "not-a-dict", {"path": ""}]}
    _drop_unread_code_refs(item, repo, SHA)
    assert item["code_tour"] == []


def test_parse_lesson_end_to_end(subject):
    repo = FakeRepo()
    lesson = _parse_lesson(_writer_output(), subject, repo)

    assert lesson.lesson_id == "gcc:2026-W36"
    assert lesson.commit_hash == SHA
    assert lesson.week_start == date(2026, 8, 31)
    assert lesson.commit_date == date(2026, 9, 2)
    assert [r.path for r in lesson.code_tour] == ["gcc/ipa-sra.cc"]


def test_parse_lesson_strips_markdown_fences(subject):
    repo = FakeRepo()
    fenced = "```json\n" + _writer_output() + "\n```"
    assert _parse_lesson(fenced, subject, repo).commit_hash == SHA


def test_parse_lesson_unwraps_a_single_element_array(subject):
    """Models wrap a lone object in an array surprisingly often."""
    repo = FakeRepo()
    wrapped = "[" + _writer_output() + "]"
    assert _parse_lesson(wrapped, subject, repo).commit_hash == SHA


@pytest.mark.parametrize("bad", ["[]", '"a string"', "not json at all"])
def test_parse_lesson_rejects_unusable_output(subject, bad):
    repo = FakeRepo()
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
    repo = FakeRepo()
    budget = _ToolBudget(limit=2)
    tools = {t.__name__: t for t in _build_tools(repo, SHA, budget)}

    assert tools["show_commit"]() == "commit body"
    assert tools["list_dir"]() == "ipa-sra.cc"
    for name in ("show_commit", "grep_repo", "find_symbol"):
        out = tools[name]("x") if name != "show_commit" else tools[name]()
        assert "[budget]" in str(out)


def test_grep_defaults_to_the_commits_own_directories():
    repo = FakeRepo()
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
