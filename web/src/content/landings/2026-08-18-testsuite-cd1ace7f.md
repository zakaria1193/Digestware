---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- alpha
- elf
commit_hash: cd1ace7fd8e9c6fd4ebc475c52d5c04bb9f2bee3
source_type: github
author: Matt Turner
headline: Disable small data for attr-retain tests on Alpha
tldr: Alpha's small data section handling required tests for `attr-retain` to be run
  with -G0.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Alpha uses gp-relative addressing for small data objects, placing them
  in `.sdata` and `.sbss` sections with an 's' flag. The `attr-retain` tests look
  for section flags like 'R' on sections such as `.text`, `.data`, etc. This commit
  applies `-G0` to these tests on Alpha, preventing the use of small data sections
  and ensuring the retain flag is correctly recognized on the general sections, fixing
  failures where scans like `.rodata.*,"aR"` previously did not match.
primer_glossary:
- term: attr-retain
  definition: A GCC attribute that influences how sections are placed and handled,
    often related to read-only data or code.
- term: gp-relative
  definition: A method of addressing data objects using a global pointer (GP), typically
    for optimizing access to small, frequently used data.
- term: .sdata
  definition: A section in an ELF object file used to store small initialized global
    or static data.
- term: .sbss
  definition: A section in an ELF object file used to store small uninitialized global
    or static data.
- term: ELF section flags
  definition: Attributes within an ELF object file's section header that describe
    the properties of the section, such as 'R' for read-only, 'W' for writable, 'a'
    for allocated, etc.
- term: -G0
  definition: A GCC flag that affects how small data sections are used. -G0 typically
    disables the use of small data sections, forcing all data into general sections.
discussion_id_link: null
bugzilla_pr: null
series_id: 'gcc:testsuite: disable small data for attr-retain tests on alpha'
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cd1ace7fd8e9c6fd4ebc475c52d5c04bb9f2bee3
date: '2026-08-18'
is_stub: true
stub_reason: low_score
---

Tests for the `attr-retain` attribute rely on specific ELF section flags (e.g., 'R' for read-only). Alpha, however, places small objects into gp-relative small data areas (`.sdata`/`.sbss`) with an 's' flag. This commit enables the `-G0` flag for these tests on Alpha, which forces all objects into general sections, resolving 57 test failures across C and C++ test suites.
