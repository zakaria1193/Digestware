---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- gcc
- optimization
- vectorization
- SLP
commit_hash: e2f1aec551be259b6ac562dae4f04eff77a06f23
source_type: github
author: Richard Biener
headline: Disable partial vectors for loads not covering whole vectors to prevent
  faults
tldr: Fixes vectorization by disabling partial vector loads when they don't align
  with vector boundaries, preventing memory access faults.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR tree-optimization/128433 by preventing the
  use of partial vectors for SLP (Short-Loop Parallelization) loads where the accessed
  group of scalars per vector iteration does not precisely fill a whole number of
  target vectors. Previously, `check_load_store_for_partial_vectors` in `tree-vect-stmts.cc`
  would round the vector count up and generate loop masks, leading to incorrect scalar
  counts per iteration. This could cause faults when the accesses crossed page boundaries
  or if loop lengths were misinterpreted. The fix ensures that such ambiguous loads
  do not enable partia…
primer_glossary:
- term: Vectorization
  definition: An optimization technique that allows the processor to perform the same
    operation on multiple data elements simultaneously using special vector instructions
    (SIMD).
- term: Partial Vectors
  definition: Vector operations that do not operate on a full vector width of data,
    often used when the data size is not a multiple of the vector width.
- term: SLP (Short-Loop Parallelization)
  definition: A compiler optimization technique that vectorizes sequences of identical
    or similar operations that occur close together in the code, even if they are
    not in a traditional loop.
- term: tree-vect-stmts.cc
  definition: A GCC source file containing routines related to statement transformations
    for vectorization.
- term: loop mask
  definition: A bitmask used in vector operations to control which elements within
    a vector are processed or updated, typically used to handle vectorized loops with
    non-vector-aligned trip counts.
- term: VF
  definition: Vector Factor. Represents the number of elements a vector instruction
    can process simultaneously.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e2f1aec551be259b6ac562dae4f04eff77a06f23
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This commit resolves an issue in GCC's vectorization optimization where partial vector loads could lead to memory access faults. The problem occurred when permuted SLP loads accessed a number of elements that did not perfectly fill a whole number of vectors. The `check_load_store_for_partial_vectors` function incorrectly rounded up the number of vectors and applied masks, causing out-of-bounds memory access. The fix disables the use of partial vectors in such cases, ensuring correct memory access and preventing program crashes.
