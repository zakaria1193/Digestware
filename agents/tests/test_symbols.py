"""Symbol extraction — the exactness layer under find_by_symbol."""

from __future__ import annotations

import pytest

from agents.index.symbols import extract_symbols, normalise_symbol


def kinds_for(text: str) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for symbol, _display, kind in extract_symbols(text):
        out.setdefault(kind, set()).add(symbol)
    return out


def test_extracts_source_paths():
    found = kinds_for("Changes to gcc/ipa-sra.cc and bfd/version.h land today.")
    assert {"gcc/ipa-sra.cc", "bfd/version.h"} <= found["file"]


def test_testsuite_paths_are_marked_as_tests():
    found = kinds_for("Adds gcc.dg/pr12345.c and ld-elf/pr22269.d coverage.")
    assert {"gcc.dg/pr12345.c", "ld-elf/pr22269.d"} <= found["test"]
    assert "gcc.dg/pr12345.c" not in found.get("file", set())


def test_extracts_flags_including_separated_z_options():
    found = kinds_for("Build with -fipa-sra -Wmaybe-uninitialized and link -z separate-code.")
    assert {"-fipa-sra", "-wmaybe-uninitialized", "-z separate-code"} <= found["flag"]


def test_flag_at_end_of_sentence_drops_the_full_stop():
    # `.` is legal inside a flag (-march=armv8.2-a), so the trailing period of a
    # sentence is trimmed rather than excluded from the pattern.
    found = kinds_for("Compile with -O2. Then try -march=armv8.2-a.")
    assert "-o2" in found["flag"]
    assert "-march=armv8.2-a" in found["flag"]


def test_relocations_are_their_own_kind_not_macros():
    found = kinds_for("Emits R_AARCH64_TLSDESC during relaxation.")
    assert "r_aarch64_tlsdesc" in found["reloc"]
    assert "r_aarch64_tlsdesc" not in found.get("macro", set())


@pytest.mark.parametrize(
    "text", ["Fixes PR 34165 upstream.", "Fixes PR34165 upstream.",
             "Fixes PR target/34165 upstream.", "See BZ #34165.", "See bug 34165."],
)
def test_bug_reference_spellings_normalise_to_one_key(text):
    assert "pr34165" in kinds_for(text)["bug"]


def test_extracts_c_identifiers_and_calls():
    found = kinds_for("bfd_elf_final_link calls bsearch() before returning.")
    assert "bfd_elf_final_link" in found["ident"]
    assert "bsearch" in found["ident"]


def test_prose_is_not_mistaken_for_identifiers():
    # Ordinary English must not populate the symbol table: the ranker treats a
    # symbol hit as strong evidence, so precision matters more than recall.
    found = kinds_for("This is a read_only mapping, e_g. a simple one.")
    assert "read_only" not in found.get("ident", set())
    assert "e_g" not in found.get("ident", set())


def test_display_form_is_preserved_while_key_is_casefolded():
    pairs = {(s, d) for s, d, _k in extract_symbols("BFD_VERSION_DATE was bumped.")}
    assert ("bfd_version_date", "BFD_VERSION_DATE") in pairs


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("`bsearch()`", "bsearch"), ("PR 34165", "pr34165"), ("BZ #34165", "pr34165"),
     ("TC-Z80.c", "tc-z80.c"), ('  "gcc/ipa-sra.cc"  ', "gcc/ipa-sra.cc")],
)
def test_normalise_symbol_tolerates_how_people_actually_type(raw, expected):
    assert normalise_symbol(raw) == expected
