---
project: binutils
subsystem: gas
patch_id: null
tags:
- microblaze
- gas
- testing
- disassembler
- opcode table
discussion_id: 20261109040811.26266-8-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH 7/7] gas: microblaze: test every opcode table entry'
headline: 'gas: microblaze: test every opcode table entry'
tldr: Adds comprehensive tests for the MicroBlaze gas opcode table to ensure all instructions
  are correctly disassembled.
proposer: Samuel Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Samuel Price
  role: proposer
  position: Submitted a patch to significantly expand the test suite for MicroBlaze
    gas opcodes, ensuring all instructions are tested.
  quote: The MicroBlaze gas tests disassemble 32 of the 277 instructions in microblaze-opc.h.
    A mask mistake, where one entry also matches a later entry's encoding, shows up
    only when someone disassembles the later instruction; the earlier patches of this
    series fix four.
primer_expert: This patch extends the test suite for the MicroBlaze assembler (gas)
  by creating comprehensive tests for its opcode table. Previously, only a small subset
  of instructions were tested, leading to potential undiscovered bugs like mask overlaps.
  The new tests, generated with varied operands and specific instruction forms, are
  validated against QEMU and architectural documentation (UG984) to ensure the accurate
  disassembly of all MicroBlaze instructions.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    language code into object files.
- term: MicroBlaze
  definition: A soft processor core from Xilinx, designed to be implemented in FPGAs.
    It has a RISC-like architecture.
- term: opcode table
  definition: A data structure within an assembler or disassembler that maps instruction
    mnemonics and their encodings to their corresponding operations.
- term: disassemble
  definition: The process of converting machine code (binary instructions) back into
    human-readable assembly language.
- term: QEMU
  definition: A popular open-source machine emulator and virtualizer that can emulate
    various hardware architectures, including MicroBlaze.
- term: UG984
  definition: A specific user guide or technical reference manual for the MicroBlaze
    processor.
series_id: 'binutils:gas: microblaze: test every opcode table entry'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261109040811.26266-8-thesamprice@gmail.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This patch introduces extensive test cases for the MicroBlaze gas opcode table, aiming to cover every instruction. The existing tests were insufficient, only covering a small fraction of the available opcodes and missing certain instruction encodings and variations. The new tests, verified against QEMU and documentation, assemble each instruction with diverse operands and special forms, ensuring accurate disassembly.
