---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- SCEV
- loop optimization
commit_hash: 09e8d26982bf4280ec41b2e5215a57900517db7c
source_type: github
author: Steve Bezalel
headline: 'tree-optimization: Reset SCEV after predcom without unrolling'
tldr: SCEV results are now reset after loop predictive commoning when a loop is transformed
  but not unrolled, fixing a bug in invariant calculation.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit addresses a caching issue within `tree_predictive_commoning`
  related to Scalar Evolution (SCEV) analysis. Previously, `tree_predictive_commoning`
  only reset its cached SCEV data-reference analysis results if a loop was unrolled
  or required loop-closed SSA fixup (indicated by `changed > 1`). In common scenarios
  at `-O2` (where `predcom` runs implicitly via `-ftree-loop-vectorize` without unrolling),
  these cached results would persist. This led to `ivopts` using stale SCEV information,
  causing it to miss opportunities like strength-reducing stores because it didn't
  detect the loop's…
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC that operates on the SSA (Static Single Assignment) form
    of the code, performing various high-level optimizations.
- term: SCEV
  definition: Scalar Evolution. A compiler analysis technique used to determine properties
    of loop-invariant values and induction variables, crucial for loop optimizations.
- term: predcom
  definition: Predictive Commoning. A compiler optimization pass that hoists loop-invariant
    computations outside the loop.
- term: unrolling
  definition: A loop optimization technique where the loop body is duplicated multiple
    times to reduce loop overhead and expose more opportunities for instruction-level
    parallelism.
- term: SSA
  definition: Static Single Assignment. An intermediate representation where every
    variable is assigned a value exactly once, simplifying many optimization analyses.
- term: ivopts
  definition: Invariant Vector Optimization. A compiler pass that optimizes loops
    by identifying and moving loop-invariant computations out of the loop body.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/09e8d26982bf4280ec41b2e5215a57900517db7c
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

A bug in tree-optimization's predictive commoning pass caused Scalar Evolution (SCEV) results to be cached even when loops were transformed without unrolling. This led to incorrect invariant calculations in subsequent passes like `ivopts`, preventing optimizations such as strength reduction of stores. The issue occurred because SCEV results were only reset when loops were unrolled or underwent significant SSA fixups. This commit modifies the pass to reset SCEV whenever any loop transformation occurs, regardless of unrolling, ensuring accurate invariant analysis and enabling more optimizations at optimization levels like -O2.
