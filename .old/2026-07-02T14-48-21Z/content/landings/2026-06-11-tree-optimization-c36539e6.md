---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- induction variables
commit_hash: c36539e6fd0dfa6bd1ebb891df68da9a5bd96163
source_type: github
author: Richard Biener
headline: IVOPTs now properly tracks pointer IVs during affine canonicalization.
tldr: GCC's IVOPTs pass no longer converts pointer induction variables to unsigned
  integers before canonicalization, fixing a bug that led to lost base tracking.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The IVOPTs pass in `tree-ssa-loop-ivopts.cc` is responsible for optimizing
  induction variables, common in loops. A key function, `alloc_iv`, performs affine
  canonicalization to simplify these variables. The bug stemmed from converting pointer
  IVs to unsigned integers too early, prior to this canonicalization step. This obscured
  the original pointer information, making it difficult for IVOPTs to identify the
  base for `TARGET_MEM_REF` expressions. The fix ensures that pointer IVs retain their
  type until canonicalization is complete, preserving critical information for optimization.
primer_general: In computer programming, loops often use 'induction variables' that
  change predictably with each iteration, like `i` in `for (int i=0; i<N; ++i)`. Compilers
  have an optimization pass called Induction Variable Optimizations (IVOPTs) that
  aims to make these loops run faster by simplifying calculations involving these
  variables. Sometimes, these variables are pointers, which refer to memory locations.
  This commit fixes a bug where the compiler would temporarily treat these pointer
  variables as plain numbers too early in the optimization process. This made the
  compiler 'forget' that they were pointers, leading to less efficient or even incorrect
  code when accessing memory inside loops. The fix ensures the compiler correctly
  understands and optimizes pointer-based loops.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c36539e6fd0dfa6bd1ebb891df68da9a5bd96163
date: '2026-06-11'
is_stub: false
---

This commit resolves a bug in the Induction Variable Optimizations (IVOPTs) pass where pointer induction variables (IVs) were incorrectly converted to unsigned integers before affine canonicalization. This conversion caused IVOPTs to lose track of the original pointer base, leading to misoptimizations in `TARGET_MEM_REF` expressions. By preventing this premature conversion, the compiler can now correctly identify and optimize pointer-based loops, ensuring more efficient code generation.
