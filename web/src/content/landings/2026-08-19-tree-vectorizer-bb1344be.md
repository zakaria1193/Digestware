---
project: gcc
subsystem: tree-vectorizer
patch_id: null
tags:
- tree-vectorizer
- optimization
- SLP
- performance
commit_hash: bb1344be44e364da8377603697933a668b651c4e
source_type: github
author: Richard Biener
headline: Decide vectorization factor (VF) independently of externals/constants.
tldr: Improves vectorization by basing the vectorization factor on assigned types,
  not external/constant node properties.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit modifies the SLP vectorizer's logic for choosing the vectorization
  factor (VF). Previously, `vect_update_slp_vf_for_node` used `max_nunits` which considered
  external and constant nodes, potentially leading to a suboptimal VF. The change
  makes the VF decision solely based on `SLP_TREE_VECTYPE`. This requires adjustments
  to functions like `vect_get_num_copies` to handle invariant vectors correctly, introducing
  `vect_get_num_copies_for_invariant` which uses `ceil_div`. The fundamental issue
  addressed is that `vectorizable_*` routines might receive invariant vectors with
  excess lanes,…
primer_glossary:
- term: VF
  definition: Vectorization Factor, indicating how many data elements are processed
    in parallel by a single SIMD instruction.
- term: SLP_TREE_VECTYPE
  definition: A field within the SLP tree structure that stores the determined vector
    type for a given operation.
- term: invariant nodes
  definition: In the context of vectorization, nodes representing values that do not
    change within the loop or vectorized region.
- term: ICE
  definition: Internal Compiler Error, a crash within the compiler itself, often due
    to unexpected program states or logic bugs.
- term: ceil_div
  definition: Ceiling division, which rounds the result of a division up to the nearest
    whole number.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bb1344be44e364da8377603697933a668b651c4e
date: '2026-08-19'
is_stub: false
stub_reason: ''
---

This commit refactors the SLP vectorizer to determine the vectorization factor (VF) based on the assigned `SLP_TREE_VECTYPE` rather than relying on `max_nunits` in the SLP graph, which previously included external and constant nodes. These external/constant nodes could artificially inflate the VF, leading to missed optimizations. By decoupling VF calculation from these nodes, the vectorizer can now select a more appropriate VF, resolving issues like ICEs in `vect_get_num_copies` and improving vectorization efficiency, particularly for code involving invariant data.
