---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- optimization
- regression
commit_hash: bbc7fd5ae68069863b77a9d614a9aa82a4079e58
source_type: github
author: Naveen
headline: 'testsuite: Add regression test for PR81549'
tldr: Adds new test cases to preserve coverage for loop-carried values and constant
  folding.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds two test files (`pr81549.c` and `pr81549-2.c`) to
  the GCC testsuite. These tests target the loop-PHI final-value replacement optimization.
  The goal is to ensure that the optimization, which already works on the current
  trunk, continues to correctly handle loop-carried values and constant folding for
  final stores and return values.
primer_glossary:
- term: loop-PHI
  definition: A PHI node in the SSA (Static Single Assignment) form that is part of
    a loop. It represents values that are live across loop iterations.
- term: constant folding
  definition: An optimization technique where compile-time expressions are evaluated
    to their constant values.
- term: SSA
  definition: Static Single Assignment form, an intermediate representation used in
    compilers where every variable is assigned a value exactly once.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bbc7fd5ae68069863b77a9d614a9aa82a4079e58
date: '2026-07-17'
is_stub: true
stub_reason: low_score
---

New test cases are added to the GCC testsuite to cover optimizations related to loop-PHI final-value replacement. These tests verify that loop-carried values are correctly handled and that final stores and return values are folded into constants, maintaining coverage for existing optimizations on the current GCC trunk.
