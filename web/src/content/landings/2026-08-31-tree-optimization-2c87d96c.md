---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- bugfix
commit_hash: 2c87d96c31157ef45c0bb80b04c444d6891ef108
source_type: github
author: Richard Biener
headline: Fixes wrong code for vectorized reduction by restoring computation order.
tldr: Restores correct computation order for vectorized reduction to avoid wrong code.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: A regression introduced by a previous change (r17-3692) caused incorrect
  `vectype_in` computation in `vect_transform_reduction`. This commit reverts the
  problematic change by restoring the computation of `vec_in_num` to happen before
  the input array `vec_oprnds` is potentially mangled, thus fixing PR127152.
primer_glossary:
- term: vectorized reduction
  definition: A reduction operation (like sum or dot product) that has been optimized
    to use SIMD instructions, processing multiple data elements in parallel to produce
    a single result.
- term: vectype_in
  definition: Represents the data type of the input vector operand within the GCC
    tree-SSA representation during vectorization.
- term: vec_in_num
  definition: Indicates the number of vector input operands for a given operation
    or transformation during the GCC vectorization pass.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2c87d96c31157ef45c0bb80b04c444d6891ef108
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This commit fixes wrong code generated for vectorized reduction operations by restoring the original computation order of `vectype_in`. The number of input vector types (`vec_in_num`) is now computed before the input array is potentially modified, ensuring correctness. A new test case is included to verify the fix.
