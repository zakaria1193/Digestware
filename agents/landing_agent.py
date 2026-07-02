"""Factory agent — digests landed commits into LandingDigest.

Model strategy (budget-aware):
- google/gemini-2.5-flash-lite for all bulk processing.
- anthropic/claude-sonnet-4-5 only when impact_score >= 9 (re-run single item).

Batching: 8 commits per LLM call (down from 15 after observing Gemini Flash
truncate LandingDigest JSON output mid-string on larger batches).

Cross-reference trailers (Closes #N, Message-Id:, Link:, PR N, Bugzilla: N) are
extracted deterministically from raw commit messages and applied post-hoc to
LandingDigest.discussion_id_link / bugzilla_pr, regardless of what the LLM
finds. Trailers are applied AFTER the premium re-run so the premium merge
doesn't clobber deterministic data.

The premium re-run receives the ORIGINAL RawCommit (not the cheap LLM's
summary), so the premium model has at least as much context as the cheap one.

Token usage goes through the shared ``agents.usage_log`` module (structured
JSON with parsed token counts, anchored path, rotated at 10 MB).
"""

from __future__ import annotations

import json
import logging
import os
import re
from urllib.parse import urlparse

from pydantic import TypeAdapter
from pydantic_ai import Agent

from agents._openrouter import (
    DEFAULT_PREMIUM_MODEL,
    DEFAULT_SUMMARISER_MODEL,
    build_model,
)
from agents._retry import retry_with_backoff
from agents.models.base import Outcome
from agents.models.landing import LandingDigest
from agents.models.raw import RawCommit
from agents.tools.headline import clean_subject
from agents.tools.patch_id import extract_patch_id
from agents.tools.series import parse_patch_tag, series_id_for, split_canonical
from agents.tools.series_grouping import series_aware_batches
from agents.tools.subsystem import extract_subsystem
from agents.tools.web_search import search_context
from agents.usage_log import append_usage

logger = logging.getLogger(__name__)

_BATCH_SIZE = 8
_DEFAULT_MODEL = DEFAULT_SUMMARISER_MODEL
_PREMIUM_MODEL = DEFAULT_PREMIUM_MODEL

# Module-level counters so main() can detect silent degradation (every LLM
# batch falling through to stubs). Reset by main() at the start of each run.
batches_total: int = 0
batches_stubbed: int = 0

_TRAILER_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("closes",      re.compile(r"Closes\s+#(\d+)", re.IGNORECASE)),
    ("message_id",  re.compile(r"Message-Id:\s*<([^>]+)>", re.IGNORECASE)),
    ("link",        re.compile(
        r"^Link:\s*(https?://\S+)", re.IGNORECASE | re.MULTILINE,
    )),
    ("pr",          re.compile(r"\bPR\s+(\d+)\b", re.IGNORECASE)),
    ("bugzilla",    re.compile(r"Bugzilla:\s*(\d+)", re.IGNORECASE)),
]

_SYSTEM_PROMPT = """\
You are the editor of a WSJ-style daily for working systems developers. You
read raw commits (compilers, linkers, kernels, libc) and produce a
LandingDigest JSON object for each one.

AUDIENCE
A working dev who does NOT specialise in this subsystem should understand
the change in under 30 seconds. Write for them.

WRITING RULES
- Use active voice and concrete verbs. No filler ("In a nutshell",
  "This patch aims to", "See commit message for details", "basically").
- Headlines are sentences, not subject lines. Strip "[PATCH …]", "Re:",
  and ``N/M`` series markers. Capitalise the first word.
- Never copy raw commit-message lines into ``summary`` verbatim — always
  rewrite into prose.
- Never echo quoted email lines (``> …`` or ``On … wrote:``).
- Keep ``summary`` at 2–4 sentences. No trailing ellipsis.

FIELDS (all required unless noted):
- ``subsystem`` — e.g. "gcc/ipa", "kernel/mm", "binutils/ld". Never "unknown".
- ``headline`` — human-readable title, ≤ 80 chars.
- ``tldr`` — one short sentence, ≤ 140 chars.
- ``summary`` — 2–4 sentences of prose covering what changed, how, and why
  a working dev should care (perf, ABI, security, ergonomics, policy).
  Weave the stakes into the flow — don't tack them on as a separate
  clause, and don't lead with "this matters because…".
- ``primer_expert`` — the "What is this even about?" context written FOR
  toolchain insiders. 2–4 sentences, ≤ 500 chars. Assume the reader already
  knows compiler passes, ELF/DWARF, relocations, PIC/PIE, ABI conventions,
  and the wider project vocabulary — don't waste words defining those.
  Instead, place THIS specific subsystem inside that map: name the concrete
  pass / file / invariant / data structure in play (e.g. ``ipa-sra.cc`` and
  ``IPA_PARAM_DESCRIPTOR`` for GCC IPA-SRA), note why a toolchain dev
  outside the subsystem still wouldn't instantly know it, and flag any
  non-obvious interaction with neighbouring subsystems.
- ``primer_glossary`` — the "For Context" block: 3–8 ``{term, definition}``
  entries for a systems programmer who does NOT work on toolchains day to
  day. Assume the reader already knows general low-level plumbing
  (pointers, processes, syscalls, the build pipeline in outline) — do NOT
  define those. Only define toolchain-specific jargon that actually
  appears in this article: compiler passes, IR forms, subsystem names,
  flags, ABI/ELF/DWARF terms, data structures. ``term`` is the exact
  spelling as it appears elsewhere in the digest (e.g. "IPA-SRA",
  "-fipa-sra", "ELF relocation"). ``definition`` is 1–3 sentences: what it
  is, what problem it solves, and where it sits in the pipeline (source →
  IR → object → binary → runtime) when that context matters. Do NOT
  restate the commit's effect or the TL;DR — background only. Return an
  empty list only when the article genuinely has nothing to unpack.
- For ``primer_expert`` and ``primer_glossary``: call the
  ``search_context`` tool with the subsystem + key terms (e.g. "GCC
  IPA-SRA inter-procedural scalar replacement") once and reuse the
  grounding for both.
- ``tags`` — up to 5 short topic tags (e.g. ["optimization", "risc-v"]).
- ``impact_score`` 1–10. Rubric:
    9–10 : CVE, ABI break, perf ≥ 10%, new arch / language feature.
    7–8  : user-visible feature, non-trivial optimisation, toolchain policy.
    4–6  : refactor, internal API, test infra, bugfix with limited user impact.
    1–3  : typo, comment, docs, cosmetic.
- ``performance_win`` / ``breaking_change`` — booleans; set only when clear.
- ``outcome`` — almost always "committed" for landed commits.
- ``headline`` / ``tldr`` / ``summary`` must NOT contain "Re:", "[PATCH", or
  ``N/M`` series markers.

INPUT HINTS
Each commit arrives with pre-extracted ``subsystem_hint`` (deterministic) and
``cross_refs`` (closes/bugzilla/etc). Use these if they're present; don't
invent values for them.

VERBATIM FIELDS (echo each one exactly as given in the input):
``commit_hash`` (= input ``sha``), ``project``, ``source_type``, ``author``,
``url``, ``date``.

Return a JSON array — raw JSON only, no markdown fences.
"""

_ADAPTER: TypeAdapter[list[LandingDigest]] = TypeAdapter(list[LandingDigest])

# Max length enforced by LandingDigest.tldr — mirror it here so we can clamp
# overlong LLM output before validation instead of failing the whole batch.
_TLDR_MAX = 160

# Mirrored from the Pydantic schema so we can repair overruns rather than let
# the whole batch fail validation.
_TAGS_MAX = 5
_PRIMER_EXPERT_MAX = 600
_GLOSSARY_MAX_ENTRIES = 10
_GLOSSARY_TERM_MAX = 80
_GLOSSARY_DEF_MAX = 400


def _repair_landing_item(item: dict) -> None:
    """Fix deterministic schema violations the cheap model keeps making.

    Observed failure modes (from production logs):
    - ``tags`` length > 5 (schema caps at 5).
    - ``primer_expert`` > 600 chars.
    - ``primer_glossary`` > 10 entries, or a ``term``/``definition`` that
      overruns its cap.
    """
    tags = item.get("tags")
    if isinstance(tags, list) and len(tags) > _TAGS_MAX:
        item["tags"] = tags[:_TAGS_MAX]

    val = item.get("primer_expert")
    if isinstance(val, str) and len(val) > _PRIMER_EXPERT_MAX:
        item["primer_expert"] = val[: _PRIMER_EXPERT_MAX - 1].rstrip() + "…"

    glossary = item.get("primer_glossary")
    if isinstance(glossary, list):
        if len(glossary) > _GLOSSARY_MAX_ENTRIES:
            glossary = glossary[:_GLOSSARY_MAX_ENTRIES]
        for entry in glossary:
            if not isinstance(entry, dict):
                continue
            for field, limit in (
                ("term", _GLOSSARY_TERM_MAX),
                ("definition", _GLOSSARY_DEF_MAX),
            ):
                text = entry.get(field)
                if isinstance(text, str) and len(text) > limit:
                    entry[field] = text[: limit - 1].rstrip() + "…"
        item["primer_glossary"] = glossary


def _fill_required_from_raw(item: dict, raw: RawCommit) -> None:
    """Backfill required fields the LLM dropped from a parsed JSON item.

    The model schema requires several fields (project, source_type, author,
    url, date, commit_hash) that we expect the LLM to echo verbatim from
    input. When it doesn't, inject deterministic values from the originating
    RawCommit before validation so a single missing field doesn't fail the
    whole batch. LLM-provided values win when present.
    """
    defaults = {
        "commit_hash": raw.sha,
        "project": raw.project,
        "source_type": raw.source_type,
        "author": raw.author,
        "url": raw.url,
        "date": raw.date.isoformat(),
    }
    for key, value in defaults.items():
        if item.get(key) in (None, ""):
            item[key] = value
    tldr = item.get("tldr")
    if isinstance(tldr, str) and len(tldr) > _TLDR_MAX:
        item["tldr"] = tldr[: _TLDR_MAX - 1].rstrip() + "…"


def _parse_landing_batch(
    text: str,
    batch: list[RawCommit] | None = None,
) -> list[LandingDigest]:
    """Parse raw JSON text (with optional markdown fences) into LandingDigest list.

    When ``batch`` is provided, each parsed item is matched back to its raw
    input (by ``commit_hash``, else by position) and missing required fields
    are backfilled from the raw data.
    """
    text = text.strip()
    if text.startswith("```"):
        text = text[text.index("\n") + 1:] if "\n" in text else text[3:]
    if text.endswith("```"):
        text = text[:text.rindex("```")].rstrip()
    raw_list = json.loads(text)
    if isinstance(raw_list, list):
        by_sha = {c.sha: c for c in batch} if batch else {}
        for idx, item in enumerate(raw_list):
            if not isinstance(item, dict):
                continue
            if batch:
                sha = item.get("commit_hash")
                raw = by_sha.get(sha) if isinstance(sha, str) else None
                if raw is None and idx < len(batch):
                    raw = batch[idx]
                if raw is not None:
                    _fill_required_from_raw(item, raw)
            _repair_landing_item(item)
    return _ADAPTER.validate_python(raw_list)


def _extract_trailers(message: str) -> dict[str, str]:
    """Extract cross-reference trailers from a commit message."""
    found: dict[str, str] = {}
    for key, pattern in _TRAILER_PATTERNS:
        m = pattern.search(message)
        if m:
            found[key] = m.group(1)
    return found


def _github_owner_repo(url: str) -> tuple[str, str] | None:
    """Parse ``https://github.com/{owner}/{repo}/...`` → (owner, repo)."""
    try:
        parsed = urlparse(url)
    except ValueError:
        return None
    if parsed.netloc != "github.com":
        return None
    parts = parsed.path.lstrip("/").split("/")
    if len(parts) < 2 or not parts[0] or not parts[1]:
        return None
    return parts[0], parts[1]


def _namespace_ref(raw_ref: str, commit: RawCommit) -> str:
    """Turn a raw cross-ref (bare PR #, message-id, URL) into a globally-unique id.

    - URLs and message-ids pass through unchanged.
    - Bare digits get prefixed with a platform-aware namespace so that GitHub
      PR #123 on project A doesn't collide with PR #123 on project B.
    """
    # Already a URL or contains '@' (message-id) — already globally unique.
    if raw_ref.startswith(("http://", "https://")) or "@" in raw_ref:
        return raw_ref
    if raw_ref.isdigit():
        if commit.source_type == "github":
            owner_repo = _github_owner_repo(commit.url)
            if owner_repo:
                return f"github:{owner_repo[0]}/{owner_repo[1]}#{raw_ref}"
        return f"{commit.source_type}:{commit.project}#{raw_ref}"
    return raw_ref



def _render_batch(batch: list[RawCommit]) -> str:
    lines: list[str] = []
    for c in batch:
        first_line = (c.message or "").splitlines()[0] if c.message else ""
        subsystem_hint = extract_subsystem(first_line, c.diff_stat, c.project)
        headline_hint = clean_subject(first_line)

        lines.append(f"--- Commit {c.sha} ---")
        lines.append(f"project: {c.project}")
        lines.append(f"source_type: {c.source_type}")
        lines.append(f"author: {c.author}")
        lines.append(f"date: {c.date.isoformat()}")
        lines.append(f"url: {c.url}")
        lines.append(f"subsystem_hint: {subsystem_hint}")
        lines.append(f"headline_hint: {headline_hint}")
        lines.append(f"message:\n{c.message[:2000]}")
        if c.diff_stat:
            lines.append(f"diff_stat:\n{c.diff_stat[:500]}")
        # Include deterministically-extracted trailers as a hint to the model
        trailers = _extract_trailers(c.message)
        if trailers:
            lines.append(f"cross_refs: {json.dumps(trailers)}")
        lines.append("")
    return "\n".join(lines)


def _make_agent(model_name: str) -> Agent[None, str]:
    model = build_model(model_name)
    return Agent(
        model=model,
        output_type=str,
        system_prompt=_SYSTEM_PROMPT,
        tools=[
            extract_patch_id,  # type: ignore[arg-type]
            search_context,    # type: ignore[arg-type]
        ],
    )


def run_landing_agent(
    commits: list[RawCommit],
    dry_run: bool = False,
) -> list[LandingDigest]:
    """Process all commits in batches and return LandingDigest objects.

    Items with impact_score >= 9 are re-run through the premium model using the
    original RawCommit data (not the cheap model's summary).

    Each digest's ``project`` and ``date`` fields are overridden post-hoc from
    the originating ``RawCommit`` so they reflect the source (and never depend
    on the LLM echoing them correctly).

    Args:
        commits: Raw items from IngestionEngine.
        dry_run: If True, skip LLM calls and return stub digests.
    """
    if not commits:
        return []

    # Collapse ``[PATCH N/M]`` series into one canonical item per series so
    # the feed doesn't show 8 near-identical cards. Non-canonical parts
    # become ``series_parts`` pointers on the canonical digest.
    canonical_commits, parts_by_canonical_index = split_canonical(
        commits,
        title_of=lambda c: (c.message.splitlines()[0] if c.message else ""),
        project_of=lambda c: c.project,
        url_of=lambda c: c.url,
    )
    commits = canonical_commits

    if dry_run:
        stubs = _stub_digests(commits)
        return _apply_series_and_subsystem(stubs, commits, parts_by_canonical_index)

    # SHA → original RawCommit for deterministic trailer injection and
    # premium re-run (premium model gets original data, not LLM summary).
    commit_by_sha: dict[str, RawCommit] = {c.sha: c for c in commits}

    cheap_model_name = os.environ.get("SUMMARISER_MODEL", _DEFAULT_MODEL)
    cheap_agent = _make_agent(cheap_model_name)
    logger.debug(
        "\033[1;35m── landing_agent: model=%s │ system prompt ──\n%s\033[0m",
        cheap_model_name, _SYSTEM_PROMPT,
    )

    results: list[LandingDigest] = []
    batches = series_aware_batches(
        commits, _BATCH_SIZE, lambda c: c.metadata.get("series_id")
    )
    for batch_idx, batch in enumerate(batches):
        results.extend(_run_batch(cheap_agent, cheap_model_name, batch, batch_idx))

    # Re-run high-impact items with premium model BEFORE applying trailers —
    # otherwise the premium merge would clobber deterministically-extracted
    # discussion_id_link / bugzilla_pr values.
    premium_items = [r for r in results if r.impact_score is not None and r.impact_score >= 9]
    if premium_items:
        logger.info(
            "Re-running %d high-impact items with premium model",
            len(premium_items),
        )
        results = _rerun_premium(results, premium_items, commit_by_sha)

    # Deterministically apply extracted trailers AFTER the premium re-run,
    # supplementing (not replacing) any discussion_id_link / bugzilla_pr the
    # LLM already set.
    results = _apply_trailers(results, commit_by_sha)

    # Deterministic project + date override from the original RawCommit,
    # applied last so premium/cheap/stub paths all converge here.
    results = _override_from_raw(results, commit_by_sha)
    return _apply_series_and_subsystem(
        results, commits, parts_by_canonical_index
    )


def _apply_series_and_subsystem(
    results: list[LandingDigest],
    canonical_commits: list[RawCommit],
    parts_by_canonical_index: dict[int, list[dict]],
) -> list[LandingDigest]:
    """Force subsystem/headline sanity + attach series_parts.

    Runs after every other post-processing step so LLM output, stubs, and
    premium re-runs all converge on the same invariants.
    """
    by_sha: dict[str, RawCommit] = {c.sha: c for c in canonical_commits}
    # Map canonical-sha → parts pointers using the canonical list's ordering.
    parts_by_sha: dict[str, list[dict]] = {
        canonical_commits[i].sha: parts
        for i, parts in parts_by_canonical_index.items()
        if 0 <= i < len(canonical_commits)
    }

    fixed: list[LandingDigest] = []
    for d in results:
        raw = by_sha.get(d.commit_hash)
        patch: dict[str, object] = {}

        if raw is not None:
            first_line = (raw.message or "").splitlines()[0] if raw.message else ""
            # Never publish "unknown" — always derive deterministically.
            if not d.subsystem or d.subsystem.lower() in {"unknown", "general", ""}:
                patch["subsystem"] = extract_subsystem(
                    first_line, raw.diff_stat, raw.project
                )
            # Headline must not carry bracketed tags or "Re:".
            clean_hl = clean_subject(d.headline or first_line)
            if clean_hl and clean_hl != d.headline:
                patch["headline"] = clean_hl

            sid = series_id_for(first_line, raw.project)
            if sid:
                patch["series_id"] = sid
                tag = parse_patch_tag(first_line) or {}
                patch["outcome"] = Outcome.COMMITTED
                # n==0 → cover letter; else ``part``. Standalone items skipped.
                if tag.get("n") == 0:
                    pass  # cover letter; canonical by construction
            parts = parts_by_sha.get(d.commit_hash)
            if parts:
                patch["series_parts"] = parts

        if patch:
            d = d.model_copy(update=patch)
        fixed.append(d)
    return fixed


def _run_batch(
    agent: Agent[None, str],
    model_name: str,
    batch: list[RawCommit],
    batch_idx: int,
) -> list[LandingDigest]:
    """Run one batch through the LLM with retry + input/output correlation.

    Missing items (present in input, absent from LLM response) are filled in
    with stub digests so batches never silently shrink.
    """
    batch_projects = sorted({c.project for c in batch})
    prompt = (
        f"Digest the following {len(batch)} commit(s) "
        f"(projects: {', '.join(batch_projects)}). "
        f"Return a JSON array of LandingDigest objects. The ``commit_hash``, "
        f"``project`` and ``date`` fields MUST be taken verbatim from each input "
        f"item — preserve them exactly so each digest can be matched back.\n\n"
        + _render_batch(batch)
    )

    def _call():
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "\033[1;33m── landing_agent batch %d ▶ SENDING TO %s ──\n%s\033[0m",
                batch_idx, model_name, prompt,
            )
        r = agent.run_sync(prompt)
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "\033[1;32m── landing_agent batch %d ◀ RESPONSE FROM %s ──\n%s\033[0m",
                batch_idx, model_name, r.output,
            )
        items = _parse_landing_batch(r.output, batch=batch)
        if not items and batch:
            raise ValueError(f"Model returned 0 items for {len(batch)} input item(s)")
        return r, items

    global batches_total, batches_stubbed
    batches_total += 1
    try:
        result, data = retry_with_backoff(
            _call,
            label=f"landing_agent batch {batch_idx}",
        )
    except Exception as exc:
        logger.error(
            "landing_agent batch %d failed after retries: %s", batch_idx, exc
        )
        batches_stubbed += 1
        return _stub_digests(batch)

    append_usage("landing_agent", model_name, result.usage)
    data = list(data)
    logger.info(
        "Batch %d: %d digest(s), usage=%s",
        batch_idx, len(data), result.usage,
    )

    # Correlation: stub any input item the LLM failed to return.
    returned_shas = {d.commit_hash for d in data}
    missing = [raw for raw in batch if raw.sha not in returned_shas]
    if missing:
        logger.warning(
            "landing_agent batch %d: LLM omitted %d of %d items (shas=%s)",
            batch_idx, len(missing), len(batch), [m.sha for m in missing],
        )
        data.extend(_stub_digests(missing))

    # Correlation: drop hallucinated items the LLM invented.
    input_shas = {raw.sha for raw in batch}
    extra = [d for d in data if d.commit_hash not in input_shas]
    if extra:
        logger.warning(
            "landing_agent batch %d: LLM returned %d unknown shas=%s — dropping",
            batch_idx, len(extra), [d.commit_hash for d in extra],
        )
        data = [d for d in data if d.commit_hash in input_shas]

    return data


def _override_from_raw(
    digests: list[LandingDigest],
    commit_by_sha: dict[str, RawCommit],
) -> list[LandingDigest]:
    """Force ``project`` and ``date`` to match the originating RawCommit."""
    fixed: list[LandingDigest] = []
    for d in digests:
        raw = commit_by_sha.get(d.commit_hash)
        if raw is not None:
            d = d.model_copy(update={"project": raw.project, "date": raw.date})
        fixed.append(d)
    return fixed


def _apply_trailers(
    digests: list[LandingDigest],
    commit_by_sha: dict[str, RawCommit],
) -> list[LandingDigest]:
    """Backfill discussion_id_link + bugzilla_pr from extracted trailers.

    Only overwrites fields the LLM left unset (prefer LLM-set values).
    Bare-number references are namespaced so PR #123 on project A can't
    collide with PR #123 on project B.
    """
    updated: list[LandingDigest] = []
    for d in digests:
        original = commit_by_sha.get(d.commit_hash)
        if original is None:
            updated.append(d)
            continue

        trailers = _extract_trailers(original.message)
        patch: dict[str, object] = {}

        if d.discussion_id_link is None:
            raw_link = (
                trailers.get("message_id")
                or trailers.get("link")
                or trailers.get("closes")
                or trailers.get("pr")
            )
            if raw_link:
                patch["discussion_id_link"] = _namespace_ref(raw_link, original)

        if d.bugzilla_pr is None and "bugzilla" in trailers:
            try:
                patch["bugzilla_pr"] = int(trailers["bugzilla"])
            except ValueError:
                pass

        if patch:
            d = d.model_copy(update=patch)
        updated.append(d)
    return updated


def _rerun_premium(
    all_results: list[LandingDigest],
    high_impact: list[LandingDigest],
    commit_by_sha: dict[str, RawCommit],
) -> list[LandingDigest]:
    """Re-analyse high-impact items with the premium model.

    Uses the original RawCommit (full message + diff_stat), not the cheap
    LLM's summary — ensuring the premium model has at least as much context
    as the cheap one did. Wrapped in retry_with_backoff so a single 429 blip
    doesn't cost us the depth we paid for.
    """
    premium_model_name = os.environ.get("BENTO_MODEL", _PREMIUM_MODEL)
    premium_agent = _make_agent(premium_model_name)

    # Look up original commits; fall back to cheap result if SHA is missing.
    original_commits: list[RawCommit] = []
    for d in high_impact:
        original = commit_by_sha.get(d.commit_hash)
        if original:
            original_commits.append(original)
        else:
            logger.warning(
                "No original RawCommit for %s — skipping premium re-run",
                d.commit_hash,
            )

    if not original_commits:
        return all_results

    batch_projects = sorted({c.project for c in original_commits})
    prompt = (
        f"Re-analyse these {len(original_commits)} high-impact commit(s) "
        f"(projects: {', '.join(batch_projects)}) with greater depth. "
        f"Return a JSON array of LandingDigest. The ``commit_hash``, "
        f"``project`` and ``date`` fields MUST be echoed verbatim.\n\n"
        + _render_batch(original_commits)
    )

    logger.debug(
        "\033[1;35m── landing_agent premium: model=%s │ system prompt ──\n%s\033[0m",
        premium_model_name, _SYSTEM_PROMPT,
    )

    refined_by_sha: dict[str, LandingDigest] = {}
    try:
        def _premium_call():
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(
                    "\033[1;33m── landing_agent PREMIUM ▶ SENDING TO %s ──\n%s\033[0m",
                    premium_model_name, prompt,
                )
            r = premium_agent.run_sync(prompt)
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(
                    "\033[1;32m── landing_agent PREMIUM ◀ RESPONSE FROM %s ──\n%s\033[0m",
                    premium_model_name, r.output,
                )
            return r, _parse_landing_batch(r.output, batch=original_commits)

        result, refined_digests = retry_with_backoff(
            _premium_call,
            label="landing_agent premium rerun",
        )
        append_usage("landing_agent_premium", premium_model_name, result.usage)
        input_shas = {c.sha for c in original_commits}
        for refined in refined_digests:
            if refined.commit_hash not in input_shas:
                logger.warning(
                    "Premium model returned unknown commit_hash=%s — dropping",
                    refined.commit_hash,
                )
                continue
            refined_by_sha[refined.commit_hash] = refined
    except Exception as exc:
        logger.error("Premium re-run failed: %s — keeping cheap results", exc)

    return [refined_by_sha.get(d.commit_hash, d) for d in all_results]


def _stub_digests(items: list[RawCommit]) -> list[LandingDigest]:
    """Deterministic placeholders when the LLM path is skipped or fails.

    Every field the UI relies on is populated with a best-effort derivation so
    dry-run output still looks publishable in structure (even if the prose is
    thin).
    """
    out: list[LandingDigest] = []
    for c in items:
        first_line = (c.message or "").splitlines()[0] if c.message else ""
        headline = clean_subject(first_line) or c.sha[:12]
        subsystem = extract_subsystem(first_line, c.diff_stat, c.project)
        tldr = headline[:160] if headline else "Commit landed."
        out.append(
            LandingDigest(
                project=c.project,
                subsystem=subsystem,
                commit_hash=c.sha,
                source_type=c.source_type,
                author=c.author,
                headline=headline,
                tldr=tldr,
                summary="Summary unavailable — see source link.",
                url=c.url,
                date=c.date,
                is_stub=True,
            )
        )
    return out
