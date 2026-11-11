---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- gas
- aarch64
- assembly
- architecture
discussion_id: 20261110133658.87026-1-muhammad.kamran@arm.com
source_type: public_inbox
title: '[PATCH v2 0/1] aarch64: Add FEAT_LSC64B assembly support'
headline: 'aarch64: Add FEAT_LSC64B assembly support'
tldr: binutils assembler and disassembler now support new aarch64 FEAT_LSC64B instructions.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 7
technical_tradeoffs:
- Adds new functionality for a specific CPU extension, increasing the complexity of
  the assembler and disassembler.
- Requires ongoing maintenance to ensure compatibility with future ARM architecture
  updates.
exchanges:
- author: Muhammad Kamran
  role: proposer
  position: Proposes adding assembly and disassembly support for the aarch64 FEAT_LSC64B
    extension and its instructions, including updates to opcode definitions and test
    suites.
  quote: This patch adds asm/disasm support for instructions from FEAT_LSC64B.
- author: Muhammad Kamran
  role: contributor
  position: Provides clarification on the new extension, noting its dependencies on
    FEAT_LSCP and FEAT_LS64, and that it reuses the LS64 Rt operand.
  quote: FEAT_LSC64B implies FEAT_LSCP, while the LSC64B instructions also require
    FEAT_LS64. Model this by making +lsc64b depend on +lscp and requiring both LSC64B
    and LS64 in the opcode feature set.
primer_expert: Binutils' gas assembler and objdump disassembler have been updated
  to support the aarch64 FEAT_LSC64B extension. This includes new instructions like
  LDA64B and STL64B, which require specific feature flags (+lsc64b, +lscp, +ls64)
  and reuse the Rt operand from FEAT_LS64. The patch series introduces the necessary
  opcode definitions, updates the C and TEXI documentation, and provides extensive
  test cases in the gas/testsuite/gas/aarch64 directory.
primer_glossary:
- term: FEAT_LSC64B
  definition: A feature (extension) for the Armv8.0-A architecture that introduces
    specific load-store-cache instructions.
- term: LDA64B
  definition: An instruction within the FEAT_LSC64B extension that likely performs
    a 64-byte atomic load-and-allocate operation.
- term: STL64B
  definition: An instruction within the FEAT_LSC64B extension that likely performs
    a 64-byte atomic store-and-allocate operation.
- term: STL64BV
  definition: An instruction within the FEAT_LSC64B extension that likely performs
    a 64-byte atomic store-and-allocate operation with a vector register operand.
- term: STL64BV0
  definition: An instruction within the FEAT_LSC64B extension that likely performs
    a 64-byte atomic store-and-allocate operation with a vector register operand,
    potentially with zeroing.
- term: aarch64
  definition: The 64-bit execution state of the Arm architecture.
- term: gas
  definition: The GNU Assembler, part of the binutils package, which translates assembly
    language into machine code.
- term: disassembler
  definition: A tool that translates machine code back into assembly language instructions.
series_id: 'binutils:aarch64: add feat_lsc64b assembly support'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261110133658.87026-1-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

This patch series adds support for the FEAT_LSC64B architecture extension and its associated instructions (LDA64B, STL64B, STL64BV, STL64BV0) to the binutils assembler and disassembler for the aarch64 architecture. The changes include updating opcode tables, documentation, and adding comprehensive test cases to ensure correct assembly and disassembly.
