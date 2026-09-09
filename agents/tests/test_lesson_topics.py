"""Tests for the lesson editorial filter.

The policy is short but load-bearing: without it the two most common GCC
subsystems on disk are `cobol` (90 landings) and `fortran` (90), and the first
real run picked `gcc/alpha` and `gcc/cobol` — precisely the subjects the
project owner does not want taught.
"""

from __future__ import annotations

import pytest

from agents.lesson_topics import (
    BIG_ARCHES,
    KNOWN_ARCHES,
    is_lesson_worthy,
    rejection_reason,
)


@pytest.mark.parametrize(
    "subsystem",
    [
        "tree-optimization", "middle-end", "libstdc++", "ipa", "match.pd",
        "bfd", "ld", "gas", "readelf", "bfd/pe", "libcpp", "lto",
        "ada", "c++", "gccrs", "libgomp",
    ],
)
def test_general_and_wanted_subjects_pass(subsystem: str) -> None:
    assert is_lesson_worthy(subsystem), rejection_reason(subsystem)


@pytest.mark.parametrize(
    "subsystem", ["aarch64", "x86", "i386", "gcc/risc-v", "risc-v", "rs6000", "arm"]
)
def test_big_architectures_pass(subsystem: str) -> None:
    assert is_lesson_worthy(subsystem), rejection_reason(subsystem)


@pytest.mark.parametrize(
    "subsystem",
    ["gcc/alpha", "alpha", "alpha/ld", "xtensa", "gas/loongarch", "z80",
     "s390", "avr", "sh", "gcc/cris", "microblaze", "amdgcn"],
)
def test_niche_architectures_are_rejected(subsystem: str) -> None:
    reason = rejection_reason(subsystem)
    assert reason is not None and "architecture" in reason


@pytest.mark.parametrize(
    "subsystem", ["cobol", "fortran", "gcc/fortran", "libgfortran",
                  "openmp/fortran", "go", "gccgo", "m2"],
)
def test_niche_languages_are_rejected(subsystem: str) -> None:
    reason = rejection_reason(subsystem)
    assert reason is not None and "language" in reason


def test_tags_catch_what_the_subsystem_hides() -> None:
    """Subsystems are inconsistent; the tags often carry the real topic.

    The COBOL stub from the first real run had subsystem `cobol`, but a
    sibling landing carried it only in the tags.
    """
    assert not is_lesson_worthy("gcc", ["cobol", "lexer"])
    assert not is_lesson_worthy("gcc", ["alpha", "security"])
    assert is_lesson_worthy("gcc", ["aarch64", "vectorization"])


def test_housekeeping_is_rejected() -> None:
    for s in ("testsuite", "gcc/testsuite", "maintainers", "doc", "ci",
              "binutils/pre-commit", "testsuite/aarch64"):
        reason = rejection_reason(s)
        assert reason is not None and "housekeeping" in reason, s


def test_unknown_tokens_are_not_arch_gated() -> None:
    """A token we don't recognise must not be treated as a niche arch.

    Otherwise every new subsystem name silently becomes unpublishable.
    """
    assert is_lesson_worthy("some-new-pass")
    assert is_lesson_worthy("bfd/elf")


def test_empty_input_is_allowed() -> None:
    assert is_lesson_worthy(None)
    assert is_lesson_worthy("")


def test_big_arches_are_a_subset_of_known() -> None:
    """Otherwise a 'big' arch could be silently unrecognised and ungated."""
    assert BIG_ARCHES <= KNOWN_ARCHES
