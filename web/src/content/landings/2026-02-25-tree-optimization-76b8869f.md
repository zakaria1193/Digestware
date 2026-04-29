---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- slp
- cost modeling
commit_hash: 76b8869f08a6ca99c72596e481dd91b2d545643a
source_type: github
author: Richard Biener
headline: tree-optimization/124222 - rewrite BB SLP costing scalar coverage
tldr: GCC now uses vector coverage indicated by `SLP_TREE_TYPE` to improve and simplify
  basic block vector scalar costing, handling SLP patterns correctly.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch addresses PR tree-optimization/124222 and modifies `tree-vect-slp.cc`
  to improve BB vector scalar costing. The changes involve removing `vect_slp_gather_vectorized_scalar_stmts`
  and simplifying `vect_bb_slp_scalar_cost` by using `SLP_TREE_TYPE` and a use-def
  walk of the scalar stmts SSA uses. A new testcase, `gcc.dg/vect/costmodel/x86_64/costmodel-pr124222.c`,
  is added to verify the changes.
primer_general: Vectorization is a compiler optimization that converts scalar operations
  into vector operations, allowing the processor to perform the same operation on
  multiple data elements simultaneously. SLP (Superword Level Parallelism) is a technique
  that identifies independent scalar operations and combines them into vector operations.
  This commit improves the cost modeling used during SLP vectorization, enabling the
  compiler to make better decisions about when and how to vectorize code, leading
  to improved performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/76b8869f08a6ca99c72596e481dd91b2d545643a
date: '2026-02-25'
---

This commit rewrites the basic block (BB) SLP (Superword Level Parallelism) costing for scalar coverage in GCC. By utilizing the vector coverage indicated by `SLP_TREE_TYPE`, the compiler can now more accurately and efficiently assess the cost of vectorizing scalar operations within SLP patterns. This improvement simplifies the costing process and enables better vectorization decisions.
