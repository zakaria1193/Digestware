---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- SIMD
- ABI
commit_hash: bfa26edeed6c88d96ae8d83c605f98d40f56394d
source_type: github
author: Matthias Kretz
headline: 'libstdc++: Refactor ScalarAbi into Abi<N, N>'
tldr: SIMD ABI definitions are refactored to unify scalar and vector representations,
  improving consistency.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `_ScalarAbi` class, previously used to tag scalar SIMD types, has
  been removed and its functionality merged into the `_Abi` class. The `__scalar_abi_tag`
  trait now correctly identifies `_Abi<N, N>` types. This change fixes a bug where
  `_Ap::_S_is_bitmask` would incorrectly evaluate to true for scalar ABIs by adding
  a `!__scalar_abi_tag<_Ap>` condition. It also adjusts `_M_and_neighbors` and `_M_or_neighbors`
  in `simd_mask.h` to handle scalar bitmasks correctly.
primer_glossary:
- term: SIMD
  definition: Single Instruction, Multiple Data. A type of parallel processing where
    a single operation is performed on multiple data points simultaneously, significantly
    speeding up computations on large datasets. In GCC, SIMD support is integrated
    into <code>libstdc++</code> for vectorized types.
- term: ABI
  definition: Application Binary Interface. Defines how software components interact
    at the machine code level. In the context of SIMD, ABI variants specify how data
    is laid out and manipulated in vector registers.
- term: _ScalarAbi
  definition: A previous helper class in <code>libstdc++</code>'s SIMD implementation
    that specifically marked scalar types within the SIMD framework. It has been removed
    and its logic integrated into the more general `_Abi` template class.
- term: _Abi<N, N>
  definition: A refactored ABI tag in <code>libstdc++</code>'s SIMD implementation
    that represents both scalar and vector types, where N denotes the number of elements.
    This unification simplifies the ABI logic.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bfa26edeed6c88d96ae8d83c605f98d40f56394d
date: '2026-03-20'
is_stub: false
stub_reason: ''
---

This commit refactors the SIMD infrastructure by replacing `_ScalarAbi<N>` with a more general `_Abi<N, N>` template. This change unifies the representation of scalar and vector types within the ABI definitions, addressing issues where scalar ABI properties were incorrectly applied to vector types. The refactoring improves the accuracy of bitmask detection and rebind operations for SIMD types.
