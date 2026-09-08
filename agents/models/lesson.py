"""LessonDigest — output model for the Lesson of the Week agent.

A lesson is a different genre from a digest. Discussions and landings *report*:
what was proposed, what merged, why a working dev should care, in a few
sentences. A lesson *teaches*: it takes the most instructive thing that merged
that week and uses it as the way in to a concept the reader can carry to the
next patch they read.

The structure below encodes that intent. ``concept`` is the transferable idea,
not the changelog line. ``code_tour`` is the evidence — every entry names a
real file the agent opened in the source tree at that commit, so a claim in the
prose can be checked against the code. ``sections`` carry the article body and
are rendered into the Markdown body by the writer, so Astro renders a lesson
with the same ``<Content />`` pipeline as every other article type.
"""

from datetime import date, datetime

from pydantic import BaseModel, Field

from agents.models.base import BimodalBase


class LessonSection(BaseModel):
    """One titled movement of the article body."""

    heading: str = Field(..., max_length=120)
    body: str = Field(..., max_length=4000)


class CodeRef(BaseModel):
    """A file the lesson actually walks through.

    ``path`` is repo-relative and must be a real path at the lesson's commit —
    the agent is instructed to only cite files it opened via the source-repo
    tools, which is what separates a code tour from a plausible-looking list.
    """

    path: str = Field(..., max_length=300)          # e.g. "gcc/ipa-sra.cc"
    symbol: str | None = Field(default=None, max_length=160)
    lines: str | None = Field(default=None, max_length=40)   # e.g. "1204-1231"
    why: str = Field(..., max_length=300)           # one sentence


class FurtherReading(BaseModel):
    title: str = Field(..., max_length=200)
    url: str = Field(..., max_length=500)


class LessonDigest(BimodalBase):
    lesson_id: str                    # "<project>:<iso-year>-W<week>", e.g. "gcc:2026-W36"
    commit_hash: str
    source_type: str                  # preserved from the landing it teaches
    headline: str = Field(..., max_length=140)
    hook: str = Field(..., max_length=200)          # why read this
    tldr: str = Field(..., max_length=160)
    concept: str = Field(..., max_length=300)       # the transferable idea
    prerequisites: list[str] = Field(default_factory=list, max_length=6)
    # 4–6 movements: background → mechanism → the change → consequences →
    # try it yourself. The writer joins these into the Markdown body.
    sections: list[LessonSection] = Field(default_factory=list, max_length=8)
    code_tour: list[CodeRef] = Field(default_factory=list, max_length=10)
    takeaways: list[str] = Field(default_factory=list, max_length=6)
    further_reading: list[FurtherReading] = Field(default_factory=list, max_length=6)
    # Slug of the landing article this lesson expands on, for the back-link.
    landing_slug: str | None = None
    url: str                          # upstream commit URL
    # The week this lesson covers. ``date`` is the week's END date, not the
    # commit's — a weekly piece should sort alongside the week it covers, and a
    # commit from Monday would otherwise bury it under Friday's landings all
    # week. The commit's own date is kept separately so the article can say
    # when the change actually landed.
    week_start: date
    week_end: date
    commit_date: date
    date: datetime
    # True when the agent could not produce a real lesson. Written to disk so
    # /admin can see the failure; filtered out of the public site.
    is_stub: bool = False
    stub_reason: str = ""


# ---------------------------------------------------------------------------
# Stage 1 — the research dossier
# ---------------------------------------------------------------------------
#
# Generating a lesson is split in two. A cheap reasoning model navigates the
# source tree over many turns and fills in the dossier below; a single call to
# a much stronger model then turns that dossier into the article.
#
# The split exists for cost. A multi-turn agent resends its whole conversation
# every turn, so token spend grows quadratically with tool calls — the worst
# possible shape to pay premium rates for. Doing the exploration cheaply and
# the writing once means the reader still gets top-tier prose at roughly a
# sixth of the price of running the strong model through the whole loop.
#
# It also means the writer never opens a file itself. Everything it is allowed
# to assert about the code has to be in here, which is why the excerpts are
# stored verbatim rather than summarised.


class SourceExcerpt(BaseModel):
    """A region of a file, copied verbatim out of the tree at this commit.

    Verbatim on purpose: the writing model cannot open files, so a paraphrase
    here becomes a paraphrase in the article, and identifiers stop being
    trustworthy. CLAUDE.md's article conventions require them to survive exact.
    """

    path: str = Field(..., max_length=300)
    lines: str | None = Field(default=None, max_length=40)    # "1204-1231"
    symbol: str | None = Field(default=None, max_length=160)
    code: str = Field(..., max_length=6000)
    note: str = Field(default="", max_length=400)   # why the explorer opened it


class LessonResearch(BaseModel):
    """What the explorer found. The sole input to the writing pass."""

    commit_hash: str
    subsystem: str
    # The commit message and diff, verbatim (capped by the repo tools).
    commit_message: str = Field(default="", max_length=8000)
    diff: str = Field(default="", max_length=12000)
    changed_files: list[str] = Field(default_factory=list, max_length=40)
    # The regions the explorer actually read, in the order it read them.
    excerpts: list[SourceExcerpt] = Field(default_factory=list, max_length=12)
    # Prose findings, in the explorer's own words. Not the article — raw
    # material for it.
    what_changed: str = Field(default="", max_length=3000)
    how_it_works: str = Field(default="", max_length=4000)
    why_it_matters: str = Field(default="", max_length=2000)
    open_questions: list[str] = Field(default_factory=list, max_length=6)
    # Outside grounding (papers, wiki pages, ISA notes) from search_web.
    external_context: list[str] = Field(default_factory=list, max_length=10)
    tool_calls_used: int = 0
