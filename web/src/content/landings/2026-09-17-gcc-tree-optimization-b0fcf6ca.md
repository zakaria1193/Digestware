---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- vectorization
- optimization
- dependence-analysis
commit_hash: b0fcf6cab6b44d916992f17297d7c248d64469dc
source_type: github
author: Richard Biener
headline: Fix vectorizer dependence analysis for negative step stores
tldr: Vectorizer now correctly analyzes store dependencies with negative steps to
  preserve scalar order.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `vect_analyze_data_ref_dependence` function in `tree-vect-data-refs.cc`
  is updated to call `vect_preserves_scalar_order_p` even when the dependence distance
  is negative. Previously, this check was only performed for positive distances. This
  change ensures that the vectorizer correctly identifies and preserves the scalar
  order of stores, particularly in scenarios involving backwards iteration or memory
  access patterns, addressing PR tree-optimization/127407.
primer_glossary:
- term: vectorizer
  definition: A compiler optimization pass that transforms scalar code (operating
    on single data elements) into vector code (operating on multiple data elements
    simultaneously) to improve performance.
- term: dependence analysis
  definition: The process by which a compiler analyzes relationships between operations
    (e.g., reads and writes to memory) to determine if they can be reordered or executed
    in parallel. It's crucial for optimizations like vectorization and instruction-level
    parallelism.
- term: scalar order
  definition: The order in which individual, non-vectorized operations would execute.
    Preserving scalar order means ensuring that the vectorized operations produce
    the same memory state and observable effects as the original scalar operations,
    even if executed differently internally.
- term: store
  definition: A memory operation that writes data from a processor register to a specific
    memory location.
- term: dependence distance
  definition: In the context of data dependence, this refers to the difference in
    iteration count between two dependent accesses. A negative distance indicates
    that a later access in the original scalar code refers to an earlier memory location
    in the loop iteration.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b0fcf6cab6b44d916992f17297d7c248d64469dc
date: '2026-09-17'
is_stub: false
stub_reason: ''
---

A missed check in GCC's vectorizer's dependence analysis has been corrected. The analysis now properly considers the preservation of scalar order for stores that have a negative step distance. This ensures that the compiler generates correct code in cases where stores access memory locations in reverse order, preventing potential data corruption.
