---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- optimization
- linker
- performance
discussion_id: 20260915163722.96043-1-sivan.shani@arm.com
source_type: public_inbox
title: '[PATCH] AArch64: Optimize short-range ADRP/ADD sequences'
headline: 'AArch64: Optimize short-range ADRP/ADD sequences'
tldr: Optimizes AArch64 ADRP/ADD sequences by relaxing them into NOP/ADR when possible.
proposer: Sivan Shani <sivan.shani@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Reduces code size by replacing two instructions with one.
- May improve performance by reducing instruction count and improving locality.
- Adds complexity to the linker's relaxation pass.
- Ensures correctness by checking for matching symbols, addends, registers, and non-overlapping
  relocations.
exchanges:
- author: Sivan Shani <sivan.shani@arm.com>
  role: proposer
  position: Proposes an optimization to relax eligible ADRP/ADD sequences into NOP/ADR
    on AArch664 when the target fits within ADR's range.
  quote: 'Relax eligible ADRP/ADD address-generation pairs into NOP/ADR when the

    target fits within the ADR relocation range.


    Require matching symbols, addends and registers, and reject sections

    containing overlapping relocations.  Preserve the transformed relocation

    information for --emit-relocs.'
primer_expert: This patch targets the AArch64 backend of the binutils linker (`ld`)
  and BFD library. It focuses on optimizing instruction sequences related to address
  generation, specifically the common `ADRP` (Add Page Relative) followed by `ADD`
  instruction pair. On AArch64, `ADRP` loads the upper 16 bits of an address (PC-relative),
  and `ADD` is used to combine this with a lower 12-bit immediate offset. This patch
  identifies cases where the combined offset is small enough to be handled by a single
  `ADR` instruction (which has a larger immediate range), thus replacing the two instructions
  with one and a N…
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture, successor to the 32-bit ARM architecture.
- term: ADRP
  definition: Add Page Relative. An AArch64 instruction that adds a signed 16-bit
    immediate, scaled by 4KB, to the program counter (PC), producing a 64-bit address
    with page granularity.
- term: ADD
  definition: Add. An instruction that adds two operands and stores the result in
    a destination register. In this context, it's used to combine the page address
    from ADRP with a lower-address offset.
- term: ADR
  definition: Add PC-Relative. An AArch64 instruction that generates a 64-bit PC-relative
    address within a larger range than ADRP/ADD combined, typically +/- 4MB.
- term: relocation
  definition: Information in an object file that tells the linker how to modify certain
    addresses or symbols when creating the final executable or shared library. For
    example, fixing up PC-relative addresses.
- term: LP64
  definition: A data model where `long` and pointers are 64 bits wide, and `int` is
    32 bits wide. Used by AArch64 and other 64-bit architectures.
- term: ILP32
  definition: A data model where `int`, `long`, and pointers are all 32 bits wide,
    even on a 64-bit architecture. Sometimes used for compatibility or specific use
    cases.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260915163722.96043-1-sivan.shani@arm.com
bugzilla_url: null
date: '2026-09-15'
is_stub: false
stub_reason: ''
---

This patch introduces an optimization for the AArch64 architecture in binutils' linker. It identifies pairs of ADRP and ADD instructions used for generating addresses within a short range. If the target address fits within the range of a single ADR instruction, the sequence is transformed into a NOP and an ADR instruction. The patch includes checks for matching symbols, addends, and registers, rejects overlapping relocations, and preserves relocation information for `--emit-relocs`. New tests are added for various scenarios including different instruction set variants (LP64, ILP32) and relax modes.
