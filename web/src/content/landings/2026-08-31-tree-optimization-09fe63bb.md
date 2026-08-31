---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- integer arithmetic
commit_hash: 09fe63bb71e6b14186b0bb1f910270be101a6385
source_type: github
author: Naveen
headline: Simplify MIN(A, B) eq/ne 0 to A when B is positive
tldr: Optimized MIN(A, B) comparisons to simplify to comparisons of A when B is known
  to be positive.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds a new pattern to `match.pd` for the tree-SSA optimizer.
  It addresses PR tree-optimization/127102 by enabling the simplification of expressions
  like `MIN(A, B) == 0` or `MIN(A, B) != 0` to `A == 0` or `A != 0`, respectively,
  provided that `B` is known to be positive. The `min:c` pattern handles both `MIN(A,
  B)` and `MIN(B, A)` symmetrically. An `INTEGRAL_TYPE_P` guard ensures this optimization
  is only applied to integer types, aligning with the semantics of the `nonneg` and
  `nonzero` predicates used in the pattern.
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC where the code is represented and manipulated using an
    intermediate 'tree' structure, allowing for various optimizations.
- term: MIN(A, B)
  definition: An expression that evaluates to the smaller of the two values, A and
    B.
- term: folding
  definition: The process of replacing an expression with its computed value at compile
    time.
- term: SSA
  definition: Static Single Assignment. An intermediate representation where every
    variable is assigned a value exactly once, which simplifies many compiler analyses
    and optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/09fe63bb71e6b14186b0bb1f910270be101a6385
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This commit introduces an optimization to simplify comparisons involving the minimum of two values. When `MIN(A, B)` is compared to zero (either equal or not equal) and operand `B` is known to be positive, the comparison is now folded to a direct comparison of `A` with zero. This helps eliminate redundant checks and potentially simplify subsequent code.
