"""Pick the commit that this week's Lesson of the Week will teach.

Deterministic on purpose — no LLM. Choosing the subject is a ranking problem
over data we already have on disk (impact score, which subsystems recent
lessons already covered, recency), and paying a model to do it would burn
budget that is better spent on the lesson itself.

**The window is an ISO week, and always the most recent COMPLETE one.** A
nightly job that targeted the current week would run at 02:00 on Monday and
choose from a pool of roughly nothing. Targeting the previous Monday–Sunday
means every run picks from a full seven days of landed commits.

That also makes the weekly cadence self-enforcing without a calendar check:
the first nightly run of a new week writes the lesson, and the other six find
it already on disk and skip. It is self-healing for free — if Monday's run
fails, Tuesday's picks the same week up.

The one non-local input is the source repo: a commit is only a viable subject
if its SHA actually resolves in the mirror. Mirror lag is routine, so the
picker walks the ranked list and takes the first commit it can actually read.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

from agents.tools.frontmatter import load_frontmatter

logger = logging.getLogger(__name__)

# How many previous lessons to consider when spreading coverage across
# subsystems. Four is roughly a month at one lesson a week — long enough to
# stop the feed camping on gcc/testsuite, short enough that a genuinely busy
# subsystem can come back around. (A day-count, which is what the daily
# version used, is meaningless at this cadence.)
_SUBSYSTEM_MEMORY_LESSONS = 4

# Landings scoring below this are never worth a long-form piece. Higher than
# the daily version's floor of 5: a week's worth of candidates means we can
# afford to be pickier about what earns a lesson.
_MIN_SUBJECT_SCORE = 6

_WEEK_RE = re.compile(r"^(\d{4})-[Ww](\d{1,2})$")


# ---------------------------------------------------------------------------
# The week
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class LessonWeek:
    """One ISO week (Monday–Sunday), the unit a lesson covers."""

    iso_year: int
    iso_week: int
    start: date          # Monday
    end: date            # Sunday

    @property
    def key(self) -> str:
        """The ``2026-W36`` form used in ``lesson_id`` and on the CLI."""
        return f"{self.iso_year}-W{self.iso_week:02d}"

    def contains(self, d: date) -> bool:
        return self.start <= d <= self.end

    def __str__(self) -> str:
        return f"{self.key} ({self.start.isoformat()}..{self.end.isoformat()})"


def week_of(d: date) -> LessonWeek:
    """The ISO week containing *d*."""
    iso_year, iso_week, iso_weekday = d.isocalendar()
    monday = d - timedelta(days=iso_weekday - 1)
    return LessonWeek(
        iso_year=iso_year,
        iso_week=iso_week,
        start=monday,
        end=monday + timedelta(days=6),
    )


def previous_complete_week(today: date) -> LessonWeek:
    """The most recent ISO week that has fully elapsed before *today*.

    Note this is week-based, not a rolling 7 days: on a Sunday it still returns
    the week that ended *last* Sunday, because the current week is not over.
    Sunday's own landings are covered by next week's lesson.
    """
    this_monday = today - timedelta(days=today.isocalendar()[2] - 1)
    return week_of(this_monday - timedelta(days=1))


def parse_week(text: str) -> LessonWeek | None:
    """Parse a ``2026-W36`` CLI argument into a LessonWeek."""
    m = _WEEK_RE.match((text or "").strip())
    if not m:
        return None
    iso_year, iso_week = int(m.group(1)), int(m.group(2))
    try:
        monday = date.fromisocalendar(iso_year, iso_week, 1)
    except ValueError:
        return None
    return LessonWeek(
        iso_year=iso_year,
        iso_week=iso_week,
        start=monday,
        end=monday + timedelta(days=6),
    )


# ---------------------------------------------------------------------------
# Candidates
# ---------------------------------------------------------------------------

@dataclass
class LessonSubject:
    """One candidate commit, flattened from a landing article's frontmatter."""

    commit_hash: str
    project: str
    subsystem: str
    headline: str
    tldr: str
    url: str
    source_type: str
    commit_date: date
    week: LessonWeek
    impact_score: int | None = None
    patch_id: str | None = None
    tags: list[str] = field(default_factory=list)
    landing_slug: str | None = None   # Astro entry id, for the back-link

    @property
    def lesson_id(self) -> str:
        return f"{self.project}:{self.week.key}"


def _read_frontmatter(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        logger.debug("lesson_picker: cannot read %s: %s", path, exc)
        return None
    parsed = load_frontmatter(text)
    if parsed is None:
        logger.debug("lesson_picker: malformed frontmatter in %s", path)
        return None
    return parsed[0]


def _coerce_date(value: object) -> date | None:
    """Frontmatter dates are day-granular; accept date, datetime or ISO text."""
    from datetime import datetime as _dt

    if isinstance(value, _dt):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value.strip()[:10])
        except ValueError:
            return None
    return None


def latest_landing_date(content_root: Path, project: str | None = None) -> date | None:
    """Newest date across the landings on disk.

    Deliberately landings-only (``dedup.latest_content_date`` also counts
    discussions): a lesson teaches something that *merged*, so this anchors on
    the newest day that actually has landed commits.
    """
    landings_dir = Path(content_root) / "landings"
    if not landings_dir.is_dir():
        return None
    latest: date | None = None
    for path in landings_dir.glob("*.md"):
        fm = _read_frontmatter(path)
        if not fm:
            continue
        if project and fm.get("project") != project:
            continue
        d = _coerce_date(fm.get("date"))
        if d is not None and (latest is None or d > latest):
            latest = d
    return latest


def _lesson_frontmatters(content_root: Path, project: str) -> list[dict]:
    """Frontmatter of every lesson on disk for *project*, newest first."""
    lessons_dir = Path(content_root) / "lessons"
    if not lessons_dir.is_dir():
        return []
    found: list[tuple[date, dict]] = []
    for path in lessons_dir.glob("*.md"):
        fm = _read_frontmatter(path)
        if not fm or fm.get("project") != project:
            continue
        d = _coerce_date(fm.get("date")) or date.min
        found.append((d, fm))
    found.sort(key=lambda pair: pair[0], reverse=True)
    return [fm for _, fm in found]


def existing_lesson_id(content_root: Path, lesson_id: str) -> bool:
    """True when a lesson with this ``lesson_id`` is already on disk.

    Matches on frontmatter rather than the filename so the check survives a
    change to the file-naming scheme, and so a re-slugged headline can never
    produce a duplicate lesson for the same week.
    """
    lessons_dir = Path(content_root) / "lessons"
    if not lessons_dir.is_dir():
        return False
    for path in lessons_dir.glob("*.md"):
        fm = _read_frontmatter(path)
        if fm and fm.get("lesson_id") == lesson_id:
            return True
    return False


def recent_subsystems(content_root: Path, project: str) -> set[str]:
    """Subsystems covered by this project's last few lessons."""
    subs: set[str] = set()
    for fm in _lesson_frontmatters(content_root, project)[:_SUBSYSTEM_MEMORY_LESSONS]:
        sub = fm.get("subsystem")
        if isinstance(sub, str) and sub:
            subs.add(sub)
    return subs


def candidates(
    content_root: Path, project: str, week: LessonWeek
) -> list[LessonSubject]:
    """Publishable landings for this project in this week, ranked best-first.

    Ranking, in order:
      1. Higher impact score. With a week's pool (~10x a day's) the standout
         commit is usually genuinely worth more than a rotation preference —
         the daily version led with rotation, which was right for a pool of
         five and wrong for a pool of fifty.
      2. A subsystem the last few lessons haven't covered.
      3. Newer.
    """
    landings_dir = Path(content_root) / "landings"
    if not landings_dir.is_dir():
        return []

    covered = recent_subsystems(content_root, project)
    subjects: list[LessonSubject] = []

    for path in sorted(landings_dir.glob("*.md")):
        fm = _read_frontmatter(path)
        if not fm or fm.get("project") != project:
            continue

        landed = _coerce_date(fm.get("date"))
        if landed is None or not week.contains(landed):
            continue

        # Mirror the public-site visibility rules (web/src/lib/visibility.ts):
        # stubs and spam are admin-only and must never become a lesson.
        if fm.get("is_stub"):
            continue
        tags = fm.get("tags") or []
        if not isinstance(tags, list):
            tags = []
        if "spam" in tags:
            continue

        score = fm.get("impact_score")
        score = score if isinstance(score, int) else None
        if score is not None and score < _MIN_SUBJECT_SCORE:
            continue

        commit_hash = fm.get("commit_hash")
        if not isinstance(commit_hash, str) or not commit_hash:
            continue

        subjects.append(
            LessonSubject(
                commit_hash=commit_hash,
                project=project,
                subsystem=str(fm.get("subsystem") or "unknown"),
                headline=str(fm.get("headline") or ""),
                tldr=str(fm.get("tldr") or ""),
                url=str(fm.get("url") or ""),
                source_type=str(fm.get("source_type") or "plain_git"),
                commit_date=landed,
                week=week,
                impact_score=score,
                patch_id=fm.get("patch_id") if isinstance(fm.get("patch_id"), str) else None,
                tags=[t for t in tags if isinstance(t, str)],
                landing_slug=path.stem,
            )
        )

    subjects.sort(
        key=lambda s: (
            -(s.impact_score or 0),
            s.subsystem in covered,      # False (novel) sorts first
            -s.commit_date.toordinal(),
            s.headline,                  # stable tiebreak
        )
    )
    return subjects


def pick_subject(
    content_root: Path,
    project: str,
    week: LessonWeek,
    resolve=None,
) -> LessonSubject | None:
    """Return the best landing to teach for *week*, or None.

    Args:
        resolve: optional ``(sha) -> bool`` — typically ``SourceRepo.resolve``.
            Candidates whose SHA is not yet in the mirror are skipped rather
            than failed, since mirror lag is expected.
    """
    lesson_id = f"{project}:{week.key}"
    if existing_lesson_id(content_root, lesson_id):
        logger.info(
            "lesson_picker: %s already has a lesson for %s — skipping",
            project,
            week.key,
        )
        return None

    ranked = candidates(content_root, project, week)
    if not ranked:
        logger.info("lesson_picker: no eligible %s landings in %s", project, week)
        return None

    for subject in ranked:
        if resolve is None or resolve(subject.commit_hash):
            return subject
        logger.info(
            "lesson_picker: %s not in the %s mirror yet — trying the next candidate",
            subject.commit_hash[:12],
            project,
        )

    logger.warning(
        "lesson_picker: none of the %d %s candidate(s) for %s resolve in the "
        "mirror — no lesson this week",
        len(ranked),
        project,
        week.key,
    )
    return None
