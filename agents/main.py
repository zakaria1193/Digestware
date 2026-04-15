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
7. Print summary
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import yaml
from dotenv import load_dotenv

from agents.adapters.github import GitHubAdapter
from agents.adapters.plain_git import PlainGitAdapter
from agents.adapters.public_inbox import PublicInboxAdapter
from agents.discussion_agent import run_discussion_agent
from agents.ingestion.engine import IngestionEngine
from agents.landing_agent import run_landing_agent
from agents.writer import write_discussion, write_landing

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("agents.main")

_SOURCES_YML = Path(__file__).parent / "sources.yml"
_CACHE_DIR = Path(__file__).parent / "cache"


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
    args = parser.parse_args()

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

    # Ingest
    engine = IngestionEngine(discussion_sources, commit_sources)
    raw = engine.run(since_hours=args.since_hours)
    raw_discussions = raw["discussions"]
    raw_commits = raw["commits"]
    logger.info(
        "Ingested %d discussions, %d commits", len(raw_discussions), len(raw_commits)
    )

    if not raw_discussions and not raw_commits:
        logger.info("Nothing to process — exiting")
        return 0

    # Run agents
    discussions = run_discussion_agent(
        raw_discussions, dry_run=args.dry_run
    )
    landings = run_landing_agent(raw_commits, dry_run=args.dry_run)

    # Write output
    written_discussions = 0
    for d in discussions:
        try:
            path = write_discussion(d)
            logger.debug("Wrote discussion → %s", path)
            written_discussions += 1
        except Exception as exc:
            logger.warning("Failed to write discussion %s: %s", d.discussion_id, exc)

    written_landings = 0
    for l in landings:
        try:
            path = write_landing(l)
            logger.debug("Wrote landing → %s", path)
            written_landings += 1
        except Exception as exc:
            logger.warning("Failed to write landing %s: %s", l.commit_hash, exc)

    # Summary
    bento_worthy = sum(1 for l in landings if l.impact_score >= 7)
    print(
        f"\n{'─'*60}\n"
        f"  Discussions written : {written_discussions}\n"
        f"  Landings written    : {written_landings}\n"
        f"  Bento-worthy (≥7)   : {bento_worthy}\n"
        f"{'─'*60}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
