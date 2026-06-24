"""OS Pulse — Phase 2 entry point.

Usage:
    python -m agents.main --since-hours 24 [--dry-run]

Steps:
1. Load .env
2. Parse agents/sources.yml → instantiate adapters
3. IngestionEngine.run(since_hours) → raw discussions + commits
4. Batch-run discussion agent
5. Batch-run landing agent
6. write_discussion() / write_landing() for each result
7. Tag categorizer → web/src/data/tag-categories/<project>.json
   (skipped with --skip-categorize; the workflow runs it once at the end)
8. Print summary
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path

import yaml
from dotenv import load_dotenv

from agents import discussion_agent as discussion_agent_module
from agents import landing_agent as landing_agent_module
from agents.adapters.github import GitHubAdapter
from agents.adapters.plain_git import PlainGitAdapter
from agents.adapters.public_inbox import PublicInboxAdapter
from agents.dedup import build_seen_index, filter_raw
from agents.discussion_agent import run_discussion_agent
from agents.ingestion.engine import IngestionEngine
from agents.landing_agent import run_landing_agent
from agents.tag_categorizer import run_tag_categorizer
from agents.tools.noise_filter import filter_noise
from agents.tools.retro_noise import sweep_content_root
from agents.writer import write_discussion, write_landing

logger = logging.getLogger("agents.main")

_ANSI_RESET = "\033[0m"
_STEP_COLORS = {
    "cyan":    "\033[1;36m",
    "magenta": "\033[1;35m",
    "blue":    "\033[1;34m",
    "green":   "\033[1;32m",
    "yellow":  "\033[1;33m",
}


def _step_banner(title: str, color: str = "cyan") -> str:
    """Return a multi-line colored ASCII banner for pipeline step headers."""
    code = _STEP_COLORS.get(color, _STEP_COLORS["cyan"])
    inner = 60
    bar = "═" * inner
    padded = title.upper().center(inner)
    return f"\n{code}╔{bar}╗\n║{padded}║\n╚{bar}╝{_ANSI_RESET}"

_SOURCES_YML = Path(__file__).parent / "sources.yml"
_CACHE_DIR = Path(__file__).parent / "cache"
_DEFAULT_CONTENT_ROOT = Path("web/src/content")
_DEFAULT_TAG_CATEGORIES_DIR = Path("web/src/data/tag-categories")


# ---------------------------------------------------------------------------
# Source factory
# ---------------------------------------------------------------------------

def _build_sources(
    config: dict,
) -> tuple[list, list]:
    """Parse sources.yml config and return (discussion_sources, commit_sources)."""
    discussion_sources: list = []
    commit_sources: list = []

    for entry in config.get("sources", []):
        src_type = entry.get("type")
        # `project` labels the output digests (e.g. "gcc", "glibc", "linux").
        # For public_inbox there can be several mailing lists per adapter, so a
        # per-list mapping is also accepted.
        project = entry.get("project", "unknown")
        list_projects = entry.get("list_projects") or {}
        if src_type == "github":
            adapter = GitHubAdapter(
                owner=entry["owner"],
                repo=entry["repo"],
                project=project,
            )
            discussion_sources.append(adapter)
            commit_sources.append(adapter)

        elif src_type == "public_inbox":
            adapter = PublicInboxAdapter(
                discussion_lists=entry.get("discussion_lists", []),
                cvs_lists=entry.get("cvs_lists", []),
                cache_dir=_CACHE_DIR,
                use_nntp=entry.get("use_nntp", True),
                project=project,
                list_projects=list_projects,
            )
            discussion_sources.append(adapter)
            commit_sources.append(adapter)

        elif src_type == "plain_git":
            adapter = PlainGitAdapter(
                repo_url=entry["url"],
                branch=entry.get("branch", "master"),
                cache_dir=_CACHE_DIR,
                project=project,
            )
            commit_sources.append(adapter)

        else:
            logger.warning("Unknown source type %r — skipping", src_type)

    return discussion_sources, commit_sources


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(description="OS Pulse digest engine")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable DEBUG-level logging (shows prompts, API payloads, raw LLM responses)",
    )
    parser.add_argument(
        "--since-hours",
        type=int,
        default=24,
        help="How many hours back to fetch (default: 24)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Skip LLM calls; write stub digests (for testing pipeline wiring)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reprocess items even if their output Markdown already exists",
    )
    parser.add_argument(
        "--content-root",
        type=Path,
        default=_DEFAULT_CONTENT_ROOT,
        help=f"Output content root (default: {_DEFAULT_CONTENT_ROOT})",
    )
    parser.add_argument(
        "--project",
        type=str,
        default=None,
        help="Only process items whose project matches (e.g. 'gcc'). "
        "Applied after ingestion, before LLM batches.",
    )
    parser.add_argument(
        "--max-discussions",
        type=int,
        default=None,
        help="Cap the number of discussions kept after filtering (newest first).",
    )
    parser.add_argument(
        "--max-landings",
        type=int,
        default=None,
        help="Cap the number of commits kept after filtering (newest first).",
    )
    parser.add_argument(
        "--skip-categorize",
        action="store_true",
        help="Skip the tag-categorizer step. Intended for the backfill loop "
        "in daily-digest.yml where main.py is re-invoked across widening "
        "windows; the workflow then runs categorization once at the end.",
    )
    parser.add_argument(
        "--tag-categories-dir",
        type=Path,
        default=_DEFAULT_TAG_CATEGORIES_DIR,
        help=f"Output dir for tag-category JSON (default: {_DEFAULT_TAG_CATEGORIES_DIR})",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S",
    )

    # Refuse to run the LLM pipeline without a key — otherwise every batch
    # silently falls back to stub digests and we commit them as if they were
    # real output. --dry-run is still supported for pipeline-wiring tests.
    if not args.dry_run and not os.environ.get("OPENROUTER_API_KEY"):
        logger.error(
            "OPENROUTER_API_KEY is not set. Refusing to run the LLM pipeline "
            "— use --dry-run if you intend to emit stub digests."
        )
        return 2

    # Reset fall-through counters so multiple main() calls in one process
    # (tests, notebooks) don't accumulate.
    discussion_agent_module.batches_stubbed = 0
    discussion_agent_module.batches_total = 0
    landing_agent_module.batches_stubbed = 0
    landing_agent_module.batches_total = 0

    # Load sources config
    try:
        with _SOURCES_YML.open() as fh:
            config = yaml.safe_load(fh)
    except FileNotFoundError:
        logger.error("sources.yml not found at %s", _SOURCES_YML)
        return 1

    discussion_sources, commit_sources = _build_sources(config)
    logger.info(
        "Loaded %d discussion source(s), %d commit source(s)",
        len(discussion_sources),
        len(commit_sources),
    )

    # Retro-apply the noise filter to already-published markdown so entries
    # that became "noise" by today's stricter rules get hidden from the
    # public site without needing a one-shot migration. Runs every night
    # regardless of whether new data was ingested.
    logger.info(_step_banner("STEP 0 — RETRO NOISE SWEEP", "cyan"))
    retro_counts = sweep_content_root(args.content_root)
    if retro_counts["total"]:
        logger.info(
            "Retro noise sweep marked %d file(s) as stub "
            "(title-noise=%d, spam=%d, bot-author=%d, low-score=%d)",
            retro_counts["total"],
            retro_counts["title-noise"],
            retro_counts["spam"],
            retro_counts["bot-author"],
            retro_counts.get("low-score", 0),
        )
    else:
        logger.info("Retro noise sweep: nothing to mark.")

    # Ingest
    logger.info(_step_banner("STEP 1 — INGESTION", "cyan"))
    engine = IngestionEngine(discussion_sources, commit_sources)
    raw = engine.run(since_hours=args.since_hours)
    raw_discussions = raw["discussions"]
    raw_commits = raw["commits"]
    logger.info(
        "Ingested %d discussions, %d commits", len(raw_discussions), len(raw_commits)
    )
    if logger.isEnabledFor(logging.DEBUG):
        for d in raw_discussions:
            logger.debug(
                "  [discussion] id=%-40s project=%-12s title=%.80s",
                d.id, d.project, d.title,
            )
        for c in raw_commits:
            logger.debug(
                "  [commit]     sha=%-12s project=%-12s msg=%.80s",
                c.sha[:12], c.project, (c.message or "").splitlines()[0],
            )

    if not raw_discussions and not raw_commits:
        logger.info("Nothing to process — exiting")
        return 0

    # Drop routine-maintenance noise ("Daily bump.", empty pings) BEFORE the
    # LLM pays attention to it. Cheap deterministic rules only.
    raw_discussions, raw_commits, dropped_d, dropped_c = filter_noise(
        raw_discussions, raw_commits
    )
    if dropped_d or dropped_c:
        logger.info(
            "Noise filter dropped %d discussion(s), %d commit(s)",
            dropped_d,
            dropped_c,
        )

    # Skip items already on disk (unless --force). This happens BEFORE the LLM
    # batches so re-runs of overlapping windows don't burn tokens.
    skipped_discussions = skipped_commits = 0
    if not args.force:
        seen_ids, seen_shas, seen_series = build_seen_index(args.content_root)
        raw_discussions, raw_commits, skipped_discussions, skipped_commits = (
            filter_raw(
                raw_discussions,
                raw_commits,
                seen_ids,
                seen_shas,
                seen_series,
            )
        )
        if skipped_discussions or skipped_commits:
            logger.info(
                "Skipped %d already-processed discussion(s), %d commit(s)",
                skipped_discussions,
                skipped_commits,
            )
        if not raw_discussions and not raw_commits:
            logger.info("Nothing new to process — exiting")
            return 0

    # Project filter + hard caps (limited mode, e.g. "gcc 5+5").
    if args.project:
        before_d, before_c = len(raw_discussions), len(raw_commits)
        raw_discussions = [d for d in raw_discussions if d.project == args.project]
        raw_commits = [c for c in raw_commits if c.project == args.project]
        logger.info(
            "Project filter %r: %d→%d discussions, %d→%d commits",
            args.project,
            before_d,
            len(raw_discussions),
            before_c,
            len(raw_commits),
        )

    if args.max_discussions is not None and len(raw_discussions) > args.max_discussions:
        raw_discussions.sort(key=lambda d: d.date, reverse=True)
        raw_discussions = raw_discussions[: args.max_discussions]
        logger.info("Capped discussions at %d (newest first)", args.max_discussions)

    if args.max_landings is not None and len(raw_commits) > args.max_landings:
        raw_commits.sort(key=lambda c: c.date, reverse=True)
        raw_commits = raw_commits[: args.max_landings]
        logger.info("Capped commits at %d (newest first)", args.max_landings)

    if not raw_discussions and not raw_commits:
        logger.info("Nothing left after project/cap filters — exiting")
        return 0

    # Run agents
    logger.info(_step_banner("STEP 2 — DISCUSSION AGENT", "magenta"))
    discussions = run_discussion_agent(
        raw_discussions, dry_run=args.dry_run
    )

    logger.info(_step_banner("STEP 3 — LANDING AGENT", "blue"))
    landings = run_landing_agent(raw_commits, dry_run=args.dry_run)

    # Mark cosmetic/typo/docs landings (score 1–3) as stubs so they are
    # written to disk (admin-visible) but hidden from the public site.
    # Dropping them outright would make the admin blind to over-filtering.
    _MIN_LANDING_SCORE = 4
    noise_filtered = sum(
        1 for ld in landings
        if ld.impact_score is not None and ld.impact_score < _MIN_LANDING_SCORE
    )
    if noise_filtered:
        logger.info(
            "Score floor (< %d) noise-filtered %d landing(s) → written as stubs",
            _MIN_LANDING_SCORE,
            noise_filtered,
        )
    landings = [
        ld.model_copy(update={"is_stub": True, "stub_reason": "low_score"})
        if (ld.impact_score is not None and ld.impact_score < _MIN_LANDING_SCORE)
        else ld
        for ld in landings
    ]

    # Write output
    logger.info(_step_banner("STEP 4 — WRITER", "green"))
    written_discussions = 0
    for d in discussions:
        try:
            path = write_discussion(d)
            logger.debug("Wrote discussion → %s", path)
            written_discussions += 1
        except Exception as exc:
            logger.warning("Failed to write discussion %s: %s", d.discussion_id, exc)

    written_landings = 0
    for landing in landings:
        try:
            path = write_landing(landing)
            logger.debug("Wrote landing → %s", path)
            written_landings += 1
        except Exception as exc:
            logger.warning(
                "Failed to write landing %s: %s", landing.commit_hash, exc
            )

    # Tag categorizer — rescans the on-disk content and emits per-project
    # category JSONs consumed by the filter bar. Best-effort: failures never
    # fail the whole pipeline.
    if args.skip_categorize:
        logger.info("Skipping tag categorizer (--skip-categorize).")
    else:
        logger.info(_step_banner("STEP 5 — TAG CATEGORIZER", "yellow"))
        try:
            run_tag_categorizer(
                args.content_root,
                args.tag_categories_dir,
                dry_run=args.dry_run,
            )
        except Exception as exc:
            logger.warning("Tag categorizer raised (%s) — continuing.", exc)

    # Summary
    bento_worthy = sum(1 for landing in landings if landing.impact_score is not None and landing.impact_score >= 7)
    d_stubbed = discussion_agent_module.batches_stubbed
    d_total = discussion_agent_module.batches_total
    l_stubbed = landing_agent_module.batches_stubbed
    l_total = landing_agent_module.batches_total
    total_batches = d_total + l_total
    total_stubbed = d_stubbed + l_stubbed
    print(
        f"\n{'─'*60}\n"
        f"  Discussions written : {written_discussions}\n"
        f"  Landings written    : {written_landings}\n"
        f"  Skipped (dedup)     : {skipped_discussions} discussions, "
        f"{skipped_commits} commits\n"
        f"  Bento-worthy (≥7)   : {bento_worthy}\n"
        f"  LLM fallbacks       : {total_stubbed} / {total_batches} batches\n"
        f"{'─'*60}"
    )

    # If every LLM batch fell back, treat the run as a failure rather than
    # committing stub content as if it were real digest output. dry-run and
    # no-batch runs (total_batches == 0) are exempt.
    if not args.dry_run and total_batches > 0 and total_stubbed == total_batches:
        logger.error(
            "Every LLM batch (%d) fell back to stub digests — refusing to "
            "report success. Check agent logs for the underlying error "
            "(likely auth/rate-limit/network).",
            total_batches,
        )
        return 3

    return 0


if __name__ == "__main__":
    sys.exit(main())
