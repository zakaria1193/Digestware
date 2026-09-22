---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- abs
- comparison
- optimization
commit_hash: 59c8c4bbac46570ac36782172ed28569affe42c4
source_type: github
author: Naveen
headline: 'tree-optimization: Fold abs(x) comparisons with x'
tldr: GCC can now fold comparisons involving abs(x) and x, simplifying expressions
  and improving optimization.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `match.pd` patterns have been extended to recognize and fold comparisons
  between `abs(x)` and `x`, including cases where `x` is an unsigned conversion of
  itself or its absolute value. The patterns account for undefined-overflow semantics
  by simplifying to constants or sign tests (e.g., `x < 0`). For wrapping-overflow,
  the `INT_MIN` case is handled explicitly using unsigned comparisons. These transformations
  help simplify complex conditional logic derived from absolute value operations.
primer_glossary:
- term: abs(x)
  definition: The absolute value of x, which is x if x is non-negative, and -x if
    x is negative.
- term: folding
  definition: A compiler optimization technique where constant expressions or comparisons
    are evaluated at compile time, replacing them with their results.
- term: undefined-overflow
  definition: An arithmetic operation where the result exceeds the maximum representable
    value for the data type, leading to unpredictable behavior in C/C++ for signed
    integers.
- term: wrapping-overflow
  definition: An arithmetic operation where the result exceeds the maximum representable
    value, and the value wraps around to the minimum representable value, as is standard
    for unsigned integers.
- term: sign test
  definition: A check to determine if a value is positive, negative, or zero.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/59c8c4bbac46570ac36782172ed28569affe42c4
date: '2026-09-22'
is_stub: false
stub_reason: ''
---

This optimization pass folds comparisons involving the absolute value of a variable `x` and `x` itself. It handles both undefined-overflow and wrapping-overflow semantics, simplifying such comparisons to constants or sign tests. This transformation is applied even when `x` is unsigned after conversion. The new patterns reduce code complexity and enable further optimizations by making the relationship between `abs(x)` and `x` explicit.
