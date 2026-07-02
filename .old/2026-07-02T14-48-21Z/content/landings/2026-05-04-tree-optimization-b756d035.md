---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- slp
- tree-optimization
commit_hash: b756d03533d7d0c92bd6a252cd4f3260973e93f5
source_type: github
author: Richard Biener
headline: 'Tree-optimization/125124: Disable sanity checking of BB SLP partitioning'
tldr: Disables a sanity check that verifies the correctness of basic block SLP partitioning,
  likely due to a bug in the check itself.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The SLP (Superword Level Parallelism) pass within GCC's tree-optimization
  pipeline attempts to vectorize code by operating on multiple scalar values simultaneously.  Basic
  block SLP partitioning divides the SLP graph within a basic block. The disabled
  sanity check in `vect_bb_slp_scalar_cost` was intended to verify the partitioning.  Disabling
  the check suggests a bug in the check itself (PR tree-optimization/125124), rather
  than in the partitioning algorithm.
primer_general: Tree optimization is a phase in the compilation process where the
  compiler analyzes and transforms the program's intermediate representation (IR)
  to improve performance. Vectorization is a type of optimization that converts scalar
  operations into vector operations, allowing the processor to perform the same operation
  on multiple data elements simultaneously. SLP (Superword Level Parallelism) is a
  vectorization technique that identifies opportunities to perform vector operations
  on adjacent scalar instructions. This commit disables a check within the SLP partitioning
  process, likely due to a bug in the check itself.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b756d03533d7d0c92bd6a252cd4f3260973e93f5
date: '2026-05-04'
---

This commit disables a sanity check that previously verified the correctness of basic block SLP partitioning within the tree-optimization pass. The check was likely found to be faulty, triggering false positives. Disabling it allows the compiler to proceed without interruption, while a proper fix for the sanity check is presumably investigated. A new test case is added.
