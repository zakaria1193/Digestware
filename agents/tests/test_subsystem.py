"""Tests for deterministic subsystem extraction."""

from __future__ import annotations

import pytest

from agents.tools.subsystem import extract_subsystem


class TestExtractSubsystem:
    @pytest.mark.parametrize(
        "title,expected",
        [
            ("gcc/ipa: improve inliner for hot callers", "gcc/ipa"),
            ("middle-end/124877 - fix mis-apply of PROMOTE_PROTOTYPES", "middle-end"),
            ("malloc: introduce ifuncs for malloc functions", "malloc"),
            ("[PATCH v3 4/8] tests: misc: Use new tunable handling", "tests"),
            ("binutils/ld: fix relaxation loop", "binutils/ld"),
            ("kernel/mm: fix TLB flush on arm64", "kernel/mm"),
        ],
    )
    def test_subject_prefix(self, title: str, expected: str):
        assert extract_subsystem(title, None, "gcc") == expected

    def test_re_prefix_stripped(self):
        assert (
            extract_subsystem(
                "Re: [PATCH] gcc/ipa: refactor", None, "gcc"
            )
            == "gcc/ipa"
        )

    def test_no_signal_falls_back_to_project(self):
        assert extract_subsystem("cleanup", None, "glibc") == "glibc"

    def test_no_signal_and_no_project_is_general(self):
        assert extract_subsystem("cleanup", None, "unknown") == "general"

    def test_never_returns_unknown(self):
        # Worst case: garbage title, unknown project, no diff.
        result = extract_subsystem("???", None, "unknown")
        assert result != "unknown"
