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

from pydantic import BaseModel, Field, model_validator

from agents.models.base import BimodalBase
from agents.models.draft import draft_model


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


class ExcerptRequest(BaseModel):
    """A region the explorer wants in the dossier — named, not copied.

    The counterpart to ``SourceExcerpt``: same identity fields, no ``code``.
    The explorer says *which* lines matter and why; ``lesson_agent`` reads the
    bytes back out of git at the lesson's commit.

    That split is why it exists. Asking the model to re-type the region put
    thousands of characters of verbatim C into a single tool call — expensive,
    and on 2026-09-14 the thing that broke stage 1 outright ("Exceeded maximum
    output retries") once the dossier's evidence fields became required. Reading
    from the clone is cheaper, cannot truncate, and makes "verbatim" structural
    rather than an instruction the model is asked to honour.
    """

    path: str = Field(..., max_length=300)
    lines: str | None = Field(default=None, max_length=40)    # "1204-1231"
    symbol: str | None = Field(default=None, max_length=160)
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

    @model_validator(mode="before")
    @classmethod
    def _null_means_absent(cls, data: object) -> object:
        """Treat an explicit ``null`` as "not provided" for optional fields.

        Most fields above carry a default, but a default only applies when the
        key is *missing*, not when it is present and null. Models routinely emit
        ``"external_context": null`` for "I found nothing", which Pydantic
        rejects as a type error — and since a ValidationError here is
        non-retryable, that one null costs the whole lesson. Two of the four
        stubs on disk as of 2026-09-14 are exactly this, both on
        ``external_context``.

        Dropping the null lets the default_factory produce ``[]``, which is
        what the model meant. Required fields are untouched: removing a null
        for ``commit_hash`` still raises "field required", which is the honest
        error rather than a silently empty article.
        """
        if not isinstance(data, dict):
            return data
        optional = {
            name for name, field in cls.model_fields.items() if not field.is_required()
        }
        return {
            key: value
            for key, value in data.items()
            if not (value is None and key in optional)
        }


# ---------------------------------------------------------------------------
# Structured-output twins
# ---------------------------------------------------------------------------
#
# What the two agents are actually asked to produce. Both are lenient
# derivations of the strict models above — see agents/models/draft.py for why
# the models are not pointed straight at LessonResearch / LessonDigest.

#: What the explorer must supply itself. The dossier's other evidence —
#: ``commit_message``, ``diff``, ``changed_files`` and each excerpt's ``code``
#: — is read from the clone instead, so it is absent from the draft entirely.
#: These carry defaults on ``LessonResearch`` because a stub has to be
#: constructible; the explorer is not free to omit them. See the ``require``
#: note in models/draft.py.
LESSON_RESEARCH_REQUIRED = frozenset(
    {
        "excerpts",
        "what_changed",
        "how_it_works",
        "why_it_matters",
    }
)

#: Fields the pipeline reads out of the source clone rather than asking for.
#: Deterministic facts we already hold: making a model re-type them costs
#: output tokens, risks truncation, and invites a paraphrase where the article
#: conventions demand the exact bytes.
LESSON_RESEARCH_FROM_REPO = frozenset({"commit_message", "diff", "changed_files"})

#: Stage 1's output shape. ``commit_hash`` stays required and is overwritten
#: from the subject afterwards, so a typo cannot misattribute the dossier.
#: ``tool_calls_used`` is dropped: the explorer cannot count its own budget,
#: and the agent fills it in from the real counter.
LessonResearchDraft = draft_model(
    LessonResearch,
    name="LessonResearchDraft",
    exclude=frozenset({"tool_calls_used"}) | LESSON_RESEARCH_FROM_REPO,
    require=LESSON_RESEARCH_REQUIRED,
    override={"excerpts": list[ExcerptRequest]},
)

#: Fields of ``LessonDigest`` the pipeline fills in from the subject rather
#: than the writer: identity, provenance, the week's dates, and the stub flags.
#: Asking a model to echo them costs tokens and invites a typo in exactly the
#: values that decide which commit the article is about.
LESSON_INJECTED_FIELDS = frozenset(
    {
        "project",
        "patch_id",
        "lesson_id",
        "commit_hash",
        "source_type",
        "url",
        "landing_slug",
        "week_start",
        "week_end",
        "commit_date",
        "date",
        "is_stub",
        "stub_reason",
    }
)

#: Stage 2's output shape: the article fields the writer actually authors.
#: ``sections`` and ``takeaways`` are required for the same reason as the
#: dossier's evidence fields — a lesson without a body is not a lesson, and
#: their defaults on ``LessonDigest`` exist to let a stub be constructed.
#: ``code_tour`` stays optional: ``_drop_unread_code_refs`` can legitimately
#: empty it, so requiring it here would promise something we then take away.
LessonDraft = draft_model(
    LessonDigest,
    name="LessonDraft",
    exclude=LESSON_INJECTED_FIELDS,
    require=frozenset({"sections", "takeaways"}),
)
