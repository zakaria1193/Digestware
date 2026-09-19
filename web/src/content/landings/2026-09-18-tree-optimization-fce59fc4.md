---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- tree-optimization
commit_hash: fce59fc4a405721468cd02eb0eba48a684e378e4
source_type: github
author: Richard Biener
headline: Avoid starting SLP groups with unvectorizable loads
tldr: Prevents SLP optimization from beginning a vectorization group with a load instruction
  that cannot be vectorized.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Fixes PR tree-optimization/127146 by refactoring `vect_build_slp_tree_3`
  in `tree-vect-slp.cc`. It duplicates the logic for rejecting non-grouped loads to
  happen before assigning `first_match`, thus avoiding the initiation of an SLP group
  with an unvectorizable load.
primer_glossary:
- term: SLP (Simultaneous Loop Parallelization)
  definition: A compiler optimization technique that identifies opportunities to perform
    loop-independent operations in parallel, even within a single iteration.
- term: SLP discovery
  definition: The phase within the SLP optimization where the compiler identifies
    potential parallelizable instruction patterns.
- term: unvectorizable load
  definition: A memory load instruction that the compiler's vectorization pass cannot
    effectively transform into a wider, parallel load operation.
- term: tree-vect-slp.cc
  definition: The GCC source file containing implementations for SLP vectorization.
- term: PR tree-optimization/127473
  definition: A bug report filed against the GCC tree-optimization component, specifically
    related to SLP vectorization issues.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fce59fc4a405721468cd02eb0eba48a684e378e4
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

This commit addresses a bug in SLP discovery by preventing it from starting a vectorization group with an unvectorizable load instruction. The change refactors how non-grouped loads are handled, ensuring that such loads are rejected early in the process before being incorrectly selected as the first match for a group.
