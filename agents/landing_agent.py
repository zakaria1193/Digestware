"""Factory agent — digests landed commits into LandingDigest.

Model strategy (budget-aware):
- google/gemini-2.0-flash-001 for all bulk processing.
- anthropic/claude-sonnet-4-5 only when impact_score >= 9 (re-run single item).

Batching: 15 commits per LLM call.
Cross-reference trailers scanned: Closes #N, Message-Id:, Link:, PR \\d+.
Token usage appended to agents/output/usage.log.
"""

from __future__ import annotations

import json
import logging
import os
import re
from datetime import datetime, timezone
from pathlib import Path

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

from agents.models.landing import LandingDigest
from agents.models.raw import RawCommit
from agents.tools.patch_id import extract_patch_id
from agents.tools.web_search import search_context

logger = logging.getLogger(__name__)

_BATCH_SIZE = 15
_DEFAULT_MODEL = "google/gemini-2.0-flash-001"
_PREMIUM_MODEL = "anthropic/claude-sonnet-4-5"
_USAGE_LOG = Path("agents/output/usage.log")

_TRAILER_PATTERNS = [
    re.compile(r"Closes\s+#(\d+)", re.IGNORECASE),
    re.compile(r"Message-Id:\s*<([^>]+)>", re.IGNORECASE),
    re.compile(r"Link:\s*(https?://\S+)", re.IGNORECASE),
    re.compile(r"\bPR\s+(\d+)\b", re.IGNORECASE),
    re.compile(r"Bugzilla:\s*(\d+)", re.IGNORECASE),
]

_SYSTEM_PROMPT = """\
You are an expert open-source systems-software analyst. For each commit
provided, produce a LandingDigest JSON object capturing:
- subsystem (e.g. "gcc/ipa", "kernel/mm", "binutils/ld")
- impact_score 1–10 (higher = more significant to end users / the ecosystem)
- whether it's a performance_win or breaking_change
- a 2–4 sentence plain-English summary

Source-type heuristics:
- "github"       → commit message conventions (Conventional Commits, etc.)
- "public_inbox" → look for Reviewed-by / Tested-by / Signed-off-by chains
- "plain_git"    → commit body only; no PR metadata available

Scan commit messages for cross-reference trailers:
  Closes #N, Message-Id: <id>, Link: <url>, PR N, Bugzilla: N

Return a JSON array — raw JSON only, no markdown fences.
"""


def _build_model(model_name: str) -> OpenAIModel:
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    return OpenAIModel(
        model_name,
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )


def _render_batch(batch: list[RawCommit]) -> str:
    lines: list[str] = []
    for c in batch:
        lines.append(f"--- Commit {c.sha[:12]} ---")
        lines.append(f"source_type: {c.source_type}")
        lines.append(f"author: {c.author}")
        lines.append(f"date: {c.date.isoformat()}")
        lines.append(f"url: {c.url}")
        lines.append(f"message:\n{c.message[:2000]}")
        if c.diff_stat:
            lines.append(f"diff_stat:\n{c.diff_stat[:500]}")
        lines.append("")
    return "\n".join(lines)


def _extract_trailers(message: str) -> dict:
    trailers: dict = {}
    for pattern in _TRAILER_PATTERNS:
        m = pattern.search(message)
        if m:
            trailers[pattern.pattern] = m.group(1)
    return trailers


def _append_usage(agent_name: str, model: str, usage: object) -> None:
    _USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "agent": agent_name,
        "model": model,
        "ts": datetime.now(tz=timezone.utc).isoformat(),
        "usage": str(usage),
    }
    with _USAGE_LOG.open("a") as fh:
        fh.write(json.dumps(record) + "\n")


def _make_agent(model_name: str) -> Agent:
    model = _build_model(model_name)
    return Agent(
        model=model,
        result_type=list[LandingDigest],
        system_prompt=_SYSTEM_PROMPT,
        tools=[
            extract_patch_id,  # type: ignore[arg-type]
            search_context,    # type: ignore[arg-type]
        ],
    )


def run_landing_agent(
    commits: list[RawCommit],
    project: str = "gcc",
    dry_run: bool = False,
) -> list[LandingDigest]:
    """Process all commits in batches and return LandingDigest objects.

    Items with impact_score >= 9 are re-run through the premium model.

    Args:
        commits: Raw items from IngestionEngine.
        project: Default project name injected into each digest.
        dry_run: If True, skip LLM calls and return stub digests.
    """
    if not commits:
        return []

    if dry_run:
        return _stub_digests(commits, project)

    cheap_model_name = os.environ.get("SUMMARISER_MODEL", _DEFAULT_MODEL)
    cheap_agent = _make_agent(cheap_model_name)

    results: list[LandingDigest] = []
    for i in range(0, len(commits), _BATCH_SIZE):
        batch = commits[i : i + _BATCH_SIZE]
        prompt = (
            f"Digest the following {len(batch)} commit(s) for project "
            f"'{project}'. Return a JSON array of LandingDigest objects.\n\n"
            + _render_batch(batch)
        )
        try:
            result = cheap_agent.run_sync(prompt)
            usage = result.usage()
            _append_usage("landing_agent", cheap_model_name, usage)
            logger.info(
                "Batch %d–%d: %d digests, usage=%s",
                i,
                i + len(batch) - 1,
                len(result.data),
                usage,
            )
            results.extend(result.data)
        except Exception as exc:
            logger.error("landing_agent batch %d failed: %s", i, exc)
            results.extend(_stub_digests(batch, project))

    # Re-run high-impact items with premium model
    premium_items = [r for r in results if r.impact_score >= 9]
    if premium_items:
        logger.info(
            "Re-running %d high-impact items with premium model", len(premium_items)
        )
        results = _rerun_premium(results, premium_items, project)

    return results


def _rerun_premium(
    all_results: list[LandingDigest],
    high_impact: list[LandingDigest],
    project: str,
) -> list[LandingDigest]:
    premium_model_name = os.environ.get("BENTO_MODEL", _PREMIUM_MODEL)
    premium_agent = _make_agent(premium_model_name)
    # Build a mapping from commit_hash for easy replacement
    updated: dict[str, LandingDigest] = {d.commit_hash: d for d in high_impact}
    # Create minimal RawCommit stubs for re-run
    stubs = [
        RawCommit(
            sha=d.commit_hash,
            author=d.author,
            date=datetime.now(tz=timezone.utc),
            message=d.summary,
            diff_stat="",
            url=d.url,
            source_type=d.source_type,
        )
        for d in high_impact
    ]
    prompt = (
        f"Re-analyse these {len(stubs)} high-impact commit(s) for project "
        f"'{project}' with greater depth. Return a JSON array of LandingDigest.\n\n"
        + _render_batch(stubs)
    )
    try:
        result = premium_agent.run_sync(prompt)
        usage = result.usage()
        _append_usage("landing_agent_premium", premium_model_name, usage)
        for refined in result.data:
            updated[refined.commit_hash] = refined
    except Exception as exc:
        logger.error("Premium re-run failed: %s — keeping cheap results", exc)

    # Replace original results with refined versions
    return [updated.get(d.commit_hash, d) for d in all_results]


def _stub_digests(items: list[RawCommit], project: str) -> list[LandingDigest]:
    return [
        LandingDigest(
            project=project,
            subsystem="unknown",
            commit_hash=c.sha,
            source_type=c.source_type,
            author=c.author,
            impact_score=5,
            summary=c.message[:200] if c.message else "(no message)",
            url=c.url,
        )
        for c in items
    ]
