---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- scalar evolution
- UB
- loops
commit_hash: 7686bcbb2b7b08688008a6a0e29e6561af1a9a98
source_type: github
author: Richard Biener
headline: Avoid undefined behavior in CHREC optimization for signed overflow
tldr: Ensures peeled CHREC optimization correctly guards against signed integer overflow
  to prevent undefined behavior.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `simplify_peeled_chrec` function in `tree-scalar-evolution.cc`
  is modified to guard the optimization when analyzing a CHREC with non-wrapping signed
  integer overflow. This prevents UB that could manifest in `infer_loop_bounds_from_signedness`
  and lead to incorrect `niter` analysis. A regression on `gomp/static-chunk-size-one.c`
  is adjusted.
primer_glossary:
- term: CHREC
  definition: Change Record, a data structure used in GCC's scalar evolution analysis
    to represent the evolution of a loop induction variable.
- term: peeled CHREC
  definition: A CHREC that has been processed or modified in a way that separates
    the first iteration of a loop from the rest, often to simplify analysis or enable
    further optimizations.
- term: scalar evolution
  definition: A compiler analysis pass that determines how variables change throughout
    a program, particularly within loops. It's used to find loop-invariant computations
    and optimize induction variables.
- term: undefined behavior (UB)
  definition: Program behavior that results from an operation that is not specified
    by the C or C++ standards. Compilers can make assumptions about UB, which can
    lead to unexpected results or optimizations.
- term: loop bounds analysis
  definition: The process of determining the starting and ending conditions, and the
    number of iterations, for loops in a program.
- term: induction variable
  definition: A variable in a loop whose value changes in a predictable way with each
    iteration, often used as a loop counter or to access array elements.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7686bcbb2b7b08688008a6a0e29e6561af1a9a98
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

An optimization for handling peeled CHRECs (CHange RECords) has been modified to prevent undefined behavior (UB) when dealing with signed integer overflow. Previously, this optimization could incorrectly infer loop bounds, leading to wrong iteration counts. The change guards the optimization when non-wrapping overflow is detected, ensuring correctness and preventing regressions in loop analysis and related optimizations.
