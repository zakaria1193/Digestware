---
project: gcc
subsystem: tree-ssa-ccp
patch_id: null
tags:
- optimization
- bitreverse
- constant propagation
commit_hash: 7ca53f9d86ef5f4c6a49f414f3cdd88d2b8a0bad
source_type: github
author: Jakub Jelinek
headline: 'tree-ssa-ccp: Correctly handle __builtin_bitreverse*.'
tldr: Fixes bitwise constant propagation (CCP) for `__builtin_bitreverse*` intrinsics.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The tree-ssa-ccp pass performs constant propagation. This commit fixes
  an error in how ``BUILT_IN_BITREVERSE*`` intrinsics were handled, ensuring that
  constants are bit-reversed rather than byte-swapped during propagation. This correction
  is crucial for the correctness of optimizations based on CCP.
primer_general: Constant propagation is an optimization technique where the compiler
  replaces variables with their known constant values. This commit fixes a bug in
  how the compiler handles bit-reversal operations during constant propagation. By
  correctly propagating constant values through bit-reversal operations, the compiler
  can further optimize code and improve performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7ca53f9d86ef5f4c6a49f414f3cdd88d2b8a0bad
date: '2026-05-16'
is_stub: false
---

This commit corrects the handling of `__builtin_bitreverse*` builtins in the tree-ssa-ccp pass. It ensures that bitwise constant propagation (CCP) correctly handles bit reversal, which requires bit-reversing the value and mask constants, unlike byte swapping where the value and mask are bswapped.
