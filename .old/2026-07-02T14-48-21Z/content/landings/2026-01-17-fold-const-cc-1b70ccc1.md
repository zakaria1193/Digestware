---
project: gcc
subsystem: fold-const.cc
patch_id: null
tags:
- optimization
- constant folding
- refactoring
- warnings
- Gimple
commit_hash: 1b70ccc1cec6a80b5415006183970e53114ca312
source_type: github
author: Daniel Barboza
headline: 'fold-const.cc: Remove strict_overflow_p flag from tree_single_nonnegative_p'
tldr: The compiler removes the `strict_overflow_p` flag from `tree_single_nonnegative_p`
  and related Gimple functions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit continues the refactoring of `fold-const.cc`, specifically
  removing the `strict_overflow_p` flag from `tree_single_nonnegative_p`. This change
  ripples into `gimple-fold.cc`, affecting functions like `gimple_assign_nonnegative_warnv_p`
  and `gimple_phi_nonnegative_warnv_p` during Gimple SSA.
primer_general: This commit focuses on simplifying the compiler's constant folding
  process by removing a flag related to strict overflow checking. The changes affect
  functions that determine whether expressions are non-negative, both in the main
  tree representation and in the Gimple intermediate representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1b70ccc1cec6a80b5415006183970e53114ca312
date: '2026-01-17'
is_stub: false
---

The compiler removes the `strict_overflow_p` flag from `tree_single_nonnegative_p` as part of ongoing efforts to remove `fold_overflow_warn()` calls. This change also affects `gimple-fold.cc`, with similar modifications to `gimple_assign_nonnegative_warnv_p` and `gimple_phi_nonnegative_warnv_p`.
