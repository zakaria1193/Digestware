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

import json
import logging
import os
from datetime import datetime, timezone

from pydantic import TypeAdapter, ValidationError
from pydantic_ai import Agent

from agents._openrouter import (
    DEFAULT_LESSON_RESEARCH_MODEL,
    DEFAULT_LESSON_WRITER_MODEL,
    build_model,
)
from agents._retry import retry_with_backoff
from agents.lesson_picker import LessonSubject
from agents.models.lesson import LessonDigest, LessonResearch
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

_BUDGET_EXHAUSTED = (
    "[budget] The source-exploration budget for this lesson is spent. Stop "
    "calling tools and return the research dossier now, using only what you "
    "have already read. Do not cite files you did not open."
)

# Mirrors of the Pydantic caps in models/lesson.py, so an overrun is repaired
# rather than failing the whole run.
_HEADLINE_MAX = 140
_HOOK_MAX = 200
_TLDR_MAX = 160
_CONCEPT_MAX = 300
_SECTION_BODY_MAX = 4000
_PRIMER_EXPERT_MAX = 600
_GLOSSARY_TERM_MAX = 80
_GLOSSARY_DEF_MAX = 400
_CODE_REF_WHY_MAX = 300

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
3. ``grep_repo`` / ``find_symbol`` — chase the one or two symbols that carry
   the concept: the caller, the data structure, the invariant being kept.
4. ``search_web`` — OUTSIDE background only (a paper, a wiki page, an ISA
   note). Never a substitute for reading the code.

Your exploration budget is limited. Spend it on the three or four files that
actually explain the change, not on a survey of the subsystem.

RETURN one JSON object (raw JSON, no markdown fences) with these fields:
- ``commit_hash``, ``subsystem`` — echo from the input.
- ``commit_message`` — the commit message, verbatim.
- ``diff`` — the diff, verbatim (trim to the hunks that matter if it is huge).
- ``changed_files`` — the paths this commit touched.
- ``excerpts`` — 3 to 8 objects ``{path, lines, symbol, code, note}``. ``code``
  is the region COPIED VERBATIM from the file — not summarised, not
  reformatted, not re-indented. This is the writer's only view of the source,
  and a paraphrase here becomes a wrong identifier in the published article.
  ``lines`` is the range you read ("1204-1231"); ``note`` is one sentence on
  why you opened it.
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


def _build_tools(repo: SourceRepo, sha: str, budget: _ToolBudget) -> list:
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

    def search_web(query: str) -> list[str]:
        """Look up OUTSIDE background: a paper, a wiki page, an ISA manual.

        Never a substitute for reading the source with the tools above.
        """
        if not budget.spend():
            return [_BUDGET_EXHAUSTED]
        return search_context(query)

    return [show_commit, read_file, list_dir, grep_repo, find_symbol, search_web]


def _strip_fences(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = text[text.index("\n") + 1:] if "\n" in text else text[3:]
    if text.endswith("```"):
        text = text[: text.rindex("```")].rstrip()
    return text


def _parse_research(text: str, subject: LessonSubject) -> LessonResearch:
    parsed = json.loads(_strip_fences(text))
    if isinstance(parsed, list):
        if not parsed:
            raise ValueError("research model returned an empty array")
        parsed = parsed[0]
    if not isinstance(parsed, dict):
        raise ValueError(f"expected a JSON object, got {type(parsed).__name__}")

    # Identity is ours, not the model's — a typo here would misattribute the
    # whole dossier to the wrong commit.
    parsed["commit_hash"] = subject.commit_hash
    if not parsed.get("subsystem"):
        parsed["subsystem"] = subject.subsystem
    return _RESEARCH_ADAPTER.validate_python(parsed)


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
        "Call show_commit first, then read the code. Return one JSON object — "
        "raw JSON, no markdown fences."
    )


def run_research(subject: LessonSubject, repo: SourceRepo) -> LessonResearch | None:
    """Stage 1: explore the source tree and return a dossier, or None on failure."""
    model_name = os.environ.get("LESSON_RESEARCH_MODEL", DEFAULT_LESSON_RESEARCH_MODEL)
    budget = _ToolBudget()
    agent: Agent[None, str] = Agent(
        model=build_model(model_name),
        output_type=str,
        system_prompt=_RESEARCH_PROMPT,
        tools=_build_tools(repo, subject.commit_hash, budget),  # type: ignore[arg-type]
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
        return r, _parse_research(r.output, subject)

    try:
        result, research = retry_with_backoff(
            _call, label=f"lesson_research {subject.project}/{subject.commit_hash[:12]}"
        )
    except (ValidationError, json.JSONDecodeError, ValueError) as exc:
        logger.error("lesson_agent[research]: unusable output (%s)", exc)
        return None
    except Exception as exc:
        logger.error("lesson_agent[research]: failed after retries (%s)", exc)
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

FIELDS (return ONE JSON object, raw JSON only, no markdown fences):
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

VERBATIM FIELDS (echo exactly as given in the input, do not invent):
``commit_hash``, ``project``, ``source_type``, ``url``.
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
    for key, limit in (
        ("headline", _HEADLINE_MAX),
        ("hook", _HOOK_MAX),
        ("tldr", _TLDR_MAX),
        ("concept", _CONCEPT_MAX),
        ("primer_expert", _PRIMER_EXPERT_MAX),
    ):
        if key in item:
            item[key] = _clip(item.get(key), limit)

    for key, cap in (
        ("prerequisites", 6),
        ("sections", 8),
        ("code_tour", 10),
        ("takeaways", 6),
        ("further_reading", 6),
        ("tags", 5),
    ):
        val = item.get(key)
        if isinstance(val, list) and len(val) > cap:
            item[key] = val[:cap]

    for section in item.get("sections") or []:
        if isinstance(section, dict):
            section["heading"] = _clip(section.get("heading") or "", 120)
            section["body"] = _clip(section.get("body") or "", _SECTION_BODY_MAX)

    for ref in item.get("code_tour") or []:
        if isinstance(ref, dict):
            ref["why"] = _clip(ref.get("why") or "", _CODE_REF_WHY_MAX)

    glossary = item.get("primer_glossary")
    if isinstance(glossary, list):
        for entry in glossary:
            if not isinstance(entry, dict):
                continue
            entry["term"] = _clip(entry.get("term") or "", _GLOSSARY_TERM_MAX)
            entry["definition"] = _clip(
                entry.get("definition") or "", _GLOSSARY_DEF_MAX
            )
        item["primer_glossary"] = filter_glossary(glossary)

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


def _parse_lesson(
    text: str, subject: LessonSubject, repo: SourceRepo
) -> LessonDigest:
    """Parse the writer's JSON object into a validated LessonDigest."""
    parsed = json.loads(_strip_fences(text))
    # Tolerate a single-element array — models wrap objects surprisingly often.
    if isinstance(parsed, list):
        if not parsed:
            raise ValueError("writer returned an empty array")
        parsed = parsed[0]
    if not isinstance(parsed, dict):
        raise ValueError(f"expected a JSON object, got {type(parsed).__name__}")

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
    lines += ["", "Return one JSON object — raw JSON, no markdown fences."]
    return "\n".join(lines)


def run_writer(
    subject: LessonSubject,
    research: LessonResearch,
    repo: SourceRepo,
) -> LessonDigest | None:
    """Stage 2: turn the dossier into the article. One call, no tools."""
    model_name = os.environ.get("LESSON_WRITER_MODEL", DEFAULT_LESSON_WRITER_MODEL)
    agent: Agent[None, str] = Agent(
        model=build_model(model_name),
        output_type=str,
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
        return r, _parse_lesson(r.output, subject, repo)

    try:
        result, lesson = retry_with_backoff(
            _call, label=f"lesson_writer {subject.project}/{subject.commit_hash[:12]}"
        )
    except (ValidationError, json.JSONDecodeError, ValueError) as exc:
        logger.error("lesson_agent[writer]: unusable output (%s)", exc)
        return None
    except Exception as exc:
        logger.error("lesson_agent[writer]: failed after retries (%s)", exc)
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

    research = run_research(subject, repo)
    if research is None:
        return stub_lesson(subject, reason="research_failed")

    lesson = run_writer(subject, research, repo)
    if lesson is None:
        return stub_lesson(subject, reason="writer_failed")
    return lesson
