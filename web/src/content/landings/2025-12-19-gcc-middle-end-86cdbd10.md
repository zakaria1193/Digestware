---
project: gcc
subsystem: gcc/middle-end
patch_id: null
tags:
- vectorization
- optimization
- middle-end
commit_hash: 86cdbd105172ac2c5ee93e1494d51b80354dbc97
source_type: github
author: Richard Biener
headline: Introduce tree_to_vec_perm_indices for vector permutation analysis
tldr: GCC adds a new utility function, `tree_to_vec_perm_indices`, to improve the
  accuracy of vector permutation analysis, especially for `vec_shl`/`vec_shr` recogni…
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `tree_to_vec_perm_indices` function streamlines the construction
  of `vec_perm_indices` from a `VEC_PERM_EXPR`'s operands, providing a more robust
  mechanism than `tree_to_vec_perm_builder`. This change is critical for `can_vec_perm_const_p`
  in `optabs-query.cc`, allowing it to accurately identify `vec_shl`/`vec_shr` patterns.
  This improved recognition of these specific permutations directly impacts `lower_vec_perm`
  in `tree-vect-generic.cc`, enabling more precise and efficient vector lowering decisions,
  ultimately enhancing the vectorizer's ability to optimize vector shifts.
primer_general: Compilers turn your human-readable code into machine instructions.
  To make programs run fast, they often use special instructions called "vector operations"
  that can process multiple pieces of data at once. A `VEC_PERM_EXPR` is a way the
  compiler represents rearranging elements within these groups of data. This change
  introduces a new internal tool (`tree_to_vec_perm_indices`) that helps the compiler
  better understand _how_ these elements are being rearranged. This is particularly
  important for operations like shifting vector elements left or right (`vec_shl`/`vec_shr`).
  By understanding these rearrangements more accurately, the compiler can make better
  decisions about how to optimize your code for vector processors, leading to faster
  execution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/86cdbd105172ac2c5ee93e1494d51b80354dbc97
date: '2025-12-19'
is_stub: false
stub_reason: ''
---

A new function, `tree_to_vec_perm_indices`, has been added to GCC to directly construct `vec_perm_indices` from all operands of a `VEC_PERM_EXPR`. This addresses inaccuracies in previous permutation analysis, particularly for `vec_shl`/`vec_shr` (vector shift left/right) patterns. By enabling `can_vec_perm_const_p` to recognize these patterns more reliably, the compiler can now make more informed decisions during vector lowering, leading to more efficient code generation and preventing misoptimizations.
