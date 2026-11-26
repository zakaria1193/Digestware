---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- middle-end
- bitint
- clmul
- big-endian
commit_hash: adbe7fb7f384b0dd0abbf2d26a978679b4a03345
source_type: github
author: Jakub Jelinek
headline: 'bitintlower: Fix up big-endian .CLMUL bitint lowering'
tldr: Correctly lower CLMUL bit-integer operations on big-endian architectures.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `bitint_large_huge::lower_clmul` function in `gimple-lower-bitint.cc`
  was not correctly accounting for big-endian limb ordering when calculating array
  indices for CLMUL operations. On big-endian, limb N is at index `p - N`, while on
  little-endian it's at index `N`. The original pseudo-code's index calculations,
  assuming little-endian, resulted in incorrect accesses on big-endian. This patch
  modifies the calculation of `idx3` and `idx4` for big-endian targets to use `idx3
  - p` and `idx - p` respectively, ensuring correct limb access and fixing PR128111.
primer_glossary:
- term: bitint
  definition: An integer type whose size is not a multiple of the machine word size,
    allowing for arbitrary-precision integer operations.
- term: CLMUL (Carry-Less Multiplication)
  definition: A multiplication operation where the carry is not propagated between
    bit positions, commonly used in cryptography and error correction codes.
- term: big-endian
  definition: A byte order where the most significant byte is stored at the lowest
    memory address.
- term: little-endian
  definition: A byte order where the least significant byte is stored at the lowest
    memory address.
- term: limb
  definition: A chunk or part of a multi-precision integer. For example, a 128-bit
    integer might be represented as two 64-bit limbs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/adbe7fb7f384b0dd0abbf2d26a978679b4a03345
date: '2026-11-26'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in the lowering of CLMUL (carry-less multiplication) operations for bit-integers on big-endian systems. Previously, the calculation of limb indices for CLMUL operations was incorrect on big-endian architectures due to differing conventions for representing limb order compared to little-endian. This led to failures in tests like `builtin-clmulg-1.c` on powerpc64-linux and s390x-linux. The fix adjusts the index calculations in `bitint_large_huge::lower_clmul` to correctly handle big-endian limb ordering, resolving the test failures.
