"""Deterministic identifier extraction from digest article text.

No LLM involved — these are regexes, so re-indexing the whole corpus is free and
the output is reproducible. The point is exactness: an agent debugging a
regression arrives with a *literal* token (``bfd_elf_final_link``, ``tc-z80.c``,
``-fipa-sra``, ``R_AARCH64_TLSDESC``, ``PR34165``) and needs the documents that
mention that token, not documents that are vaguely about linking.

Each harvester returns ``(display, kind)`` pairs; ``extract_symbols`` merges them
and casefolds a lookup key. Precision matters more than recall: a symbol table
full of English words is worse than a small exact one, because the ranker treats
symbol overlap as a strong signal.
"""

from __future__ import annotations

import re

# ── Source-file and testsuite paths ──────────────────────────────────────────
# `gcc/ipa-sra.cc`, `mm/slub.c`, `bfd/version.h`, `gcc.dg/pr12345.c`,
# `ld-elf/pr22269.d`. Segments may contain dots (`gcc.dg`, `g++.dg`), so the
# extension is anchored to the end of the final segment.
_SUFFIXES = (
    "c|cc|cpp|cxx|h|hh|hpp|inc|S|s|def|opt|texi|exp|d|md|am|ac|in|py|sh|f90|adb|ads|rs|go|java"
)
_FILE_RE = re.compile(
    rf"(?<![\w/.-])((?:[A-Za-z0-9_+.-]+/)*[A-Za-z0-9_+.-]+\.(?:{_SUFFIXES}))(?![\w])"
)

# Directory fragments that mark a path as a testcase rather than compiler source.
_TEST_MARKERS = ("testsuite/", "gcc.dg", "gcc.target", "g++.dg", "gfortran.dg",
                 "ld-elf", "ld-x86", "gas/testsuite", "libstdc++.dg", "tests/")

# ── Command-line flags ───────────────────────────────────────────────────────
# `-fipa-sra`, `-Wmaybe-uninitialized`, `-march=armv9-a`, `-O2`, `-mcpu=neoverse-v2`.
# Deliberately anchored to the known flag letters: a bare `-foo` regex would
# swallow every hyphenated word in English prose.
_FLAG_RE = re.compile(
    r"(?<![\w-])(-(?:f|W|m|O|g|std=|z\b)[A-Za-z0-9][A-Za-z0-9_.+=-]*)(?![\w])"
)
# `-z separate-code`, `-z now` — the option is a *separate* argument, so the
# flag regex above cannot see it.
_Z_OPT_RE = re.compile(r"(?<![\w-])-z\s+([a-z][a-z0-9-]{2,})(?![\w])")

# ── ELF relocations ──────────────────────────────────────────────────────────
_RELOC_RE = re.compile(r"\b(R_[A-Z0-9]+_[A-Z0-9_]+)\b")

# ── Bug references ───────────────────────────────────────────────────────────
# `PR 34165`, `PR34165`, `PR target/34165`, `BZ #33085`, `bug 22944`.
_BUG_RE = re.compile(
    r"\b(?:PR\s*(?:[a-z+-]+/)?|BZ\s*#?\s*|bugzilla\s*#?\s*|bug\s+)(\d{4,7})\b",
    re.IGNORECASE,
)

# ── Macros / constants ───────────────────────────────────────────────────────
# `BFD_VERSION_DATE`, `CONFIG_SLUB`, `GNU_PROPERTY_1_NEEDED`, `IPA_PARAM_DESCRIPTOR`.
_MACRO_RE = re.compile(r"\b([A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+)\b")

# ── C-style identifiers ──────────────────────────────────────────────────────
# `bfd_elf_final_link`, `d_compact_number`, `__libc_arm_za_disable`, `bsearch()`.
# Requires an underscore (or a trailing `()`), which is what separates a real
# identifier from an English word.
_IDENT_RE = re.compile(r"\b([a-z_][a-z0-9_]*_[a-z0-9_]+)\b")
_CALL_RE = re.compile(r"\b([a-z_][a-z0-9_]{2,})\s*\(\)")

# Underscored tokens that are ordinary prose or project jargon, not identifiers.
_IDENT_STOPLIST = frozenset({
    "e_g", "i_e", "a_k_a", "read_only", "run_time", "compile_time", "so_called",
})

# Macro-looking tokens that are acronyms or headline shouting, not real macros.
_MACRO_STOPLIST = frozenset({
    "GNU_TOOLS", "OS_LEVEL", "TODO_NOTE",
})


def _add(out: dict[tuple[str, str], str], display: str, kind: str) -> None:
    """Record ``display`` under kind, keyed by its casefolded lookup form."""
    display = display.strip()
    if not display:
        return
    key = (display.casefold(), kind)
    # First spelling wins — headline casing is usually the canonical one.
    out.setdefault(key, display)


def extract_symbols(text: str) -> list[tuple[str, str, str]]:
    """Return ``(symbol, display, kind)`` triples found in *text*.

    ``symbol`` is the casefolded lookup key, ``display`` the spelling as found,
    ``kind`` one of file/test/flag/reloc/bug/macro/ident.
    """
    found: dict[tuple[str, str], str] = {}

    for match in _FILE_RE.finditer(text):
        path = match.group(1)
        # A bare `version.h` is useful; a bare `2.5.c` is not.
        if path[0].isdigit() and "/" not in path:
            continue
        kind = "test" if any(m in path for m in _TEST_MARKERS) else "file"
        _add(found, path, kind)

    for match in _FLAG_RE.finditer(text):
        # `.` is legal mid-flag (`-std=c++2a`, `-march=armv8.2-a`) but a flag at
        # the end of a sentence picks up the full stop, so trim trailing prose
        # punctuation rather than excluding `.` from the pattern.
        _add(found, match.group(1).rstrip(".,;:="), "flag")
    for match in _Z_OPT_RE.finditer(text):
        _add(found, f"-z {match.group(1)}", "flag")

    for match in _RELOC_RE.finditer(text):
        _add(found, match.group(1), "reloc")

    for match in _BUG_RE.finditer(text):
        _add(found, f"PR{match.group(1)}", "bug")

    for match in _MACRO_RE.finditer(text):
        macro = match.group(1)
        # Relocations already have their own, more specific kind.
        if macro.startswith("R_") or macro in _MACRO_STOPLIST:
            continue
        _add(found, macro, "macro")

    for match in _IDENT_RE.finditer(text):
        ident = match.group(1)
        if ident in _IDENT_STOPLIST or len(ident) < 6:
            continue
        _add(found, ident, "ident")
    for match in _CALL_RE.finditer(text):
        _add(found, match.group(1), "ident")

    return [(key, display, kind) for (key, kind), display in found.items()]


def normalise_symbol(query: str) -> str:
    """Casefold a user-supplied symbol into its lookup key.

    Tolerates the shapes people actually type: ``bsearch()`` for a function,
    ``PR 34165`` / ``BZ #34165`` for a bug, surrounding backticks from Markdown.
    """
    q = query.strip().strip("`\"'").strip()
    q = re.sub(r"\(\s*\)$", "", q)
    bug = _BUG_RE.fullmatch(q)
    if bug:
        return f"pr{bug.group(1)}"
    return q.casefold()
