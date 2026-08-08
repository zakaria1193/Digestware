---
project: gcc
subsystem: gcc/range-op-float
patch_id: null
tags:
- optimization
- floating-point
- compiler
commit_hash: 5038e4ade5289798cdeb30723facb481d707c426
source_type: github
author: Aldy Hernandez
headline: Convert int to float casts to sub-ranges
tldr: Integer to float casts now correctly handle sub-ranges for more accurate floating-point
  range analysis.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `operator_cast::fold_range` function within `range-op-float.cc`
  was updated to iterate over and convert each integer sub-range of an input type,
  rather than just processing the bounding hull. This is essential because an integer
  range might be composed of multiple disjoint sub-ranges (e.g., due to prior reductions
  or analyses), and simply widening the hull could lose precision. The new `range_op_float_tests`
  verifies this behavior.
primer_glossary:
- term: range analysis
  definition: A compiler optimization technique that determines the possible range
    of values an expression can take during runtime. This information can be used
    to eliminate redundant checks or improve other optimizations.
- term: sub-ranges
  definition: In the context of range analysis, if a variable's possible values are
    not contiguous, they can be represented as a union of multiple disjoint ranges,
    known as sub-ranges.
- term: operator_cast::fold_range
  definition: A specific function within GCC's range analysis framework responsible
    for calculating the resulting range after a type cast operation.
- term: hull
  definition: The smallest convex set containing a given set of points. In range analysis,
    it typically refers to the minimum and maximum values of a range.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5038e4ade5289798cdeb30723facb481d707c426
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

GCC's range analysis for floating-point operations now correctly handles integer-to-float casts by processing each sub-range of the integer type individually. Previously, `operator_cast::fold_range` only considered the overall hull of the integer range, potentially leading to inaccuracies. This change improves the precision of floating-point range analysis, especially for complex integer-to-float conversions, and includes a new test case.
