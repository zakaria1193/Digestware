---
project: gcc
subsystem: gcc/riscv
patch_id: null
tags:
- risc-v
- optimization
- code generation
commit_hash: de2ea1f8b15f05264310a5e7c29328591c13de49
source_type: github
author: Jeff Law
headline: Fix RISC-V AOP regressions for different modes and extensions
tldr: Improves RISC-V code generation for arithmetic operations (AOP) to handle various
  modes and extensions correctly.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The RISC-V backend's expander for aop<mode>3 in config/riscv/riscv.md
  has been updated to correctly steer AOP operations. It now prioritizes PLUS when
  ZBA is enabled and arguments are registers, otherwise steering towards IOR. For
  RV64, sub-word logical operations are handled by punning to DImode and emitting
  64-bit operations. This resolves regressions on riscv32-elf and riscv64-elf related
  to AOP steering.
primer_glossary:
- term: AOP
  definition: Arithmetic Operation. Refers to basic mathematical operations like addition,
    subtraction, logical AND, OR, etc., performed by the CPU.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles.
- term: ZBA
  definition: A RISC-V extension that adds bit manipulation instructions, including
    byte manipulations.
- term: PLUS
  definition: Likely refers to the ADD instruction or a similar arithmetic operation.
- term: IOR
  definition: Inclusive OR. A logical operation that results in true if at least one
    of the operands is true.
- term: DImode
  definition: GCC machine mode for a double integer, typically 64 bits on a 64-bit
    system.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/de2ea1f8b15f05264310a5e7c29328591c13de49
date: '2026-10-11'
is_stub: false
stub_reason: ''
---

This commit addresses regressions in the RISC-V port's handling of arithmetic operations (AOP), specifically related to the choice between PLUS and IOR instructions. The changes ensure correct steering based on enabled extensions like ZBA, and properly handle sub-word logical operations on RV64 by converting them to 64-bit operations. This resolves issues with PR80770-2, PR58727, and PR93504.
