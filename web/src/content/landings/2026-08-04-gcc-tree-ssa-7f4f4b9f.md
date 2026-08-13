---
project: gcc
subsystem: gcc/tree-ssa
patch_id: null
tags:
- optimization
- floating point
- range analysis
- bugfix
commit_hash: 7f4f4b9fe867c07b597412629c7b33636db4a066
source_type: github
author: Aldy Hernandez
headline: Convert range_operator::fold_range to use sub-ranges
tldr: Improves floating-point range analysis by correctly handling gaps between sub-ranges.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `range_operator::fold_range` in `range-op-float.cc` previously
  computed the hull of two input ranges. This commit modifies it to iterate over pairs
  of sub-ranges from each operand, compute their fold via `rv_fold`, and union the
  results. This preserves gaps between sub-ranges, similar to `irange::fold_range`.
  When operands are equal, it folds the diagonal (each sub-range against itself).
  This refactoring aims to improve the precision of Value Range Propagation (VRP)
  for floating-point types.
primer_glossary:
- term: range_operator::fold_range
  definition: A function within GCC that computes the resulting range when a binary
    operation is applied to two input ranges.
- term: sub-ranges
  definition: A portion of a larger range. In this context, a range might be composed
    of multiple disjoint sub-ranges, each with a lower and upper bound.
- term: Value Range Propagation (VRP)
  definition: A compiler optimization pass that determines the possible range of values
    for variables at different points in the program, enabling further optimizations.
- term: hull
  definition: In the context of ranges, the hull is the smallest continuous range
    that encompasses all the given points or sub-ranges.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7f4f4b9fe867c07b597412629c7b33636db4a066
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

The `fold_range` function in GCC's floating-point range analysis has been updated to process operands as pairs of sub-ranges. This change ensures that gaps between sub-ranges are preserved, rather than folding the entire hull, leading to more precise range analysis. It also optimizes by folding the diagonal when operands are known to be equal, mirroring the behavior of integer range analysis.
