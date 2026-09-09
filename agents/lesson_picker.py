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

**One lesson per week TOTAL, alternating projects.** Not one per project —
the article is written by a premium model and volume is the dominant cost
lever, so gcc and binutils take turns. Whose turn it is falls out of the
calendar (``project_for_week``), and the "already done this week" check is
therefore scoped to the week rather than to the project.

The one non-local input is the source repo: a commit is only a viable subject
if its SHA actually resolves in the mirror. Mirror lag is routine, so the
picker walks the ranked list and takes the first commit it can actually read.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field, replace
from datetime import date, timedelta
from pathlib import Path

from agents.lesson_topics import rejection_reason
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


def project_for_week(week: LessonWeek, projects: list[str]) -> str | None:
    """Whose turn it is this week, rotating stably forever.

    Keyed on the Monday's ordinal rather than ``iso_week``: a naive
    ``iso_week % n`` hands two consecutive weeks to the same project whenever a
    52-week year rolls into week 1, because 52 and 1 are both even/odd in the
    same way. Counting weeks since the epoch has no such seam.

    Deterministic and stateless, so the rotation cannot drift and does not need
    to be recorded anywhere. ``projects`` must be in a stable order — the
    caller passes ``sorted()`` output for that reason.
    """
    if not projects:
        return None
    return projects[(week.start.toordinal() // 7) % len(projects)]


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
        # A stub is a record of a FAILED run, not a lesson. Counting it as one
        # would let a single bad night burn that week permanently — which is
        # exactly the opposite of the self-healing the nightly cadence needs.
        if fm and not fm.get("is_stub") and fm.get("lesson_id") == lesson_id:
            return True
    return False


def existing_lesson_for_week(content_root: Path, week: LessonWeek) -> str | None:
    """The project that already has this week's lesson, or None.

    Week-scoped rather than project-scoped because there is only ONE lesson a
    week across all projects. Asking "does gcc have this week's lesson?" would
    let binutils write a second one the same week and double the bill.
    """
    lessons_dir = Path(content_root) / "lessons"
    if not lessons_dir.is_dir():
        return None
    suffix = f":{week.key}"
    for path in sorted(lessons_dir.glob("*.md")):
        fm = _read_frontmatter(path)
        if not fm:
            continue
        if fm.get("is_stub"):
            continue        # a failed run never claims the week — see above
        lesson_id = fm.get("lesson_id")
        if isinstance(lesson_id, str) and lesson_id.endswith(suffix):
            project = fm.get("project")
            return str(project) if project else lesson_id.split(":", 1)[0]
    return None


def recent_subsystems(content_root: Path, project: str) -> set[str]:
    """Subsystems covered by this project's last few lessons."""
    subs: set[str] = set()
    published = [
        fm for fm in _lesson_frontmatters(content_root, project)
        if not fm.get("is_stub")
    ]
    for fm in published[:_SUBSYSTEM_MEMORY_LESSONS]:
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

        # Editorial remit: no niche front ends, no obscure architectures, no
        # process churn. See agents/lesson_topics.py — a high impact score is
        # not the same as being worth teaching.
        unfit = rejection_reason(fm.get("subsystem"), tags)
        if unfit is not None:
            logger.debug(
                "lesson_picker: skipping %s — %s", path.name, unfit
            )
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


def _first_resolvable(
    subjects: list[LessonSubject], project: str, resolve
) -> LessonSubject | None:
    """The first subject whose SHA the clone actually has, or None."""
    for subject in subjects:
        if resolve is None or resolve(subject.commit_hash):
            return subject
        logger.info(
            "lesson_picker: %s not in the %s clone — trying the next candidate",
            subject.commit_hash[:12],
            project,
        )
    return None


def pick_subject(
    content_root: Path,
    project: str,
    week: LessonWeek,
    resolve=None,
    fallback_weeks: int = 0,
) -> LessonSubject | None:
    """Return the best landing to teach for *week*, or None.

    Args:
        resolve: optional ``(sha) -> bool`` — typically ``SourceRepo.resolve``.
            Candidates whose SHA is not yet in the mirror are skipped rather
            than failed, since mirror lag is expected.
        fallback_weeks: how many earlier weeks to search when *week* has
            candidates but the clone holds none of them. Pass this when the
            clone is known to be stale (``SourceRepo.is_stale``); see the note
            below.

    **The stale-clone fallback.** When ``git fetch`` fails, the clone on disk
    still holds the project's whole history up to the last successful fetch —
    everything except the newest commits. Filtering this week's candidates
    through ``resolve`` then rejects all of them and the week produces nothing,
    even though there is a perfectly readable repository sitting right there.
    ``fallback_weeks`` walks backwards until it finds a commit the clone does
    have, so an unreachable mirror costs freshness rather than the whole
    article.

    Two boundaries are deliberate:

    * It triggers **only when the target week had candidates that failed to
      resolve** — never on a week with nothing eligible. An empty week is a
      quiet week, and reaching into the past to fill it would be dishonest.
    * The returned subject is **rebased onto the target week**. The lesson is
      still this week's lesson: its ``lesson_id``, week range and sort date all
      name *week*, and only ``commit_date`` reveals the subject is older. If
      the identity moved with the subject, the weekly "already done" guard
      would stop matching and the step would rewrite — and re-bill — the lesson
      every single night.
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

    subject = _first_resolvable(ranked, project, resolve)
    if subject is not None:
        return subject

    if fallback_weeks <= 0:
        logger.warning(
            "lesson_picker: none of the %d %s candidate(s) for %s resolve in the "
            "clone — no lesson this week",
            len(ranked),
            project,
            week.key,
        )
        return None

    earlier = week
    for _ in range(fallback_weeks):
        earlier = week_of(earlier.start - timedelta(days=7))
        older = candidates(content_root, project, earlier)
        if not older:
            continue
        subject = _first_resolvable(older, project, resolve)
        if subject is None:
            continue
        logger.warning(
            "lesson_picker: the %s clone has none of %s's commits — teaching "
            "%s from %s instead. The lesson is still filed under %s.",
            project,
            week.key,
            subject.commit_hash[:12],
            earlier.key,
            week.key,
        )
        # Rebased onto the target week on purpose — see the docstring.
        return replace(subject, week=week)

    logger.warning(
        "lesson_picker: nothing in the last %d week(s) resolves in the %s "
        "clone — no lesson for %s",
        fallback_weeks + 1,
        project,
        week.key,
    )
    return None
