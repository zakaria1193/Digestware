---
project: gcc
subsystem: gcc/fold-const.cc
patch_id: null
tags:
- optimization
- constant folding
- overflow
commit_hash: 4c5a290ae5ab612941b6313d429978b9b19e48eb
source_type: github
author: Daniel Barboza
headline: Remove strict_overflow_p Flag from tree_expr_nonzero_warnv_p
tldr: The strict_overflow_p flag was removed from tree_expr_nonzero_warnv_p, which
  simplifies code and removes a call to fold_overflow_warn.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The commit removes the `strict_overflow_p` flag from `tree_expr_nonzero_warnv_p`
  in `fold-const.cc`.  This predicate determines if an expression is provably non-zero
  at compile time, and optionally emits a warning on overflow. After internal helper
  changes, the separate `strict_overflow_p` flag became unnecessary, as the function
  now handles overflow warnings internally. This simplifies the code and removes a
  direct call to `fold_overflow_warn`.  The larger context is deprecating `-Wstrict-overflow`,
  which relies on compile-time constant folding.
primer_general: GCC optimizes code by evaluating constant expressions at compile time,
  a process called constant folding.  Part of this involves determining if an expression's
  result will be non-zero.  The `tree_expr_nonzero_warnv_p` function checks this,
  and optionally warns about potential overflows. This commit removes an explicit
  flag (`strict_overflow_p`) that controlled the overflow warning behavior, integrating
  the warning logic directly into the function.  This is to simplify the code as part
  of deprecating the `-Wstrict-overflow` compiler flag, which controlled how aggressively
  the compiler warned about potential integer overflows during constant folding.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4c5a290ae5ab612941b6313d429978b9b19e48eb
date: '2026-01-17'
is_stub: false
---

The `strict_overflow_p` flag was removed from `tree_expr_nonzero_warnv_p`. This change allows the existing `tree_expr_nonzero_p` to be removed, as it becomes redundant. The function `tree_expr_nonzero_warnv_p` is then renamed to `tree_expr_nonzero_p` without changing the API or behavior for existing callers, ultimately removing a call to `fold_overflow_warn()`. This is part of a larger effort to deprecate the `-Wstrict-overflow` warning.
