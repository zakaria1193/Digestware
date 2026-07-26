---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- strlen
- constant folding
- bugfix
commit_hash: 1649ee187dfdb89f52e6acf15525465f77b67a64
source_type: github
author: Ashley Chekhova
headline: 'tree-optimization: Fix strlen(s) != 0 not folded into *s [PR92408]'
tldr: Fixes a bug where strlen(s) != 0 was not being optimized into *s != 0, improving
  constant folding.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `optimize_strlen_comp` function in `tree-ssa-forwprop.cc` has been
  enhanced to correctly rewrite `strlen(s) == 0` as `*s == 0` and `strlen(s) != 0`
  as `*s != 0`. This logic, previously limited by `PROP_last_full_fold` in `fold-const.cc`,
  is now integrated into the forward propagation pass. This addresses PR92408 by enabling
  the optimization in more complex scenarios involving SSA form, where variable assignments
  might have obscured the simple pattern.
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC optimization that operates on an intermediate representation
    called GENERIC/GIMPLE (often referred to as 'tree' internally), which is a higher-level
    representation than RTL, facilitating algebraic transformations and optimizations.
- term: strlen
  definition: A C standard library function that calculates the length of a null-terminated
    string. Optimizing checks involving strlen can reduce runtime overhead.
- term: constant folding
  definition: An optimization technique where expressions with constant operands are
    evaluated at compile time rather than runtime. For example, `2 + 3` would be replaced
    by `5`.
- term: forwprop
  definition: Forward propagation, an optimization pass that propagates constants
    and expressions through the code. It's often used to simplify code and enable
    further optimizations.
- term: SSA
  definition: Static Single Assignment form, an intermediate representation where
    every variable is assigned exactly once. This simplifies many analyses and optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1649ee187dfdb89f52e6acf15525465f77b67a64
date: '2026-07-25'
is_stub: false
stub_reason: ''
---

A bug in the tree optimization pass that prevented `strlen(s) != 0` from being folded into the more efficient check `*s != 0` has been fixed. Previously, this optimization was only applied in simple cases and not during complex scenarios involving variable assignments. The fix moves this logic to the `forwprop` pass, ensuring the optimization is applied more broadly and improving code generation for string checks.
