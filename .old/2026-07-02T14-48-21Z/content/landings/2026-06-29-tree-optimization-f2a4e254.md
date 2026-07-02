---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop optimization
- compiler bug
commit_hash: f2a4e2540221cb731e5b4296885279da6c58576f
source_type: github
author: Richard Biener
headline: 'tree-optimization: Fix loop-invariant code motion with POINTER_PLUS_EXPR'
tldr: Fixes incorrect generation of POINTER_PLUS_EXPRs in loop-invariant code motion,
  resolving a performance regression.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses a regression in loop-invariant code motion (LICM)
  related to `POINTER_PLUS_EXPR` generation. The issue, PR125730, involved IVOPTs
  incorrectly creating these expressions when distributing memory references after
  affine transformations. The fix reverts a change in `alloc_iv` and modifies `add_to_parts`
  to use unsigned arithmetic for accumulating base addresses, preventing the spurious
  `POINTER_PLUS_EXPR` nodes that could disrupt subsequent optimizations or cause ICEs.
primer_general: Compilers optimize code to make it run faster. A common optimization
  is loop-invariant code motion, which moves calculations that don't change inside
  a loop to before the loop starts. This commit fixes a bug in how GCC handles a specific
  type of memory address calculation (`POINTER_PLUS_EXPR`) during this optimization.
  Previously, the compiler sometimes created incorrect memory address expressions,
  which could lead to performance issues or even crashes. The fix ensures these expressions
  are generated correctly, improving the efficiency and stability of the optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f2a4e2540221cb731e5b4296885279da6c58576f
date: '2026-06-29'
is_stub: false
stub_reason: ''
---

This commit corrects an issue where loop-invariant code motion incorrectly generated `POINTER_PLUS_EXPR` constructs. The problem stemmed from association performed by IVOPTs (invariant value optimizer) through `tree-affine` and `create_mem_ref` during code distribution. By reverting a previous change in `alloc_iv` and using unsigned arithmetic for base accumulation in `add_to_parts`, the compiler now avoids generating these erroneous expressions, thus fixing a bug and a related test case.
