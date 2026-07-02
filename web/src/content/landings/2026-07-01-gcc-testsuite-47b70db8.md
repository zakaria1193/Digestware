---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- powerpc
- vectorization
commit_hash: 47b70db8779a0991b9370e571ab18901b2643a63
source_type: github
author: Jeevitha
headline: Update PowerPC VSX arithmetic tests
tldr: VSX arithmetic tests no longer force operands into FPRs, testing default instruction
  selection.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: These tests for the `vsx_arith_builtin` family of functions previously
  used inline assembly to ensure arguments were placed in FPRs, forcing the use of
  VSX arithmetic instructions. This commit removes that constraint, allowing the compiler's
  natural instruction selection logic to determine operand placement. This enables
  testing of default instruction selection, crucial as compiler heuristics for vectorization
  and instruction choice evolve.
primer_glossary:
- term: VSX
  definition: Vector-Scalar Extension is an instruction set extension for PowerPC
    processors that provides single-instruction, multiple-data (SIMD) capabilities
    for both floating-point and integer operations.
- term: FPR
  definition: Floating-Point Register. Registers on a processor specifically designated
    for holding floating-point values.
- term: inline asm
  definition: Inline assembly allows developers to embed assembly language instructions
    directly within C/C++ code. It's often used for performance-critical sections
    or to access hardware-specific features not exposed by standard language constructs.
- term: instruction selection
  definition: The compiler phase responsible for choosing specific machine instructions
    to implement the operations in the intermediate representation, considering factors
    like available instructions, their performance, and register constraints.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/47b70db8779a0991b9370e571ab18901b2643a63
date: '2026-07-01'
is_stub: true
stub_reason: low_score
---

PowerPC VSX arithmetic tests have been updated to remove inline assembly that forced operands into floating-point registers (FPRs). This change allows the tests to evaluate the compiler's default instruction selection for future VSX arithmetic instructions, enabling detection of any regressions or unintended changes in instruction generation.
