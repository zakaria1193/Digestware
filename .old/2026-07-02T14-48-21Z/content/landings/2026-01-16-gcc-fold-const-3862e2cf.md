---
project: gcc
subsystem: gcc/fold-const
patch_id: null
tags:
- optimization
- constant folding
- deprecated
- warning
commit_hash: 3862e2cf5d033bf6070b40b3f2c6b2bfb8942592
source_type: github
author: Daniel Barboza
headline: Remove code related to deferring -Wstrict-overflow warnings.
tldr: The compiler no longer defers `-Wstrict-overflow` warnings, since they are no
  longer issued.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This commit removes `fold_defer_overflow_warnings`, `fold_undefer_overflow_warnings`,
  `fold_deferring_overflow_warnings_p` from `fold-const.h` and `fold-const.cc`. It
  also removes uses of these functions in `gimple-fold.cc`, `passes.cc`, `tree-cfgcleanup.cc`,
  `tree-data-ref.cc`, `tree-ssa-ccp.cc`, `tree-ssa-forwprop.cc`, `tree-ssa-loop-niter.cc`,
  `tree-ssa-threadedge.cc`, and `tree-vrp.cc`. Search terms: GCC constant folding
  -Wstrict-overflow'
primer_general: Constant folding is a compiler optimization technique where expressions
  involving constants are evaluated at compile time instead of at runtime. This can
  improve performance by reducing the amount of work the CPU needs to do at runtime.
  This commit removes code related to handling `-Wstrict-overflow` warnings during
  constant folding.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3862e2cf5d033bf6070b40b3f2c6b2bfb8942592
date: '2026-01-16'
is_stub: false
---

The code for deferring `-Wstrict-overflow` warnings has been removed from the `fold-const.cc` file.  This includes removing the `fold_defer_overflow_warnings` counter, associated helper functions, and related logic in various compiler passes.  Since `-Wstrict-overflow` is now a no-op, this code is no longer needed.  This change simplifies the compiler and removes dead code.
