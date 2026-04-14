"""Factory agent — digests landed commits into LandingDigest.

Model strategy (budget-aware):
- google/gemini-2.0-flash-001 for all bulk processing.
- anthropic/claude-sonnet-4-5 only when impact_score >= 9 (re-run single item).

Batching: 15 commits per LLM call.

Cross-reference trailers (Closes #N, Message-Id:, Link:, PR N, Bugzilla: N) are
extracted deterministically from raw commit messages and applied post-hoc to
LandingDigest.discussion_id_link, regardless of what the LLM finds.

The premium re-run receives the ORIGINAL RawCommit (not the cheap LLM's summary),
so the premium model has at least as much context as the cheap one.

Token usage is appended as JSON lines to agents/output/usage.log, which is
rotated when it exceeds _MAX_USAGE_LOG_BYTES.
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
from agents.tools.series_grouping import series_aware_batches
from agents.tools.web_search import search_context

logger = logging.getLogger(__name__)

_BATCH_SIZE = 15
_DEFAULT_MODEL = "google/gemini-2.0-flash-001"
_PREMIUM_MODEL = "anthropic/claude-sonnet-4-5"
_USAGE_LOG = Path("agents/output/usage.log")
_MAX_USAGE_LOG_BYTES = 10 * 1024 * 1024  # 10 MB — rotate when exceeded

_TRAILER_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("closes",      re.compile(r"Closes\s+#(\d+)", re.IGNORECASE)),
    ("message_id",  re.compile(r"Message-Id:\s*<([^>]+)>", re.IGNORECASE)),
    ("link",        re.compile(r"^Link:\s*(https?://\S+)", re.IGNORECASE | re.MULTILINE)),
    ("pr",          re.compile(r"\bPR\s+(\d+)\b", re.IGNORECASE)),
    ("bugzilla",    re.compile(r"Bugzilla:\s*(\d+)", re.IGNORECASE)),
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

Cross-reference trailers are listed explicitly — use them to populate
discussion_id_link where present.

Return a JSON array — raw JSON only, no markdown fences.
"""


def _extract_trailers(message: str) -> dict[str, str]:
    """Extract cross-reference trailers from a commit message."""
    found: dict[str, str] = {}
    for key, pattern in _TRAILER_PATTERNS:
        m = pattern.search(message)
        if m:
            found[key] = m.group(1)
    return found


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
        # Include deterministically-extracted trailers as a hint to the model
        trailers = _extract_trailers(c.message)
        if trailers:
            lines.append(f"cross_refs: {json.dumps(trailers)}")
        lines.append("")
    return "\n".join(lines)


def _maybe_rotate_log(path: Path) -> None:
    """Rotate the usage log when it exceeds _MAX_USAGE_LOG_BYTES (one backup kept)."""
    if path.exists() and path.stat().st_size > _MAX_USAGE_LOG_BYTES:
        backup = path.with_suffix(".log.1")
        backup.unlink(missing_ok=True)
        path.rename(backup)
        logger.info("Rotated usage log → %s", backup)


def _append_usage(agent_name: str, model: str, usage: object) -> None:
    _USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
    _maybe_rotate_log(_USAGE_LOG)
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

    Items with impact_score >= 9 are re-run through the premium model using the
    original RawCommit data (not the cheap model's summary).

    Args:
        commits: Raw items from IngestionEngine.
        project: Default project name injected into each digest.
        dry_run: If True, skip LLM calls and return stub digests.
    """
    if not commits:
        return []

    if dry_run:
        return _stub_digests(commits, project)

    # Build SHA → original RawCommit map for deterministic trailer injection
    # and premium re-run (C5 fix: premium model gets original data, not LLM summary)
    commit_by_sha: dict[str, RawCommit] = {c.sha: c for c in commits}

    cheap_model_name = os.environ.get("SUMMARISER_MODEL", _DEFAULT_MODEL)
    cheap_agent = _make_agent(cheap_model_name)

    results: list[LandingDigest] = []
    batches = series_aware_batches(
        commits, _BATCH_SIZE, lambda c: c.metadata.get("series_id")
    )
    for batch_idx, batch in enumerate(batches):
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
                "Batch %d: %d digest(s), usage=%s",
                batch_idx, len(result.data), usage,
            )
            results.extend(result.data)
        except Exception as exc:
            logger.error("landing_agent batch %d failed: %s", batch_idx, exc)
            results.extend(_stub_digests(batch, project))

    # Deterministically apply extracted trailers (C3 fix: _extract_trailers is
    # now actually called; LLM cross-ref is supplemented, not replaced)
    results = _apply_trailers(results, commit_by_sha)

    # Re-run high-impact items with premium model
    premium_items = [r for r in results if r.impact_score >= 9]
    if premium_items:
        logger.info("Re-running %d high-impact items with premium model", len(premium_items))
        results = _rerun_premium(results, premium_items, commit_by_sha, project)

    return results


def _apply_trailers(
    digests: list[LandingDigest],
    commit_by_sha: dict[str, RawCommit],
) -> list[LandingDigest]:
    """Backfill discussion_id_link from deterministically-extracted trailers.

    Only overwrites if the LLM left the field None (prefer LLM-set values).
    """
    updated: list[LandingDigest] = []
    for d in digests:
        if d.discussion_id_link is None:
            original = commit_by_sha.get(d.commit_hash)
            if original:
                trailers = _extract_trailers(original.message)
                link = (
                    trailers.get("message_id")
                    or trailers.get("link")
                    or trailers.get("closes")
                    or trailers.get("pr")
                )
                if link:
                    d = d.model_copy(update={"discussion_id_link": str(link)})
        updated.append(d)
    return updated


def _rerun_premium(
    all_results: list[LandingDigest],
    high_impact: list[LandingDigest],
    commit_by_sha: dict[str, RawCommit],
    project: str,
) -> list[LandingDigest]:
    """Re-analyse high-impact items with the premium model.

    C5 fix: uses the original RawCommit (full message + diff_stat), not the
    cheap LLM's summary — ensuring the premium model has at least as much
    context as the cheap one did.
    """
    premium_model_name = os.environ.get("BENTO_MODEL", _PREMIUM_MODEL)
    premium_agent = _make_agent(premium_model_name)

    # Look up original commits; fall back to stub if SHA is missing
    original_commits: list[RawCommit] = []
    for d in high_impact:
        original = commit_by_sha.get(d.commit_hash)
        if original:
            original_commits.append(original)
        else:
            logger.warning("No original RawCommit for %s — skipping premium re-run", d.commit_hash)

    if not original_commits:
        return all_results

    prompt = (
        f"Re-analyse these {len(original_commits)} high-impact commit(s) for project "
        f"'{project}' with greater depth. Return a JSON array of LandingDigest.\n\n"
        + _render_batch(original_commits)
    )

    refined_by_sha: dict[str, LandingDigest] = {}
    try:
        result = premium_agent.run_sync(prompt)
        usage = result.usage()
        _append_usage("landing_agent_premium", premium_model_name, usage)
        for refined in result.data:
            refined_by_sha[refined.commit_hash] = refined
    except Exception as exc:
        logger.error("Premium re-run failed: %s — keeping cheap results", exc)

    return [refined_by_sha.get(d.commit_hash, d) for d in all_results]


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
