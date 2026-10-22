---
project: gcc
subsystem: rtl-optimization
patch_id: null
tags:
- risc-v
- optimization
- builtin
commit_hash: 5827af4ea1ea11036b336e1029b4a25ca670b594
source_type: github
author: Milan Tripkovic
headline: PR rtl-optimization/123905 - Failure to optimize away sign extension on
  RISC-V
tldr: Fixes redundant sign extensions for bitwise intrinsics on RISC-V, improving
  generated code quality.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The change targets the interaction between `ext-dce` and `rtlanal`
  on RISC-V, specifically concerning redundant sign extensions when optimizing intrinsics
  like `clz`, `ctz`, and `popcount`. `is_trivially_redundant_extension` is introduced
  in `ext-dce.cc` to detect extensions where the sign bit is already implicitly propagated.
  `nonzero_bits1` in `rtlanal.cc` is improved to handle `clz` and `ctz` when the operand
  mode differs from the return mode, as long as they are scalar integer modes, ensuring
  correct optimization when the result depends on the operand's value, not just its
  mode.
primer_glossary:
- term: RISC-V
  definition: A free and open instruction set architecture (ISA) based on reduced
    instruction set computer principles, increasingly popular for embedded systems
    and high-performance computing.
- term: sign extension
  definition: An operation that widens a signed integer type by replicating the sign
    bit (the most significant bit) to fill the more significant bits of the larger
    type.
- term: __builtin_clz
  definition: A GCC intrinsic function that counts the number of leading zero bits
    in an integer.
- term: __builtin_ctz
  definition: A GCC intrinsic function that counts the number of trailing zero bits
    in an integer.
- term: __builtin_popcount
  definition: A GCC intrinsic function that counts the number of set bits (population
    count) in an integer.
- term: RTL (Register Transfer Language)
  definition: An intermediate representation used by GCC. It describes operations
    at a lower level than GENERIC but higher than machine code, focusing on registers
    and memory accesses.
- term: dead code elimination (DCE)
  definition: A compiler optimization pass that removes code that does not affect
    the program's output or behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5827af4ea1ea11036b336e1029b4a25ca670b594
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

This patch resolves an issue on RISC-V where redundant sign extensions and bit masks were generated for bitwise intrinsics like __builtin_clz and __builtin_popcount. It refactors the dead code elimination pass to better identify and remove these unnecessary operations, leading to cleaner and potentially more efficient assembly code. A new test case ensures these optimizations are correctly applied.
