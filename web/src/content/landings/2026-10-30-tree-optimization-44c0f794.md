---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- loop-optimization
commit_hash: 44c0f794dd4129f279ca9010955095307b981b55
source_type: github
author: Richard Biener
headline: Fix loop vectorizer's IV update for shift operations
tldr: Loop vectorizer's loop invariant variable update for shift operations now uses
  widest_int to prevent overflow and disallows early exits with non-constant itera…
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch revises the loop invariant variable (IV) update logic within
  GCC's vectorization passes, particularly for `vect_step_op_sh{lr}` operations in
  `tree-vect-loop.cc`. The previous implementation performed validity checks for IV
  updates using the IV's type, which could lead to overflow when the update involved
  shifts. The fix introduces `widest_int` for these checks, ensuring correctness for
  wider integer types. Additionally, `vect_can_peel_nonlinear_iv_p` in `tree-vect-loop-manip.cc`
  is updated to disallow early loop peeling when `skip_niters` is non-constant, further
  enhancing the sta…
primer_glossary:
- term: Loop Vectorizer
  definition: A compiler optimization pass that transforms a loop to execute its iterations
    in parallel using SIMD (Single Instruction, Multiple Data) instructions.
- term: Loop Invariant Variable (IV)
  definition: A variable whose value does not change within the iterations of a loop.
    In vectorization, such variables are often used to calculate loop bounds or stride.
- term: widest_int
  definition: An internal GCC type representing the largest possible integer type
    supported by the target, used for intermediate calculations to prevent overflow.
- term: SIMD
  definition: Single Instruction, Multiple Data. A class of parallel computers in
    Flynn's taxonomy that perform the same operation on multiple data points simultaneously.
- term: Scalar Epilog
  definition: The portion of code that executes after a vectorized loop, handling
    any remaining iterations that did not fit into a full vector width.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/44c0f794dd4129f279ca9010955095307b981b55
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This commit corrects how the loop vectorizer, specifically in `tree-vect-loop.cc`, calculates updates for loop invariant variables (IVs) involving shift operations. It now uses `widest_int` for validity checks to prevent potential overflows and disables early loop exits when the number of iterations is not constant. These changes improve the robustness and correctness of loop vectorization for certain shift-based IV updates and add new test cases to cover these scenarios.
