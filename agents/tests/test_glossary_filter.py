"""Tests for the deterministic primer_glossary exclusion filter."""

from __future__ import annotations

from agents.tools.glossary_filter import filter_glossary, is_excluded_term


def test_excludes_bare_project_names():
    assert is_excluded_term("gcc")
    assert is_excluded_term("GCC")
    assert is_excluded_term("binutils")
    assert is_excluded_term("GNU Binutils")
    assert is_excluded_term("the Linux kernel")


def test_keeps_subsystem_specific_terms():
    assert not is_excluded_term("IPA-SRA")
    assert not is_excluded_term("-fipa-sra")
    assert not is_excluded_term("ELF relocation")
    assert not is_excluded_term("tcache")


def test_keeps_terms_that_merely_contain_an_excluded_word():
    assert not is_excluded_term("GCC IPA pass")
    assert not is_excluded_term("binutils/ld")


def test_filter_glossary_drops_only_excluded_entries():
    entries = [
        {"term": "GCC", "definition": "The compiler."},
        {"term": "IPA-SRA", "definition": "A GCC optimization pass."},
        {"term": "binutils", "definition": "The binary utilities suite."},
    ]
    result = filter_glossary(entries)
    assert result == [{"term": "IPA-SRA", "definition": "A GCC optimization pass."}]


def test_filter_glossary_handles_empty_and_malformed_input():
    assert filter_glossary([]) == []
    assert filter_glossary([{"definition": "no term key"}]) == [
        {"definition": "no term key"}
    ]
