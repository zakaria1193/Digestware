"""Writer — serialises DiscussionDigest and LandingDigest to Markdown files.

Output paths:
  web/src/content/discussions/YYYY-MM-DD-<slug>.md
  web/src/content/landings/YYYY-MM-DD-<slug>.md

Format: YAML frontmatter (all model fields) + blank line + summary prose body.
Slug: lowercase, non-word chars collapsed to single hyphens, stripped.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

from agents.models.discussion import DiscussionDigest
from agents.models.landing import LandingDigest

_DEFAULT_DISCUSSION_DIR = Path("web/src/content/discussions")
_DEFAULT_LANDING_DIR = Path("web/src/content/landings")


# ---------------------------------------------------------------------------
# Slug helper
# ---------------------------------------------------------------------------

def _slugify(title: str) -> str:
    """Convert a title to a URL-safe slug."""
    slug = title.lower()
    slug = re.sub(r"[^\w]+", "-", slug)
    return slug.strip("-")[:80]  # cap length


def _today() -> str:
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def write_discussion(
    d: DiscussionDigest,
    output_dir: Path | None = None,
) -> Path:
    """Write a DiscussionDigest to a Markdown file and return the path."""
    base = Path(output_dir) if output_dir else _DEFAULT_DISCUSSION_DIR
    base.mkdir(parents=True, exist_ok=True)

    date_str = _today()
    slug = _slugify(d.title)
    path = base / f"{date_str}-{slug}.md"

    frontmatter: dict = {
        "project": d.project,
        "subsystem": d.subsystem,
        "patch_id": d.patch_id,
        "discussion_id": d.discussion_id,
        "source_type": d.source_type,
        "title": d.title,
        "proposer": d.proposer,
        "consensus": d.consensus.value,
        "sentiment_score": d.sentiment_score,
        "technical_tradeoffs": d.technical_tradeoffs,
        "url": d.url,
        "bugzilla_url": d.bugzilla_url,
        "date": date_str,
    }

    path.write_text(_render(frontmatter, d.summary), encoding="utf-8")
    return path


def write_landing(
    l: LandingDigest,
    output_dir: Path | None = None,
) -> Path:
    """Write a LandingDigest to a Markdown file and return the path."""
    base = Path(output_dir) if output_dir else _DEFAULT_LANDING_DIR
    base.mkdir(parents=True, exist_ok=True)

    date_str = _today()
    slug = _slugify(l.subsystem + "-" + l.commit_hash[:8])
    path = base / f"{date_str}-{slug}.md"

    frontmatter: dict = {
        "project": l.project,
        "subsystem": l.subsystem,
        "patch_id": l.patch_id,
        "commit_hash": l.commit_hash,
        "source_type": l.source_type,
        "author": l.author,
        "impact_score": l.impact_score,
        "performance_win": l.performance_win,
        "breaking_change": l.breaking_change,
        "discussion_id_link": l.discussion_id_link,
        "bugzilla_pr": l.bugzilla_pr,
        "url": l.url,
        "date": date_str,
    }

    path.write_text(_render(frontmatter, l.summary), encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _render(frontmatter: dict, body: str) -> str:
    fm_str = yaml.dump(
        frontmatter,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    )
    return f"---\n{fm_str}---\n\n{body}\n"
