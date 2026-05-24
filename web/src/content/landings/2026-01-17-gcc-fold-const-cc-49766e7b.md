---
project: gcc
subsystem: gcc/fold-const.cc
patch_id: null
tags:
- optimization
- constant folding
- overflow
commit_hash: 49766e7b5df144693dc3eda40e6d86e6f1c74b65
source_type: github
author: Daniel Barboza
headline: Remove strict_overflow_p from tree_unary_nonzero_warnv_p
tldr: The strict_overflow_p flag was removed from tree_unary_nonzero_warnv_p, which
  was then renamed to tree_unary_nonzero_p.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes `strict_overflow_p` from `tree_unary_nonzero_warnv_p`
  within `fold-const.cc`. This function, called by `tree_expr_nonzero_warnv_p`, determines
  if a unary expression is non-zero. As the function no longer directly handles overflow
  warnings, the `warnv` suffix is dropped.  The broader context is deprecating `-Wstrict-overflow`,
  which is not immediately obvious from the file itself.
primer_general: GCC optimizes code by simplifying constant expressions at compile
  time. The `tree_unary_nonzero_warnv_p` function helps determine if a unary expression
  is non-zero. This commit removes the `strict_overflow_p` flag, which controlled
  potential overflow warnings, and renames the function to `tree_unary_nonzero_p`.
  The `warnv` suffix indicated that the function might trigger overflow warnings,
  which is no longer the case. This is part of a larger effort to deprecate the `-Wstrict-overflow`
  compiler flag.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/49766e7b5df144693dc3eda40e6d86e6f1c74b65
date: '2026-01-17'
is_stub: false
---

The `strict_overflow_p` flag was removed from the `tree_unary_nonzero_warnv_p` helper function, and the function was subsequently renamed to `tree_unary_nonzero_p`.  This function is called by `tree_expr_nonzero_warnv_p`, which is part of a broader effort to remove calls to `fold_overflow_warning()`. The renaming reflects that the function no longer directly handles overflow warnings.
