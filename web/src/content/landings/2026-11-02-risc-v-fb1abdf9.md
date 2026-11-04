---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- vector
- testing
commit_hash: fb1abdf96ba0fb9fe0656fbad5805083b74c49f9
source_type: github
author: Pan Li
headline: 'RISC-V: Add tests for vfwredusum.vs register overlap.'
tldr: New test cases ensure RISC-V vector instructions do not cause register group
  overlaps.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds test cases for the `vfwredusum.vs` instruction within
  the RISC-V vector extension. The tests focus on ensuring that the `vs1` operand,
  which has an EEW of 2x SEW, does not overlap with the `vs2` register group (SEW),
  as required by section 5.2 of the vector specification to avoid encoding conflicts.
  This is particularly relevant for auto-vectorization and code generation quality.
primer_glossary:
- term: RISC-V Vector Extension (RVV)
  definition: An extension to the RISC-V instruction set architecture that adds support
    for vector processing, enabling single-instruction, multiple-data (SIMD) operations
    for improved performance on parallelizable tasks.
- term: vfwredusum.vs
  definition: A RISC-V vector instruction for widening floating-point sum reductions
    where the destination and second source registers are the same. It involves operations
    with different element widths.
- term: SEW (Standard Element Width)
  definition: The base element width for vector operations in RISC-V, which can be
    8, 16, 32, or 64 bits.
- term: EEW (Extended Element Width)
  definition: The element width used for operations that require a wider data path
    than the SEW, such as widening reductions in RISC-V.
- term: Register Group
  definition: In the RISC-V vector extension, a set of consecutive vector registers
    that are treated as a unit for certain operations or constraints.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fb1abdf96ba0fb9fe0656fbad5805083b74c49f9
date: '2026-11-02'
is_stub: false
stub_reason: ''
---

This commit introduces new test cases to verify that the `vfwredusum.vs` RISC-V vector instruction does not cause register group overlaps. It specifically targets scenarios where the destination register (`vs1`) might overlap with the source register group (`vs2`), ensuring compliance with the RISC-V vector specification's constraints on register usage for operations with differing element widths.
