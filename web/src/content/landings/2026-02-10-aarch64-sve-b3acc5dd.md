---
project: gcc
subsystem: aarch64/sve
patch_id: null
tags:
- aarch64
- sve
- vectorization
- optimization
- performance
commit_hash: b3acc5dd98f44d152c9ac3bef9f26ab2d3fecef1
source_type: github
author: Christopher Bazley
headline: Optimize vec_init for partial SVE vector modes
tldr: GCC's AArch64 SVE backend now generates more efficient code for initializing
  partial vectors, improving performance for vectorized stores.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change targets the code generation for SVE vector initialization
  in `gcc/aarch64/sve.c`. Specifically, it addresses the `vec_init` intrinsic used
  for constructing vectors from scalar components, particularly when dealing with
  partially filled SVE vectors (e.g., when a loop has a vector tail). The optimization
  reduces the overhead of these initializations, which the cost model previously assumed
  to be cheap but were in practice inefficient, thus enabling more effective vectorization
  of stores.
primer_general: Compilers like GCC convert your human-readable code into machine instructions.
  For modern processors with vector extensions like ARM's Scalable Vector Extension
  (SVE), the compiler tries to group operations on multiple data items into a single
  vector instruction, which is much faster. This commit improves how GCC handles initializing
  'partial' vectors on AArch64 SVE. A partial vector occurs when you have some data
  to put into a vector register, but not enough to fill it completely. Previously,
  this process was inefficient, slowing down programs that could otherwise benefit
  from vectorization. This update makes that initialization much faster, leading to
  better-performing code, especially for loops that process data in chunks.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b3acc5dd98f44d152c9ac3bef9f26ab2d3fecef1
date: '2026-02-10'
is_stub: false
stub_reason: ''
---

This commit optimizes the `vec_init` operation within GCC's AArch64 SVE backend. Previously, initializing partial SVE vectors could be expensive, involving multiple write-modify-read operations and temporary stack storage. The change introduces more direct register moves, significantly reducing the instruction count and improving the profitability of vectorizing stores for basic block vectorization.
