---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop optimization
- memory optimization
commit_hash: d7837b35f0195737e7afbb2a16f47b49ef743a91
source_type: github
author: Richard Biener
headline: Allow redundant store skipping on loop backedge
tldr: Redundant store elimination can now safely skip the store itself when encountered
  on a loop backedge.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-sccvn.cc` pass, specifically the `vn_reference_lookup`
  function, has been updated to handle redundant store elimination more robustly within
  loops. When searching for a redundant store, if the current statement being considered
  (`def_stmt`) is the same as the `redundant_store` being eliminated, and this encounter
  happens along a loop backedge, it can now be safely ignored. This is because the
  store being eliminated would not execute in any iteration if removed, thus not affecting
  effective types. The function parameter `redundant_store_removal_p` is changed to
  `gimple *redundant…
primer_glossary:
- term: loop backedge
  definition: In control flow graphs, a backedge is an edge that points from a node
    to one of its ancestors in the depth-first spanning tree. In loops, it typically
    represents the jump from the end of the loop body back to the loop header.
- term: TBAA
  definition: Type-Based Alias Analysis. An analysis technique used by compilers to
    determine whether two memory accesses might refer to the same memory location,
    based on the types of the data being accessed.
- term: effective type
  definition: The type of data that a memory access operation actually operates on,
    which may differ from the declared type due to type conversions or aliasing.
- term: gimple *redundant_store
  definition: A pointer to a GIMPLE statement that represents the specific store instruction
    being considered for elimination as redundant.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d7837b35f0195737e7afbb2a16f47b49ef743a91
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

This change enhances redundant store elimination by allowing the optimization to safely ignore a store instruction when it is encountered on a loop backedge. This is crucial because skipping the store itself on a backedge does not alter the program's effective types, even under TBAA (Type-Based Alias Analysis). The optimization can now correctly identify stores in loops as redundant with earlier stores before the loop, resolving issues seen in test cases like `pr87126.c`.
