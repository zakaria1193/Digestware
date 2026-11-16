---
project: gcc
subsystem: mips/testsuite
patch_id: null
tags:
- mips
- testsuite
- whitespace
commit_hash: 1b99cfcd437afa4132c074e766ba02cd5372ad02
source_type: github
author: Maciej W. Rozycki
headline: 'MIPS testsuite: Fix whitespace in mulsize-3.c and mulsize-4.c.'
tldr: Cleans up trailing whitespace and ensures files end with newlines in MIPS testsuite
  files.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Testsuite files, particularly those in `gcc/testsuite/gcc.target/mips/`,
  are subject to strict formatting rules. This change cleans up accidental trailing
  whitespace in `mulsize-3.c` and `mulsize-4.c` and ensures they end with a newline,
  preventing potential test failures due to cosmetic changes.
primer_glossary:
- term: testsuite
  definition: A collection of tests used to verify the correctness of a software project,
    in this case, the GCC compiler. Testsuite files exercise various language features,
    optimization passes, and target-specific behaviors.
- term: MIPS
  definition: A reduced instruction set computer (RISC) architecture that was popular
    in the 1980s and 1990s, often used in embedded systems and early workstations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1b99cfcd437afa4132c074e766ba02cd5372ad02
date: '2026-11-15'
is_stub: true
stub_reason: low_score
---

This commit addresses minor whitespace issues in two MIPS testsuite files, mulsize-3.c and mulsize-4.c. It removes trailing random whitespace characters and ensures both files properly terminate with a newline, maintaining code hygiene.
