---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- memory-reference
- compiler-internals
commit_hash: 45a36dc994b3a6157111570b2601e8f632af7d5d
source_type: github
author: Xin Wang
headline: Loop Rearchitects Memory Reference Equality Logic
tldr: The Loop Interchangeable Memory (LIM) pass in GCC now clearly distinguishes
  between decomposed and non-decomposed memory references during equality checks.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses the `mem_ref_hasher::equal` function in `tree-ssa-loop-im.cc`,
  which is part of the Loop Interchangeable Memory (LIM) pass in GCC's tree-optimization.
  LIM is an optimization pass that aims to improve cache utilization by reordering
  loop iterations. Correctly identifying equal memory references is crucial for this
  pass to function as intended. The refinement separates the comparison logic for
  memory references that have been 'decomposed' into base-offset-size components from
  those that remain in their original, non-decomposed form, ensuring accurate hashing
  and comparison.
primer_general: Compilers like GCC try to make your programs run faster through various
  optimizations. One such optimization, called Loop Interchangeable Memory (LIM),
  focuses on loops in your code and how they access computer memory. To optimize memory
  access effectively, the compiler needs to be able to tell if two different ways
  of referring to memory actually point to the same location. This change clarifies
  how the compiler determines if two memory references are identical, specifically
  by making a clear distinction between simple memory references and those that have
  been broken down, or 'decomposed,' into their individual parts (like a starting
  address plus an offset). This ensures the optimization works correctly and efficiently.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/45a36dc994b3a6157111570b2601e8f632af7d5d
date: '2026-05-20'
is_stub: false
---

This commit refactors the `mem_ref_hasher::equal` function within GCC's Loop Interchangeable Memory (LIM) pass to explicitly handle decomposed and non-decomposed memory references. Previously, the equality logic was less clear, potentially leading to inconsistencies. The adjusted logic aligns with the existing `gather_mem_refs_stmt` function, ensuring that memory references are compared correctly based on their representation.
