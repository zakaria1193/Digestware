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
from agents.models.discussion import DiscussionDigest
from agents.models.raw import RawDiscussion
from agents.tools.patch_id import extract_patch_id
from agents.tools.series_grouping import series_aware_batches
from agents.tools.web_search import search_context
from agents.usage_log import append_usage

logger = logging.getLogger(__name__)

_BATCH_SIZE = 10
_DEFAULT_MODEL = "google/gemini-2.0-flash-001"

_SYSTEM_PROMPT = """\
You are an expert open-source software analyst specialising in low-level systems
software (compilers, linkers, kernels, libc). Your job is to read batches of
raw discussions (GitHub PRs, mailing-list threads, etc.) and produce structured
digests for each one.

Source-type heuristics:
- "github_pr"      → infer consensus from review state (approvals,
                     "changes_requested", LGTM comments).
- "public_inbox"   → infer consensus from ACK / NACK / RFC patterns in email.
- "gitlab_mr"      → same as github_pr.

Return a JSON array where each element matches the DiscussionDigest schema.
Do not include markdown fences — raw JSON only.
"""



def _render_batch(batch: list[RawDiscussion]) -> str:
    lines: list[str] = []
    for d in batch:
        lines.append(f"--- Discussion {d.id} ---")
        lines.append(f"project: {d.project}")
        lines.append(f"source_type: {d.source_type}")
        lines.append(f"title: {d.title}")
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

    raw_by_id: dict[str, RawDiscussion] = {d.id: d for d in discussions}

    if dry_run:
        return _stub_digests(discussions)

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
    return _override_from_raw(results, raw_by_id)


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

    try:
        result = retry_with_backoff(
            lambda: agent.run_sync(prompt),
            label=f"discussion_agent batch {batch_idx}",
        )
    except Exception as exc:
        logger.error(
            "discussion_agent batch %d failed after retries: %s", batch_idx, exc
        )
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

    return [
        DiscussionDigest(
            project=d.project,
            subsystem="unknown",
            discussion_id=d.id,
            source_type=d.source_type,
            title=d.title,
            proposer=d.author,
            consensus=ConsensusStatus.PROPOSED,
            sentiment_score=5,
            technical_tradeoffs=[],
            summary=d.body[:200] if d.body else "(no body)",
            url=d.url,
            date=d.date,
        )
        for d in items
    ]
