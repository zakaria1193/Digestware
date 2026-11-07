---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- gcc
- optimization
- loop optimization
- SROA
commit_hash: c71ad4260fe73a20c002721491a4d4291f1fb3d8
source_type: github
author: Richard Biener
headline: Preserve Scalar Replacement of Aggregates (SROA) during loop store motion
tldr: Ensures Scalar Replacement of Aggregates is maintained when moving stores within
  loops.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch fixes PR tree-optimization/128461 by ensuring that the Scalar
  Replacement of Aggregates (SROA) invariant is maintained during loop store motion.
  Specifically, the `gather_mem_refs_stmt` function in `tree-ssa-loop-im.cc` is modified
  to preserve SROA when building a canonicalized reference. This prevents the loop
  store motion pass from invalidating scalar replacements that were previously applied,
  ensuring that SSA-based optimizations continue to function correctly across loop
  transformations.
primer_glossary:
- term: Scalar Replacement of Aggregates (SROA)
  definition: An optimization pass in GCC that replaces accesses to fields of aggregate
    types (like structs) with accesses to scalar variables. This can enable further
    scalar optimizations.
- term: loop store motion
  definition: An optimization technique that moves store operations (writes to memory)
    within a loop to an earlier, invariant location, potentially reducing redundant
    stores.
- term: tree-ssa-loop-im.cc
  definition: A GCC source file that implements loop invariant code motion and other
    loop optimizations within the SSA (Static Single Assignment) representation.
- term: canonicalized reference
  definition: A standardized or normalized representation of a memory access, used
    within the compiler to simplify alias analysis and other memory-related optimizations.
- term: SSA (Static Single Assignment)
  definition: A property of intermediate representations where each variable is assigned
    a value exactly once. This simplifies many compiler analyses and optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c71ad4260fe73a20c002721491a4d4291f1fb3d8
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This commit enhances the loop store motion optimization in GCC by preserving Scalar Replacement of Aggregates (SROA). Previously, when performing loop store motion, the optimization could inadvertently break the SROA transformation. This patch modifies the `gather_mem_refs_stmt` function to correctly handle SROA when building canonicalized references, ensuring that scalar replacements are not lost during loop optimizations and potentially improving the effectiveness of SROA.
