---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- unused operand
- code cleanup
discussion_id: d6c7e355-689d-7438-3cd4-8f7c05768d95@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 04/23] aarch64: Remove unused operand SM3_IMM2'
headline: 'Aarch64: Remove unused operand SM3_IMM2'
tldr: Removes the unused `AARCH64_OPND_SM3_IMM2` operand from the AArch64 assembler,
  simplifying the codebase.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improved code clarity by removing an unused operand.
- No performance impact.
exchanges: []
primer_expert: This patch removes `AARCH64_OPND_SM3_IMM2` from `include/opcode/aarch64.h`
  and related code in `gas/config/tc-aarch64.c` and `opcodes/aarch64-asm-2.c`. This
  operand was intended for SM3 instructions but was never used.
primer_general: '`binutils` is a collection of binary tools such as the assembler,
  linker, etc. This patch modifies the assembler (`gas`) for the AArch64 architecture.
  The assembler translates human-readable assembly code into machine code that a computer
  can execute. This patch removes an unused operand, simplifying the code.'
series_id: 'binutils:aarch64: remove unused operand sm3_imm2'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/d6c7e355-689d-7438-3cd4-8f7c05768d95@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-05-07'
---

This patch removes the `AARCH64_OPND_SM3_IMM2` operand, which was intended for use with the sm3tt* instructions, but was ultimately unused. The operand is removed from the enum `aarch64_opnd` and related code in the assembler. This simplifies the code and removes a potential source of confusion.
