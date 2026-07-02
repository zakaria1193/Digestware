---
project: gcc
subsystem: fold-const.cc
patch_id: null
tags:
- optimization
- constant folding
- refactoring
- warnings
commit_hash: 6ed5ed56da3d7450bd55334771930125c1131881
source_type: github
author: Daniel Barboza
headline: 'fold-const.cc: Overhaul tree_expr_nonnegative_(warn)_p'
tldr: The compiler refactors `tree_expr_nonnegative_warnv_p` to remove `strict_overflow_p`,
  simplifying its API and eliminating associated code.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit focuses on refactoring the `tree_expr_nonnegative_warnv_p`
  function within `fold-const.cc`, a part of GCC's constant folding mechanism. By
  removing the `strict_overflow_p` argument, the function simplifies to `tree_expr_nonnegative_p`,
  which determines if a tree expression is non-negative. This change eliminates strict
  overflow warnings and simplifies the code.
primer_general: Compilers use constant folding to evaluate constant expressions at
  compile time. Determining whether an expression is non-negative is important for
  various optimizations. This commit modifies a function responsible for this check
  (`tree_expr_nonnegative_warnv_p`) to remove an unnecessary flag related to strict
  overflow warnings, streamlining the code and potentially impacting the conditions
  under which overflow warnings are generated.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6ed5ed56da3d7450bd55334771930125c1131881
date: '2026-01-17'
is_stub: false
---

The compiler removes the `strict_overflow_p` argument from `tree_expr_nonnegative_warnv_p`, which is then renamed to `tree_expr_nonnegative_p`. This change simplifies the function's API and eliminates the need for local `strict_overflow_p` variables used with the `RECURSE()` macro. The original `tree_expr_nonnegative_p` function, which had a different API, is also removed, as its functionality is now covered by the modified `tree_expr_nonnegative_p`.
