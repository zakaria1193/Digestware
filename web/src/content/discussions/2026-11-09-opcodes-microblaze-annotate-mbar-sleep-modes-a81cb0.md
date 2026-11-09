---
project: binutils
subsystem: opcodes
patch_id: null
tags:
- microblaze
- disassembler
- opcodes
- annotations
discussion_id: 20261109040811.26266-5-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH 4/7] opcodes: microblaze: annotate mbar sleep modes'
headline: 'opcodes: microblaze: annotate mbar sleep modes'
tldr: Improves MicroBlaze disassembler output for 'mbar' instructions to show sleep
  modes and skipped waits.
proposer: Samuel Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Samuel Price
  role: proposer
  position: Enhances the MicroBlaze disassembler to provide more detailed annotations
    for 'mbar' instructions related to sleep modes and waits.
  quote: 'An mbar other than sleep, hibernate and suspend can still enter a sleep
    mode. In UG984''s pseudocode for mbar, IMM & 24 selects the mode, and IMM & 1
    and IMM & 2 skip the instruction-side and data-side waits. Print that as a comment,
    in the "// " form already used for branch targets:'
primer_expert: This patch modifies the MicroBlaze disassembler's handling of the `mbar`
  (memory barrier) instruction in `opcodes/microblaze-dis.c`. It interprets the instruction's
  immediate field to identify specific sleep modes (sleep, hibernate, suspend) and
  whether instruction-side or data-side waits are skipped. This information is appended
  as comments to the disassembled output, e.g., `mbar 17 // sleep, without the instruction-side
  wait`, providing a more precise understanding of the barrier's behavior beyond just
  the mnemonic.
primer_glossary:
- term: mbar
  definition: A memory barrier instruction used in some architectures to enforce ordering
    of memory operations.
- term: disassembler
  definition: A program that translates machine code into assembly language.
- term: MicroBlaze
  definition: A soft processor core from Xilinx, designed to be implemented in FPGAs.
    It has a RISC-like architecture.
- term: UG984
  definition: A specific user guide or technical reference manual for the MicroBlaze
    processor.
- term: immediate value
  definition: A constant value embedded directly within an instruction.
series_id: 'binutils:opcodes: microblaze: annotate mbar sleep modes'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261109040811.26266-5-thesamprice@gmail.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This patch enhances the disassembly output for MicroBlaze 'mbar' instructions. It annotates instructions that enter sleep modes (sleep, hibernate, suspend) and indicates which memory waits (instruction-side, data-side) are skipped based on the instruction's immediate value. This provides clearer information to users when interpreting 'mbar' instructions, especially those involving different wait behaviors.
