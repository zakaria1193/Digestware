---
project: gcc
subsystem: avoid-store-forwarding
patch_id: null
tags:
- optimization
- store-forwarding
- performance
- gcc
commit_hash: 9892eb566c4cbf6feba50c7d98b10ea8c204018a
source_type: github
author: Konstantinos Eleftheriou
headline: 'Avoid-store-forwarding: Remove unnecessary store_exprs_del mechanism'
tldr: The avoid-store-forwarding pass removes an unnecessary mechanism that caused
  O(n^2) behavior for large basic blocks.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `store_exprs_del` vector in `store_forwarding_analyzer::avoid_store_forwarding`
  is removed. This vector was a conservative measure added alongside the PR119795
  fixes.  It's now deemed unnecessary because the load reads all bytes from memory
  in the non-load-elimination path, and all bytes are covered by forwarded stores
  in the load-elimination path.  The quadratic complexity arose from scanning this
  vector for each forwarding candidate.  A toolchain developer might not immediately
  appreciate the performance impact on large basic blocks.
primer_general: Store forwarding is a compiler optimization technique that reduces
  memory accesses by having a load instruction retrieve data directly from a previous
  store instruction. This commit removes an unnecessary check in the compiler's store-forwarding
  optimization, which simplifies the code and improves performance.  The removed check
  was causing the compiler to take much longer to optimize code in some cases. This
  change makes the compiler faster and more efficient.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9892eb566c4cbf6feba50c7d98b10ea8c204018a
date: '2026-03-24'
is_stub: false
---

The `store_exprs_del` vector in GCC's avoid-store-forwarding pass was introduced as a safety measure but is no longer needed for correctness.  Its removal simplifies the code and eliminates an O(n^2) scan, improving performance for large basic blocks. The vector tracked deleted store candidates and blocked forwarding when a deleted store's range overlapped with the load, but the intended memory effects were already visible.
