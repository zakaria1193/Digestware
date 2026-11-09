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
discussion_id: 20261109040811.26266-4-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH 3/7] opcodes: microblaze: don''t print mbar 17 as sleep'
headline: 'opcodes: microblaze: don''t print mbar 17 as sleep'
tldr: Corrects MicroBlaze opcode masking to distinguish 'mbar' from specific sleep
  instructions and preserve wait-skip information.
proposer: Samuel Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Samuel Price
  role: proposer
  position: Adjusts MicroBlaze opcode masks to correctly differentiate 'mbar' from
    pseudo-instructions like 'sleep' and retain information about skipped waits.
  quote: OPCODE_MASK_HN, shared by mbar, sleep, hibernate and suspend, compares only
    the top two bits of mbar's five-bit immediate. objdump therefore prints every
    mbar with an immediate of 8 or more as hibernate, sleep or suspend, mbar 17 as
    sleep for example, and drops the low bits, which select the memory waits the instruction
    skips.
primer_expert: This patch refines the opcode matching logic for MicroBlaze instructions
  in `opcodes/microblaze-opc.h`. The `OPCODE_MASK_HN` was too broad, causing `mbar`
  instructions with certain immediate values to be incorrectly identified as pseudo-instructions
  like `sleep`, `hibernate`, or `suspend`. This change updates the masks and reorders
  the instruction table so that `mbar` instructions are correctly recognized, and
  the specific sleep pseudo-instructions retain their distinct entries. This ensures
  that the disassembler accurately reflects the instruction's intended operation and
  any associated wait…
primer_glossary:
- term: opcode mask
  definition: A bitmask used to isolate specific fields within an instruction's binary
    encoding for matching purposes.
- term: MicroBlaze
  definition: A soft processor core from Xilinx, designed to be implemented in FPGAs.
    It has a RISC-like architecture.
- term: disassembler
  definition: A program that translates machine code into assembly language.
- term: pseudo-instruction
  definition: An assembly language construct that does not correspond directly to
    a single machine instruction but is expanded by the assembler into one or more
    machine instructions or directives.
- term: UG984
  definition: A specific user guide or technical reference manual for the MicroBlaze
    processor.
series_id: 'binutils:opcodes: microblaze: don''t print mbar 17 as sleep'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261109040811.26266-4-thesamprice@gmail.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This patch corrects the opcode mask for MicroBlaze 'mbar' instructions to prevent misinterpretation. Previously, a shared mask caused 'mbar' instructions with specific immediate values (like 17) to be incorrectly displayed as 'sleep', losing information about skipped memory waits. By refining the masks and reordering pseudo-instructions, 'mbar' now disassembles correctly, and specific sleep instructions remain distinct.
