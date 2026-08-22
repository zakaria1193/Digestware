---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- SLP
commit_hash: c3c082917c72ccf2928a39dc5e54a65245f46568
source_type: github
author: Richard Biener
headline: Fix SLP pattern representative checks for VEC_PERM nodes.
tldr: Corrects SLP vectorization by properly handling VEC_PERM nodes in pattern comparisons.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The SLP vectorizer in GCC uses `compatible_complex_nodes_p` to determine
  if two GIMPLE nodes can be part of the same vector operation. This function was
  incorrectly comparing `VEC_PERM` nodes when they still held a representative. This
  commit adds a special case for `VEC_PERM` to `compatible_complex_nodes_p`, ensuring
  that these specific permutation nodes are handled correctly and do not cause the
  SLP pass to misidentify compatible operations, thus avoiding incorrect vectorization.
primer_glossary:
- term: SLP
  definition: Superword Level Parallelism, an optimization technique that enables
    the compiler to identify and vectorize sequences of identical operations on different
    data elements.
- term: VEC_PERM
  definition: A GIMPLE operation representing a vector permutation, where elements
    from one or more vectors are rearranged to form a new vector.
- term: tree-optimization
  definition: GCC's optimization passes that operate on the GIMPLE intermediate representation.
- term: vectorization
  definition: The process of transforming code to use SIMD (Single Instruction, Multiple
    Data) instructions, allowing a single instruction to operate on multiple data
    elements simultaneously.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c3c082917c72ccf2928a39dc5e54a65245f46568
date: '2026-08-21'
is_stub: false
stub_reason: ''
---

This commit fixes an issue in the SLP (Superword Level Parallelism) vectorization pass where comparisons of complex nodes failed due to improper handling of `VEC_PERM` nodes. When these nodes still had a representative, the comparison logic incorrectly used arbitrary operations, leading to incorrect vectorization decisions. The fix ensures that `VEC_PERM` nodes are special-cased, preventing erroneous comparisons and improving the accuracy of vectorization.
