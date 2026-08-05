---
project: gcc
subsystem: gcc/range-op-float
patch_id: null
tags:
- optimization
- gcc
- floating-point
- compiler bug
commit_hash: 217df27883c450f3f098bd0d1dc1ea7d5dbe8ff8
source_type: github
author: Jakub Jelinek
headline: Removes inappropriate frange_drop_infs call.
tldr: Corrects floating-point range analysis to avoid incorrectly dropping infinities.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In the `range-op-float` pass, the `operator_cast::fold_range` function
  was modified to call `frange_drop_infs` after handling integer-to-floating-point
  conversions. This was based on an incorrect assumption that integers converted to
  floats would never yield infinity. However, due to the limited range of `_Float16`
  or large `_BitInt` types, infinity can indeed be a result. This commit corrects
  the misstep by removing the `frange_drop_infs` call, ensuring that potential infinity
  values are not prematurely discarded during range analysis.
primer_glossary:
- term: range-op-float
  definition: A GCC optimization pass that analyzes and manipulates ranges of floating-point
    values to enable further optimizations.
- term: frange_drop_infs
  definition: A function within GCC's range analysis framework that removes positive
    or negative infinity from a floating-point range.
- term: operator_cast::fold_range
  definition: A method within the GCC compiler that optimizes range-based calculations
    involving type casts, particularly for floating-point numbers.
- term: _Float16
  definition: A half-precision floating-point data type, defined by the IEEE 754 standard,
    with a smaller range and precision than single-precision floats.
- term: _BitInt
  definition: A GCC extension for arbitrary-precision integers, allowing integers
    of specified bit lengths beyond standard types like int or long.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/217df27883c450f3f098bd0d1dc1ea7d5dbe8ff8
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

A call to `frange_drop_infs` was inappropriately added to the range analysis for integer-to-floating-point conversions. This function incorrectly removed positive or negative infinity from floating-point ranges, even when such values could legitimately result from conversions, especially with types like `_Float16` or large `_BitInt` values. The fix removes this call, allowing the analysis to correctly represent potential infinity values in the computed ranges.
