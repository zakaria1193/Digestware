---
project: gcc
subsystem: gcc/tree-vect
patch_id: null
tags:
- vectorization
- SLP
- refactor
commit_hash: 6ef45ba65b3b19d8ae53d04bbfc1eef9cee141cc
source_type: github
author: Richard Biener
headline: Improve Code Flow in vect_slp_analyze_operations
tldr: This commit rearranges code within the vectorization analysis to improve code
  readability and isolate responsibilities.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit moves BB vect live statement marking out of ``vect_slp_analyze_operations``
  to ``vect_slp_analyze_bb_1`` and SLP statement marking, which marks some vectorized
  statements as ``PURE_SLP``, right before it. This change removes an unused overload
  of ``vect_mark_slp_stmts``.
primer_general: SLP vectorization is a compiler optimization that transforms scalar
  code into vector instructions for increased performance. During the analysis phase,
  the compiler identifies opportunities for vectorization and marks statements accordingly.  This
  commit rearranges some of the analysis code to improve the readability and organization
  of the vectorization process, which can make it easier to understand and maintain.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6ef45ba65b3b19d8ae53d04bbfc1eef9cee141cc
date: '2026-03-02'
---

This commit reorganizes the basic block vectorization live statement marking process. It moves the `vect_bb_slp_mark_live_stmts` call and SLP statement marking to `vect_slp_analyze_bb_1`, placing it right before its only consumer. This change aims to improve code flow and make the logic more obvious, which could help with maintainability and future development.
