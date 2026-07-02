---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- tree-ssa-pre
commit_hash: b052d6bbbeea2b04c8a4f765e89b0b3f19f81764
source_type: github
author: Richard Biener
headline: tree-optimization/125040 - Iterate PRE for cyclic value graphs.
tldr: Compiler now iterates Per-Redge Elimination (PRE) optimizations to handle cyclic
  value graphs, fixing PR125040.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `clean` function in `tree-ssa-pre.cc` has been modified to iterate
  its processing loop. This is necessary to correctly prune invalid expressions when
  the ANTIC_IN value graph contains cycles. Previously, a single pass was insufficient
  to resolve all redundancies in such cases. The change ensures that the loop continues
  until no further pruning is possible, addressing PR125040. A new torture test case
  is included.
primer_general: This commit improves an optimization technique within the GCC compiler
  called Per-Redge Elimination (PRE). PRE aims to eliminate redundant computations
  in programs. The issue addressed was that if the program's logic created a circular
  dependency in how values were computed (a 'cyclic value graph'), the PRE optimization
  might not be able to remove all unnecessary calculations in one go. This change
  makes the optimization process repeat itself until all redundant calculations are
  found and removed. A new test case has been added to confirm this fix works correctly.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b052d6bbbeea2b04c8a4f765e89b0b3f19f81764
date: '2026-06-26'
is_stub: false
stub_reason: ''
---

This commit addresses a specific optimization issue (PR125040) within GCC's tree optimization passes. The problem occurred when the Per-Redge Elimination (PRE) pass encountered a cycle in the value graph of ANTIC_IN expressions. Such cycles prevent PRE from fully pruning all invalid expressions in a single pass. The fix modifies the `tree-ssa-pre.cc` file to iterate the PRE cleaning process, ensuring that all redundant expressions are removed even when cyclic dependencies exist. A new test case `pr125040.c` has been added to verify this fix.
