---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- SLP
commit_hash: bca597522679903c66f28afff49971663a37ab37
source_type: github
author: Richard Biener
headline: Delay SLP discovery failure in BB vectorization
tldr: Vectorization pass defers potential failures in SLP discovery.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The SLP vectorization strategy in GCC's tree-vectorizer sometimes requires
  unrolling to discover vectorizable patterns. In the context of BB vectorization,
  `vect_build_slp_tree_1` could 'soft-fail' prematurely. This commit moves the soft-failing
  logic to `vect_build_slp_tree_2`, placing it after `vect_get_and_check_slp_defs`.
  This ensures that potential defs are analyzed first, potentially revealing better
  ways to split SLP groups. Additionally, `vect_get_and_check_slp_defs` is updated
  to not fall back to `vect_external_def` on mismatches when soft-failing, preventing
  extraneous analysis.
primer_glossary:
- term: tree-optimization
  definition: A phase in the compiler where the code is represented as a tree structure
    to perform various high-level transformations and optimizations.
- term: vectorization
  definition: An optimization technique where the compiler transforms code that operates
    on single data elements into code that operates on multiple data elements simultaneously,
    often using SIMD instructions.
- term: SLP
  definition: Simultaneous Linear Patterns. A vectorization technique that identifies
    sequences of identical scalar operations on different data elements and transforms
    them into a single vector operation.
- term: basic block (BB)
  definition: A sequence of consecutive instructions in a program that has only one
    entry point and one exit point.
- term: unrolling
  definition: A loop optimization technique where the loop body is duplicated multiple
    times to reduce loop overhead and potentially expose more parallelism.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bca597522679903c66f28afff49971663a37ab37
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

This commit modifies the basic block (BB) vectorization pass in GCC to delay the failure of SLP (Simultaneous Linear Patterns) discovery. Previously, failures could occur early in the process. Now, the failure is delayed until after analyzing definitions that might provide better splitting points for the pattern group. This change aims to improve the success rate of vectorization for simple cases without significantly impacting compile times.
