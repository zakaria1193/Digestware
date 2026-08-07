---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- floating-point
- range analysis
commit_hash: b9c9f9350ca8cb8d0a59cb99b5e48f6f7328adc6
source_type: github
author: Aldy Hernandez
headline: Fix floating-point range comparisons with sub-ranges.
tldr: Correctly handles floating-point range equality and inequality checks when sub-ranges
  are involved.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `range-op-float.cc` implementation of `operator_equal::fold_range`
  and `operator_not_equal::fold_range` now uses the `irange::contains_zero_p` method.
  This addresses a bug where these operations incorrectly handled sub-ranges by only
  inspecting hull endpoints. The `contains_zero_p` method provides a more accurate
  check for the presence of zero within the potentially complex structure of nested
  or sub-ranged intervals, ensuring correct pruning of code involving such comparisons.
primer_glossary:
- term: sub-range
  definition: A portion of a larger range, representing a more specific interval within
    a broader one.
- term: constant folding
  definition: A compiler optimization that evaluates constant expressions at compile
    time rather than runtime.
- term: hull endpoints
  definition: The minimum and maximum values that define the outermost boundary of
    a range or a set of ranges.
- term: irange
  definition: An internal GCC representation for representing integer or floating-point
    ranges during optimization.
- term: contains_zero_p
  definition: A method or function that checks whether a given range (irange) includes
    the value zero.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b9c9f9350ca8cb8d0a59cb99b5e48f6f7328adc6
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

This change corrects a bug in floating-point range comparisons (`==` and `!=`) that affected cases involving sub-ranges. Previously, the compiler's range analysis incorrectly determined equality or inequality by only examining the outer boundaries of the ranges, missing situations where a zero value could be contained within a sub-range. This led to incorrect constant folding, for instance, where `e != 0.0` could be wrongly simplified to true.
