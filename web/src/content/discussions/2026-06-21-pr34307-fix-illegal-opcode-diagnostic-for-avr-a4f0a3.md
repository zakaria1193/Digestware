---
project: binutils
subsystem: gas/avr
patch_id: null
tags:
- gas
- AVR
- assembler
- diagnostic
- bug fix
discussion_id: 28e3d238-7b0c-4cf7-bc49-cf172810efea@gjlay.de
source_type: public_inbox
title: '[patch, avr, applied] PR34307: Fix illegal opcode diagnostic'
headline: 'PR34307: Fix illegal opcode diagnostic for AVR'
tldr: A patch fixes an AVR assembler bug where illegal opcode errors incorrectly reported
  the mnemonic of the subsequent instruction.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Georg-Johann Lay
  role: proposer
  position: Proposes a patch to fix an AVR assembler diagnostic bug where illegal
    opcode errors reported the mnemonic of the subsequent instruction.
  quote: 'When there is an AVR instruction in include/opcode/avr.h that is not supported
    by a specific core, then gas will diagnose with the mnemonic of the next instruction:
    ... The reason is that in gas/config/tc-avr.c::md_assemble() we have ... which
    in the as_bad case prints the next instruction''s mnemonic due to the opcode++
    above.'
primer_expert: This patch addresses a bug in the GNU Assembler (`gas`) for the AVR
  architecture, specifically within `gas/config/tc-avr.c::md_assemble()`. The issue
  arises during the instruction matching loop (`while ((opcode->isa & avr_mcu->isa)
  != opcode->isa)`), where `opcode++` increments the `opcode` pointer before the `as_bad`
  diagnostic is issued. Consequently, the diagnostic prints `opcode->name` for the
  *next* instruction in `include/opcode/avr.h` rather than the one that failed the
  ISA compatibility check. The fix would involve correcting the index or pointer used
  for printing the error message.
primer_general: This is about a fix for a small but annoying bug in `gas`, the GNU
  Assembler, when it's used for AVR microcontrollers. Microcontrollers are tiny computers
  often used in embedded systems. When you write assembly code for an AVR chip, `gas`
  translates it into machine instructions. The bug occurred when an instruction wasn't
  supported by a specific AVR chip; the error message would mistakenly report the
  instruction *after* the problematic one. This patch fixes that, ensuring that when
  an error occurs, `gas` points to the correct, unsupported instruction, making it
  much easier for developers to find and fix errors in their assembly code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/28e3d238-7b0c-4cf7-bc49-cf172810efea@gjlay.de
bugzilla_url: null
date: '2026-06-21'
is_stub: false
---

This patch corrects a long-standing diagnostic issue in the GNU Assembler (`gas`) for AVR microcontrollers. Previously, when an unsupported opcode was encountered for a specific AVR core, the error message would incorrectly display the mnemonic of the *next* instruction in the instruction table, rather than the problematic one. This fix ensures that `gas` accurately reports the mnemonic of the illegal opcode, improving developer experience and debugging clarity for AVR assembly programming.
