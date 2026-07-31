---
project: gcc
subsystem: gcc/frange
patch_id: null
tags:
- optimization
- value-range analysis
commit_hash: 8cfdd1ed0f0da83a8426ac6a30e33dc945fbfcde
source_type: github
author: Aldy Hernandez
headline: Rewrite union to merge sub-ranges.
tldr: frange::union_ operation now correctly merges sub-ranges instead of widening
  to the hull.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The frange::union_ method was refactored to use set_pairs to merge
  sub-ranges from both operands, rather than computing the convex hull. Currently,
  MAX_PAIRS = 1, so set_pairs collapses the result. This is a precursor to raising
  MAX_PAIRS.
primer_glossary:
- term: frange::union_
  definition: A method within GCC for calculating the union of two value range sets,
    potentially comprising multiple sub-ranges.
- term: sub-ranges
  definition: Distinct, contiguous portions of a larger value range, used to represent
    more precise information about a variable's possible values.
- term: hull
  definition: The smallest convex set containing a given set of points. In this context,
    it refers to the minimal encompassing range that covers all sub-ranges.
- term: set_pairs
  definition: A function that sets or updates the sub-ranges within a frange object,
    potentially merging or normalizing them.
- term: MAX_PAIRS
  definition: A compile-time constant defining the maximum number of sub-ranges that
    can be stored in a frange object.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8cfdd1ed0f0da83a8426ac6a30e33dc945fbfcde
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

The `frange::union_` operation has been rewritten to correctly handle and merge sub-ranges. Previously, it would widen the result to the outer bounds (hull) of the combined ranges, losing precision. The new implementation merges the sub-ranges of both operands, resulting in a more accurate representation of the union, although currently, due to `MAX_PAIRS` still being one, the result is collapsed back to a single range by `set_pairs`. This change is a preparatory step for future enhancements.
