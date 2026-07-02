---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- alignment
- ssa
commit_hash: 878b5b0030d4b42b94b7df38375d6bf5f187dc33
source_type: github
author: Richard Biener
headline: Forward propagation now preserves alignment for LHS assignments.
tldr: A bug in forward propagation that missed updating alignment for assignments
  to the left-hand side has been fixed.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch targets `forward_propagate_addr_expr_1` in `tree-ssa-forwprop.cc`,
  specifically rectifying an omission from a previous bug fix related to PR125296.
  The issue arose because the alignment of an address expression was not being preserved
  when propagated to the LHS (left-hand side) of an assignment. This oversight could
  lead to subsequent optimization passes or code generation making incorrect alignment
  assumptions, potentially penalizing performance or generating suboptimal code. The
  fix ensures that the original alignment information is correctly transferred, maintaining
  the semantic…
primer_general: Compilers like GCC try to optimize your code to make it run faster.
  One such optimization is called "forward propagation," where the compiler tracks
  how values change and tries to simplify expressions. When a program reads from memory,
  the location of that memory (its 'alignment') can be important for performance.
  This commit fixes a bug where, during an optimization, the compiler sometimes forgot
  to keep track of the correct alignment for certain memory operations, specifically
  when a value was being assigned to a memory location. This could cause the compiler
  to generate less efficient code, or in rare cases, incorrect code. The fix ensures
  that the compiler correctly preserves this alignment information, leading to more
  reliable and potentially faster optimized programs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/878b5b0030d4b42b94b7df38375d6bf5f187dc33
date: '2026-06-08'
is_stub: false
---

This commit fixes a bug in GCC's forward propagation pass where the alignment of expressions was not correctly preserved when propagating values into the left-hand side of an assignment. This oversight, introduced in a previous fix, could lead to incorrect assumptions about memory access alignment, potentially causing performance issues or incorrect code generation. The fix ensures that the original access alignment is maintained during such propagations.
