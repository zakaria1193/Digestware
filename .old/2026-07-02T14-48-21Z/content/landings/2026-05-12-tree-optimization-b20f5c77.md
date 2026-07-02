---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- optimization
- gimple
commit_hash: b20f5c7760e4c5032e8f9d84145d3be7d0238029
source_type: github
author: Naveen
headline: 'Tree-optimization: Fold SAT_ADD at GIMPLE level'
tldr: Extends scalar SAT_ADD constant folding to recognize cases where one operand
  is zero.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit introduces optimizations for SAT_ADD operations at the
  GIMPLE level, specifically handling cases where one operand is zero. It involves
  modifying `fold-const-call.cc`, `match.pd`, and `genmatch.cc` to recognize and fold
  these specific SAT_ADD patterns.  The changes primarily affect the middle-end optimization
  passes of the compiler.
primer_general: SAT_ADD refers to saturating addition, where the result is clamped
  to a maximum or minimum value if the true sum exceeds the representable range. GIMPLE
  is a simplified intermediate representation of code used within GCC to perform optimizations.
  Constant folding involves evaluating constant expressions at compile time, replacing
  the expression with its result, thereby improving performance by reducing runtime
  calculations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b20f5c7760e4c5032e8f9d84145d3be7d0238029
date: '2026-05-12'
is_stub: false
---

This commit extends scalar SAT_ADD constant folding to recognize cases where one operand is zero at the GIMPLE level. By folding SAT_ADD expressions with constant operands early, it improves optimization opportunities and avoids emitting unnecessary SAT_ADD operations. This optimization can lead to more efficient code generation.
