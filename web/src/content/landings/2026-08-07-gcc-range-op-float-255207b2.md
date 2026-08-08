---
project: gcc
subsystem: gcc/range-op-float
patch_id: null
tags:
- optimization
- floating-point
- compiler
commit_hash: 255207b2ce6168cd9620980d448dc23e2488de7f
source_type: github
author: Jakub Jelinek
headline: Fix float_widen_lhs_range for float range operations
tldr: Corrected float range widening to prevent overflows and ensure valid range calculations
  in floating-point operations.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `float_widen_lhs_range` function, previously a standalone utility,
  has been converted into a `frange` method. This refactoring addresses an overflow
  issue where passing `SIGNIFICANT_BITS` could lead to an excessively large extension
  of a floating-point range. The new `wlhs.widen(type)` method provides a more controlled
  widening, preventing the incorrect propagation of extreme values that previously
  caused problems with functions like `frange_nextafter` in reverse operations.
primer_glossary:
- term: float_widen_lhs_range
  definition: A GCC internal function used in floating-point range analysis to slightly
    extend a given floating-point range. This extension is intended to accommodate
    potential inaccuracies or representational differences during subsequent calculations.
- term: frange
  definition: GCC's internal representation and analysis framework for floating-point
    values, often used to track ranges of possible values for expressions.
- term: frange_nextafter
  definition: A function within GCC's floating-point range analysis that determines
    the next representable floating-point number after a given value. It's crucial
    for accurately representing the boundaries of computed ranges.
- term: PR109008
  definition: A GCC bug report related to a specific optimization that was affected
    by issues in floating-point range handling.
- term: ulp
  definition: Unit in the Last Place. Refers to the smallest possible change in the
    least significant bit of a floating-point number. ULP-based extensions are common
    in floating-point error analysis.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/255207b2ce6168cd9620980d448dc23e2488de7f
date: '2026-08-07'
is_stub: false
stub_reason: ''
---

The `float_widen_lhs_range` function in GCC's floating-point range analysis has been fixed to prevent potential overflows when extending ranges. The function now correctly handles cases where it's called with significand bits, ensuring that the widened range remains valid. This change rectifies issues in optimizations like PR109008 and improves the robustness of floating-point range operations, especially when interacting with `frange_nextafter`.
