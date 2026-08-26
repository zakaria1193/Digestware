---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- rvv
- testing
commit_hash: cafeac4496cbe047d429540e3ae23bf9eb64bab4
source_type: github
author: Pan Li
headline: 'RISC-V: Add more test cases for vwmulsu.vx'
tldr: Adds new test cases for RISC-V `vwmulsu.vx` instruction, focusing on non-asm
  checks.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Adds a new test case, `pr112431-52.c`, to the RISC-V test suite. This
  test specifically targets the `vwmulsu.vx` instruction and is designed to ensure
  that no `csrr` instructions are generated in the assembly output when register overlap
  is enabled. This complements existing tests by focusing on non-assembly-check scenarios
  for instruction codegen.
primer_glossary:
- term: vwmulsu.vx
  definition: A RISC-V vector instruction for unsigned widening multiplication of
    a vector register by a scalar from another vector register.
- term: csrr
  definition: A RISC-V instruction that reads from a Control and Status Register (CSR)
    into a general-purpose register. In this context, it might be used to inspect
    register state, and its absence in assembly indicates a more direct code generation.
- term: register overlap
  definition: In the context of RISC-V vector operations, this refers to a scenario
    where destination and source registers in an instruction might partially or fully
    overlap, requiring careful handling by the compiler to maintain correctness.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cafeac4496cbe047d429540e3ae23bf9eb64bab4
date: '2026-08-23'
is_stub: true
stub_reason: low_score
---

This commit introduces new test cases for the RISC-V `vwmulsu.vx` instruction. These tests focus on scenarios where the compiler should not perform `csrr` (Control and Status Register read) operations in the assembly output, particularly when overlap is enabled. This expands test coverage for the vector multiplication instruction.
