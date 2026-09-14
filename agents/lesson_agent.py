"""Lesson of the Week agent — one in-depth, source-grounded piece per project.

Where the landing agent reads a commit *message*, this reads the **code**. It
is handed one commit that merged during the week and a local bare clone of the
project at that revision, and it navigates the real tree — listing directories,
grepping for a symbol, reading the region the patch touches — before writing an
article that teaches the concept behind the change.

TWO STAGES, AND WHY
-------------------
Stage 1 (``run_research``) explores. Cheap reasoning model, tools bound to one
clone at one SHA, many turns, and it produces a ``LessonResearch`` dossier —
verbatim source excerpts plus notes — rather than prose.

Stage 2 (``run_writer``) writes. One call to an Opus-tier model with the
dossier and no tools at all.

The split is a cost decision, not an aesthetic one. A multi-turn agent resends
its whole conversation every turn, so spend grows quadratically with tool
calls; running a premium model through the exploration loop costs several euro
per article against a EUR 5/month project ceiling. Exploring cheaply and
writing once buys premium prose for roughly a sixth of that.

It has a second benefit worth naming: the writer never opens a file, so
everything it may assert has to be in the dossier. ``_drop_unread_code_refs``
then re-checks every path it cites against the real tree, which is why a
fabricated file reference cannot reach the page.

Both calls are logged to ``agents/output/usage.log`` under distinct agent names
(``lesson_research``, ``lesson_writer``) so the two-stage cost is separable.
"""

from __future__ import annotations

import logging
import re
from datetime import datetime, timezone
from types import UnionType
from typing import Union, get_args, get_origin

from pydantic import BaseModel, TypeAdapter, ValidationError
from pydantic_ai import Agent

from agents._openrouter import (
    DEFAULT_LESSON_RESEARCH_MODEL,
    DEFAULT_LESSON_WRITER_MODEL,
    LESSON_WRITER_MAX_TOKENS,
    build_model,
    model_from_env,
)
from agents._retry import retry_with_backoff
from agents.lesson_picker import LessonSubject
from agents.models.base import GlossaryEntry
from agents.models.lesson import (
    CodeRef,
    FurtherReading,
    LessonDigest,
    LessonDraft,
    LessonResearch,
    LessonResearchDraft,
    LessonSection,
    SourceExcerpt,
)
from agents.tools.glossary_filter import filter_glossary
from agents.tools.source_repo import SourceRepo
from agents.tools.web_search import search_context
from agents.usage_log import append_usage

logger = logging.getLogger(__name__)

# Ceiling on repo/search calls for one lesson. Each call costs a round-trip
# plus the returned text in every subsequent turn's context, so this is the
# dominant cost lever in stage 1 — and, via the dossier it fills, a driver of
# stage 2's input too. Sixteen is enough to read the diff, orient in three or
# four files, and chase a couple of symbols. Raise it only with usage.log
# evidence; lower it first if the budget overruns.
_MAX_TOOL_CALLS = 16

# Excerpts the explorer may flag. Mirrors the cap on ``LessonResearch.excerpts``
# so the log cannot outrun what the dossier can hold. ``note_excerpt`` is
# deliberately NOT charged to the tool budget above: it reads nothing, and
# making bookkeeping compete with the read budget would buy fewer files read.
_MAX_EXCERPTS = 12

_BUDGET_EXHAUSTED = (
    "[budget] The source-exploration budget for this lesson is spent. Stop "
    "calling tools and return the research dossier now, using only what you "
    "have already read. Do not cite files you did not open."
)


_RESEARCH_ADAPTER: TypeAdapter[LessonResearch] = TypeAdapter(LessonResearch)


# ---------------------------------------------------------------------------
# Stage 1 — exploration
# ---------------------------------------------------------------------------

_RESEARCH_PROMPT = """\
You are a staff engineer preparing research notes for a colleague who will
write an in-depth article about one commit. You are NOT writing the article.
Your job is to read the code and hand over everything the writer will need.

YOU HAVE THE SOURCE TREE. The tools below read the project's real repository,
pinned at the exact commit in question. The writer has no such access — they
can only use what you put in the dossier. So anything the article should be
able to assert about the code has to come back in your excerpts.

METHOD (work in this order):
1. ``show_commit`` — read the full message and diff first.
2. ``read_file`` — open the region each hunk touches, plus enough surrounding
   context to see what the code is actually for.
3. ``note_excerpt`` — the moment a region is worth showing the reader, mark it:
   ``note_excerpt(path, lines, symbol, note)``. Do this AS YOU READ, 3 to 8
   times over the run. You are naming the region, not copying it — the code is
   fetched from the repository for you. A region you do not mark does not
   reach the writer.
4. ``grep_repo`` / ``find_symbol`` — chase the one or two symbols that carry
   the concept: the caller, the data structure, the invariant being kept.
5. ``search_web`` — OUTSIDE background only (a paper, a wiki page, an ISA
   note). Never a substitute for reading the code.

Your exploration budget is limited. Spend it on the three or four files that
actually explain the change, not on a survey of the subsystem.

DO NOT finish before you have read the code and called ``note_excerpt`` at
least once. A dossier with no excerpts is rejected outright — the writer
cannot open a file, so it would have nothing to ground the article in.

DO NOT copy code into your answer. The commit message, the diff and the file
contents are read from the repository for you. Your final answer is prose
only.

FINISH by returning these fields, all plain text:
- ``commit_hash``, ``subsystem`` — echo from the input.
- ``what_changed`` — what this commit does, mechanically, in your own words.
- ``how_it_works`` — how the surrounding machinery works: the pass, the data
  structure, the invariant, the control flow the reader needs to follow the
  change. This is the longest field and the most valuable one.
- ``why_it_matters`` — consequences for someone outside this subsystem.
- ``open_questions`` — anything you could not determine from the code.
- ``external_context`` — facts from ``search_web``, if you used it.

Be precise and be concrete. Name files, functions, macros, structs, fields and
flags exactly as they appear. Do not speculate: if the code does not show you
something, say so in ``open_questions`` rather than guessing.
"""


class _ToolBudget:
    """Counts tool calls and cuts them off at the ceiling."""

    def __init__(self, limit: int = _MAX_TOOL_CALLS) -> None:
        self.limit = limit
        self.used = 0

    def spend(self) -> bool:
        """Consume one call. False once the budget is gone."""
        if self.used >= self.limit:
            return False
        self.used += 1
        return True


class _ExcerptLog:
    """Regions the explorer flagged while reading, in the order it read them.

    Excerpts arrive as tool calls rather than as part of the final answer, for
    two reasons. The schema one is decisive: a list of ``{path, lines, symbol,
    note}`` objects in the output schema means ``$defs``/``$ref``, which
    Gemini's function-calling dialect does not support — and OpenRouter's
    OpenAI-compatible endpoint means pydantic-ai does not rewrite it away.
    Three runs died there. A tool with four plain string parameters is the
    best-supported shape there is.

    The second is that it fits how the work actually happens: the explorer
    flags a region at the moment it reads it, instead of having to remember
    every region until the end.
    """

    def __init__(self, limit: int = _MAX_EXCERPTS) -> None:
        self.limit = limit
        self.records: list[dict] = []

    def add(self, record: dict) -> bool:
        """Record a region. False once the log is full."""
        if len(self.records) >= self.limit:
            return False
        self.records.append(record)
        return True


def _build_tools(
    repo: SourceRepo, sha: str, budget: _ToolBudget, excerpts: _ExcerptLog
) -> list:
    """Return repo-navigation tools bound to one clone at one commit.

    The SHA is closed over rather than passed by the model: the model has no
    business choosing which revision it reads, and a hallucinated SHA would
    silently produce research about the wrong code.
    """
    default_scope = repo.changed_dirs(sha) or ["."]

    def show_commit() -> str:
        """Show the full commit message, diffstat and patch for this commit.

        Start here. Returns the complete commit message followed by the diff.
        """
        if not budget.spend():
            return _BUDGET_EXHAUSTED
        return repo.show_commit(sha)

    def read_file(path: str, start_line: int = 1, end_line: int = 0) -> str:
        """Read a numbered slice of a source file as it was at this commit.

        Args:
            path: repo-relative path, e.g. "gcc/ipa-sra.cc".
            start_line: 1-based first line to return.
            end_line: last line to return; 0 means "a default-sized window".
        """
        if not budget.spend():
            return _BUDGET_EXHAUSTED
        return repo.read_file(
            sha, path, start_line=start_line, end_line=end_line or None
        )

    def list_dir(path: str = ".") -> str:
        """List the files in a directory of the source tree at this commit.

        Args:
            path: repo-relative directory, e.g. "gcc/config/aarch64".
        """
        if not budget.spend():
            return _BUDGET_EXHAUSTED
        return repo.list_dir(sha, path)

    def grep_repo(pattern: str, paths: list[str] | None = None) -> str:
        """Search the source tree at this commit for a regular expression.

        Args:
            pattern: the regex to search for.
            paths: directories or globs to search under, e.g. ["gcc/", "gcc/config/"].
                Required — a whole-tree search is not permitted. Omit to search
                only the directories this commit touched.
        """
        if not budget.spend():
            return _BUDGET_EXHAUSTED
        return repo.grep_repo(sha, pattern, paths or default_scope)

    def find_symbol(name: str, paths: list[str] | None = None) -> str:
        """Find where a function, struct, macro or enum is defined.

        Args:
            name: the exact symbol name, e.g. "IPA_PARAM_DESCRIPTOR".
            paths: directories to search under. Omit to search the directories
                this commit touched.
        """
        if not budget.spend():
            return _BUDGET_EXHAUSTED
        return repo.find_symbol(sha, name, paths or default_scope)

    def note_excerpt(
        path: str, lines: str = "", symbol: str = "", note: str = ""
    ) -> str:
        """Mark a region you have read as one the article should quote.

        Call this as you read, once per region worth showing the reader. The
        code itself is fetched from the repository — you are naming the region,
        not copying it.

        Args:
            path: repo-relative file you read, e.g. "gcc/ipa-sra.cc".
            lines: the range it covers, e.g. "1204-1231".
            symbol: the function, struct or macro it covers, if one fits.
            note: one sentence on why this region matters.
        """
        if not path.strip():
            return "[error] note_excerpt needs a path."
        if not excerpts.add(
            {"path": path.strip(), "lines": lines, "symbol": symbol, "note": note}
        ):
            return (
                f"[budget] Already holding {excerpts.limit} excerpts — that is "
                "enough. Finish your findings and return."
            )
        return f"Recorded excerpt {len(excerpts.records)}: {path} {lines}".strip()

    def search_web(query: str) -> list[str]:
        """Look up OUTSIDE background: a paper, a wiki page, an ISA manual.

        Never a substitute for reading the source with the tools above.
        """
        if not budget.spend():
            return [_BUDGET_EXHAUSTED]
        return search_context(query)

    return [
        show_commit, read_file, list_dir, grep_repo, find_symbol,
        note_excerpt, search_web,
    ]


def _max_lengths(model: type[BaseModel], kinds: tuple[type, ...]) -> dict[str, int]:
    """`{field: max_length}` read off the model itself, not copied from it.

    Derived rather than hardcoded so the clamp can never drift out of step with
    the schema it exists to satisfy.
    """
    caps: dict[str, int] = {}
    for name, field in model.model_fields.items():
        for meta in field.metadata:
            limit = getattr(meta, "max_length", None)
            if limit is None:
                continue
            annotation = field.annotation
            origin = get_origin(annotation) or annotation
            # `str | None` is types.UnionType on 3.10+, typing.Union when
            # spelled Optional[str] — unwrap either and check the real type.
            if origin in (Union, UnionType):
                if any(a in kinds for a in get_args(annotation)):
                    caps[name] = limit
            elif any(origin is k for k in kinds):
                caps[name] = limit
    return caps


_RESEARCH_STR_CAPS = _max_lengths(LessonResearch, (str,))
_RESEARCH_LIST_CAPS = _max_lengths(LessonResearch, (list,))
_EXCERPT_STR_CAPS = _max_lengths(SourceExcerpt, (str,))
_LESSON_LIST_CAPS = _max_lengths(LessonDigest, (list,))
_LESSON_STR_CAPS = _max_lengths(LessonDigest, (str,))

# The caps inside each list-of-objects field. Every one of these was a way to
# lose a finished article: `code_tour.path`/`symbol`/`lines` and
# `further_reading.title`/`url` had no repair at all, and the hand-written
# mirrors that did exist are how `primer_glossary` got missed. Derived from the
# models so the repair cannot fall behind the schema.
_LESSON_NESTED_CAPS: dict[str, type[BaseModel]] = {
    "sections": LessonSection,
    "code_tour": CodeRef,
    "further_reading": FurtherReading,
    "primer_glossary": GlossaryEntry,
}
_NESTED_STR_CAPS = {
    field: _max_lengths(model, (str,))
    for field, model in _LESSON_NESTED_CAPS.items()
}
_NESTED_REQUIRED = {
    field: {n for n, f in model.model_fields.items() if f.is_required()}
    for field, model in _LESSON_NESTED_CAPS.items()
}


def _clamp_to_schema(parsed: dict) -> None:
    """Trim over-long values to the caps `LessonResearch` enforces.

    The tools can legitimately hand back more than the model is allowed to
    store — ``read_file`` returns up to 8192 bytes while ``SourceExcerpt.code``
    caps at 6000 — so a model that copies an excerpt verbatim, exactly as
    instructed, produces a value pydantic rejects. One oversized excerpt would
    otherwise fail the *entire* dossier and cost the whole article. Losing the
    tail of one excerpt is strictly the better trade.
    """
    def _cut(value: object, limit: int) -> object:
        return value[:limit] if isinstance(value, str) and len(value) > limit else value

    for field, limit in _RESEARCH_STR_CAPS.items():
        if field in parsed:
            parsed[field] = _cut(parsed[field], limit)

    for field, limit in _RESEARCH_LIST_CAPS.items():
        value = parsed.get(field)
        if isinstance(value, list) and len(value) > limit:
            parsed[field] = value[:limit]

    excerpts = parsed.get("excerpts")
    if isinstance(excerpts, list):
        for item in excerpts:
            if not isinstance(item, dict):
                continue
            for field, limit in _EXCERPT_STR_CAPS.items():
                if field in item:
                    item[field] = _cut(item[field], limit)


_LINE_RANGE = re.compile(r"(\d+)\s*[-–—:]\s*(\d+)")


def _parse_line_range(lines: str | None) -> tuple[int, int | None]:
    """``"1204-1231"`` -> ``(1204, 1231)``; anything unusable -> ``(1, None)``.

    A malformed range is not worth failing a dossier over — ``read_file``'s
    default window is a perfectly good fallback, and the excerpt still names
    the file the explorer meant.
    """
    if not lines:
        return 1, None
    match = _LINE_RANGE.search(lines)
    if match:
        start, end = int(match.group(1)), int(match.group(2))
        return (start, end) if end >= start else (end, start)
    digits = re.search(r"\d+", lines)
    return (int(digits.group()), None) if digits else (1, None)


def _split_commit_output(text: str) -> tuple[str, str]:
    """Split ``git show`` output into (message-and-diffstat, patch)."""
    marker = text.find("diff --git")
    if marker == -1:
        return text.strip(), ""
    return text[:marker].strip(), text[marker:].strip()


def _read_excerpts(
    repo: SourceRepo, sha: str, requests: list[dict]
) -> list[dict]:
    """Turn the explorer's region requests into excerpts read from the clone.

    A request naming a path that does not exist at this commit is dropped, the
    same way ``_drop_unread_code_refs`` drops a fabricated citation from the
    writer — except here it costs nothing, because the bytes were never going
    to come from the model in the first place.

    Returns plain dicts, deliberately. ``read_file`` hands back up to 8192
    bytes and ``SourceExcerpt.code`` caps at 6000, so building the model here
    would validate — and fail — before ``_clamp_to_schema`` ever got the
    chance to trim. That cost a run: the caps are repairs applied to the dict,
    and anything that constructs the strict model early opts out of them.
    """
    excerpts: list[dict] = []
    for request in requests:
        path = request.get("path")
        if not isinstance(path, str) or not path:
            continue
        start, end = _parse_line_range(request.get("lines"))
        code = repo.read_file(sha, path, start_line=start, end_line=end)
        if code.startswith("[error]"):
            logger.warning(
                "lesson_agent[research]: dropping excerpt %r — not readable at %s",
                path, sha[:12],
            )
            continue
        excerpts.append(
            {
                "path": path,
                "lines": request.get("lines") or None,
                "symbol": request.get("symbol") or None,
                "code": code,
                "note": request.get("note") or "",
            }
        )
    return excerpts


def _assert_dossier_has_evidence(research: LessonResearch) -> None:
    """Refuse a dossier the writer could not honestly write from.

    The writer never opens a file: the commit message, the diff and the
    excerpts are its entire view of the source. Hand it an empty dossier and it
    does not fail — it writes, truthfully and at length, about having no
    evidence. That article is ``is_stub: false``, so it passes validation, gets
    committed, and publishes.

    That is not hypothetical. On 2026-09-14 the explorer returned after one
    tool call and 53 tokens, and $0.08 of Opus went on "No Dossier, No Lesson:
    Why This Week's Article Cannot Be Written", which was one merge away from
    the front page.

    A stub is the right outcome for this: it is visible in /admin, it never
    claims its week, and the next night retries. So the emptiness is caught
    here, where it still reads as the stage-1 failure it actually is, rather
    than downstream where it reads as an editorial decision.

    Raised as a ``ValueError`` on purpose, which ``retry_with_backoff`` does
    retry. Unlike a schema mismatch, an explorer that returned early may well
    do the work on a second ask, and stage 1 runs on the cheap tier — the
    empty run above cost $0.0008. Three attempts at that price beats losing
    the week.
    """
    if not research.excerpts:
        raise ValueError(
            "dossier has no source excerpts — the writer would have nothing "
            "to ground the article in"
        )
    if not research.diff.strip() and not research.commit_message.strip():
        raise ValueError("dossier has neither a diff nor a commit message")


def _finalise_research(
    draft: BaseModel,
    subject: LessonSubject,
    repo: SourceRepo,
    requests: list[dict],
) -> LessonResearch:
    """Assemble the dossier: the explorer's findings plus the code, from git.

    The model supplies judgement — what changed, how the machinery works, which
    regions matter. Everything quotable is read from the clone at this commit,
    so the excerpts are verbatim by construction rather than by instruction,
    and stage 1's output stays small enough to cross the wire intact.
    """
    parsed = draft.model_dump(exclude_none=True)

    # Identity is ours, not the model's — a typo here would misattribute the
    # whole dossier to the wrong commit.
    parsed["commit_hash"] = subject.commit_hash
    if not parsed.get("subsystem"):
        parsed["subsystem"] = subject.subsystem

    message, diff = _split_commit_output(repo.show_commit(subject.commit_hash))
    parsed["commit_message"] = message
    parsed["diff"] = diff
    parsed["changed_files"] = repo.changed_paths(subject.commit_hash)
    parsed["excerpts"] = _read_excerpts(repo, subject.commit_hash, requests)

    _clamp_to_schema(parsed)
    research = _RESEARCH_ADAPTER.validate_python(parsed)
    _assert_dossier_has_evidence(research)
    return research


def _research_prompt(subject: LessonSubject, repo: SourceRepo) -> str:
    scope = repo.changed_dirs(subject.commit_hash) or ["."]
    paths = repo.changed_paths(subject.commit_hash)[:20]
    return (
        "Research this commit for a Lesson of the Week article.\n\n"
        f"commit_hash: {subject.commit_hash}\n"
        f"project: {subject.project}\n"
        f"subsystem_hint: {subject.subsystem}\n"
        f"landed: {subject.commit_date.isoformat()}\n"
        f"landing_headline: {subject.headline}\n"
        f"landing_tldr: {subject.tldr}\n\n"
        "Files this commit touched:\n  " + "\n  ".join(paths) + "\n\n"
        f"Default grep scope (the directories above): {', '.join(scope)}\n\n"
        "Call show_commit first, then read the code, calling note_excerpt on "
        "each region worth quoting. Return your findings last."
    )


def run_research(
    subject: LessonSubject,
    repo: SourceRepo,
    errors: list[str] | None = None,
) -> LessonResearch | None:
    """Stage 1: explore the source tree and return a dossier, or None on failure.

    Args:
        errors: optional sink. On failure the reason is appended here so the
            caller can put it in the stub's ``stub_reason`` instead of the
            useless bare ``research_failed``.
    """
    model_name = model_from_env("LESSON_RESEARCH_MODEL", DEFAULT_LESSON_RESEARCH_MODEL)
    budget = _ToolBudget()
    excerpts = _ExcerptLog()
    agent: Agent[None, BaseModel] = Agent(
        model=build_model(model_name),
        # Structured output, not prose the pipeline parses: the dossier carries
        # a raw diff and verbatim C, and hand-encoding that as JSON is what the
        # model kept getting wrong. See agents/models/draft.py. PydanticAI's
        # default `retries=1` covers the one reprompt worth paying for here —
        # a second would resend every tool result in the run a third time.
        output_type=LessonResearchDraft,
        system_prompt=_RESEARCH_PROMPT,
        tools=_build_tools(  # type: ignore[arg-type]
            repo, subject.commit_hash, budget, excerpts
        ),
    )
    prompt = _research_prompt(subject, repo)

    logger.info(
        "lesson_agent[research]: %s / %s (%s) via %s",
        subject.project,
        subject.commit_hash[:12],
        subject.subsystem,
        model_name,
    )
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "\033[1;33m── lesson research ▶ SENDING TO %s ──\n%s\033[0m",
            model_name, prompt,
        )

    def _call():
        r = agent.run_sync(prompt)
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "\033[1;32m── lesson research ◀ RESPONSE FROM %s ──\n%s\033[0m",
                model_name, r.output,
            )
        return r, _finalise_research(r.output, subject, repo, excerpts.records)

    try:
        result, research = retry_with_backoff(
            _call, label=f"lesson_research {subject.project}/{subject.commit_hash[:12]}"
        )
    except (ValidationError, ValueError) as exc:
        logger.error("lesson_agent[research]: unusable output (%s)", exc, exc_info=True)
        if errors is not None:
            errors.append(_stage_reason("research_failed", exc))
        return None
    except Exception as exc:
        logger.error(
            "lesson_agent[research]: failed after retries (%s)", exc, exc_info=True
        )
        if errors is not None:
            errors.append(_stage_reason("research_failed", exc))
        return None

    append_usage("lesson_research", model_name, result.usage)
    research = research.model_copy(update={"tool_calls_used": budget.used})
    logger.info(
        "lesson_agent[research]: %d excerpt(s) from %d file(s), "
        "%d/%d tool call(s), usage=%s",
        len(research.excerpts),
        len(research.changed_files),
        budget.used,
        budget.limit,
        result.usage,
    )
    return research


# ---------------------------------------------------------------------------
# Stage 2 — writing
# ---------------------------------------------------------------------------

_WRITER_PROMPT = """\
You write the Lesson of the Week for a WSJ-style publication read by working
systems developers. Every other article in this paper reports what happened.
Yours teaches — it takes one change that merged this week and uses it as the
way into a concept the reader can carry to the next patch they read.

You are given a research dossier compiled by an engineer who read the actual
source tree at this commit: the commit message, the diff, and verbatim excerpts
of the files involved. That dossier is your ONLY source of truth about the
code. Every claim you make about what a function does, what a struct holds, or
what an invariant guarantees must be supported by an excerpt in it. Where the
dossier is silent, say less — do not fill the gap with plausible-sounding
detail, and never cite a file that is not in the dossier.

AUDIENCE
A working systems programmer — comfortable with pointers, processes, syscalls,
the compile→link→load pipeline — who does NOT work on this subsystem. Do not
define general low-level plumbing. Do unpack every toolchain-specific term you
use.

WRITING RULES
- Teach the concept, don't narrate the changelog. "What is inter-procedural
  scalar replacement, why does it need this invariant, and what broke without
  it" — not "the patch modifies three files".
- Stay technically precise: filenames, function names, macro names, struct and
  field names, flag names (``-fipa-sra``, ``CONFIG_SLUB``), symbol names and
  ABI/ISA terms are reproduced verbatim from the dossier, never paraphrased.
  Quote the relevant snippet when it clarifies intent.
- Active voice, concrete verbs, no filler ("in a nutshell", "this patch aims
  to", "basically"). No trailing ellipsis. Never echo quoted email lines.
- Markdown in section bodies: paragraphs, ``inline code``, fenced blocks for
  snippets, bullet lists where they earn their place. No headings inside a
  section body — the ``heading`` field is the heading.

FIELDS (return the article through the output tool):
- ``headline`` — the lesson's title, <= 140 chars. Names the concept, not the
  commit. Not a commit subject line.
- ``hook`` — <= 200 chars, why a reader should spend ten minutes here.
- ``tldr`` — one sentence, <= 160 chars.
- ``concept`` — <= 300 chars, the transferable idea in one or two sentences.
- ``prerequisites`` — up to 6 short phrases naming what a reader should
  already know (e.g. "what a GIMPLE pass is"). Empty if genuinely none.
- ``sections`` — 4 to 6 ``{heading, body}`` objects, in this arc:
    1. the background: what this subsystem is and what it is responsible for
    2. the mechanism: how it actually works, per the dossier's excerpts
    3. the change: what this commit did, and what it means at that level
    4. the consequences: what a dev outside the subsystem should now expect
    5. (optional) how to see it yourself — a flag, a dump, a test to run
  Each body is 2-6 paragraphs. This is a full article, not a summary.
- ``code_tour`` — 3 to 8 ``{path, symbol, lines, why}`` entries, drawn from the
  dossier's excerpts. ``path`` and ``lines`` must match an excerpt. ``why`` is
  one sentence on what the reader will find there.
- ``takeaways`` — 3 to 5 one-line lessons that outlive this commit.
- ``further_reading`` — up to 6 ``{title, url}``. Real URLs only, and only ones
  present in the dossier; omit rather than invent.
- ``subsystem`` — e.g. "gcc/ipa", "binutils/ld". Never "unknown".
- ``tags`` — up to 5 short topic tags.
- ``primer_expert`` — the "In Details" block for toolchain insiders. 2-4
  sentences, <= 500 chars. They already know compiler passes, ELF/DWARF,
  relocations, PIC/PIE, ABI conventions — don't define those. Place THIS
  subsystem inside that map: name the concrete file / pass / invariant / data
  structure, note why a toolchain dev outside this corner still wouldn't
  recognise it, and flag non-obvious interactions with neighbours.
- ``primer_glossary`` — the "For Context" block: ``{term, definition}`` entries
  for every toolchain-specific term used in the article that a non-specialist
  systems programmer wouldn't know. ``term`` is the exact spelling used in the
  article. ``definition`` is 1-3 sentences: what it is, what problem it solves,
  and where it sits in the pipeline when that matters. Background only — never
  restate this commit's effect. Never define the top-level project itself
  ("GCC", "binutils", "glibc", "Linux") — the reader knows what paper this is.
  Err on the side of more entries.
"""


def _clip(value: object, limit: int) -> object:
    if isinstance(value, str) and len(value) > limit:
        return value[: limit - 1].rstrip() + "…"
    return value


def _repair_lesson_item(item: dict, subject: LessonSubject) -> None:
    """Fix deterministic schema violations before validation.

    Same rationale as ``landing_agent._repair_landing_item``: a model that
    overshoots a length cap by ten characters should not cost us the whole
    run, and these are all mechanical fixes with no editorial judgement.
    """
    for key, limit in _LESSON_STR_CAPS.items():
        if key in item:
            item[key] = _clip(item.get(key), limit)

    for field, caps in _NESTED_STR_CAPS.items():
        for entry in item.get(field) or []:
            if not isinstance(entry, dict):
                continue
            for key, limit in caps.items():
                value = entry.get(key)
                if isinstance(value, str):
                    entry[key] = _clip(value, limit)
                elif key in _NESTED_REQUIRED[field]:
                    # A required string the model left out: "" validates and
                    # renders as empty, which beats losing the article. An
                    # absent *optional* one stays absent, so `symbol: null`
                    # does not become `symbol: ""` in the frontmatter.
                    entry[key] = ""

    glossary = item.get("primer_glossary")
    if isinstance(glossary, list):
        item["primer_glossary"] = filter_glossary(glossary)

    # Every capped list, trimmed. Derived from the model rather than listed
    # here, because the hand-written version left `primer_glossary` out and
    # that cost a run: the writer is told to "err on the side of more entries"
    # and duly produced 17 against a cap of 10, so an article that was written,
    # paid for and otherwise valid died on `too_long`. A new capped field on
    # `LessonDigest` is now covered the day it is added.
    #
    # After the glossary filtering above, not before — `filter_glossary` can
    # drop entries, and trimming first would discard good ones to make room
    # for entries that were about to be removed anyway.
    for key, cap in _LESSON_LIST_CAPS.items():
        value = item.get(key)
        if isinstance(value, list) and len(value) > cap:
            item[key] = value[:cap]

    # Fields the model must echo, forced from the subject regardless. These
    # identify the article; an LLM typo here mislabels the whole piece.
    item["commit_hash"] = subject.commit_hash
    item["project"] = subject.project
    item["source_type"] = subject.source_type
    item["url"] = subject.url
    item["lesson_id"] = subject.lesson_id
    item["landing_slug"] = subject.landing_slug
    item["week_start"] = subject.week.start.isoformat()
    item["week_end"] = subject.week.end.isoformat()
    item["commit_date"] = subject.commit_date.isoformat()
    # The article is dated by the week it covers, not the commit — see the
    # note on LessonDigest.week_start.
    item["date"] = subject.week.end.isoformat()
    if not item.get("subsystem") or str(item["subsystem"]).lower() in {
        "unknown",
        "general",
        "",
    }:
        item["subsystem"] = subject.subsystem


def _drop_unread_code_refs(item: dict, repo: SourceRepo, sha: str) -> None:
    """Remove code_tour entries whose path doesn't exist at this commit.

    The writing model never opened a file — it works entirely from the dossier
    — so a cited path is only as good as its discipline in copying one across.
    The code tour is the article's evidence, so it is verified against the real
    tree rather than trusted.
    """
    refs = item.get("code_tour")
    if not isinstance(refs, list):
        return
    kept: list[dict] = []
    for ref in refs:
        if not isinstance(ref, dict):
            continue
        path = ref.get("path")
        if not isinstance(path, str) or not path:
            continue
        probe = repo.read_file(sha, path, start_line=1, end_line=1)
        if probe.startswith("[error]"):
            logger.warning(
                "lesson_agent: dropping cited path %r — not present at %s",
                path, sha[:12],
            )
            continue
        kept.append(ref)
    item["code_tour"] = kept


def _finalise_lesson(
    draft: BaseModel, subject: LessonSubject, repo: SourceRepo
) -> LessonDigest:
    """Turn the writer's draft article into a validated ``LessonDigest``."""
    parsed = draft.model_dump(exclude_none=True)
    _repair_lesson_item(parsed, subject)
    _drop_unread_code_refs(parsed, repo, subject.commit_hash)
    return LessonDigest.model_validate(parsed)


def _render_dossier(research: LessonResearch, subject: LessonSubject) -> str:
    """Flatten the dossier into the writer's prompt."""
    lines: list[str] = [
        "Write this week's Lesson of the Week from the research below.",
        "",
        f"commit_hash: {subject.commit_hash}",
        f"project: {subject.project}",
        f"source_type: {subject.source_type}",
        f"url: {subject.url}",
        f"subsystem: {research.subsystem or subject.subsystem}",
        f"landed: {subject.commit_date.isoformat()}",
        f"week covered: {subject.week.start.isoformat()} to {subject.week.end.isoformat()}",
        "",
        "=== COMMIT MESSAGE ===",
        research.commit_message,
        "",
        "=== DIFF ===",
        research.diff,
        "",
        "=== FILES TOUCHED ===",
        "\n".join(research.changed_files) or "(none recorded)",
        "",
        "=== SOURCE EXCERPTS (verbatim, at this commit) ===",
    ]
    for ex in research.excerpts:
        header = ex.path
        if ex.lines:
            header += f"  lines {ex.lines}"
        if ex.symbol:
            header += f"  [{ex.symbol}]"
        lines.append(f"--- {header} ---")
        if ex.note:
            lines.append(f"(why this file: {ex.note})")
        lines.append(ex.code)
        lines.append("")

    lines += [
        "=== RESEARCH NOTES ===",
        f"What changed:\n{research.what_changed}",
        "",
        f"How it works:\n{research.how_it_works}",
        "",
        f"Why it matters:\n{research.why_it_matters}",
    ]
    if research.open_questions:
        lines += [
            "",
            "Open questions (the researcher could NOT determine these from the "
            "code — do not assert anything about them):",
            "\n".join(f"- {q}" for q in research.open_questions),
        ]
    if research.external_context:
        lines += [
            "",
            "External context:",
            "\n".join(f"- {c}" for c in research.external_context),
        ]
    lines += ["", "Return the article through the output tool."]
    return "\n".join(lines)


def run_writer(
    subject: LessonSubject,
    research: LessonResearch,
    repo: SourceRepo,
    errors: list[str] | None = None,
) -> LessonDigest | None:
    """Stage 2: turn the dossier into the article. One call, no tools.

    ``errors`` is the same failure sink ``run_research`` takes.
    """
    model_name = model_from_env("LESSON_WRITER_MODEL", DEFAULT_LESSON_WRITER_MODEL)
    agent: Agent[None, BaseModel] = Agent(
        model=build_model(model_name, max_tokens=LESSON_WRITER_MAX_TOKENS),
        output_type=LessonDraft,
        system_prompt=_WRITER_PROMPT,
    )
    prompt = _render_dossier(research, subject)

    logger.info(
        "lesson_agent[writer]: %s / %s via %s (%d chars of research)",
        subject.project, subject.commit_hash[:12], model_name, len(prompt),
    )
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug(
            "\033[1;33m── lesson writer ▶ SENDING TO %s ──\n%s\033[0m",
            model_name, prompt,
        )

    def _call():
        r = agent.run_sync(prompt)
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "\033[1;32m── lesson writer ◀ RESPONSE FROM %s ──\n%s\033[0m",
                model_name, r.output,
            )
        return r, _finalise_lesson(r.output, subject, repo)

    try:
        result, lesson = retry_with_backoff(
            _call, label=f"lesson_writer {subject.project}/{subject.commit_hash[:12]}"
        )
    except (ValidationError, ValueError) as exc:
        logger.error("lesson_agent[writer]: unusable output (%s)", exc, exc_info=True)
        if errors is not None:
            errors.append(_stage_reason("writer_failed", exc))
        return None
    except Exception as exc:
        logger.error(
            "lesson_agent[writer]: failed after retries (%s)", exc, exc_info=True
        )
        if errors is not None:
            errors.append(_stage_reason("writer_failed", exc))
        return None

    append_usage("lesson_writer", model_name, result.usage)
    logger.info(
        "lesson_agent[writer]: %r — %d section(s), %d code ref(s), usage=%s",
        lesson.headline, len(lesson.sections), len(lesson.code_tour), result.usage,
    )
    return lesson


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

_MAX_STUB_REASON = 200


def _stage_reason(stage: str, exc: BaseException) -> str:
    """``"research_failed: <what actually went wrong>"``.

    A bare ``research_failed`` is unactionable — it was on both of the first two
    real runs, and diagnosing them meant trying to pull a CI log that the API
    truncates. The exception text rides into committed frontmatter instead, so
    the next failure is one ``git show`` away. Upstream API errors keep the
    response body on ``exc.response.text``; ``str(exc)`` often drops it.
    """
    body = getattr(getattr(exc, "response", None), "text", None)
    detail = f"{type(exc).__name__}: {exc}"
    if body:
        detail = f"{detail} | {body}"
    detail = " ".join(detail.split())          # frontmatter-safe: one line
    return f"{stage}: {detail}"[:_MAX_STUB_REASON]


def stub_lesson(subject: LessonSubject, reason: str = "llm_failure") -> LessonDigest:
    """A placeholder lesson, written to disk so /admin can see the failure."""
    return LessonDigest(
        lesson_id=subject.lesson_id,
        commit_hash=subject.commit_hash,
        project=subject.project,
        subsystem=subject.subsystem or "unknown",
        source_type=subject.source_type,
        headline=subject.headline or f"Lesson for {subject.commit_hash[:12]}",
        hook="Lesson unavailable — see the source link.",
        tldr=(subject.tldr or "Lesson unavailable.")[:160],
        concept="Lesson unavailable.",
        tags=list(subject.tags)[:5],
        patch_id=subject.patch_id,
        landing_slug=subject.landing_slug,
        url=subject.url,
        week_start=subject.week.start,
        week_end=subject.week.end,
        commit_date=subject.commit_date,
        date=datetime.combine(
            subject.week.end, datetime.min.time(), tzinfo=timezone.utc
        ),
        is_stub=True,
        stub_reason=reason,
    )


def run_lesson_agent(
    subject: LessonSubject,
    repo: SourceRepo,
    dry_run: bool = False,
) -> LessonDigest:
    """Produce one LessonDigest for *subject*: research, then write.

    Always returns a digest. On failure it is a stub, which is still written to
    disk so the failure shows up under /admin rather than silently leaving the
    week without a lesson and no explanation.
    """
    if dry_run:
        return stub_lesson(subject, reason="dry_run")

    # The reason a stage failed is worth more than the fact that it did — it
    # travels into the stub's frontmatter and gets committed, so a failure is
    # diagnosable from the repo without digging a CI log out.
    errors: list[str] = []

    research = run_research(subject, repo, errors)
    if research is None:
        return stub_lesson(
            subject, reason=errors[-1] if errors else "research_failed"
        )

    lesson = run_writer(subject, research, repo, errors)
    if lesson is None:
        return stub_lesson(subject, reason=errors[-1] if errors else "writer_failed")
    return lesson
