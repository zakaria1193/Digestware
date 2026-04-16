"""Tests for subject-line → headline cleaning."""

from __future__ import annotations

import pytest

from agents.tools.headline import clean_subject


class TestCleanSubject:
    @pytest.mark.parametrize(
        "raw,expected_startswith",
        [
            ("[PATCH v3 4/8] tests: misc: Use new tunable handling", "tests: misc:"),
            ("Re: [PATCH 1/2] misc: fix lint", "misc:"),
            ("Re: Re: [RFC] redesign callbacks", "redesign callbacks"),
            ("[PATCH] gcc/ipa: inline hot functions", "gcc/ipa:"),
            ("no brackets here", "no brackets here"),
        ],
    )
    def test_strips_cruft(self, raw: str, expected_startswith: str):
        assert clean_subject(raw).startswith(expected_startswith)

    def test_never_empty_when_input_non_empty(self):
        assert clean_subject("[PATCH] [RFC]") != ""

    def test_drops_series_markers(self):
        assert "4/8" not in clean_subject("[PATCH 4/8] tests: misc")
