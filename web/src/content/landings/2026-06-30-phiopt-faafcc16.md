---
project: gcc
subsystem: phiopt
patch_id: null
tags:
- optimization
- compiler
- memory management
commit_hash: faafcc163b261d640aad43dacc645fbc43db757c
source_type: github
author: Andrew Pinski
headline: 'phiopt: Use remove_phi_node for efficiency'
tldr: Replaces `gsi_remove` with `remove_phi_node` in the phiopt pass for better memory
  management of PHI nodes.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit replaces calls to `gsi_remove` with `remove_phi_node` in
  `factor_out_conditional_operation` and `factor_out_conditional_load` within the
  `phiopt` pass. The former leaves the PHI node allocated, leading to delayed garbage
  collection. `remove_phi_node`, when called with `false` (indicating the PHI node's
  result is still used), correctly removes the PHI node from the GSI graph while ensuring
  its resources are managed efficiently.
primer_glossary:
- term: PHI node
  definition: A node in Static Single Assignment (SSA) form that represents the merging
    of values from different control flow paths. It determines which value to use
    based on which path was taken to reach the node.
- term: SSA form
  definition: Static Single Assignment form is an intermediate representation property
    where each variable is assigned a value exactly once. This simplifies many compiler
    optimizations.
- term: phiopt
  definition: An optimization pass in GCC that focuses on simplifying and optimizing
    PHI nodes in the SSA representation.
- term: gsi_remove
  definition: A function in GCC's internal representation often used to remove an
    instruction or node from the instruction stream without necessarily freeing its
    associated data structures immediately.
- term: remove_phi_node
  definition: A specific function in GCC's SSA infrastructure designed to correctly
    remove a PHI node from the graph, managing its associated memory and data structures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/faafcc163b261d640aad43dacc645fbc43db757c
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

The phiopt optimization pass in GCC has been refactored to use `remove_phi_node` instead of `gsi_remove` when processing PHI nodes. This change ensures that PHI nodes are immediately freed or made available for reuse, rather than remaining in memory until the next garbage collection cycle. This improves the efficiency of the phiopt pass.
