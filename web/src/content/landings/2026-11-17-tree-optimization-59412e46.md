---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler bug
- memory optimization
commit_hash: 59412e46c04fc5a6142283983ae7f8ff3d520c88
source_type: github
author: Richard Biener
headline: 'Tree optimization: Avoid redundant store skipping on same-value stores'
tldr: Fixes redundant store elimination to avoid skipping stores with identical values,
  preventing incorrect code.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-sccvn.cc` implementation of Value Numbering (VN) for
  redundant store elimination had a flaw where it would skip stores with identical
  values (`same-val may-defs`). This behavior interfered with correctly identifying
  redundant stores and also impacted hash table insertions in `vn_walk_cb_data::finish`.
  This change modifies `vn_reference_lookup_3` to avoid skipping these same-value
  stores when performing redundant store elimination and adjusts `vn_walk_cb_data::finish`
  to handle the hash table insertion correctly. These changes resolve incorrect optimizations
  related to redundant…
primer_glossary:
- term: Value Numbering (VN)
  definition: An optimization technique that assigns a unique number (value number)
    to expressions that compute the same value, allowing the compiler to eliminate
    redundant computations.
- term: redundant store elimination
  definition: An optimization pass that removes store operations to memory if the
    value being stored is identical to a value already stored in the same location,
    and no intervening memory operations have occurred.
- term: tree-ssa-sccvn.cc
  definition: A GCC source file containing the implementation of the Sparse Conditional
    Constant Propagation and Value Numbering (SCCVN) optimization pass, which operates
    on the SSA representation of GIMPLE.
- term: may-defs
  definition: In optimization analysis, 'may-defs' refers to potential definitions
    (writes) to memory locations. 'Same-val may-defs' specifically indicates that
    the value being written is identical across these potential definitions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/59412e46c04fc5a6142283983ae7f8ff3d520c88
date: '2026-11-17'
is_stub: false
stub_reason: ''
---

This commit addresses issues in the Value Numbering (VN) based redundant store elimination pass by preventing it from skipping stores that write the same value. Previously, the optimization incorrectly skipped such stores when searching for redundant earlier stores, leading to incorrect code generation. The fix ensures that same-value stores are not skipped during redundant store elimination and are handled correctly during hash table insertions, resolving incorrect optimizations in test cases like `pr91091-2.c`.
