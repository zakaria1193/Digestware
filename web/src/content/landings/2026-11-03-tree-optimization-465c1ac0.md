---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- gcc
- floating-point
- optimization
commit_hash: 465c1ac0dddb92d38be6b602d1732478cc16e7ae
source_type: github
author: Richard Biener
headline: 'tree-optimization: Fix hosting of trapping FP comparisons'
tldr: Improves handling of potentially trapping floating-point operations in GCC's
  optimization passes.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vn_nary_may_trap` function in `tree-ssa-sccvn.cc` and `gimple_could_trap_p_1`
  in `gimple.cc` have been updated to correctly identify trapping behavior for floating-point
  comparisons and `FIX_TRUNC_EXPR`. This ensures that the Value Numbering (VN) and
  GIMPLE analysis passes do not incorrectly omit checks for operations that can trap,
  addressing issues related to FP exceptions and conversions that were tracked in
  PR128398 and PR128237.
primer_glossary:
- term: trapping FP comparisons
  definition: Floating-point comparisons that can raise an exception under certain
    conditions, such as comparing NaNs or operations involving denormalized numbers,
    depending on the floating-point environment settings.
- term: FIX_TRUNC_EXPR
  definition: A GCC internal representation (GIMPLE) for an expression that truncates
    a floating-point value to an integer type. This operation can trap if the floating-point
    value is outside the range of the target integer type.
- term: VEC_COND_EXPR
  definition: A GIMPLE expression representing a conditional selection between two
    values, often used in vector operations. This commit notes that these should not
    inherently trap.
- term: Value Numbering (VN)
  definition: An optimization technique that identifies equivalent expressions by
    assigning them a unique 'value number'. This allows the compiler to avoid recomputing
    expressions that have already been computed and determined to have the same value.
    `sccvn` refers to the Strongly Connected Components Value Numbering pass.
- term: GIMPLE
  definition: GCC's internal three-address code representation. It is designed to
    be simpler than RTL (Register Transfer Language) and is the primary intermediate
    representation for many optimization passes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/465c1ac0dddb92d38be6b602d1732478cc16e7ae
date: '2026-11-03'
is_stub: false
stub_reason: ''
---

This commit enhances GCC's ability to correctly analyze floating-point operations that might trap (e.g., due to NaN or overflow) within its optimization passes. It specifically fixes the `vn_nary_may_trap` function to properly identify trapping behaviors for FP comparisons and `FIX_TRUNC_EXPR` (float-to-integer conversions). This ensures that optimizations do not incorrectly assume these operations are safe, thus preventing potential runtime errors or unexpected behavior, particularly in the context of PR128398 and PR128237.
