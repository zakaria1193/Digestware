---
project: binutils
subsystem: opcodes
patch_id: null
tags:
- microblaze
- opcodes
- disassembler
- masking
- bug fix
discussion_id: 20261109040811.26266-2-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH 1/7] opcodes: microblaze: tell bslli, bsrai and bsrli apart'
headline: 'opcodes: microblaze: tell bslli, bsrai and bsrli apart'
tldr: Corrects MicroBlaze opcode mask to accurately distinguish between shift immediate
  instructions.
proposer: Samuel Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Samuel Price
  role: proposer
  position: Proposes updating the MicroBlaze opcode mask to correctly differentiate
    immediate barrel shift instructions.
  quote: OPCODE_MASK_H3B, the mask of the immediate barrel shifts, leaves out bits
    21:22 (0x600), the only bits that tell bslli, bsrai and bsrli apart. The bit_sequence
    of bslli and bsrai has bits outside the mask, so the opcode lookup never matches
    them, and every immediate barrel shift disassembles as bsrli.
primer_expert: This patch addresses an opcode recognition issue for MicroBlaze immediate
  barrel shift instructions in `opcodes/microblaze-opc.h`. The `OPCODE_MASK_H3B` was
  insufficient, failing to account for bits 21:22, which differentiate `bslli` (shift
  left logical immediate), `bsrai` (shift right arithmetic immediate), and `bsrli`
  (shift right logical immediate). Consequently, all these instructions were being
  disassembled as `bsrli`. The patch updates the mask to `0xFC00FFE0`, correctly covering
  these differentiating bits, aligning with QEMU's decoder and fixing failing test
  cases.
primer_glossary:
- term: opcode mask
  definition: A bitmask used to isolate specific fields within an instruction's binary
    encoding for matching purposes.
- term: bslli
  definition: 'MicroBlaze instruction: Shift Left Logical Immediate.'
- term: bsrai
  definition: 'MicroBlaze instruction: Shift Right Arithmetic Immediate.'
- term: bsrli
  definition: 'MicroBlaze instruction: Shift Right Logical Immediate.'
- term: MicroBlaze
  definition: A soft processor core from Xilinx, designed to be implemented in FPGAs.
    It has a RISC-like architecture.
- term: QEMU
  definition: A popular open-source machine emulator and virtualizer that can emulate
    various hardware architectures, including MicroBlaze.
series_id: 'binutils:opcodes: microblaze: tell bslli, bsrai and bsrli apart'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261109040811.26266-2-thesamprice@gmail.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This patch corrects a flaw in the MicroBlaze opcode mask (`OPCODE_MASK_H3B`) that prevented the assembler and disassembler from distinguishing between `bslli`, `bsrai`, and `bsrli` instructions. The existing mask omitted critical bits, causing all immediate barrel shifts to be treated as `bsrli`. The updated mask includes these bits, enabling correct disassembly and simulation, and fixing a test case that previously failed due to this ambiguity.
