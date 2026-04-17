"""Tests for patch-series detection and canonical collapse."""

from __future__ import annotations

from agents.tools.series import parse_patch_tag, series_id_for, split_canonical


class TestParsePatchTag:
    def test_full(self):
        tag = parse_patch_tag("[PATCH v3 4/8] tests: misc")
        assert tag == {"version": 3, "n": 4, "total": 8}

    def test_no_version(self):
        tag = parse_patch_tag("[PATCH 1/5] thing")
        assert tag == {"version": 1, "n": 1, "total": 5}

    def test_bare_patch(self):
        tag = parse_patch_tag("[PATCH] thing")
        assert tag == {"version": 1, "n": None, "total": None}

    def test_non_patch(self):
        assert parse_patch_tag("Re: RFC discussion") is None


class TestSeriesIdFor:
    def test_same_for_all_parts(self):
        a = series_id_for("[PATCH 0/5] malloc: introduce ifuncs", "glibc")
        b = series_id_for("[PATCH 1/5] malloc: introduce ifuncs", "glibc")
        c = series_id_for("[PATCH 5/5] malloc: introduce ifuncs", "glibc")
        assert a == b == c
        assert a is not None

    def test_version_does_not_split(self):
        v2 = series_id_for("[PATCH v2 0/5] malloc: introduce ifuncs", "glibc")
        v3 = series_id_for("[PATCH v3 0/5] malloc: introduce ifuncs", "glibc")
        assert v2 == v3

    def test_standalone_bare_patch_has_no_id(self):
        # Without N/M we cannot declare it a series.
        assert series_id_for("[PATCH] one-off fix", "glibc") is None

    def test_different_series_distinct(self):
        a = series_id_for("[PATCH 0/5] malloc: foo", "glibc")
        b = series_id_for("[PATCH 0/5] nptl: bar", "glibc")
        assert a != b


class _Item:
    def __init__(self, title: str, url: str, project: str = "glibc"):
        self.title = title
        self.url = url
        self.project = project


class TestSplitCanonical:
    def test_cover_letter_is_canonical(self):
        # Real patch series share the cover-letter subject across every
        # message (the per-part body varies, the subject does not).
        items = [
            _Item("[PATCH 1/3] malloc: introduce ifuncs", "u1"),
            _Item("[PATCH 2/3] malloc: introduce ifuncs", "u2"),
            _Item("[PATCH 0/3] malloc: introduce ifuncs", "u0"),
            _Item("[PATCH 3/3] malloc: introduce ifuncs", "u3"),
        ]
        canonical, parts_by_idx = split_canonical(
            items,
            title_of=lambda i: i.title,
            project_of=lambda i: i.project,
            url_of=lambda i: i.url,
        )
        assert len(canonical) == 1
        assert canonical[0].url == "u0"
        assert len(parts_by_idx[0]) == 3

    def test_standalones_pass_through(self):
        items = [
            _Item("gcc/ipa: standalone", "u1"),
            _Item("binutils/ld: another", "u2"),
        ]
        canonical, parts_by_idx = split_canonical(
            items,
            title_of=lambda i: i.title,
            project_of=lambda i: i.project,
            url_of=lambda i: i.url,
        )
        assert len(canonical) == 2
        assert parts_by_idx == {}

    def test_newer_version_wins(self):
        items = [
            _Item("[PATCH v1 0/2] cover", "old"),
            _Item("[PATCH v3 0/2] cover", "new"),
        ]
        canonical, _ = split_canonical(
            items,
            title_of=lambda i: i.title,
            project_of=lambda i: i.project,
            url_of=lambda i: i.url,
        )
        assert canonical[0].url == "new"
