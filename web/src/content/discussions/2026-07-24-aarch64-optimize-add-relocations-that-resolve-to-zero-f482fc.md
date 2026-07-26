---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- optimization
- linker
- performance
discussion_id: 20260724095859.909158-1-sivan.shani@arm.com
source_type: public_inbox
title: '[PATCH] AArch64: Optimize ADD relocations that resolve to zero'
headline: 'AArch64: Optimize ADD relocations that resolve to zero'
tldr: Implements an optimization for AArch64 ADD instructions that can be replaced
  by MOV or NOP.
proposer: Sivan Shani <sivan.shani@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Replacing ADD with MOV/NOP can reduce instruction count and potentially improve
  performance by utilizing simpler instructions or reducing pipeline stalls.
- Ensuring the optimization is applied correctly according to the ELF specification
  and handles all edge cases (e.g., SP register usage, 32-bit vs 64-bit modes).
exchanges: []
primer_expert: This patch introduces an optimization to the AArch64 backend of binutils
  as recommended by the Arm64 ELF specification. Specifically, it targets ADD instructions
  where the immediate operand, after relocation, evaluates to zero. The optimization
  replaces `ADD Rx, Ry, 0` with `MOV Rx, Ry` (for different registers) or `ADD Rx,
  Rx, 0` with `NOP` (for same registers, 64-bit mode). Special care is taken for 32-bit
  operations and instructions involving the stack pointer (SP). The change affects
  `bfd/elfxx-aarch64.c` and adds new tests to `ld/testsuite/ld-aarch64/`.
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: ADD instruction
  definition: A processor instruction that adds two operands together and stores the
    result in one of them.
- term: relocation
  definition: The process of updating symbolic references in code to absolute or relocatable
    addresses after compilation.
- term: immediate
  definition: A value that is a part of an instruction, rather than a reference to
    a memory location or register.
- term: MOV instruction
  definition: A processor instruction that copies data from one location to another.
- term: NOP instruction
  definition: No-Operation instruction. A processor instruction that does nothing.
- term: BFD
  definition: Binary File Descriptor library, a GNU library that provides a common
    interface to various object file formats.
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files used in Unix-like systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260724095859.909158-1-sivan.shani@arm.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

Sivan Shani proposes an optimization for the AArch64 architecture in binutils, following the 'ELF for the Arm 64-bit Architecture' specification. The patch optimizes ADD instructions where the immediate value becomes zero after relocation, replacing them with MOV or NOP instructions for efficiency. The changes include updates to BFD and the `ld` testsuite.
