---
project: gcc
subsystem: gcc/ranger-fold
patch_id: null
tags:
- optimization
- range analysis
- gimple
- ada
commit_hash: a94d2d065efd35473c113cfb38b87234218341a3
source_type: github
author: Andrew Pinski
headline: 'Ranger-fold: Avoid calling gimple_stmt_nonnegative_p with varying ranges.'
tldr: Range folding now correctly handles varying ranges by setting the range to `[type_min,
  type_max]` instead of calling `gimple_stmt_nonnegative_p`.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `ranger-fold` subsystem performs range analysis and folding on
  GIMPLE IR. This commit modifies `fold_using_range::fold_stmt` to avoid calling `gimple_stmt_nonnegative_p`
  when dealing with varying ranges.  Instead, it sets the range to `[type_min, type_max]`
  if the type's min/max differs from its precision. This change is relevant when the
  tree expression's nonnegative property is being determined via the ranger.  The
  issue could lead to recursion.
primer_general: Range analysis is a compiler optimization technique that tracks the
  possible range of values a variable can hold during program execution.  Range folding
  uses this information to simplify expressions and perform constant propagation.
  GIMPLE is the simplified intermediate representation (IR) used by GCC for optimization.  By
  improving the accuracy of range analysis, the compiler can generate more efficient
  code, potentially eliminating unnecessary computations and improving performance.
  This change targets a specific case where the range analysis was leading to incorrect
  assumptions, preventing further optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a94d2d065efd35473c113cfb38b87234218341a3
date: '2026-05-28'
is_stub: false
---

The range folding optimization now correctly handles varying ranges by setting the range to `[type_min, type_max]` when the precision is different from the type's min/max values, avoiding an infinite recursion.  Previously, it would call `gimple_stmt_nonnegative_p`, which always returned true for unsigned types, leading to incorrect range assumptions. This fix prevents potential recursion issues and may improve code generation, particularly for Ada.
