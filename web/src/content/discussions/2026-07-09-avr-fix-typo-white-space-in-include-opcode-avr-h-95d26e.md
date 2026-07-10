---
project: binutils
subsystem: avr
patch_id: null
tags:
- avr
- typo
- whitespace
- documentation
- committed
discussion_id: 9fc1b835-7859-4474-9898-240ebc5455ce@gjlay.de
source_type: public_inbox
title: '[patch,pushed] AVR: Fix typo / white space in include/opcode/avr.h'
headline: 'AVR: Fix typo / white space in include/opcode/avr.h'
tldr: Fixes a typo and trailing whitespace in a comment within the AVR opcode header
  file.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Committed
outcome: committed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Improves code readability and correctness by fixing a typo.
- No functional changes; purely cosmetic.
exchanges: []
primer_expert: This commit rectifies a typographical error ('fux-ups' to 'fix-ups')
  and cleans up trailing whitespace in a comment within `include/opcode/avr.h`. This
  file defines assembly instructions and their properties for the AVR microcontroller
  architecture, used by `gas` and `avr-dis.c`. The change is a standard code hygiene
  improvement and does not impact code generation or disassembly logic.
primer_glossary:
- term: AVR
  definition: A family of microcontrollers developed by Atmel (now Microchip Technology),
    commonly used in embedded systems.
- term: opcode
  definition: A part of a machine language instruction that specifies the operation
    to be performed.
- term: avr.h
  definition: A header file within binutils that defines the opcodes and instruction
    set for the AVR architecture.
- term: gas
  definition: The GNU Assembler, part of the binutils package, responsible for converting
    assembly code into machine code.
- term: typo
  definition: A typographical error; a mistake made in the typed copy of text.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/9fc1b835-7859-4474-9898-240ebc5455ce@gjlay.de
bugzilla_url: null
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

This patch addresses a minor issue in the AVR opcode header file (`include/opcode/avr.h`) by correcting a typo in a comment and removing trailing whitespace. The typo changed 'fux-ups' to 'fix-ups'. The change is purely cosmetic and does not affect the functionality of the AVR toolchain.
