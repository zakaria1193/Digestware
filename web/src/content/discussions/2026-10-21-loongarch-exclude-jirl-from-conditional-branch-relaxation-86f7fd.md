---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- gas
- LoongArch
- assembly
- relaxation
discussion_id: 20261021014144.64102-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Exclude JIRL from conditional branch relaxation'
headline: 'LoongArch: Exclude JIRL from conditional branch relaxation'
tldr: A patch to prevent the LoongArch assembler from incorrectly altering JIRL instructions
  during conditional branch relaxation.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: zhaozhou <zhaozhou@loongson.cn>
  role: proposer
  position: Submits a patch to prevent the LoongArch assembler from inverting JIRL
    opcodes and appending a B instruction when the immediate is out of range.
  quote: 'JIRL can use an R_LARCH_B16 relocation, therefore cause GAS to invert

    the JIRL opcode and append a B instruction when its immediate is out

    of range, changing the instruction''s semantics.'
primer_expert: This patch targets the LoongArch backend in GNU Assembler (GAS), part
  of the Binutils project. It addresses an issue with branch relaxation, where the
  assembler adjusts branch instructions for optimal size. The problem occurs with
  JIRL instructions using `R_LARCH_B16` relocations; if the immediate value is out
  of range for a `B` instruction (which GAS might substitute), GAS incorrectly inverts
  the JIRL opcode and appends a `B`, altering the instruction's meaning. The fix excludes
  JIRL from this relaxation process.
primer_glossary:
- term: JIRL
  definition: Jump If Register Less, a LoongArch instruction. In this context, it
    refers to a specific jump instruction that can use a 16-bit relocation.
- term: Conditional branch relaxation
  definition: An assembler optimization where branch instructions are adjusted to
    use shorter or longer forms to fit their target distance, optimizing code size
    or reachability.
- term: GAS
  definition: GNU Assembler, the default assembler for the GCC toolchain.
- term: R_LARCH_B16
  definition: A LoongArch-specific relocation type for 16-bit branches.
- term: Opcode
  definition: The part of a machine instruction that specifies the operation to be
    performed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261021014144.64102-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

This patch for the LoongArch architecture in Binutils addresses an issue where the assembler, GAS, incorrectly modifies JIRL opcodes by appending a B instruction when the immediate value is out of range. This alteration changes the instruction's semantics. The patch excludes JIRL from conditional branch relaxation to prevent this incorrect behavior.
