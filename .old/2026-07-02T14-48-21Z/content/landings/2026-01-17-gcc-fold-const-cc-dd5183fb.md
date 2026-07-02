---
project: gcc
subsystem: gcc/fold-const.cc
patch_id: null
tags:
- optimization
- constant folding
- overflow
commit_hash: dd5183fbcba0cd6a727aecd8ce86029eb1640499
source_type: github
author: Daniel Barboza
headline: Remove strict_overflow_p from tree_binary_nonzero_warnv_p
tldr: The strict_overflow_p flag was removed from tree_binary_nonzero_warnv_p, and
  the function was renamed to tree_binary_nonzero_p.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes the `strict_overflow_p` flag from `tree_binary_nonzero_warnv_p`
  in `fold-const.cc`. This function, called by `tree_expr_nonzero_warnv_p`, checks
  if a binary expression is provably non-zero. The `warnv` suffix is dropped as the
  function no longer throws overflow warnings directly; this logic is now handled
  elsewhere. This change contributes to the broader effort of deprecating the `-Wstrict-overflow`
  flag.
primer_general: GCC optimizes constant expressions at compile time. The `tree_binary_nonzero_warnv_p`
  function helps to determine if a binary expression is non-zero. The `warnv` suffix
  on the function name originally indicated that it might trigger overflow warnings.
  This commit removes the `strict_overflow_p` flag that controlled the warning and
  renames the function to `tree_binary_nonzero_p`. This change is part of a larger
  effort to deprecate the `-Wstrict-overflow` compiler flag.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dd5183fbcba0cd6a727aecd8ce86029eb1640499
date: '2026-01-17'
is_stub: false
---

The `strict_overflow_p` flag was removed from the `tree_binary_nonzero_warnv_p` helper function, and the function was renamed to `tree_binary_nonzero_p`. This helper is called by `tree_expr_nonzero_warnv_p`, which aims to eliminate a call to `fold_overflow_warning()`. The renaming reflects that the function no longer directly handles overflow warnings.
