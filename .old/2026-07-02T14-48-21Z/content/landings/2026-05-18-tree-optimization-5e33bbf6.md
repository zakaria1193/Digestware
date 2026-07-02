---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop splitting
- bugfix
- profiling
commit_hash: 5e33bbf6faefa4f848e47e2a3bfec1a971d19cf2
source_type: github
author: Xin Wang
headline: 'tree-optimization: Fix profile update in loop splitting (initial_true=false)'
tldr: Fixes a bug in loop splitting that caused incorrect profile updates when the
  loop guard condition is inverted.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The patch addresses an issue in `tree-ssa-loop-split.cc`, specifically
  in the `split_loop` function, which performs iteration space splitting. The bug
  was related to profile update when the guard condition is swapped, resulting in
  `initial_true` being false. The fix ensures that `loop1_edge` and `loop2_edge` are
  derived correctly from `initial_true` and used consistently for `loop1_prob`, `fix_loop_bb_probability`,
  and iteration estimate scaling.
primer_general: Loop splitting is a compiler optimization technique that divides a
  loop into multiple versions, each handling a subset of the original iteration space.  This
  allows the compiler to optimize each version more effectively based on different
  conditions. This commit fixes a bug in how the compiler tracks the execution frequency
  (profile) of these split loops, ensuring that the performance data is accurate even
  when the loop's condition is inverted. Accurate profiling helps the compiler make
  better optimization decisions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5e33bbf6faefa4f848e47e2a3bfec1a971d19cf2
date: '2026-05-18'
is_stub: false
---

A bug in loop splitting's profile update logic has been fixed. When the loop splitting process inverts the guard condition of a loop (e.g., changing `t < i` to `i > t`), the profile update code was using incorrect edge probabilities. This resulted in inaccurate BB counts and iteration estimates for the split loops, especially when the `initial_true` flag was false. The fix ensures that profile quantities are correctly associated with the semantic edges of the split loops.
