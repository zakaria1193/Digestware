"""Lab agent — digests mailing-list / PR discussions into DiscussionDigest.

Model: google/gemini-2.0-flash-001 (cheap, fast, good at long context).
Batching: 10 discussions per LLM call to stay within budget.
Token usage is appended as a JSON line to agents/output/usage.log.
"""

from __future__ import annotations

import json
import logging
import os

from pydantic import TypeAdapter
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

VERBATIM FIELDS (echo each one exactly as given in the input):
``discussion_id``, ``project``, ``source_type``, ``title``, ``url``, ``date``,
``proposer`` (= input ``author``). Also set ``consensus`` (one of Proposed,
Under Review, Needs Revision, NACK'd, Ready to Land, Committed).

Return a JSON array — raw JSON only, no markdown fences.
"""

_ADAPTER: TypeAdapter[list[DiscussionDigest]] = TypeAdapter(list[DiscussionDigest])

# Max length enforced by DiscussionDigest.tldr — mirror it here so we can clamp
# overlong LLM output before validation instead of failing the whole batch.
_TLDR_MAX = 160


def _fill_required_from_raw(item: dict, raw: RawDiscussion) -> None:
    """Backfill required fields the LLM dropped from a parsed JSON item.

    The model schema requires several fields that we expect the LLM to echo
    verbatim from input (project, source_type, title, url, date, proposer,
    discussion_id). In practice LLMs sometimes omit them — rather than fail
    the whole batch, inject deterministic values from the originating
    RawDiscussion before validation. LLM-provided values win when present.
    """
    defaults = {
        "discussion_id": raw.id,
        "project": raw.project,
        "source_type": raw.source_type,
        "title": raw.title,
        "url": raw.url,
        "date": raw.date.isoformat(),
        "proposer": raw.author,
        "consensus": "Proposed",
    }
    for key, value in defaults.items():
        if item.get(key) in (None, ""):
            item[key] = value
    tldr = item.get("tldr")
    if isinstance(tldr, str) and len(tldr) > _TLDR_MAX:
        item["tldr"] = tldr[: _TLDR_MAX - 1].rstrip() + "…"


def _parse_discussion_batch(
    text: str,
    batch: list[RawDiscussion] | None = None,
) -> list[DiscussionDigest]:
    """Parse raw JSON text (with optional markdown fences) into DiscussionDigest list.

    When ``batch`` is provided, each parsed item is matched back to its raw
    input (by ``discussion_id``, else by position) and missing required fields
    are backfilled from the raw data.
    """
    text = text.strip()
    if text.startswith("```"):
        text = text[text.index("\n") + 1:] if "\n" in text else text[3:]
    if text.endswith("```"):
        text = text[:text.rindex("```")].rstrip()
    raw_list = json.loads(text)
    if batch and isinstance(raw_list, list):
        by_id = {d.id: d for d in batch}
        for idx, item in enumerate(raw_list):
            if not isinstance(item, dict):
                continue
            disc_id = item.get("discussion_id")
            raw = by_id.get(disc_id) if isinstance(disc_id, str) else None
            if raw is None and idx < len(batch):
                raw = batch[idx]
            if raw is not None:
                _fill_required_from_raw(item, raw)
    return _ADAPTER.validate_python(raw_list)


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
    agent: Agent[None, str] = Agent(
        model=model,
        output_type=str,
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
    agent: Agent[None, str],
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

    def _call():
        r = agent.run_sync(prompt)
        items = _parse_discussion_batch(r.output, batch=batch)
        if not items and batch:
            raise ValueError(f"Model returned 0 items for {len(batch)} input item(s)")
        return r, items

    global batches_total, batches_stubbed
    batches_total += 1
    try:
        result, data = retry_with_backoff(
            _call,
            label=f"discussion_agent batch {batch_idx}",
        )
    except Exception as exc:
        logger.error(
            "discussion_agent batch %d failed after retries: %s", batch_idx, exc
        )
        batches_stubbed += 1
        return _stub_digests(batch)

    append_usage("discussion_agent", model_name, result.usage())
    data = list(data)
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
