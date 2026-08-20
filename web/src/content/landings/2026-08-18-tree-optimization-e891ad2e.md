---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- cost-model
commit_hash: e891ad2e77a5373d62af39c8b5f815993fccf253
source_type: github
author: Richard Biener
headline: Assign vertex weight to all SLP nodes, including those without representatives
tldr: SLP optimization now assigns vertex weights to all nodes, ensuring consistent
  cost analysis even for nodes without a representative.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In GCC's SLP vectorization, `SLP_TREE_REPRESENTATIVE` identifies a
  canonical node for a group of equivalent operations. Some nodes, particularly `VEC_PERM_EXPR`
  nodes, may not have a representative. The `vect_slp_node_weight` function calculates
  a cost weight for each SLP node, used in layout selection. This commit modifies
  `vect_slp_node_weight` to accept `vinfo` (vector information) as context and, when
  no representative is present, uses the `region_entry_block` to determine the weight.
  Furthermore, `vect_optimize_slp_pass::start_choosing_layouts` now guarantees that
  a vertex weight is assi…
primer_glossary:
- term: SLP vectorization
  definition: A compiler optimization technique that identifies sequences of identical
    or similar instructions operating on different data elements and replaces them
    with a single vector instruction that operates on multiple data elements simultaneously.
- term: SLP_TREE_REPRESENTATIVE
  definition: A flag or pointer within GCC's SLP vectorization framework that identifies
    a specific node as the canonical representative for a set of equivalent operations.
- term: Vertex weight
  definition: In the context of graph-based optimizations like SLP, a 'weight' assigned
    to a node, likely representing its cost or importance in the optimization process.
- term: Region entry block
  definition: The first basic block of a control flow region within the compiler's
    intermediate representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e891ad2e77a5373d62af39c8b5f815993fccf253
date: '2026-08-18'
is_stub: false
stub_reason: ''
---

This change ensures that all nodes within GCC's SLP (Straight-Line-Progression) vectorization process are assigned a vertex weight, which is used for cost-based analysis. Previously, nodes lacking an `SLP_TREE_REPRESENTATIVE` might not have had their weights initialized, potentially leading to incorrect cost estimations. The `vect_slp_node_weight` function is updated to use the region entry block for context when a representative is absent, and `vect_optimize_slp_pass::start_choosing_layouts` now unconditionally assigns a vertex weight to all nodes.
