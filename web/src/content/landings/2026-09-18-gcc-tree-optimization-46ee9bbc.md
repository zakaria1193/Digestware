---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- integer overflow
- compiler bug
commit_hash: 46ee9bbc9a7d92eb3435999b59c3d8b42254f88a
source_type: github
author: Kael Andrew Alonzo Franco
headline: Restrict (X {+,-} M*N) / N optimization to avoid overflow
tldr: Compiler avoids integer overflow by restricting an optimization for division
  by -1.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `tree-opt.c` `match.pd` pattern for simplifying `(X op M*N) / N`
  to `(X / N) op M` is overly aggressive. It fails to consider the overflow case of
  `INT_MIN / -1`. The fix adds checks to `match.pd` to prevent this specific overflow,
  ensuring the integrity of intermediate values during optimization.
primer_glossary:
- term: tree-optimization
  definition: A phase in the compiler where the code is represented as a tree structure
    to perform various high-level transformations and optimizations.
- term: INT_MIN
  definition: The smallest possible value for a signed integer type. Operations that
    result in a value less than INT_MIN cause an overflow.
- term: integer overflow
  definition: A condition that occurs when an arithmetic operation produces a result
    that exceeds the maximum or falls below the minimum value that can be represented
    by the data type.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/46ee9bbc9a7d92eb3435999b59c3d8b42254f88a
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

The compiler's tree optimizer previously performed an optimization on expressions of the form ((X {+,-} M*N) / N), simplifying it to ((X / N) {+,-} M). However, this transformation can cause integer overflow when X is INT_MIN and N is -1, because INT_MIN / -1 overflows while the original expression may not. This commit adds checks for X > INT_MIN and N != -1 to prevent this overflow.
