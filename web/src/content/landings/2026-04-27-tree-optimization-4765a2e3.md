---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- memcpy
- mempcpy
- gimple
- performance
commit_hash: 4765a2e3980749c9eebd313b53d5be5aecf855be
source_type: github
author: Netanel Komm
headline: Tree-optimization Lowers mempcpy to memcpy When Result is Unused.
tldr: The compiler now optimizes `mempcpy` calls to `memcpy` when the return value
  is ignored, potentially improving performance.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change adds a case to `gimple_fold_builtin` in `gimple-fold.cc`
  to handle `BUILT_IN_MEMPCPY`.  When the result of `__builtin_mempcpy` is unused,
  it's replaced with `__builtin_memcpy`.  `gimple-fold.cc` is part of the tree-ssa
  optimisations.  The optimisation relies on the target providing an efficient implementation
  of `memcpy`.
primer_general: '`mempcpy` and `memcpy` are standard C library functions that copy
  memory. `mempcpy` returns a pointer to the end of the copied memory block, while
  `memcpy` returns a pointer to the beginning. If the return value is not needed,
  using `memcpy` can be more efficient because it avoids the overhead of calculating
  and returning the end pointer.  This commit optimizes code by replacing `mempcpy`
  with `memcpy` when the return value is ignored, which can lead to better performance,
  as modern architectures often have optimized `memcpy` implementations.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4765a2e3980749c9eebd313b53d5be5aecf855be
date: '2026-04-27'
---

The GIMPLE folding pass now transforms `__builtin_mempcpy` into `__builtin_memcpy` when the return value of `mempcpy` is unused.  Since many targets have highly optimized `memcpy` implementations, this transformation can improve code generation.  New tests were added to ensure both the unfolded and folded `mempcpy` are properly handled.
