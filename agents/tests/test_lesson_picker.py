"""Tests for weekly lesson subject selection.

Two areas carry real risk:

1. **ISO week arithmetic.** Year boundaries are where week logic goes wrong —
   Jan 1 can belong to the previous ISO year, and a naive "seven days back"
   drifts. The target is always the most recent *complete* week, never the
   current one (which on a Monday-morning run would be an empty pool).
2. **The idempotence guard.** It is the only thing making a nightly job
   produce weekly output, so a false negative means duplicate lessons and a
   double LLM bill.
"""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

import pytest

from agents.lesson_picker import (
    candidates,
    existing_lesson_for_week,
    existing_lesson_id,
    latest_landing_date,
    parse_week,
    pick_subject,
    previous_complete_week,
    project_for_week,
    recent_subsystems,
    week_of,
)


def _landing(
    tmp: Path,
    *,
    name: str,
    project: str = "gcc",
    d: str = "2026-09-02",
    sha: str = "a" * 40,
    subsystem: str = "gcc/ipa",
    score: int | None = 8,
    is_stub: bool = False,
    tags: list[str] | None = None,
) -> Path:
    body = [
        "---",
        f"project: {project}",
        f"subsystem: {subsystem}",
        f"commit_hash: {sha}",
        "source_type: github",
        f"headline: {name}",
        "tldr: something landed",
        "url: https://github.com/gcc-mirror/gcc/commit/" + sha,
        f"date: '{d}'",
        f"is_stub: {str(is_stub).lower()}",
    ]
    if score is not None:
        body.append(f"impact_score: {score}")
    body.append("tags:")
    for tag in (tags if tags is not None else ["ipa"]):
        body.append(f"- {tag}")
    body += ["---", "", "Body."]
    path = tmp / "landings" / f"{d}-{name}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(body), encoding="utf-8")
    return path


def _lesson(tmp: Path, *, lesson_id: str, project: str, subsystem: str, d: str) -> Path:
    path = tmp / "lessons" / f"{d}-{project}-x.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join([
            "---",
            f"project: {project}",
            f"subsystem: {subsystem}",
            f"lesson_id: {lesson_id}",
            f"date: '{d}'",
            "---",
            "",
            "Body.",
        ]),
        encoding="utf-8",
    )
    return path


# ---------------------------------------------------------------------------
# ISO week arithmetic
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "today,expected_key,expected_start,expected_end",
    [
        # Mid-week: the week that ended last Sunday.
        (date(2026, 9, 9), "2026-W36", date(2026, 8, 31), date(2026, 9, 6)),
        # Monday: the week that ended yesterday.
        (date(2026, 9, 7), "2026-W36", date(2026, 8, 31), date(2026, 9, 6)),
        # Sunday: the CURRENT week is not over, so still the previous one.
        (date(2026, 9, 6), "2026-W35", date(2026, 8, 24), date(2026, 8, 30)),
        # New year: Jan 1 2027 belongs to ISO year 2026.
        (date(2027, 1, 1), "2026-W52", date(2026, 12, 21), date(2026, 12, 27)),
        # Early January resolving back into the previous ISO year.
        (date(2026, 1, 4), "2025-W52", date(2025, 12, 22), date(2025, 12, 28)),
    ],
)
def test_previous_complete_week(today, expected_key, expected_start, expected_end):
    week = previous_complete_week(today)
    assert week.key == expected_key
    assert (week.start, week.end) == (expected_start, expected_end)
    # A complete week is always exactly 7 days and starts on a Monday.
    assert (week.end - week.start).days == 6
    assert week.start.isoweekday() == 1
    # And it is strictly in the past.
    assert week.end < today


def test_previous_complete_week_never_returns_the_current_week():
    """The whole point: a Monday 02:00 run must not target an empty pool."""
    for offset in range(400):
        today = date(2026, 1, 1) + __import__("datetime").timedelta(days=offset)
        assert previous_complete_week(today).end < today


def test_week_of_contains_its_own_days():
    week = week_of(date(2026, 9, 3))
    assert week.contains(week.start) and week.contains(week.end)
    assert not week.contains(week.start - __import__("datetime").timedelta(days=1))
    assert not week.contains(week.end + __import__("datetime").timedelta(days=1))


@pytest.mark.parametrize("text", ["2026-W36", "2026-w36", " 2026-W36 ", "2026-W6"])
def test_parse_week_accepts(text):
    assert parse_week(text) is not None


@pytest.mark.parametrize("text", ["", "nope", "2026-36", "2026-W99", "W36"])
def test_parse_week_rejects(text):
    assert parse_week(text) is None


def test_parse_week_roundtrips():
    week = previous_complete_week(date(2026, 9, 9))
    assert parse_week(week.key) == week


# ---------------------------------------------------------------------------
# Candidate filtering
# ---------------------------------------------------------------------------

def test_only_landings_inside_the_week(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))   # Aug 31 – Sep 6
    _landing(tmp_path, name="inside", d="2026-09-02", sha="a" * 40)
    _landing(tmp_path, name="edge-start", d="2026-08-31", sha="b" * 40)
    _landing(tmp_path, name="edge-end", d="2026-09-06", sha="c" * 40)
    _landing(tmp_path, name="too-late", d="2026-09-07", sha="d" * 40)
    _landing(tmp_path, name="too-early", d="2026-08-30", sha="e" * 40)

    names = {s.headline for s in candidates(tmp_path, "gcc", week)}
    assert names == {"inside", "edge-start", "edge-end"}


def test_excludes_stubs_spam_and_low_scores(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))
    _landing(tmp_path, name="good", sha="a" * 40, score=8)
    _landing(tmp_path, name="stub", sha="b" * 40, is_stub=True)
    _landing(tmp_path, name="spam", sha="c" * 40, tags=["spam"])
    _landing(tmp_path, name="low", sha="d" * 40, score=5)
    _landing(tmp_path, name="other-project", sha="e" * 40, project="binutils")

    assert [s.headline for s in candidates(tmp_path, "gcc", week)] == ["good"]


def test_ranks_by_impact_first(tmp_path: Path):
    """A week's pool is large enough that the standout commit beats rotation."""
    week = previous_complete_week(date(2026, 9, 9))
    _landing(tmp_path, name="mid", sha="a" * 40, score=7, subsystem="gcc/ipa")
    _landing(tmp_path, name="best", sha="b" * 40, score=10, subsystem="gcc/rtl")
    _landing(tmp_path, name="floor", sha="c" * 40, score=6, subsystem="gcc/c")

    assert [s.headline for s in candidates(tmp_path, "gcc", week)] == [
        "best", "mid", "floor",
    ]


def test_subsystem_rotation_breaks_impact_ties(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))
    _landing(tmp_path, name="seen-again", sha="a" * 40, score=8, subsystem="gcc/ipa")
    _landing(tmp_path, name="fresh", sha="b" * 40, score=8, subsystem="gcc/rtl")
    _lesson(tmp_path, lesson_id="gcc:2026-W35", project="gcc",
            subsystem="gcc/ipa", d="2026-08-30")

    assert candidates(tmp_path, "gcc", week)[0].headline == "fresh"


def test_recent_subsystems_is_scoped_to_the_project(tmp_path: Path):
    _lesson(tmp_path, lesson_id="gcc:2026-W35", project="gcc",
            subsystem="gcc/ipa", d="2026-08-30")
    _lesson(tmp_path, lesson_id="binutils:2026-W35", project="binutils",
            subsystem="binutils/ld", d="2026-08-30")

    assert recent_subsystems(tmp_path, "gcc") == {"gcc/ipa"}
    assert recent_subsystems(tmp_path, "binutils") == {"binutils/ld"}


def test_subject_carries_the_week_and_commit_date(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))
    _landing(tmp_path, name="x", d="2026-09-02", sha="a" * 40)
    subject = candidates(tmp_path, "gcc", week)[0]

    assert subject.commit_date == date(2026, 9, 2)   # when it landed
    assert subject.week == week                       # what the lesson covers
    assert subject.lesson_id == "gcc:2026-W36"
    assert subject.landing_slug == "2026-09-02-x"


def test_missing_directories_are_empty_not_fatal(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))
    assert candidates(tmp_path, "gcc", week) == []
    assert recent_subsystems(tmp_path, "gcc") == set()
    assert latest_landing_date(tmp_path) is None
    assert existing_lesson_id(tmp_path, "gcc:2026-W36") is False


# ---------------------------------------------------------------------------
# Idempotence — what makes a nightly job weekly
# ---------------------------------------------------------------------------

def test_skips_a_week_that_already_has_a_lesson(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))
    _landing(tmp_path, name="x", sha="a" * 40)
    assert pick_subject(tmp_path, "gcc", week) is not None

    _lesson(tmp_path, lesson_id="gcc:2026-W36", project="gcc",
            subsystem="gcc/ipa", d="2026-09-06")
    assert pick_subject(tmp_path, "gcc", week) is None


def test_a_lesson_for_one_project_does_not_block_the_other(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))
    _landing(tmp_path, name="g", sha="a" * 40, project="gcc")
    _landing(tmp_path, name="b", sha="b" * 40, project="binutils",
             subsystem="binutils/ld")
    _lesson(tmp_path, lesson_id="gcc:2026-W36", project="gcc",
            subsystem="gcc/ipa", d="2026-09-06")

    assert pick_subject(tmp_path, "gcc", week) is None
    assert pick_subject(tmp_path, "binutils", week) is not None


def test_the_guard_matches_on_lesson_id_not_filename(tmp_path: Path):
    """A re-slugged headline must not produce a second lesson for the week."""
    week = previous_complete_week(date(2026, 9, 9))
    _landing(tmp_path, name="x", sha="a" * 40)
    path = _lesson(tmp_path, lesson_id="gcc:2026-W36", project="gcc",
                   subsystem="gcc/ipa", d="2026-09-06")
    path.rename(path.parent / "totally-different-name.md")

    assert pick_subject(tmp_path, "gcc", week) is None


# ---------------------------------------------------------------------------
# Mirror lag
# ---------------------------------------------------------------------------

def test_falls_through_to_a_resolvable_commit(tmp_path: Path):
    """Mirror lag is routine: skip what we can't read, don't fail the run."""
    week = previous_complete_week(date(2026, 9, 9))
    _landing(tmp_path, name="not-mirrored", sha="a" * 40, score=10)
    _landing(tmp_path, name="mirrored", sha="b" * 40, score=9)

    subject = pick_subject(
        tmp_path, "gcc", week, resolve=lambda sha: sha.startswith("b")
    )
    assert subject is not None and subject.headline == "mirrored"


def test_none_when_nothing_resolves(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))
    _landing(tmp_path, name="x", sha="a" * 40)
    assert pick_subject(tmp_path, "gcc", week, resolve=lambda sha: False) is None


def test_none_when_the_week_is_empty(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))
    _landing(tmp_path, name="x", d="2026-07-01", sha="a" * 40)
    assert pick_subject(tmp_path, "gcc", week) is None


# ---------------------------------------------------------------------------
# Anchoring
# ---------------------------------------------------------------------------

def test_latest_landing_date_filters_by_project(tmp_path: Path):
    _landing(tmp_path, name="g", d="2026-09-02", sha="a" * 40, project="gcc")
    _landing(tmp_path, name="b", d="2026-09-05", sha="b" * 40, project="binutils")

    assert latest_landing_date(tmp_path) == date(2026, 9, 5)
    assert latest_landing_date(tmp_path, "gcc") == date(2026, 9, 2)


# ---------------------------------------------------------------------------
# Project rotation — one lesson per week TOTAL, not one per project
# ---------------------------------------------------------------------------

PROJECTS = ["binutils", "gcc"]


def test_rotation_alternates_week_to_week():
    weeks = [previous_complete_week(date(2026, 9, 9) - timedelta(days=7 * i))
             for i in range(8)]
    picks = [project_for_week(w, PROJECTS) for w in weeks]

    # Every adjacent pair differs — that is the whole point of the rotation.
    assert all(a != b for a, b in zip(picks, picks[1:])), picks
    assert set(picks) == set(PROJECTS)


def test_rotation_survives_the_year_boundary():
    """The case a naive `iso_week % n` gets wrong.

    A 53-week year rolls W53 into W01; both are odd, so modulo-on-week-number
    hands the same project two weeks running. Counting weeks since the epoch
    has no such seam.
    """
    consecutive = [
        week_of(date(2026, 12, 21)),   # 2026-W52
        week_of(date(2026, 12, 28)),   # 2026-W53
        week_of(date(2027, 1, 4)),     # 2027-W01
        week_of(date(2027, 1, 11)),    # 2027-W02
    ]
    picks = [project_for_week(w, PROJECTS) for w in consecutive]
    assert all(a != b for a, b in zip(picks, picks[1:])), picks

    # Demonstrate the bug this guards against, so the test explains itself.
    naive = [PROJECTS[w.iso_week % 2] for w in consecutive]
    assert naive[1] == naive[2], "expected the naive scheme to repeat here"


def test_rotation_is_stable_for_a_given_week():
    week = previous_complete_week(date(2026, 9, 9))
    assert project_for_week(week, PROJECTS) == project_for_week(week, PROJECTS)


def test_rotation_edge_cases():
    week = previous_complete_week(date(2026, 9, 9))
    assert project_for_week(week, []) is None
    assert project_for_week(week, ["gcc"]) == "gcc"


# ---------------------------------------------------------------------------
# The week-scoped guard — what stops a second lesson (and a second bill)
# ---------------------------------------------------------------------------

def test_week_guard_fires_across_projects(tmp_path: Path):
    """A gcc lesson must block binutils from also writing one that week."""
    week = previous_complete_week(date(2026, 9, 9))
    assert existing_lesson_for_week(tmp_path, week) is None

    _lesson(tmp_path, lesson_id="gcc:2026-W36", project="gcc",
            subsystem="gcc/ipa", d="2026-09-06")

    assert existing_lesson_for_week(tmp_path, week) == "gcc"


def test_week_guard_ignores_other_weeks(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))          # 2026-W36
    _lesson(tmp_path, lesson_id="gcc:2026-W35", project="gcc",
            subsystem="gcc/ipa", d="2026-08-30")

    assert existing_lesson_for_week(tmp_path, week) is None


def test_week_guard_does_not_confuse_similar_week_keys(tmp_path: Path):
    """`:2026-W3` must not match `:2026-W36` — suffix, not substring."""
    week = parse_week("2026-W03")
    assert week is not None
    _lesson(tmp_path, lesson_id="gcc:2026-W36", project="gcc",
            subsystem="gcc/ipa", d="2026-09-06")

    assert existing_lesson_for_week(tmp_path, week) is None


def test_week_guard_on_missing_directory(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))
    assert existing_lesson_for_week(tmp_path, week) is None


# ---------------------------------------------------------------------------
# The stale-clone fallback
# ---------------------------------------------------------------------------
#
# When `git fetch` fails, the clone on disk still holds every commit up to the
# last successful fetch. Rejecting the whole week because its newest commits
# aren't in there yet throws away a perfectly readable repository. These tests
# pin the two boundaries that keep the fallback honest.

def test_fallback_reaches_back_when_the_clone_is_behind(tmp_path: Path):
    week = previous_complete_week(date(2026, 9, 9))          # 2026-W36
    _landing(tmp_path, name="this-week", d="2026-09-02", sha="a" * 40, score=10)
    _landing(tmp_path, name="last-week", d="2026-08-26", sha="b" * 40, score=7)

    subject = pick_subject(
        tmp_path,
        "gcc",
        week,
        resolve=lambda sha: sha.startswith("b"),   # clone predates this week
        fallback_weeks=4,
    )

    assert subject is not None
    assert subject.headline == "last-week"
    assert subject.commit_date == date(2026, 8, 26)


def test_fallback_keeps_the_target_weeks_identity(tmp_path: Path):
    """The lesson is still *this* week's lesson — only the subject is older.

    If the identity moved to the subject's week, the weekly "already done"
    guard would stop matching and the nightly step would rewrite, and re-bill,
    the lesson every night.
    """
    week = previous_complete_week(date(2026, 9, 9))          # 2026-W36
    _landing(tmp_path, name="this-week", d="2026-09-02", sha="a" * 40)
    _landing(tmp_path, name="older", d="2026-08-26", sha="b" * 40)

    subject = pick_subject(
        tmp_path, "gcc", week, resolve=lambda sha: sha.startswith("b"),
        fallback_weeks=4,
    )

    assert subject is not None
    assert subject.week == week
    assert subject.lesson_id == "gcc:2026-W36"


def test_fallback_does_not_invent_a_lesson_for_a_quiet_week(tmp_path: Path):
    """No eligible landings this week means no lesson — not an old one.

    The widening exists for source-access failure, not for filling silence.
    """
    week = previous_complete_week(date(2026, 9, 9))          # 2026-W36
    _landing(tmp_path, name="older", d="2026-08-26", sha="b" * 40)

    assert pick_subject(
        tmp_path, "gcc", week, resolve=lambda sha: True, fallback_weeks=4
    ) is None


def test_fallback_is_bounded(tmp_path: Path):
    """It must not walk back indefinitely looking for something to teach."""
    week = previous_complete_week(date(2026, 9, 9))          # W36
    _landing(tmp_path, name="this-week", d="2026-09-02", sha="a" * 40)
    _landing(tmp_path, name="ancient", d="2026-06-01", sha="b" * 40)

    assert pick_subject(
        tmp_path, "gcc", week, resolve=lambda sha: sha.startswith("b"),
        fallback_weeks=2,
    ) is None


def test_no_fallback_by_default(tmp_path: Path):
    """A healthy clone gets the old behaviour: this week's commits or nothing."""
    week = previous_complete_week(date(2026, 9, 9))
    _landing(tmp_path, name="this-week", d="2026-09-02", sha="a" * 40)
    _landing(tmp_path, name="older", d="2026-08-26", sha="b" * 40)

    assert pick_subject(
        tmp_path, "gcc", week, resolve=lambda sha: sha.startswith("b")
    ) is None
