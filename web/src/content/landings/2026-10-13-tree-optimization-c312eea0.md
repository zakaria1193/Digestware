---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler
- loops
- memory
commit_hash: c312eea008ebfefc946d51cd064adaaa0efe8fb0
source_type: github
author: Richard Biener
headline: tree-optimization/127858 - fix memory access canonicalization in LIM
tldr: 'tree-optimization: Fixes memory access canonicalization in the Loop Intermediate
  Representation (LIM).'
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit corrects a bug in `tree-ssa-loop-im.cc` within the `gather_mem_refs_stmt`
  function. When canonicalizing memory accesses (merging them into a `MEM_REF`), if
  the original accesses had different access paths (base + offset), the existing `ao_refs`
  base and offset were not cleared. This change ensures they are reset to the canonical
  form by re-using the canonical `ao_ref`, fixing incorrect merging of memory accesses.
primer_glossary:
- term: memory access canonicalization
  definition: The process of transforming various forms of memory accesses (e.g.,
    with different base pointers or offsets) into a standard, simplified representation
    for easier analysis and optimization.
- term: LIM
  definition: Loop Intermediate Representation. A compiler internal representation
    specifically designed to facilitate analysis and transformation of loops.
- term: MEM_REF
  definition: A tree-based representation in GCC for a memory reference, typically
    consisting of a base address and an offset.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned a value exactly once, simplifying many compiler analyses
    and optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c312eea008ebfefc946d51cd064adaaa0efe8fb0
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

This commit resolves an issue in memory access canonicalization within the Loop Intermediate Representation (LIM). When merging memory accesses with differing access paths, the code incorrectly failed to clear the base and offset of the access path. The fix ensures that these are properly reset to their canonical form, preventing incorrect analysis and potential optimizations.
