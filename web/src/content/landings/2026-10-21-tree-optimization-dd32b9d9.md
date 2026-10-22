---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- tree-optimization
commit_hash: dd32b9d9d1d74650c0e67dce5c5eef539846638e
source_type: github
author: Richard Biener
headline: tree-optimization/128069 - BB SLP and abnormal edges
tldr: Fixes vectorization by splitting basic blocks with abnormal edges to handle
  vector SSA flow correctly.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The vector SLP (Straight-Line Program) optimization pass in GCC relies
  on vector SSA, which cannot cross 'abnormal' control flow edges (e.g., setjmp/longjmp,
  exceptions). This commit modifies `vect_slp_function` in `tree-vect-slp.cc` to identify
  basic blocks with incoming abnormal edges and split the SLP region at those points.
  This ensures that the vectorization analysis remains confined within well-behaved
  control flow, resolving PR128069.
primer_glossary:
- term: BB SLP (Basic Block Straight-Line Program)
  definition: A compiler optimization technique that identifies sequences of identical
    or similar instructions within a basic block and replaces them with equivalent
    vector instructions.
- term: vectorization
  definition: The process of transforming code that operates on scalar values into
    code that operates on multiple data elements simultaneously using SIMD (Single
    Instruction, Multiple Data) instructions.
- term: SSA (Static Single Assignment)
  definition: An intermediate representation form used in compilers where every variable
    is assigned a value exactly once. This simplifies many data-flow analyses.
- term: abnormal edge
  definition: In control flow graphs, an edge that does not represent a standard sequential
    fall-through or conditional branch. Examples include edges from setjmp/longjmp
    or exception handling mechanisms.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dd32b9d9d1d74650c0e67dce5c5eef539846638e
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

This change addresses a limitation in the vector Strength Reduction (SLP) pass where it could not properly handle abnormal edges in the control flow graph. Abnormal edges, such as those created by exceptions or non-local jumps, prevent vector SSA flow analysis. The patch ensures that the BB SLP region is split at basic blocks with incoming abnormal edges, preventing misbehavior and enabling correct vectorization in such cases.
