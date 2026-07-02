---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- simd
- refactoring
commit_hash: bfa26edeed6c88d96ae8d83c605f98d40f56394d
source_type: github
author: Matthias Kretz
headline: 'libstdc++: SIMD scalar ABI refactored'
tldr: SIMD scalar ABI handling in libstdc++ is refactored, with `_ScalarAbi<N>` replaced
  by `_Abi<N, N>`, improving logic for bitmask usage and scalar type identific…
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The refactoring consolidates SIMD ABI traits by removing `_ScalarAbi<N>`
  in favor of `_Abi<N, N>`. The `__scalar_abi_tag` now correctly identifies `_Abi<N,
  N>` as scalar. This necessitated changes to `_S_is_bitmask` logic in `simd_mask.h`
  and `simd_vec.h`; it's now only true if `!_S_is_scalar`, preventing incorrect short-circuiting.
  For `_S_nreg == 1` specializations, explicit checks `!__scalar_abi_tag<_Ap>` are
  used. The `_S_is_bitmask` bit is retained in `__scalar_abi_tag` for `__abi_rebind`
  compatibility. Test cases in `traits_impl.cc` were updated.
primer_general: This commit revises how the C++ Standard Library (libstdc++) internally
  represents and manages vectorized data types for SIMD (Single Instruction, Multiple
  Data) operations. The concept of a 'scalar ABI' (how single, non-vectorized values
  are handled) has been updated. Previously, a separate category `_ScalarAbi` existed;
  it's now integrated into the more general `_Abi` structure. This change cleans up
  the internal logic, ensuring that SIMD operations correctly identify whether they
  are dealing with a truly scalar type versus a vector type, which impacts how certain
  optimizations, like bitmask operations, are applied.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bfa26edeed6c88d96ae8d83c605f98d40f56394d
date: '2026-03-20'
is_stub: false
stub_reason: ''
---

The handling of scalar ABI traits within libstdc++'s SIMD infrastructure has been refactored. The `_ScalarAbi<N>` class has been removed and replaced by `_Abi<N, N>`, where `N` represents the number of elements. This change clarifies the distinction between scalar and vectorized types, ensuring that bitmask behaviors are correctly determined, particularly when dealing with scalar types that do not use bitmask optimizations. The test suite has been updated to reflect these changes.
