---
project: gcc
subsystem: gcc/range-op-float
patch_id: null
tags:
- refactor
- gcc
- floating-point
commit_hash: dd4a1a6a494f3afc0fac9ad95824ddf9e1c459c8
source_type: github
author: Aldy Hernandez
headline: Factor float_widen_bound out of float_widen_lhs_range.
tldr: Refactors float range analysis code for better organization.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `range-op-float` pass analyzes and optimizes operations on floating-point
  ranges. This commit refactors `float_widen_lhs_range` by extracting its per-bound
  logic into `float_widen_bound`. This is a code organization change with no impact
  on the generated code or analysis results.
primer_glossary:
- term: float_widen_bound
  definition: A new helper function introduced to handle the widening logic for individual
    floating-point range bounds.
- term: float_widen_lhs_range
  definition: A function within the `range-op-float` pass that computes the widened
    range for the left-hand side of an operation.
- term: range-op-float
  definition: A GCC optimization pass that analyzes and manipulates ranges of floating-point
    values to enable further optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dd4a1a6a494f3afc0fac9ad95824ddf9e1c459c8
date: '2026-08-03'
is_stub: true
stub_reason: low_score
---

This change extracts the logic for widening floating-point range bounds into a new helper function, `float_widen_bound`. This improves code clarity and maintainability within the `float_widen_lhs_range` function. No functional changes or performance impacts are expected. The change was tested on ppc64le Linux.
