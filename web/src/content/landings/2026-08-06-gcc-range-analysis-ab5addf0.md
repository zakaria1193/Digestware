---
project: gcc
subsystem: gcc/range-analysis
patch_id: null
tags:
- optimization
- range analysis
- floating point
- zero
commit_hash: ab5addf0674f07d64b18695a54f1b43bb99e61a4
source_type: github
author: Aldy Hernandez
headline: Convert frange_add_zeros to use multi-range detection
tldr: Fixes floating-point zero handling in range analysis for complex multi-pair
  ranges.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Corrects `frange_add_zeros` in `range-op-float.cc` to properly handle
  multi-pair ranges containing zero. The prior implementation incorrectly used the
  hull endpoints to determine if zero was present, failing when zero was an interior
  point of a multi-pair range (e.g., `[-1.0,-0.0][1.0,1.0]`). The fix introduces a
  `contains_zero_p` method to accurately detect zero within any sub-range.
primer_glossary:
- term: frange_add_zeros
  definition: A function in GCC's floating-point range analysis that ensures both
    +0.0 and -0.0 are represented in the range if zero is a possible value.
- term: multi-range
  definition: A representation of a floating-point range that consists of multiple
    disjoint intervals (pairs of lower and upper bounds), used when a simple single
    interval is insufficient.
- term: hull
  definition: The smallest single interval that completely encloses all values of
    a given range or set of sub-ranges.
- term: +0.0 and -0.0
  definition: Signed zero values in floating-point arithmetic. While numerically equal,
    their signs can be significant in certain operations and comparisons.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ab5addf0674f07d64b18695a54f1b43bb99e61a4
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

This commit corrects the `frange_add_zeros` function in GCC's floating-point range analysis. Previously, it relied on the range's hull endpoints to detect the presence of zero, which failed for multi-pair ranges where zero might exist on an internal boundary. The function now uses a `contains_zero_p` method for more robust detection, ensuring that both positive and negative zero are correctly accounted for.
