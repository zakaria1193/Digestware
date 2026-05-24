---
project: gcc
subsystem: fold-const.cc
patch_id: null
tags:
- optimization
- constant folding
- refactoring
- warnings
commit_hash: 07299ccf1077ac12b6e449aefbd2cbd4196181a7
source_type: github
author: Daniel Barboza
headline: 'fold-const.cc: Remove strict_overflow_p from tree_expr_nonnegative helpers'
tldr: The compiler removes the `strict_overflow_p` flag from helper functions used
  by `tree_expr_nonnegative`, further simplifying the code.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit continues refactoring efforts within `fold-const.cc`, specifically
  targeting the removal of `strict_overflow_p` from helper functions associated with
  `tree_expr_nonnegative_warnv_p`. Functions like `tree_call_nonnegative_warnv_p`
  and `tree_invalid_nonnegative_warnv_p` are renamed and modified to remove the flag.
  Similar changes are made in `gimple-fold.cc`.
primer_general: As part of constant folding, compilers may check whether expressions
  are non-negative. This commit focuses on removing a flag related to strict overflow
  checking from helper functions used in this process. The changes streamline the
  code and prepare for the complete removal of overflow warning generation in this
  area.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/07299ccf1077ac12b6e449aefbd2cbd4196181a7
date: '2026-01-17'
is_stub: false
---

The compiler removes the `strict_overflow_p` flag from several helper functions used by `tree_expr_nonnegative_warnv_p`. This is part of an effort to remove `fold_overflow_warn()` calls. The `strict_overflow_p` argument in `tree_expr_nonnegative_warnv_p` is marked as unused in this commit and functions are renamed to reflect that they no longer handle warnings.
