---
project: binutils
subsystem: opcodes
patch_id: null
tags:
- microblaze
- disassembler
- objdump
- bug fix
discussion_id: 20261109040811.26266-6-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH 5/7] opcodes: microblaze: disassemble the word 0'
headline: 'opcodes: microblaze: disassemble the word 0'
tldr: Modifies MicroBlaze disassembler to correctly handle zero words, allowing disassembly
  to continue past padding.
proposer: Samuel Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Samuel Price
  role: proposer
  position: Introduces a change to the MicroBlaze disassembler to correctly handle
    zero words, improving disassembly continuity.
  quote: objdump stops disassembling a section at the first zero word, such as the
    padding " .align 3 " leaves after a single instruction. read_insn_microblaze returns
    the instruction word, or 0 when the read fails, so its two callers cannot tell
    a failed read from the word 0 and return -1 for both.
primer_expert: This patch modifies the MicroBlaze disassembler (`opcodes/microblaze-dis.c`)
  to correctly handle instruction words that are zero. Previously, `read_insn_microblaze`
  returned 0 for both a valid 'add r0, r0, r0' instruction and a failed memory read,
  causing disassembly to halt. The function is refactored to return a boolean success
  status and pass the instruction word via an output parameter. This allows `objdump`
  and other tools to differentiate a zero instruction from a read error, preventing
  premature termination of disassembly, especially after padding.
primer_glossary:
- term: objdump
  definition: A standard utility in the GNU Binutils package used to display information
    from object files, including disassembly of machine code.
- term: disassembler
  definition: A program that translates machine code into assembly language.
- term: padding
  definition: Unused space inserted into a data structure or code section, often for
    alignment purposes. In disassembly, it can appear as zero bytes.
- term: MicroBlaze
  definition: A soft processor core from Xilinx, designed to be implemented in FPGAs.
    It has a RISC-like architecture.
- term: UG984
  definition: A specific user guide or technical reference manual for the MicroBlaze
    processor.
series_id: 'binutils:opcodes: microblaze: disassemble the word 0'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261109040811.26266-6-thesamprice@gmail.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where objdump stops disassembling at the first zero word encountered, often due to padding. The `read_insn_microblaze` function is updated to return a boolean indicating success and pass the instruction word via a pointer. This change allows the disassembler to distinguish between a failed memory read and the valid instruction 'add r0, r0, r0' (word 0), ensuring continuous disassembly.
