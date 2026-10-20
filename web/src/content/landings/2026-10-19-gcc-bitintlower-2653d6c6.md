---
project: gcc
subsystem: gcc/bitintlower
patch_id: null
tags:
- bitint
- ssa
- optimization
- register allocation
commit_hash: 2653d6c63d491dd8f61efff553ad4d7bcc33d53c
source_type: github
author: Jakub Jelinek
headline: 'bitintlower: Remove dead PHIs for large/huge _BitInt to fix coalescing'
tldr: Removes unused PHI nodes for large/huge _BitInt types before coalescing to prevent
  miscompilation.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `eliminate_useless_phis()` function in `tree-outof-ssa.cc` is crucial
  for optimizing SSA form. However, the coalescing logic for large/huge _BitInt SSA
  name subsets was exhibiting incorrect behavior when dead PHIs were present. This
  patch ensures that dead PHIs specific to these _BitInt types are removed prior to
  coalescing, preventing the reuse of SSA partitions that led to value clobbering
  and subsequent miscompilation in testcases like `bitint-111.c`.
primer_glossary:
- term: PHI node
  definition: In static single assignment (SSA) form, a PHI node is used to merge
    values from different control flow paths. It represents a variable that can have
    different definitions depending on which path was taken to reach that point.
- term: SSA (Static Single Assignment)
  definition: An intermediate representation property where every variable is assigned
    exactly once. This simplifies many compiler optimizations and analyses.
- term: Coalescing
  definition: A register allocation optimization where different virtual registers
    that hold the same value are merged into a single physical register or virtual
    register, reducing register pressure.
- term: _BitInt
  definition: A GCC extension for arbitrary-precision integers, allowing users to
    specify integers of any bit width.
- term: gimple-lower-bitint
  definition: A GCC compiler pass that lowers operations on _BitInt types into GIMPLE,
    GCC's intermediate representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2653d6c63d491dd8f61efff553ad4d7bcc33d53c
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This commit resolves a miscompilation issue related to large and huge _BitInt types by removing unused PHI nodes before the coalescing phase. The coalescing of SSA name subsets for these types was being confused by dead PHIs, leading to incorrect value clobbering and subsequent miscompilations. By cleaning up dead PHIs, the coalescing process now functions correctly.
