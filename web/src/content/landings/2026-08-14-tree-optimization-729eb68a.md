---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- SIMD
- pattern matching
commit_hash: 729eb68a0021bd37acff6a07a505b89687b974b9
source_type: github
author: Naveen
headline: Fold canonicalized vector min/max conditionals
tldr: Improves optimization of vector min/max expressions with conditional operations.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The `match.pd` and related tree-optimization passes now recognize
  and fold vector conditional expressions that represent min/max operations, even
  when they are in a canonicalized form not previously handled. Specifically, patterns
  are added for `VEC_COND_EXPR` where the comparison involves `GE`/`LT` (for max)
  or `LE`/`GT` (for min) and the result is a vector constant. This allows folding
  of expressions like `X >= { -99, -98 } ? X : { -100, -99 }` into `MAX_EXPR <X, {
  -100, -99 }>`. The implementation includes helper functions like `record_uniform_integer_difference`
  and `uniform_vector_differ…'
primer_glossary:
- term: VEC_COND_EXPR
  definition: GCC's internal representation for a conditional expression operating
    on vector types. It typically involves a condition, a value if true, and a value
    if false.
- term: vector constant
  definition: A constant value representing multiple elements of a vector type, e.g.,
    `{1, 2, 3, 4}` for a 4-element vector.
- term: canonicalized form
  definition: A standardized or simplified representation of an expression or value,
    making it easier for the compiler to match and optimize.
- term: uniform vector constant
  definition: A vector constant where all elements have the same value.
- term: MAX_EXPR
  definition: GCC's internal representation for a maximum expression, similar to `VEC_COND_EXPR`
    but specifically for finding the maximum of two values.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/729eb68a0021bd37acff6a07a505b89687b974b9
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This commit enhances GCC's ability to optimize vector conditional expressions involving minimum and maximum operations. It introduces new pattern matching rules in `match.pd` to recognize canonicalized forms of `VEC_COND_EXPR` for min/max, including those resulting from negative signed maximums or positive signed/unsigned minimums. The optimization handles both normal and reversed conditional arms and works with uniform and non-uniform vector constants. New test cases validate the improvements.
