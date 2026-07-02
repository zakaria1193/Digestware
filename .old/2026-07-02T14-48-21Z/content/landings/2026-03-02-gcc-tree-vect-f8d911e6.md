---
project: gcc
subsystem: gcc/tree-vect
patch_id: null
tags:
- optimization
- vectorization
- SLP
commit_hash: f8d911e6ae3fc14c33780ab950511e2b5a20484c
source_type: github
author: Richard Biener
headline: Simplify Scalar Statement Coverage in vect_bb_slp_mark_live_stmts
tldr: The compiler now uses full scalar statement coverage to determine live lanes
  during vectorization more precisely.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit simplifies ``vect_bb_slp_mark_live_stmts`` by using ``SLP_TREE_TYPE``
  to determine ``STMT_VINFO_LIVE_P``, which is used for code generation of live lanes.
  This change removes the ``vec_slp_has_scalar_use`` function. The goal is to improve
  the precision of live lane detection during SLP vectorization.
primer_general: SLP vectorization is a compiler optimization that transforms scalar
  code into vector instructions for increased performance. This optimization identifies
  sequences of independent scalar operations that can be executed in parallel using
  vector registers. Determining which scalar statements are still "live" (i.e., their
  results are needed later) after vectorization is crucial for generating efficient
  code, this commit improves the precision of determining the liveness of lanes during
  the vectorization for better code generation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f8d911e6ae3fc14c33780ab950511e2b5a20484c
date: '2026-03-02'
---

This change simplifies the process of marking live statements in basic blocks during SLP vectorization. By utilizing the full scalar statement coverage denoted by SLP_TREE_TYPE, the compiler can more accurately identify which lanes are live for code generation, leading to potential performance improvements.
