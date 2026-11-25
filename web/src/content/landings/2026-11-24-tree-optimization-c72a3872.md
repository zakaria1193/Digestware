---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- tree-ssa
- performance
commit_hash: c72a38721a678c540e821c68b3e9e1ed2bd6017e
source_type: github
author: Michele Dionisio
headline: 'forwprop: Fold BIT_INSERT_EXPR chains into CONSTRUCTOR'
tldr: Optimizes chains of vector element insertions into single CONSTRUCTOR operations.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The forward propagation pass (`pass_forwprop`) now identifies and simplifies
  chains of `BIT_INSERT_EXPR`s. These chains often arise from element-wise vector
  initialization loops. The new `simplify_bit_insert_chain` function recognizes when
  such a chain effectively creates a vector where each element is assigned the same
  scalar value or when the initial vector is a `CONSTRUCTOR` or `VECTOR_CST` and the
  inserts complete it. It then replaces the chain with a single `CONSTRUCTOR` or `VECTOR_CST`,
  which can be more efficiently expanded by downstream passes into vector splat instructions
  (e.g., `sh…
primer_glossary:
- term: BIT_INSERT_EXPR
  definition: A GCC intermediate representation (tree) node representing an operation
    that inserts a value into a specific bitfield within a larger integer or vector
    type.
- term: CONSTRUCTOR
  definition: A GCC intermediate representation (tree) node used to represent the
    initialization of aggregate types, including vectors, by listing their element
    values.
- term: VECTOR_CST
  definition: A GCC intermediate representation (tree) node representing a constant
    vector.
- term: SLP vectorizer
  definition: Short, Loop, and Parallelism vectorizer; a GCC optimization pass that
    identifies opportunities to vectorize code by finding sequences of operations
    that can be performed on multiple data elements simultaneously.
- term: SSA
  definition: Static Single Assignment form, an intermediate representation where
    every variable is assigned exactly once. This simplifies many optimization passes.
- term: PHI node
  definition: In SSA form, a node that merges values from different control flow paths.
    An 'abnormal' PHI node might indicate complex control flow or potential issues.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c72a38721a678c540e821c68b3e9e1ed2bd6017e
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This commit optimizes chains of `BIT_INSERT_EXPR` operations that sequentially update vector elements. Instead of generating multiple instructions for each insert, the compiler now transforms such chains into a single `CONSTRUCTOR` (or `VECTOR_CST` for constants). This optimization significantly reduces instruction count for vector splats, translating to better performance on target architectures like x86-64 and aarch64.
