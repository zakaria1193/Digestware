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
commit_hash: ab8cd1385e70f8e445d239b88a8ca514d70f2de8
source_type: github
author: Daniel Barboza
headline: 'fold-const.cc: Remove strict_overflow_p from tree_binary_nonnegative'
tldr: The compiler removes the `strict_overflow_p` flag from `tree_binary_nonnegative`
  and updates `gimple-fold.cc` accordingly.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit focuses on removing `strict_overflow_p` from `tree_binary_nonnegative_warnv_p`
  in `fold-const.cc`. Due to the `RECURSE()` macro, a local variable is introduced
  temporarily. Updates are reflected in `gimple-fold.cc`, particularly affecting `gimple_assign_nonnegative_warnv_p`
  during Gimple SSA.
primer_general: This commit removes overflow flags from the function `tree_binary_nonnegative_warnv_p`
  used during constant folding, as part of a larger effort to simplify overflow checking.
  This change impacts both the main tree representation and the Gimple intermediate
  representation within the compiler.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ab8cd1385e70f8e445d239b88a8ca514d70f2de8
date: '2026-01-17'
is_stub: false
---

The compiler removes the `strict_overflow_p` flag from `tree_binary_nonnegative_warnv_p`, renaming it to `tree_binary_nonnegative_p`. A local variable with the same name is temporarily added for the `RECURSE()` macro.  The change also necessitates updates to `gimple-fold.cc`.
