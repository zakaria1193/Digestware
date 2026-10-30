---
project: gcc
subsystem: gcc/vect
patch_id: null
tags:
- vectorization
- optimization
- x86
- cost model
commit_hash: 1dbbdf48e4d191dbde028c8b6dce7960630736ba
source_type: github
author: wangzicong
headline: Correctly calculate scalar loop costs for vectorization
tldr: Fixes vectorizer's double-counting of inner-loop frequencies when estimating
  scalar costs, improving loop vectorization accuracy.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `vect_compute_single_scalar_iteration_cost` function in `tree-vect-loop.cc`
  was double-counting loop frequencies. Specifically, it recorded the inner-loop frequency
  in the statement count, and then the target cost model re-applied it for outer-loop
  vectorization of scalar `vect_body` entries. This commit corrects this by having
  the function record unweighted counts and delegates frequency adjustments to the
  cost model, with specific handling for peeling iterations via a new function `vect_scalar_peeling_stmt_count`.
primer_glossary:
- term: vectorization
  definition: An optimization technique where a single instruction operates on multiple
    data elements simultaneously, significantly speeding up computations on large
    datasets.
- term: inner-loop frequency
  definition: The number of times a loop is expected to execute, used by the compiler
    to estimate the cost and potential benefit of vectorization.
- term: scalar costs
  definition: The estimated computational cost of executing code using scalar (single-element)
    operations, as opposed to vector (multiple-element) operations.
- term: peeling
  definition: A loop optimization technique where a small number of initial iterations
    are 'peeled off' and executed separately to align data or satisfy loop invariants,
    allowing the main loop body to be more easily vectorized.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1dbbdf48e4d191dbde028c8b6dce7960630736ba
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

The vectorizer incorrectly accounted for inner-loop frequencies when calculating scalar costs, leading to inaccurate estimates for outer-loop vectorization. This commit modifies `vect_compute_single_scalar_iteration_cost` to record unweighted statement counts and introduces `vect_scalar_peeling_stmt_count` to handle frequency adjustments specifically for peeling iterations. This ensures that scalar costs are estimated more accurately, particularly for x86 targets.
