---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- integer
- compiler
- PR126627
commit_hash: ff133b4cd2202fc7a5be5cd9dc935c0a75fb6b68
source_type: github
author: Uttam Bhadauriya
headline: Simplify (a & -a) < 0 to a == INT_MIN.
tldr: Optimized a bitwise expression to a direct comparison for INT_MIN.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The pattern `(a & -a) < 0` in C/C++ evaluates to true if and only if
  `a` is the minimum value for its signed integer type (e.g., `INT_MIN`). This is
  because `-a` for `INT_MIN` results in `INT_MIN` itself (due to two's complement
  representation and overflow behavior), and `INT_MIN & INT_MIN` is `INT_MIN`, which
  is negative. The optimization is added to `match.pd` and is guarded by `!TYPE_OVERFLOW_TRAPS`
  to avoid removing potential traps when `-ftrapv` is used. The patch also accounts
  for negation on unsigned types using `negate_maybe_without_ud`.
primer_glossary:
- term: INT_MIN
  definition: A macro defined in `<limits.h>` (or equivalent) that represents the
    minimum value for a signed integer type.
- term: tree-optimization
  definition: A phase in the GCC compiler where the code is represented using an intermediate
    tree structure, allowing for various optimizations to be applied.
- term: match.pd
  definition: A file within GCC's source code that contains pattern matching rules
    for the tree-ssa (Static Single Assignment) optimization passes.
- term: two's complement
  definition: A standard method of representing signed integers in binary. It simplifies
    arithmetic operations and is used by most modern computers.
- term: -ftrapv
  definition: A GCC compiler flag that causes signed integer overflow to generate
    a runtime trap.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ff133b4cd2202fc7a5be5cd9dc935c0a75fb6b68
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This commit introduces an optimization that simplifies the expression `(a & -a) < 0` to `a == INT_MIN` for signed integers. This pattern occurs when the lowest set bit is the sign bit, which is characteristic of the minimum representable signed integer. The optimization is guarded by `!TYPE_OVERFLOW_TRAPS` to prevent incorrect simplification when traps are enabled, and it also handles unsigned negations. This change improves code efficiency by replacing a complex bitwise operation with a simpler equality check.
