---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop
- crashfix
commit_hash: 8ff8114e4448307f27e38fbdb98028283ab64f1c
source_type: github
author: Richard Biener
headline: Fix crash in loop IV optimization due to missed folding
tldr: Avoid a crash in loop IV optimization when simplifying an induction variable
  candidate to zero.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-loop-ivopts.cc` file's `create_new_iv` function now guards
  against crashing when an invariant IV is encountered due to prior SCEV simplification.
  This handles a corner case where the IV step simplifies to zero, but the IV itself
  remains invariant, which could lead to unexpected states in the optimization.
primer_glossary:
- term: IVOPTs
  definition: Loop Invariant Code Motion optimization. It identifies computations
    within a loop that do not change with each iteration and moves them outside the
    loop to improve performance.
- term: SCEV
  definition: Scalar Evolution analysis. A compiler analysis that computes properties
    of values that evolve arithmetically over loops, such as induction variables.
- term: Induction Variable
  definition: A variable that is updated by a constant amount in each iteration of
    a loop, typically used for loop control or array indexing.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8ff8114e4448307f27e38fbdb98028283ab64f1c
date: '2026-08-18'
is_stub: false
stub_reason: ''
---

This commit addresses a crash in the loop invariant code (IVOPTs) optimization pass. Previously, if a simplification of an induction variable candidate resulted in a zero step, the Scalar Evolution (SCEV) analysis might still consider it an IV with a zero step. This change prevents a crash by handling cases where the IV is invariant.
