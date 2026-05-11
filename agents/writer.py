"""Writer — serialises DiscussionDigest and LandingDigest to Markdown files.

Output paths:
  web/src/content/discussions/YYYY-MM-DD-<slug>-<id_hash>.md
  web/src/content/landings/YYYY-MM-DD-<slug>.md

The discussion filename includes a 6-char SHA-1 hash of the discussion_id to
prevent slug collisions when two discussions share the same normalised title on
the same day (C15 fix).

Format: YAML frontmatter (all model fields) + blank line + summary prose body.
Slug: lowercase, non-word chars collapsed to single hyphens, stripped, max 80 chars.

Body validation: summary text is sanity-checked before being written. Obvious
LLM failures (truncated mid-word, quoted email lines, too short / too long)
are replaced with a visible fallback rather than shipped as-is — better a
known gap than a broken-looking article.
"""

from __future__ import annotations

import hashlib
import logging
import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

from agents.models.discussion import DiscussionDigest
from agents.models.landing import LandingDigest

logger = logging.getLogger(__name__)

_DEFAULT_DISCUSSION_DIR = Path("web/src/content/discussions")
_DEFAULT_LANDING_DIR = Path("web/src/content/landings")

_FALLBACK_BODY = "Summary unavailable — see source link."
_MIN_BODY_WORDS = 10
_MAX_BODY_WORDS = 260


# ---------------------------------------------------------------------------
# Slug helper
# ---------------------------------------------------------------------------

def _slugify(title: str) -> str:
    """Convert a title to a URL-safe slug (max 80 chars).

    ``re.ASCII`` forces ``\\w`` to match only [A-Za-z0-9_]; without it the
    Unicode default would keep accented/CJK characters, which break URL
    slugs and filesystem paths on non-UTF8 filesystems.
    """
    slug = title.lower()
    slug = re.sub(r"[^\w]+", "-", slug, flags=re.ASCII)
    return slug.strip("-")[:80]


def _format_date(dt: datetime) -> str:
    """Format a datetime as YYYY-MM-DD in UTC."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%d")


def _sanitise_body(body: str | None, *, context: str) -> str:
    """Validate and clean a summary body before writing it to disk.

    Reasons a body is rejected (replaced with the fallback string):
      - None / empty.
      - Starts with ``Re:``, ``>`` or ``On … wrote:`` (quoted email leak).
      - Ends mid-word / with dangling ``[`` or ``(`` (truncation).
      - Fewer than _MIN_BODY_WORDS or more than _MAX_BODY_WORDS words.
    """
    if not body:
        logger.info("writer: empty body in %s — using fallback", context)
        return _FALLBACK_BODY

    text = body.strip()
    if not text:
        logger.info("writer: whitespace-only body in %s — using fallback", context)
        return _FALLBACK_BODY

    # Body is already the stub fallback (stub-digest path). Skip the rest of
    # the validation so we don't emit a misleading "body too short" log for
    # something we deliberately set upstream.
    if text == _FALLBACK_BODY:
        return _FALLBACK_BODY

    first_line = text.splitlines()[0]
    if re.match(r"^\s*(re\s*:|>|On .+ wrote:)", first_line, re.IGNORECASE):
        logger.info("writer: quoted-email body in %s — using fallback", context)
        return _FALLBACK_BODY

    # Truncation detectors: trailing dangling bracket / open paren / comma /
    # hyphen, or ending mid-word (no terminal punctuation at all).
    tail = text[-3:]
    ends_dangling = tail.endswith(("[", "(", ",", "-", ":"))
    ends_mid_word = bool(re.search(r"\b[a-z]+$", tail.lower())) and not re.search(
        r"[.!?\"'\)]$", text
    )
    if ends_dangling or ends_mid_word:
        logger.info("writer: truncated body in %s — using fallback", context)
        return _FALLBACK_BODY

    word_count = len(re.findall(r"\S+", text))
    if word_count < _MIN_BODY_WORDS:
        logger.info(
            "writer: body too short (%d words) in %s — using fallback",
            word_count,
            context,
        )
        return _FALLBACK_BODY
    if word_count > _MAX_BODY_WORDS:
        logger.info(
            "writer: body too long (%d words) in %s — truncating to fallback",
            word_count,
            context,
        )
        return _FALLBACK_BODY

    return text


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

    # Use the discussion's own date so re-runs stay idempotent and the filename
    # reflects when the discussion actually happened, not when the job ran.
    date_str = _format_date(d.date)
    # Prefer the cleaned headline over the raw subject for the slug.
    slug = _slugify(d.headline or d.title)
    # Append a 6-char hash of discussion_id to guarantee uniqueness even when
    # two discussions share the same normalised title on the same day (C15).
    id_hash = hashlib.sha1(d.discussion_id.encode()).hexdigest()[:6]
    path = base / f"{date_str}-{slug}-{id_hash}.md"

    frontmatter: dict = {
        "project": d.project,
        "subsystem": d.subsystem,
        "patch_id": d.patch_id,
        "tags": list(d.tags),
        "discussion_id": d.discussion_id,
        "source_type": d.source_type,
        "title": d.title,
        "headline": d.headline,
        "tldr": d.tldr,
        "proposer": d.proposer,
        "consensus": d.consensus.value,
        "outcome": d.outcome.value,
        "impact_score": d.impact_score,
        "sentiment_score": d.sentiment_score,
        "technical_tradeoffs": d.technical_tradeoffs,
        "exchanges": [e.model_dump() for e in d.exchanges],
        "primer_expert": d.primer_expert,
        "primer_general": d.primer_general,
        "series_id": d.series_id,
        "series_role": d.series_role,
        "series_parts": d.series_parts,
        "url": d.url,
        "bugzilla_url": d.bugzilla_url,
        "date": date_str,
        "is_stub": d.is_stub,
    }

    body = _sanitise_body(d.summary, context=f"discussion {d.discussion_id}")
    path.write_text(_render(frontmatter, body), encoding="utf-8")
    return path


def write_landing(
    landing: LandingDigest,
    output_dir: Path | None = None,
) -> Path:
    """Write a LandingDigest to a Markdown file and return the path."""
    base = Path(output_dir) if output_dir else _DEFAULT_LANDING_DIR
    base.mkdir(parents=True, exist_ok=True)

    # Use the commit's own landing date so re-runs stay idempotent and the
    # filename reflects when the commit actually landed.
    date_str = _format_date(landing.date)
    slug = _slugify(landing.subsystem + "-" + landing.commit_hash[:8])
    path = base / f"{date_str}-{slug}.md"

    frontmatter: dict = {
        "project": landing.project,
        "subsystem": landing.subsystem,
        "patch_id": landing.patch_id,
        "tags": list(landing.tags),
        "commit_hash": landing.commit_hash,
        "source_type": landing.source_type,
        "author": landing.author,
        "headline": landing.headline,
        "tldr": landing.tldr,
        "impact_score": landing.impact_score,
        "performance_win": landing.performance_win,
        "breaking_change": landing.breaking_change,
        "outcome": landing.outcome.value,
        "primer_expert": landing.primer_expert,
        "primer_general": landing.primer_general,
        "discussion_id_link": landing.discussion_id_link,
        "bugzilla_pr": landing.bugzilla_pr,
        "series_id": landing.series_id,
        "series_parts": landing.series_parts,
        "url": landing.url,
        "date": date_str,
        "is_stub": landing.is_stub,
    }

    body = _sanitise_body(landing.summary, context=f"landing {landing.commit_hash}")
    path.write_text(_render(frontmatter, body), encoding="utf-8")
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
