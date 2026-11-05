---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- disassembler
- opcode
- interrupts
discussion_id: 4e0393b1-f4b8-42d8-6668-b66d20fa2924@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 27/28] aarch64: Fix GICR encoding'
headline: 'aarch64: Fix GICR encoding'
tldr: Patch corrects a bit in the aarch64 GICR instruction encoding, distinguishing
  it from SYS aliases.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch addresses an encoding error for a specific aarch64 instruction,
  `gicr`, within the binutils disassembler. The instruction's binary representation
  was incorrectly interpreted due to a single bit error (bit 21). This bit differentiates
  between `SYS` and `SYSL` instruction aliases. By correcting this bit, the `gicr`
  instruction is now properly classified as a `SYSL` alias, ensuring accurate disassembly.
  The patch also updates the test case (`gcie.d`) to reflect the corrected encoding.
primer_glossary:
- term: GICR
  definition: Generic Interrupt Controller Register access instruction in ARM architecture.
- term: encoding
  definition: The binary representation of an instruction.
- term: alias
  definition: In this context, an instruction that is a variation or shorthand for
    another, often differing in a few bits that control its specific behavior or target.
- term: SYS/SYSL
  definition: Instructions in the ARM architecture that interact with system registers
    or perform system-level operations. The 'L' suffix typically indicates 'long'
    or a specific operand variant.
- term: aarch64
  definition: The 64-bit ARM architecture instruction set.
series_id: 'binutils:aarch64: fix gicr encoding'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/4e0393b1-f4b8-42d8-6668-b66d20fa2924@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch corrects bit 21 in the encoding for the aarch64 GICR instruction. The incorrect bit caused it to be treated as a `SYS` alias when it should be a `SYSL` alias (where L=1). This fix ensures the instruction is correctly identified and disassembled.
