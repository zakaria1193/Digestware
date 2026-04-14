"""Writer — serialises DiscussionDigest and LandingDigest to Markdown files.

Output paths:
  web/src/content/discussions/YYYY-MM-DD-<slug>-<id_hash>.md
  web/src/content/landings/YYYY-MM-DD-<slug>.md

The discussion filename includes a 6-char SHA-1 hash of the discussion_id to
prevent slug collisions when two discussions share the same normalised title on
the same day (C15 fix).

Format: YAML frontmatter (all model fields) + blank line + summary prose body.
Slug: lowercase, non-word chars collapsed to single hyphens, stripped, max 80 chars.
"""

from __future__ import annotations

import hashlib
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
    """Convert a title to a URL-safe slug (max 80 chars)."""
    slug = title.lower()
    slug = re.sub(r"[^\w]+", "-", slug)
    return slug.strip("-")[:80]


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
    # Append a 6-char hash of discussion_id to guarantee uniqueness even when
    # two discussions share the same normalised title on the same day (C15).
    id_hash = hashlib.sha1(d.discussion_id.encode()).hexdigest()[:6]
    path = base / f"{date_str}-{slug}-{id_hash}.md"

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
    landing: LandingDigest,
    output_dir: Path | None = None,
) -> Path:
    """Write a LandingDigest to a Markdown file and return the path."""
    base = Path(output_dir) if output_dir else _DEFAULT_LANDING_DIR
    base.mkdir(parents=True, exist_ok=True)

    date_str = _today()
    slug = _slugify(landing.subsystem + "-" + landing.commit_hash[:8])
    path = base / f"{date_str}-{slug}.md"

    frontmatter: dict = {
        "project": landing.project,
        "subsystem": landing.subsystem,
        "patch_id": landing.patch_id,
        "commit_hash": landing.commit_hash,
        "source_type": landing.source_type,
        "author": landing.author,
        "impact_score": landing.impact_score,
        "performance_win": landing.performance_win,
        "breaking_change": landing.breaking_change,
        "discussion_id_link": landing.discussion_id_link,
        "bugzilla_pr": landing.bugzilla_pr,
        "url": landing.url,
        "date": date_str,
    }

    path.write_text(_render(frontmatter, landing.summary), encoding="utf-8")
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
