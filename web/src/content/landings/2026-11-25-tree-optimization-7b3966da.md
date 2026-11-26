---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler
- GCC
- UB
commit_hash: 7b3966da181fe0c8ad4354b462aee74e6c50ba62
source_type: github
author: Richard Biener
headline: 'Tree-optimization: Avoid UB negating ratio in IVOPTS cost compute'
tldr: Fixes undefined behavior in loop invariant code motion by negating ratios in
  unsigned integer types.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The tree-ssa-loop-ivopts.cc file's get_computation_cost function calculates
  the cost of operations within loops for optimization purposes. This commit corrects
  an overflow/underflow issue in the cost calculation when dealing with ratios by
  performing the negation in unsigned arithmetic, avoiding undefined behavior on signed
  integer negation. This change affects the cost heuristics used by the IVOPTS pass.
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC's compilation pipeline where the intermediate representation
    (the 'tree') is analyzed and transformed to improve code efficiency.
- term: IVOPTS
  definition: Loop Invariant Code Motion Optimization. This pass identifies computations
    within a loop that produce the same result across all iterations and moves them
    outside the loop to reduce redundant work.
- term: tree-ssa
  definition: Static Single Assignment form applied to GCC's intermediate representation
    tree. SSA helps in simplifying many optimizations by ensuring each variable is
    assigned a value only once.
- term: Undefined Behavior (UB)
  definition: Behavior that results from an erroneous program condition for which
    the C and C++ standards impose no requirements. Compilers may take any action,
    including returning an incorrect result, or crashing.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7b3966da181fe0c8ad4354b462aee74e6c50ba62
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This commit addresses undefined behavior in the loop invariant code motion (IVOPTS) optimization pass within GCC's tree-ssa. Specifically, it resolves an issue where negating a ratio could lead to undefined behavior when performed on signed integers. The fix ensures that the negation is performed using unsigned types, maintaining correctness and preventing potential runtime errors or unexpected optimizations.
