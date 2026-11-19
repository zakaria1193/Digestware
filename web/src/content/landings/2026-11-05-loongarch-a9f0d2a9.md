---
project: gcc
subsystem: loongarch
patch_id: null
tags:
- loongarch
- optimization
- performance
commit_hash: a9f0d2a9c91246bce74b01cf1a06d39d9dfc724e
source_type: github
author: Deng Jianbo
headline: 'LoongArch: Optimize 64-bit moves to floating-point registers'
tldr: LoongArch 64-bit register moves to floating-point registers are optimized, avoiding
  unnecessary instructions and improving performance.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `movdi_64bit` pattern in `config/loongarch/loongarch.md` previously
  used a '*' constraint on floating-point register classes (`f` and `m`). This wildcard
  implies that the register allocator should consider both floating-point and general-purpose
  registers, but it introduces an overhead associated with `FP_REGS`. By removing
  the '*', the pattern now allows for a more direct selection of floating-point registers.
  This enables the use of the `fld.d` instruction for loading 64-bit values directly
  into floating-point registers, bypassing the need for a load-then-move-between-register-classes
  s…
primer_glossary:
- term: movdi_64bit
  definition: A machine-dependent instruction or pattern in GCC for moving a 64-bit
    doubleword value. In this context, it specifically refers to moving data into
    floating-point registers on the LoongArch architecture.
- term: constraint
  definition: In GCC's machine description files, constraints specify the type of
    operand (e.g., register, immediate value) that an instruction pattern can accept.
    A wildcard '*' modifies a constraint, often indicating a broader or more flexible
    match.
- term: fld.d
  definition: A LoongArch instruction that loads a 64-bit double-precision floating-point
    value from memory into a floating-point register.
- term: ld.d
  definition: A LoongArch instruction that loads a 64-bit doubleword value from memory
    into a general-purpose register.
- term: movgr2fr.d
  definition: A LoongArch instruction that moves a 64-bit value from a general-purpose
    register to a floating-point register.
- term: FP_REGS
  definition: A symbolic name representing the set of floating-point registers available
    on the target architecture.
- term: GR_REGS
  definition: A symbolic name representing the set of general-purpose registers available
    on the target architecture.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a9f0d2a9c91246bce74b01cf1a06d39d9dfc724e
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

This commit optimizes the `movdi_64bit` pattern in LoongArch by removing a wildcard ('*') from floating-point register constraints. This change allows the compiler to directly generate the `fld.d` instruction instead of a more costly sequence of `ld.d` followed by `movgr2fr.d`. By preferring `fld.d` when floating-point and general-purpose register costs are equal, this optimization reduces instruction counts and has shown significant performance improvements in SPEC2017 benchmarks.
