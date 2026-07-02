---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- scev
- undefined-behavior
commit_hash: de3a13dd7f6c2856e96fc2b7924f9b34b638940f
source_type: github
author: Richard Biener
headline: SCEV constant folding avoids signed overflow undefined behavior.
tldr: A latent bug in SCEV's `chrec_fold_plus_poly_poly` that could lead to signed
  overflow undefined behavior has been addressed.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This fix targets a latent signed integer overflow vulnerability in
  `chrec_fold_plus_poly_poly` within `tree-chrec.cc`, a core component of GCC's Scalar
  Evolution (SCEV) framework used for analyzing loop induction variables. The function,
  which performs symbolic addition of polynomial CHRECs, could incur undefined behavior
  due to how it aggregates coefficients, particularly `CHREC_RIGHT`. While this patch,
  akin to r16-2781-gafafae097232e7, only explicitly handles cases involving constant
  terms, it mitigates the most common scenarios where this overflow might occur, thus
  reducing the risk of mi…
primer_general: Compilers often optimize loops in your code to make them run faster.
  A sophisticated part of this optimization is called "Scalar Evolution" (SCEV), which
  analyzes how variables change within loops. This commit fixes a hidden problem in
  GCC's SCEV component, specifically in a function that adds together different ways
  a variable can grow or shrink in a loop (called "polynomial CHRECs"). The problem
  was that this addition could sometimes cause a 'signed integer overflow,' which
  is when a number gets too large to fit into its storage, leading to unpredictable
  and incorrect behavior in the program. This fix prevents such overflows, especially
  when dealing with constant values in these calculations, making the compiler's loop
  optimizations more robust and less prone to generating incorrect code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/de3a13dd7f6c2856e96fc2b7924f9b34b638940f
date: '2026-06-08'
is_stub: false
---

This commit fixes a latent issue within GCC's Scalar Evolution (SCEV) component, specifically in the `chrec_fold_plus_poly_poly` function. The function, responsible for folding additions of polynomial chain of recurrences (CHREC), was susceptible to signed integer overflow, resulting in undefined behavior. The current fix, similar to a previous one, addresses the most common cases involving constants to prevent this overflow, improving the reliability of loop-related optimizations.
