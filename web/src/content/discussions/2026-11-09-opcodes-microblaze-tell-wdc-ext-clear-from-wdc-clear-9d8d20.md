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
discussion_id: 20261109040811.26266-3-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH 2/7] opcodes: microblaze: tell wdc.ext.clear from wdc.clear'
headline: 'opcodes: microblaze: tell wdc.ext.clear from wdc.clear'
tldr: Updates MicroBlaze opcode masks to correctly distinguish between 'wdc' variants
  and improve disassembly accuracy.
proposer: Samuel Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Samuel Price
  role: proposer
  position: Adjusts MicroBlaze opcode masks to differentiate between 'wdc' variants
    like 'wdc.clear' and 'wdc.ext.clear', improving disassembly.
  quote: objdump prints "wdc.ext.clear r5, r9" (0x90054c66) as "wdc.clear r5, r9".
    The disassembler takes the first entry that matches under its mask. wdc.clear
    comes first, and its mask, OPCODE_MASK_H34B (0xFC0000FF), leaves out the E bit
    (0x400), the only bit in which the two differ (UG984, Figure 141).
primer_expert: This patch addresses an opcode disambiguation issue in the MicroBlaze
  disassembler by modifying opcode masks in `opcodes/microblaze-opc.h`. The instructions
  `wdc.clear` and `wdc.ext.clear` share a common opcode prefix but differ in a single
  bit (the 'E' bit). The previous mask `OPCODE_MASK_H34B` was too permissive, causing
  `wdc.ext.clear` to be disassembled as `wdc.clear`. The fix applies a more precise
  mask, `OPCODE_MASK_H35B`, to the relevant `wdc` variants, ensuring they are correctly
  identified. Instructions that still don't match any defined mnemonic after this
  change will now be treated…
primer_glossary:
- term: opcode mask
  definition: A bitmask used to isolate specific fields within an instruction's binary
    encoding for matching purposes.
- term: wdc
  definition: Likely refers to 'write data cache' or a similar memory-related instruction
    set in the MicroBlaze architecture.
- term: disassembler
  definition: A program that translates machine code into assembly language.
- term: MicroBlaze
  definition: A soft processor core from Xilinx, designed to be implemented in FPGAs.
    It has a RISC-like architecture.
- term: UG984
  definition: A specific user guide or technical reference manual for the MicroBlaze
    processor.
series_id: 'binutils:opcodes: microblaze: tell wdc.ext.clear from wdc.clear'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261109040811.26266-3-thesamprice@gmail.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This patch refines the opcode masks for MicroBlaze 'wdc' instructions to ensure accurate disassembly. Previously, a shared mask caused instructions like 'wdc.ext.clear' to be misidentified as 'wdc.clear'. By applying a more specific mask (`OPCODE_MASK_H35B`) to relevant 'wdc' variants, these instructions are now distinguished correctly. Instructions lacking the 'E' bit, which were previously misidentified, will now be treated as unknown data, preventing incorrect disassembly and potential simulator issues.
