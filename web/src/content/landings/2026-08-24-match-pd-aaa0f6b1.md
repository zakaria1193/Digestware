---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- vectorization
- arm
- sve
- pr127039
commit_hash: aaa0f6b1e87bc62ea15da6eab431af6dcebf6414
source_type: github
author: Kyrylo Tkachov
headline: Fold reductions of vector duplicates and repeats [PR127039]
tldr: Optimizes vector reductions by folding idempotent operations on duplicate vectors.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Enhances `match.pd` and `fold_const_reduction` to handle idempotent
  vector reductions on duplicate or repeating vector constants. This includes folding
  `REDUC_MAX/MIN/AND/IOR` of `VEC_DUPLICATE_EXPR` to the duplicated element, and `REDUC_XOR`
  to zero for even lane counts. It handles both fixed-length and scalable vectors,
  and considers NaN propagation for floating-point reductions.
primer_glossary:
- term: REDUC_MAX/MIN/AND/IOR
  definition: Vector reduction operations that compute the maximum, minimum, bitwise
    AND, or bitwise OR across all lanes of a vector.
- term: VEC_DUPLICATE_EXPR
  definition: An expression that represents a vector where all elements are copies
    of a single scalar value.
- term: match.pd
  definition: A pattern matching file used by GCC for optimizing instruction selection,
    particularly for vector operations.
- term: SVE
  definition: Scalable Vector Extension, an ARM architecture extension providing vector
    processing capabilities with a vector length that can vary at runtime.
- term: NaN propagation
  definition: The behavior of floating-point operations where a NaN (Not a Number)
    input can result in a NaN output, potentially with specific signaling or quieting
    behavior.
discussion_id_link: github:gcc-mirror/gcc#127039
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/aaa0f6b1e87bc62ea15da6eab431af6dcebf6414
date: '2026-08-24'
is_stub: false
stub_reason: ''
---

This commit enables GCC to fold vector reductions like REDUC_MAX, REDUC_MIN, REDUC_AND, and REDUC_IOR when applied to duplicate vectors. For example, a `REDUC_MAX` of a vector `[x, x, x]` now simplifies to `x`. It also handles XOR reductions on duplicate vectors, folding them to zero if the lane count is provably even, and correctly processes scalable vectors.
