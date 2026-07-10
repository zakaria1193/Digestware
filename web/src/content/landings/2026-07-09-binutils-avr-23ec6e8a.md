---
project: binutils
subsystem: binutils/avr
patch_id: null
tags:
- binutils
- avr
- typo
commit_hash: 23ec6e8a1ac897c4ee16f521e626b2382af32a40
source_type: public_inbox
author: Georg-Johann Lay <gjl@sourceware.org>
headline: Fix typo and whitespace in AVR opcode header
tldr: Corrects a typo and trailing whitespace in the AVR opcode header file.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit fixes a minor typo ('fux-ups' to 'fix-ups') and removes
  trailing whitespace in a comment within the AVR opcode header file (include/opcode/avr.h).
  These are cosmetic changes that improve code readability and maintainability without
  affecting functionality.
primer_glossary:
- term: AVR
  definition: A family of microcontrollers developed by Atmel (now Microchip Technology).
    Binutils include support for assembling and disassembling AVR code.
- term: opcode header
  definition: A header file that defines the instructions (opcodes) for a specific
    processor architecture. It includes information such as instruction mnemonics,
    encodings, and operand types.
- term: pseudo-instruction
  definition: An instruction that is not directly executed by the CPU but is processed
    by the assembler or compiler. They are often used for convenience or to represent
    complex operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260709111024.33B1B4BA23C2@sourceware.org
date: '2026-07-09'
is_stub: true
stub_reason: low_score
---

A typo and trailing whitespace in the include/opcode/avr.h file are corrected. The change adjusts a comment related to operand evaluation for pseudo-instructions, ensuring code clarity and adherence to formatting standards.
