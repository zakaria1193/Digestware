---
project: gcc
subsystem: gcc/fold-const.cc
patch_id: null
tags:
- optimization
- constant folding
- overflow
commit_hash: e27a905ad03c0e8cbbefb0d94f14dc570ad233f1
source_type: github
author: Daniel Barboza
headline: Remove strict_overflow_p from tree_single_nonzero_warnv_p
tldr: The strict_overflow_p flag was removed from tree_single_nonzero_warnv_p and
  the function was renamed to tree_single_nonzero_p.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes `strict_overflow_p` from `tree_single_nonzero_warnv_p`
  within `fold-const.cc`. This function helps determine if a single-operand expression
  is provably non-zero, and is called by `tree_expr_nonzero_warnv_p`.  The `warnv`
  suffix indicated potential emission of overflow warnings, which are now handled
  differently. The ripple effect touches various optimization passes like IPA and
  SSA reassoc. Outside the immediate files, the connection to the larger `-Wstrict-overflow`
  deprecation effort might not be obvious.
primer_general: GCC optimizes code by simplifying constant expressions at compile
  time. `tree_single_nonzero_warnv_p` helps determine if a single-operand expression
  is non-zero.  Originally, the `warnv` suffix implied the function might trigger
  overflow warnings during this check. This commit removes the `strict_overflow_p`
  flag, which controlled this warning behavior, and renames the function to `tree_single_nonzero_p`.
  This is a step to deprecate the `-Wstrict-overflow` flag, which controlled how aggressively
  the compiler warned about potential integer overflows during constant folding.  The
  changes impact several files, showing the widespread usage of compile-time range
  analysis.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e27a905ad03c0e8cbbefb0d94f14dc570ad233f1
date: '2026-01-17'
is_stub: false
---

The `strict_overflow_p` flag was removed from the `tree_single_nonzero_warnv_p` helper function. This helper is part of the larger `tree_expr_nonzero_warnv_p` function, which aims to eliminate a call to `fold_overflow_warning()`. As part of the change, the helper was renamed to `tree_single_nonzero_p` to reflect that it no longer handles overflow warnings directly. This change also impacts `c-ubsan.cc`, `gimple-range-fold.cc`, `ipa-prop.cc`, `tree-ssa-phiopt.cc`, and `value-query.cc`.
