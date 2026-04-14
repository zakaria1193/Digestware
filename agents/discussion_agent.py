"""Lab agent — digests mailing-list / PR discussions into DiscussionDigest.

Model: google/gemini-2.0-flash-001 (cheap, fast, good at long context).
Batching: 10 discussions per LLM call to stay within budget.
Token usage is appended as a JSON line to agents/output/usage.log.
"""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

from agents.models.discussion import DiscussionDigest
from agents.models.raw import RawDiscussion
from agents.tools.patch_id import extract_patch_id
from agents.tools.web_search import search_context

logger = logging.getLogger(__name__)

_BATCH_SIZE = 10
_DEFAULT_MODEL = "google/gemini-2.0-flash-001"
_USAGE_LOG = Path("agents/output/usage.log")

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


def _build_openrouter_model(model_name: str) -> OpenAIModel:
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    return OpenAIModel(
        model_name,
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )


def _render_batch(batch: list[RawDiscussion]) -> str:
    lines: list[str] = []
    for d in batch:
        lines.append(f"--- Discussion {d.id} ---")
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


def _append_usage(agent_name: str, usage: object) -> None:
    _USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "agent": agent_name,
        "ts": datetime.now(tz=timezone.utc).isoformat(),
        "usage": str(usage),
    }
    with _USAGE_LOG.open("a") as fh:
        fh.write(json.dumps(record) + "\n")


def run_discussion_agent(
    discussions: list[RawDiscussion],
    project: str = "gcc",
    dry_run: bool = False,
) -> list[DiscussionDigest]:
    """Process all discussions in batches and return DiscussionDigest objects.

    Args:
        discussions: Raw items from IngestionEngine.
        project: Default project name injected into each digest.
        dry_run: If True, skip LLM calls and return stub digests.
    """
    if not discussions:
        return []

    if dry_run:
        return _stub_digests(discussions, project)

    model = _build_openrouter_model(
        os.environ.get("SUMMARISER_MODEL", _DEFAULT_MODEL)
    )
    agent: Agent[None, list[DiscussionDigest]] = Agent(
        model=model,
        result_type=list[DiscussionDigest],
        system_prompt=_SYSTEM_PROMPT,
        tools=[
            extract_patch_id,  # type: ignore[arg-type]
            search_context,    # type: ignore[arg-type]
        ],
    )

    results: list[DiscussionDigest] = []
    for i in range(0, len(discussions), _BATCH_SIZE):
        batch = discussions[i : i + _BATCH_SIZE]
        prompt = (
            f"Digest the following {len(batch)} discussion(s) for project "
            f"'{project}'. Return a JSON array of DiscussionDigest objects.\n\n"
            + _render_batch(batch)
        )
        try:
            result = agent.run_sync(prompt)
            usage = result.usage()
            _append_usage("discussion_agent", usage)
            logger.info(
                "Batch %d–%d: %d digests produced, usage=%s",
                i,
                i + len(batch) - 1,
                len(result.data),
                usage,
            )
            results.extend(result.data)
        except Exception as exc:
            logger.error("discussion_agent batch %d failed: %s", i, exc)
            results.extend(_stub_digests(batch, project))

    return results


def _stub_digests(
    items: list[RawDiscussion], project: str
) -> list[DiscussionDigest]:
    from agents.models.base import ConsensusStatus

    return [
        DiscussionDigest(
            project=project,
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
        )
        for d in items
    ]
