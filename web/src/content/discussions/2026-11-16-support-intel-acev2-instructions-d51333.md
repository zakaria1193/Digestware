---
project: binutils
subsystem: binutils
patch_id: null
tags:
- x86
- acev2
- instructions
- assembler
- disassembler
discussion_id: 20261116081937.1879560-2-haochen.jiang@intel.com
source_type: public_inbox
title: Support Intel ACEV2 instructions
headline: Support Intel ACEV2 instructions
tldr: Adds support for Intel ACEv2 instructions by updating assembler and disassembler
  components.
proposer: Haochen Jiang
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Expands instruction set support for new Intel processors.
- Reuses existing code patterns where possible to maintain code efficiency.
exchanges: []
primer_expert: This patch introduces support for ACEv2 instructions into binutils.
  It modifies `gas/config/tc-i386.c`, `gas/doc/c-i386.texi`, and various files within
  `opcodes/` to recognize the new instruction encodings and mnemonics. The changes
  include updates to EVEX length, prefix, and width tables, as well as regenerating
  related header files. New test suites are added to cover the ACEv2 instructions.
primer_glossary:
- term: ACEv2
  definition: The second version of Intel's Advanced Core Extensions instruction set,
    providing new capabilities for performance-critical workloads.
- term: VNNI
  definition: Vector Neural Network Instructions, an x86 instruction set extension
    designed to accelerate deep learning inference.
- term: EVEX
  definition: An advanced instruction encoding scheme used in AVX-512 and later x86
    extensions, capable of encoding longer instructions and supporting more features
    than previous schemes like VEX.
- term: GAS
  definition: GNU Assembler, part of the GNU Binutils package, responsible for translating
    assembly language code into machine code.
series_id: binutils:support intel acev2 instructions
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116081937.1879560-2-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch adds support for the Intel ACEv2 instruction set to binutils. It involves modifications to the assembler's configuration and opcode table, as well as updates to the disassembler's internal tables and definitions. The changes leverage existing mechanisms like the VNNI instruction reuse of `<dpw>` to minimize code duplication and include new test cases to verify functionality.
