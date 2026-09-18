---
project: gcc
subsystem: loongarch
patch_id: null
tags:
- loongarch
- compiler error
- intrinsic
commit_hash: 11ae0ce305601ebf85b1a09b130cb3e7b46157f9
source_type: github
author: Xi Ruoyao
headline: 'LoongArch: Fix __builtin_bitreverse16 ICE on LA32R'
tldr: Fixes an internal compiler error for __builtin_bitreverse16 on LoongArch 32-bit
  Reduced.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change disables the `bitreverseqi2` RTL pattern on the LoongArch
  LA32R architecture to fix an ICE. The `bitreverseqi2` pattern, when used for 16-bit
  bit reversal, appears to be incompatible or has an issue on the LA32R variant, likely
  due to specific instruction encoding or available vector operations. The fix ensures
  correct compilation for this target by preventing the problematic pattern from being
  selected.
primer_glossary:
- term: LoongArch
  definition: A family of RISC-based instruction set architectures developed in China,
    with variants for 32-bit and 64-bit systems.
- term: LA32R
  definition: LoongArch 32-bit Reduced architecture, a specific configuration of the
    LoongArch ISA.
- term: ICE
  definition: Internal Compiler Error. An unexpected condition encountered during
    compilation that causes the compiler to terminate abnormally.
- term: __builtin_bitreverse16
  definition: A GCC intrinsic function that reverses the order of bits in a 16-bit
    integer.
- term: RTL
  definition: Register Transfer Language. An intermediate representation used by GCC
    to represent the program before generating machine code. Optimization passes operate
    on RTL.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/11ae0ce305601ebf85b1a09b130cb3e7b46157f9
date: '2026-09-03'
is_stub: false
stub_reason: ''
---

This commit resolves an internal compiler error (ICE) on the LoongArch 32-bit Reduced (LA32R) architecture when using the `__builtin_bitreverse16` intrinsic. The fix involves disabling this intrinsic specifically for the LA32R target, along with a new test case to confirm the correction.
