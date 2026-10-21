---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- gas
- LoongArch
- assembly
- optimization
discussion_id: 20261021015156.65492-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH v2] LoongArch: Exclude JIRL from conditional branch relaxation'
headline: 'LoongArch: Exclude JIRL from conditional branch relaxation (v2)'
tldr: Version 2 of a patch that prevents the LoongArch assembler from incorrectly
  altering JIRL instructions during conditional branch relaxation.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: zhaozhou <zhaozhou@loongson.cn>
  role: proposer
  position: Submits version 2 of a patch to prevent the LoongArch assembler from inverting
    JIRL opcodes and appending a B instruction when the immediate is out of range.
  quote: 'JIRL can use an R_LARCH_B16 relocation, therefore cause GAS to invert

    the JIRL opcode and append a B instruction when its immediate is out

    of range, changing the instruction''s semantics.'
primer_expert: This patch targets the LoongArch backend in GNU Assembler (GAS), part
  of the Binutils project. It specifically addresses an issue with branch relaxation,
  a process where the assembler adjusts branch instructions to use shorter immediate
  offsets when possible. The problem arises because JIRL instructions, when using
  the `R_LARCH_B16` relocation, can be misinterpreted by GAS's relaxation logic. If
  the immediate value for JIRL is out of range for a `B` instruction (which GAS might
  try to substitute), GAS incorrectly inverts the JIRL opcode and appends a `B`, semantically
  altering the instruction…
primer_glossary:
- term: JIRL
  definition: Jump If Register Less, a LoongArch instruction. In this context, it
    appears to be a specific variant or usage of a jump instruction.
- term: Conditional branch relaxation
  definition: A compiler or assembler optimization where short, fixed-length branch
    instructions are rewritten to use longer, variable-length forms if the target
    is too far away. This ensures all branches can reach their targets.
- term: GAS
  definition: GNU Assembler, the default assembler used by the GCC toolchain.
- term: R_LARCH_B16
  definition: A relocation type specific to the LoongArch architecture, indicating
    a 16-bit branch relocation.
- term: Opcode
  definition: The part of a machine language instruction that specifies the operation
    to be performed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261021015156.65492-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

This is the second version of a patch for the LoongArch architecture in Binutils. It addresses an issue where the assembler, GAS, incorrectly modifies JIRL opcodes by appending a B instruction when the immediate value is out of range. This modification changes the instruction's semantics. The patch excludes JIRL from conditional branch relaxation to prevent this behavior.
