---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- optimization
- range analysis
- bugfix
commit_hash: 24e96a7911669fc81febcf887b443c8aef15a4cc
source_type: github
author: Naveen
headline: Tighten unsigned-add range via no-overflow relation
tldr: Improves range analysis for unsigned addition by detecting and utilizing non-overflow
  conditions.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch enhances the GORI (Global Optimizing Range Inference) pass
  by improving range analysis for unsigned addition. Specifically, it introduces a
  new `operator_plus::fold_range` function in `range-op.cc` that leverages the 'no-overflow'
  relation. If `lhs = op1 + op2` and it's known that `lhs >= op1` (implying no unsigned
  overflow if `op2` is non-negative), then `lhs >= op2`. This allows tightening `lhs`'s
  range to `[max(lhs_lb, op2_lb), lhs_ub]`. The necessary `relation_trio` (containing
  `lhs_op1` and `lhs_op2` relations) is passed to the `fold_range` call sites within
  `gori_compute::ref…
primer_glossary:
- term: GORI
  definition: Global Optimizing Range Inference. A GCC optimization pass that analyzes
    and infers the possible range of values for variables throughout the program to
    enable other optimizations.
- term: Range analysis
  definition: A compiler analysis that determines the set of possible values a variable
    or expression can take at a given point in the program. This information is used
    to optimize code, e.g., by eliminating checks or choosing more efficient instructions.
- term: Unsigned overflow
  definition: In unsigned integer arithmetic, overflow occurs when the result of an
    operation exceeds the maximum representable value. In C/C++, unsigned overflow
    wraps around (modulo 2^N).
- term: Tree optimization
  definition: A phase in GCC's compilation pipeline that operates on the 'tree' intermediate
    representation (specifically GIMPLE). This is where many high-level optimizations,
    like constant folding and dead code elimination, are performed.
- term: GIMPLE
  definition: Generic Intermediate Representation Simplification. An SSA (Static Single
    Assignment) based intermediate representation used by GCC, designed to be simpler
    than GENERIC and suitable for optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/24e96a7911669fc81febcf887b443c8aef15a4cc
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

This commit enhances range analysis for unsigned addition operations in GCC's tree optimization passes. When an unsigned addition `lhs = op1 + op2` is known to not have overflowed, and `lhs >= op1`, it can be deduced that `lhs >= op2`. This information, particularly when `op2` has a positive lower bound, allows the compiler to tighten the computed range of `lhs`. The changes involve adding a new `fold_range` function for `operator_plus` and threading the deduced relations through the GORI refinement process.
