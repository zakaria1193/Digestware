---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- avr
- documentation
- bfd
- typo
commit_hash: 933a5bf71939ba2fda55e7010008b06231f0f82f
source_type: public_inbox
author: Georg-Johann Lay <gjl@sourceware.org>
headline: 'AVR: Fix comment typos in BFD''s ELF32 AVR backend'
tldr: Typographical errors in comments within the AVR ELF32 backend of BFD are corrected.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch corrects typos in comments within `bfd/elf32-avr.c`. The
  affected comments relate to diff relocations, instruction layout, and the logic
  for deciding whether to relax jump instructions in AVR code generation.
primer_glossary:
- term: AVR
  definition: A family of microcontrollers developed by Atmel (now Microchip Technology).
    Binutils supports assembling and linking code for these processors.
- term: ELF32
  definition: Executable and Linkable Format, 32-bit. A standard file format for object
    code, executables, and shared libraries, commonly used on Unix-like systems. This
    specific variant is for 32-bit AVR targets.
- term: BFD
  definition: Binary Descriptor format, a library within GNU Binutils for handling
    various object file formats.
- term: comment typos
  definition: Minor spelling or grammatical errors in explanatory text within source
    code. Correcting these improves code readability and maintainability.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260729174503.05AD94BB58AD@sourceware.org
date: '2026-07-29'
is_stub: true
stub_reason: low_score
---

This commit addresses several minor typographical errors found in the comments of the `elf32-avr.c` file. These corrections improve the clarity and accuracy of the documentation within the source code for the AVR ELF32 object file format handler in the BFD library.
