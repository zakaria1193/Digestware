---
project: gcc
subsystem: gcc/vectorization
patch_id: null
tags:
- vectorization
- optimization
commit_hash: d94e8b70b025afa1f7de15149a07377f6dd59ae2
source_type: github
author: Richard Biener
headline: Simplify vect_schedule_slp_node
tldr: Simplifies the calculation of loop iterations for SLP scheduling in the vectorization
  pass.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `vect_schedule_slp_node` function in `tree-vect-slp.cc` is part
  of the SLP (Scalar and Vector Linking) vectorizer, which attempts to vectorize loops
  by identifying straight-line code sequences (basic blocks) that can be executed
  as vector instructions. This commit simplifies the calculation of the number of
  iterations required for scheduling these SLP nodes, likely by optimizing how loop
  bounds or trip counts are determined and used in the scheduling heuristic. The goal
  is to improve the efficiency and effectiveness of the SLP vectorizer's ability to
  schedule vector operations.
primer_glossary:
- term: SLP scheduling
  definition: Scalar and Vector Linking (SLP) is a loop vectorization technique that
    identifies opportunities to combine scalar operations within a basic block into
    a single vector instruction. SLP scheduling refers to the process of ordering
    these vector operations, considering dependencies and loop structure.
- term: vectorization
  definition: The process by which a compiler transforms code that operates on single
    data items into code that operates on multiple data items simultaneously using
    special CPU instructions (e.g., SIMD instructions). This can significantly speed
    up data-parallel computations.
- term: basic block
  definition: A sequence of consecutive instructions with exactly one entry point
    (the first instruction) and one exit point (the last instruction). Compilers often
    analyze and transform code at the basic block level.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d94e8b70b025afa1f7de15149a07377f6dd59ae2
date: '2026-07-22'
is_stub: false
stub_reason: ''
---

The `vect_schedule_slp_node` function within GCC's vectorization pass has been simplified. This change improves the computation of loop iterations during the Scalar and Vector Linking (SLP) scheduling phase, aiming for a more efficient and robust scheduling process.
