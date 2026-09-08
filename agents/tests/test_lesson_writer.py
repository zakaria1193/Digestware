"""Tests for serialising a lesson to Markdown.

A lesson is long-form, so it exercises the writer's body validation from the
opposite side to the digest types: the same guards that reject a truncated
two-sentence summary must not reject a legitimate 800-word article.
"""

from __future__ import annotations

from datetime import date, datetime, timezone
from pathlib import Path

import pytest

from agents.models.lesson import CodeRef, LessonDigest, LessonSection
from agents.tools.frontmatter import load_frontmatter
from agents.writer import render_sections, write_lesson

WEEK_START = date(2026, 8, 31)
WEEK_END = date(2026, 9, 6)


def _paragraph(words: int) -> str:
    return " ".join(["compiler"] * (words - 1)) + " pass."


def _lesson(**overrides) -> LessonDigest:
    defaults = dict(
        lesson_id="gcc:2026-W36",
        commit_hash="a" * 40,
        project="gcc",
        subsystem="gcc/ipa",
        source_type="github",
        headline="How IPA-SRA decides a parameter is dead",
        hook="A three-line fix is the shortest route into interprocedural analysis.",
        tldr="GCC repairs parameter liveness in IPA-SRA.",
        concept="Interprocedural passes must agree on what a parameter means.",
        prerequisites=["what a GIMPLE pass is"],
        sections=[
            LessonSection(heading="Background", body=_paragraph(150)),
            LessonSection(heading="The change", body=_paragraph(150)),
        ],
        code_tour=[
            CodeRef(path="gcc/ipa-sra.cc", symbol="isra_call_summary",
                    lines="1204-1231", why="Where liveness is decided."),
        ],
        takeaways=["Check both directions of an analysis."],
        tags=["ipa", "optimization"],
        url="https://github.com/gcc-mirror/gcc/commit/" + "a" * 40,
        week_start=WEEK_START,
        week_end=WEEK_END,
        commit_date=date(2026, 9, 2),
        date=datetime(2026, 9, 6, tzinfo=timezone.utc),
    )
    defaults.update(overrides)
    return LessonDigest(**defaults)


def test_filename_is_dated_by_week_end_and_project(tmp_path: Path):
    """Named by the week it covers, not the commit — so it sorts with the week."""
    path = write_lesson(_lesson(), output_dir=tmp_path)
    assert path.name.startswith("2026-09-06-gcc-")
    assert path.name.endswith(".md")


def test_two_projects_same_week_do_not_collide(tmp_path: Path):
    a = write_lesson(_lesson(), output_dir=tmp_path)
    b = write_lesson(
        _lesson(project="binutils", lesson_id="binutils:2026-W36"),
        output_dir=tmp_path,
    )
    assert a != b
    assert len(list(tmp_path.glob("*.md"))) == 2


def test_frontmatter_roundtrips(tmp_path: Path):
    path = write_lesson(_lesson(), output_dir=tmp_path)
    fm, body = load_frontmatter(path.read_text(encoding="utf-8"))

    assert fm["lesson_id"] == "gcc:2026-W36"
    assert fm["project"] == "gcc"
    assert fm["commit_hash"] == "a" * 40
    # The three date fields are distinct facts and must all survive.
    assert str(fm["week_start"]) == "2026-08-31"
    assert str(fm["week_end"]) == "2026-09-06"
    assert str(fm["commit_date"]) == "2026-09-02"
    assert str(fm["date"]) == "2026-09-06"
    assert fm["code_tour"][0]["path"] == "gcc/ipa-sra.cc"
    assert fm["takeaways"] == ["Check both directions of an analysis."]
    assert "Background" in body


def test_sections_become_markdown_headings(tmp_path: Path):
    path = write_lesson(_lesson(), output_dir=tmp_path)
    body = path.read_text(encoding="utf-8")
    assert "## Background" in body
    assert "## The change" in body


def test_render_sections_skips_empty_bodies():
    out = render_sections([
        LessonSection(heading="Kept", body="Real prose."),
        LessonSection(heading="Dropped", body="   "),
    ])
    assert "## Kept" in out
    assert "Dropped" not in out


def test_long_article_is_accepted(tmp_path: Path):
    """The 260-word digest cap would reject every lesson — hence the wider bounds."""
    lesson = _lesson(sections=[
        LessonSection(heading=f"Part {i}", body=_paragraph(200)) for i in range(4)
    ])
    body = write_lesson(lesson, output_dir=tmp_path).read_text(encoding="utf-8")
    assert "Summary unavailable" not in body
    assert body.count("## Part ") == 4


def test_too_short_falls_back(tmp_path: Path):
    lesson = _lesson(sections=[LessonSection(heading="Stub", body="Too short.")])
    body = write_lesson(lesson, output_dir=tmp_path).read_text(encoding="utf-8")
    assert "Summary unavailable" in body


def test_truncation_detector_still_fires(tmp_path: Path):
    """Wider word bounds must not disable the truncation guard."""
    lesson = _lesson(sections=[
        LessonSection(heading="Cut off", body=_paragraph(300)[:-1] + " and then the"),
    ])
    body = write_lesson(lesson, output_dir=tmp_path).read_text(encoding="utf-8")
    assert "Summary unavailable" in body


def test_quoted_email_detector_still_fires(tmp_path: Path):
    lesson = _lesson(sections=[
        LessonSection(heading="", body="> On Mon, someone wrote:\n\n" + _paragraph(300)),
    ])
    body = write_lesson(lesson, output_dir=tmp_path).read_text(encoding="utf-8")
    assert "Summary unavailable" in body


def test_stub_lesson_writes_without_error(tmp_path: Path):
    """A stub must reach disk — that is how a failure stays visible in /admin."""
    lesson = _lesson(sections=[], is_stub=True, stub_reason="research_failed")
    path = write_lesson(lesson, output_dir=tmp_path)
    fm, body = load_frontmatter(path.read_text(encoding="utf-8"))
    assert fm["is_stub"] is True
    assert fm["stub_reason"] == "research_failed"
    assert "Summary unavailable" in body


# "x" * 140 is the longest headline the schema allows; the slug must still
# come out short enough to be a usable filename.
@pytest.mark.parametrize("headline", ["a/b:c", "Ünïcödé — em dash", "x" * 140])
def test_awkward_headlines_produce_usable_filenames(tmp_path: Path, headline):
    path = write_lesson(_lesson(headline=headline), output_dir=tmp_path)
    assert path.exists()
    # Path separators and non-ASCII must never reach the filename.
    assert "/" not in path.name[len("2026-09-06-gcc-"):]
    assert path.name.isascii()
    assert len(path.name) < 150
