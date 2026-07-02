---
project: gcc
subsystem: gcc/tree-vect
patch_id: null
tags:
- optimization
- vectorization
- SLP
commit_hash: 53e0c6b96561c4f2f7fc7831793c4ad8bd4db0f7
source_type: github
author: Richard Biener
headline: Compute Full Scalar Statement Coverage During Vectorization
tldr: The compiler now computes full scalar statement coverage during basic block
  vectorization for simpler and more precise live lane determination and scalar costi…
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit re-purposes ``STMT_SLP_TYPE`` for BB vectorization to indicate
  the scalar (non-pattern) statement coverage of the vectorized SLP graph.  New helper
  ``vect_slp_gather_extern_scalar_stmts`` is introduced. The goal is to simplify determining
  live lanes and scalar costing.
primer_general: SLP vectorization is a compiler optimization technique where sequences
  of scalar operations are transformed into vector instructions for parallel execution.
  After vectorizing a code block, it is essential to accurately track which original
  scalar statements are still relevant. This commit improves how the compiler tracks
  the coverage of scalar statements after vectorization, leading to more precise live
  lane detection and better cost analysis, which in turn can improve performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/53e0c6b96561c4f2f7fc7831793c4ad8bd4db0f7
date: '2026-03-03'
---

This commit re-purposes STMT_SLP_TYPE to indicate the scalar statement coverage of the vectorized SLP graph in basic block vectorization. This allows for simpler and more precise determination of live lanes and scalar costing, potentially improving the efficiency of vectorized code.
