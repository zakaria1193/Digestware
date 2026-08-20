---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- refactor
commit_hash: cd962857ea3d8db2e7ed08f98df4152e7739e8cd
source_type: github
author: Richard Biener
headline: Avoid setting SLP_TREE_REPRESENTATIVE for vector permute operations
tldr: Vector SLP optimization now correctly handles permute nodes by not setting SLP_TREE_REPRESENTATIVE.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `SLP_TREE_REPRESENTATIVE` flag in GCC's SLP vectorization pass
  marks a node as the canonical representative for a group of identical or similar
  operations. For `VEC_PERM_EXPR` nodes, which represent vector permutations, this
  flag is often not applicable or can lead to incorrect analysis. This series of changes
  across `tree-vect-slp.cc` and `tree-vect-slp-patterns.cc` ensures that `SLP_TREE_REPRESENTATIVE`
  is consistently cleared or not set for these permute nodes. This involves adjustments
  in functions like `vect_slp_build_two_operator_nodes`, `vect_build_slp_tree_2`,
  `vect_lower_load_per…
primer_glossary:
- term: SLP vectorization
  definition: A compiler optimization technique that identifies sequences of identical
    or similar instructions operating on different data elements and replaces them
    with a single vector instruction that operates on multiple data elements simultaneously.
- term: VEC_PERM_EXPR
  definition: An internal GCC representation (tree node) for a vector permutation
    expression, which rearranges elements within a vector.
- term: SLP_TREE_REPRESENTATIVE
  definition: A flag or pointer within GCC's SLP vectorization framework that identifies
    a specific node as the canonical representative for a set of equivalent operations.
- term: CSE
  definition: Common Subexpression Elimination, an optimization that replaces multiple
    identical expressions with a single temporary variable holding the result.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cd962857ea3d8db2e7ed08f98df4152e7739e8cd
date: '2026-08-18'
is_stub: false
stub_reason: ''
---

This commit refactors GCC's SLP (Straight-Line-Progression) vectorization pass to consistently avoid setting the `SLP_TREE_REPRESENTATIVE` flag for `VEC_PERM_EXPR` nodes. Several functions within `tree-vect-slp.cc` and `tree-vect-slp-patterns.cc` have been adjusted to either not set this flag or to correctly handle cases where it is not set for permute operations. This change ensures that the SLP analysis and optimization of vector permutations are handled more robustly, preventing potential issues during CSE (Common Subexpression Elimination) and analysis.
