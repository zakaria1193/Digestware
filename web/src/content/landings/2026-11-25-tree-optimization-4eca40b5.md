---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- reduction
commit_hash: 4eca40b54dd7763d571755cb13a91550f3bb56c5
source_type: github
author: Richard Biener
headline: Constrain even/odd widen multiplication use
tldr: Vectorization of even/odd widening multiplications is now restricted to non-conditional,
  non-masked, and non-fold-left reductions.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vectorizable_conversion` function in `tree-vect-stmts.cc` previously
  allowed even/odd widening multiplication to be used in reduction operations that
  might not support lane-swizzling. This commit adds checks to ensure that such reductions
  are strictly in-order and do not involve masking or fold-left semantics. This is
  important because widening multiplications rely on specific data movement patterns
  (lane-swizzling) that are not universally supported by all reduction types, preventing
  potential ICEs or incorrect vectorization.
primer_glossary:
- term: tree-optimization
  definition: A phase in the GCC compiler pipeline that operates on an intermediate
    representation called GENERIC and GIMPLE, performing various high-level optimizations.
- term: even/odd widen multiplication
  definition: A vector multiplication operation where the results of two parallel
    multiplications (e.g., even lanes and odd lanes) are combined or widened into
    a larger result.
- term: reduction
  definition: A loop operation that combines elements of a vector or array into a
    single result (e.g., sum, product, minimum, maximum).
- term: lane-swizzling
  definition: Reordering or shuffling of elements within a vector register, often
    used to align data for specific operations.
- term: masked operation
  definition: A vector operation where only a subset of the vector lanes (determined
    by a mask) are affected.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4eca40b54dd7763d571755cb13a91550f3bb56c5
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This commit refines the vectorization rules for even/odd widening multiplications to prevent incorrect code generation. The `vectorizable_conversion` function now correctly constrains the use of these operations, ensuring they are only applied to reduction operations that do not involve conditional logic, masking, or fold-left patterns. This avoids issues where lane-swizzling reduction operations, which are integral to widening multiplications, would not be applicable.
