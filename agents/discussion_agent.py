"""Lab agent — digests mailing-list / PR discussions into DiscussionDigest.

Model: google/gemini-2.0-flash-001 (cheap, fast, good at long context).
Batching: 10 discussions per LLM call to stay within budget.
Token usage is appended as a JSON line to agents/output/usage.log.
"""

from __future__ import annotations

import logging
import os

from pydantic_ai import Agent

from agents._openrouter import build_model
from agents._retry import retry_with_backoff
from agents.models.base import Outcome
from agents.models.discussion import DiscussionDigest
from agents.models.raw import RawDiscussion
from agents.tools.headline import clean_subject
from agents.tools.outcome import derive_discussion_outcome
from agents.tools.patch_id import extract_patch_id
from agents.tools.series import parse_patch_tag, series_id_for, split_canonical
from agents.tools.series_grouping import series_aware_batches
from agents.tools.subsystem import extract_subsystem
from agents.tools.web_search import search_context
from agents.usage_log import append_usage

logger = logging.getLogger(__name__)

_BATCH_SIZE = 10
_DEFAULT_MODEL = "google/gemini-2.0-flash-001"

# Module-level counters so main() can detect silent degradation (every LLM
# batch falling through to stubs). Reset by main() at the start of each run.
batches_total: int = 0
batches_stubbed: int = 0

_SYSTEM_PROMPT = """\
You are the editor of a WSJ-style daily for working systems developers. You
read in-flight proposals (PRs, mailing-list RFCs, patch series) and produce a
DiscussionDigest JSON object for each one.

AUDIENCE
A working dev who does NOT specialise in this subsystem should understand in
under 30 seconds what's being proposed and whether they should care.

WRITING RULES
- Active voice, concrete verbs. No filler ("basically", "in a nutshell",
  "this patch aims to", "see commit message").
- ``headline`` is a sentence, not a subject line. Strip "[PATCH …]", "Re:",
  and ``N/M`` markers. Capitalise the first word.
- Never copy raw email lines into ``summary`` — always rewrite as prose.
- Never echo quoted email lines (``> …`` or ``On … wrote:``).
- ``summary`` is 2–4 sentences of prose. No trailing ellipsis.

FIELDS (all required unless noted):
- ``subsystem`` — e.g. "gcc/ipa", "malloc", "kernel/mm". Never "unknown".
- ``headline`` — readable title, ≤ 80 chars, no brackets, no "Re:".
- ``tldr`` — one sentence, ≤ 140 chars.
- ``stakes`` — 1–2 sentences: why a general dev should care (perf, ABI,
  security, ergonomics, policy).
- ``summary`` — 2–4 sentences covering what's proposed and where the thread
  sits.
- ``tags`` — up to 5 topic tags.
- ``technical_tradeoffs`` — bullet list; never empty for a non-trivial RFC.
- ``sentiment_score`` 1–10 (1=hostile/NACK storm, 5=neutral debate, 10=wide
  approval) with a one-line ``sentiment_rationale``.
- ``outcome`` — one of proposed / under_review / needs_revision / nackd /
  ready / committed / withdrawn / stalled. Use the ``outcome_hint`` from
  the input unless the thread clearly contradicts it.
- ``series_role`` — "cover" for the 0/N cover letter, "reply" for discussion
  replies in a series, "standalone" otherwise. ``series_id`` may be set from
  the input hint.

INPUT HINTS
Each discussion arrives with pre-extracted ``subsystem_hint``,
``headline_hint``, ``outcome_hint``, and (if applicable) ``series_id_hint``.
Use these as defaults; override only when the thread contradicts them.

The ``discussion_id`` field MUST be echoed verbatim from the input.

Return a JSON array — raw JSON only, no markdown fences.
"""



def _render_batch(batch: list[RawDiscussion]) -> str:
    lines: list[str] = []
    for d in batch:
        reply_bodies = [
            r.get("body", r.get("comment", "")) or ""
            for r in (d.replies or [])
        ]
        subsystem_hint = extract_subsystem(
            d.title, d.diff_text, d.project
        )
        headline_hint = clean_subject(d.title)
        outcome_hint = derive_discussion_outcome(
            d.title, d.body, reply_bodies, last_activity=d.date
        ).value
        series_hint = series_id_for(d.title, d.project)

        lines.append(f"--- Discussion {d.id} ---")
        lines.append(f"project: {d.project}")
        lines.append(f"source_type: {d.source_type}")
        lines.append(f"title: {d.title}")
        lines.append(f"subsystem_hint: {subsystem_hint}")
        lines.append(f"headline_hint: {headline_hint}")
        lines.append(f"outcome_hint: {outcome_hint}")
        if series_hint:
            lines.append(f"series_id_hint: {series_hint}")
        lines.append(f"author: {d.author}")
        lines.append(f"date: {d.date.isoformat()}")
        lines.append(f"url: {d.url}")
        lines.append(f"body:\n{d.body[:2000]}")
        if d.replies:
            lines.append(f"replies ({len(d.replies)} total):")
            for r in d.replies[:5]:
                body = r.get("body", r.get("comment", ""))[:500]
                lines.append(f"  - {body}")
        if d.diff_text:
            lines.append(f"diff (truncated):\n{d.diff_text[:1000]}")
        lines.append("")
    return "\n".join(lines)


def run_discussion_agent(
    discussions: list[RawDiscussion],
    dry_run: bool = False,
) -> list[DiscussionDigest]:
    """Process all discussions in batches and return DiscussionDigest objects.

    Each digest's ``project`` and ``date`` fields are overridden post-hoc from
    the originating ``RawDiscussion`` so they reflect the source (and never
    depend on the LLM echoing them correctly).

    Args:
        discussions: Raw items from IngestionEngine.
        dry_run: If True, skip LLM calls and return stub digests.
    """
    if not discussions:
        return []

    # Collapse ``[PATCH N/M]`` series so the feed shows one card per series.
    canonical, parts_by_canonical_index = split_canonical(
        discussions,
        title_of=lambda d: d.title or "",
        project_of=lambda d: d.project,
        url_of=lambda d: d.url,
    )
    discussions = canonical
    raw_by_id: dict[str, RawDiscussion] = {d.id: d for d in discussions}

    if dry_run:
        stubs = _stub_digests(discussions)
        return _apply_series_and_subsystem(stubs, discussions, parts_by_canonical_index)

    model_name = os.environ.get("SUMMARISER_MODEL", _DEFAULT_MODEL)
    model = build_model(model_name)
    agent: Agent[None, list[DiscussionDigest]] = Agent(
        model=model,
        output_type=list[DiscussionDigest],
        system_prompt=_SYSTEM_PROMPT,
        tools=[
            extract_patch_id,  # type: ignore[arg-type]
            search_context,    # type: ignore[arg-type]
        ],
    )

    results: list[DiscussionDigest] = []
    batches = series_aware_batches(
        discussions, _BATCH_SIZE, lambda d: d.metadata.get("series_id")
    )
    for batch_idx, batch in enumerate(batches):
        results.extend(_run_batch(agent, model_name, batch, batch_idx))

    # Deterministic project + date override from the original RawDiscussion.
    results = _override_from_raw(results, raw_by_id)
    return _apply_series_and_subsystem(
        results, discussions, parts_by_canonical_index
    )


def _apply_series_and_subsystem(
    results: list[DiscussionDigest],
    canonical: list[RawDiscussion],
    parts_by_canonical_index: dict[int, list[dict]],
) -> list[DiscussionDigest]:
    """Enforce subsystem / headline / outcome invariants and attach parts."""
    by_id: dict[str, RawDiscussion] = {d.id: d for d in canonical}
    parts_by_id: dict[str, list[dict]] = {
        canonical[i].id: parts
        for i, parts in parts_by_canonical_index.items()
        if 0 <= i < len(canonical)
    }

    fixed: list[DiscussionDigest] = []
    for d in results:
        raw = by_id.get(d.discussion_id)
        patch: dict[str, object] = {}

        if raw is not None:
            if not d.subsystem or d.subsystem.lower() in {"unknown", "general", ""}:
                patch["subsystem"] = extract_subsystem(
                    raw.title, raw.diff_text, raw.project
                )
            clean_hl = clean_subject(d.headline or raw.title)
            if clean_hl and clean_hl != d.headline:
                patch["headline"] = clean_hl

            sid = series_id_for(raw.title, raw.project)
            if sid:
                patch["series_id"] = sid
                tag = parse_patch_tag(raw.title) or {}
                patch["series_role"] = "cover" if tag.get("n") == 0 else "reply"
            elif d.series_role is None:
                patch["series_role"] = "standalone"

            parts = parts_by_id.get(d.discussion_id)
            if parts:
                patch["series_parts"] = parts

            # Trust the deterministic outcome if the LLM hasn't set one or
            # set it to a value that contradicts strong signals.
            reply_texts = [
                r.get("body", r.get("comment", "")) or ""
                for r in (raw.replies or [])
            ]
            derived = derive_discussion_outcome(
                raw.title,
                raw.body,
                reply_texts,
                last_activity=raw.date,
            )
            # Only override when LLM's output is the default PROPOSED but
            # stronger signals were present.
            if d.outcome == Outcome.PROPOSED and derived != Outcome.PROPOSED:
                patch["outcome"] = derived

        if patch:
            d = d.model_copy(update=patch)
        fixed.append(d)
    return fixed


def _run_batch(
    agent: Agent[None, list[DiscussionDigest]],
    model_name: str,
    batch: list[RawDiscussion],
    batch_idx: int,
) -> list[DiscussionDigest]:
    """Run one batch through the LLM with retry + input/output correlation.

    Missing items (present in input, absent from LLM response) are filled in
    with stub digests so batches never silently shrink.
    """
    batch_projects = sorted({d.project for d in batch})
    prompt = (
        f"Digest the following {len(batch)} discussion(s) "
        f"(projects: {', '.join(batch_projects)}). "
        f"Return a JSON array of DiscussionDigest objects. The ``discussion_id``, "
        f"``project`` and ``date`` fields MUST be taken verbatim from each input "
        f"item — preserve them exactly so each digest can be matched back.\n\n"
        + _render_batch(batch)
    )

    global batches_total, batches_stubbed
    batches_total += 1
    try:
        result = retry_with_backoff(
            lambda: agent.run_sync(prompt),
            label=f"discussion_agent batch {batch_idx}",
        )
    except Exception as exc:
        logger.error(
            "discussion_agent batch %d failed after retries: %s", batch_idx, exc
        )
        batches_stubbed += 1
        return _stub_digests(batch)

    append_usage("discussion_agent", model_name, result.usage())
    data: list[DiscussionDigest] = list(result.output)
    logger.info(
        "Batch %d: %d item(s) digested, usage=%s",
        batch_idx, len(data), result.usage(),
    )

    # Correlation: stub any input item the LLM failed to return.
    returned_ids = {d.discussion_id for d in data}
    missing = [raw for raw in batch if raw.id not in returned_ids]
    if missing:
        logger.warning(
            "discussion_agent batch %d: LLM omitted %d of %d items (ids=%s)",
            batch_idx, len(missing), len(batch), [m.id for m in missing],
        )
        data.extend(_stub_digests(missing))

    # Correlation: drop hallucinated items the LLM invented.
    input_ids = {raw.id for raw in batch}
    extra = [d for d in data if d.discussion_id not in input_ids]
    if extra:
        logger.warning(
            "discussion_agent batch %d: LLM returned %d unknown ids=%s — dropping",
            batch_idx, len(extra), [d.discussion_id for d in extra],
        )
        data = [d for d in data if d.discussion_id in input_ids]

    return data


def _override_from_raw(
    digests: list[DiscussionDigest],
    raw_by_id: dict[str, RawDiscussion],
) -> list[DiscussionDigest]:
    """Force ``project`` and ``date`` to match the originating RawDiscussion."""
    fixed: list[DiscussionDigest] = []
    for d in digests:
        raw = raw_by_id.get(d.discussion_id)
        if raw is not None:
            d = d.model_copy(update={"project": raw.project, "date": raw.date})
        fixed.append(d)
    return fixed


def _stub_digests(items: list[RawDiscussion]) -> list[DiscussionDigest]:
    from agents.models.base import ConsensusStatus

    out: list[DiscussionDigest] = []
    for d in items:
        headline = clean_subject(d.title) or (d.title or d.id)
        subsystem = extract_subsystem(d.title, d.diff_text, d.project)
        reply_bodies = [
            r.get("body", r.get("comment", "")) or ""
            for r in (d.replies or [])
        ]
        outcome = derive_discussion_outcome(
            d.title, d.body, reply_bodies, last_activity=d.date
        )
        out.append(
            DiscussionDigest(
                project=d.project,
                subsystem=subsystem,
                discussion_id=d.id,
                source_type=d.source_type,
                title=d.title,
                headline=headline,
                tldr=headline[:160] if headline else "Discussion open.",
                stakes="Summary unavailable — see source link.",
                proposer=d.author,
                consensus=ConsensusStatus.PROPOSED,
                outcome=outcome,
                sentiment_score=5,
                sentiment_rationale="Stub digest; sentiment not evaluated.",
                technical_tradeoffs=[],
                summary="Summary unavailable — see source link.",
                url=d.url,
                date=d.date,
            )
        )
    return out
