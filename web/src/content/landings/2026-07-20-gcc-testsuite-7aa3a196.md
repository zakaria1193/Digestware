---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- vectorization
- enum
commit_hash: 7aa3a196148f8b35619f38020164d15e1eace7fb
source_type: github
author: Torbjörn SVENSSON
headline: Prevent packing enum in vect-early-break_65.c
tldr: Ensures enum types are not packed to a size smaller than int in a specific test
  case.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test `vect-early-break_65.c` relies on enum sizes not being reduced
  below `int` when vectorization is enabled by `-fshort-enum`. This commit ensures
  that the enum in this test case is not packed to a smaller size, preventing vectorization
  mismatches.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7aa3a196148f8b35619f38020164d15e1eace7fb
date: '2026-07-20'
is_stub: true
stub_reason: low_score
---

The test case vect-early-break_65.c might fail if GCC is compiled with -fshort-enum and enums are packed to a size smaller than int. This commit prevents such packing for enum types in this specific test file to ensure vectorization matching.
