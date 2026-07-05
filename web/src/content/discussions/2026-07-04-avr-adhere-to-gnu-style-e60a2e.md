---
project: binutils
subsystem: avr
patch_id: null
tags:
- binutils
- avr
- style
- coding standards
discussion_id: fd48d485-ac3b-44a9-849c-a025ad1e9125@gjlay.de
source_type: public_inbox
title: '[patch,pushed] avr: Adhere to GNU style'
headline: 'avr: Adhere to GNU style'
tldr: Binutils code for the AVR target has been updated to comply with GNU coding
  standards.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: committed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- No functional changes, only cosmetic improvements to code readability and maintainability.
exchanges:
- author: Georg-Johann Lay <avr@gjlay.de>
  role: proposer
  position: Submitted a patch to bring binutils' AVR-specific code into compliance
    with GNU coding style.
  quote: 'This patch fixes some style nits:


    - Fix indentations

    - Using TABs for indentation

    - Breaking long lines

    - Remove ; after the closing } of a code block'
primer_expert: This commit applies standard GNU coding style guidelines to the AVR-specific
  source files within the binutils project. It affects `bfd/cpu-avr.c`, `bfd/elf32-avr.c`,
  `bfd/elf32-avr.h`, `gas/config/tc-avr.c`, `opcodes/avr-dis.c`, and `include/opcode/avr.h`.
  The changes are purely stylistic, focusing on consistent indentation (using tabs),
  line wrapping, and brace placement, ensuring uniformity across the codebase.
primer_glossary:
- term: GNU coding style
  definition: A set of recommended conventions for writing code within the GNU project,
    covering aspects like indentation, naming, and formatting.
- term: AVR
  definition: A family of microcontrollers developed by Atmel (now Microchip Technology).
    Binutils includes support for assembling and disassembling code for AVR processors.
- term: BFD
  definition: Binary File Descriptor library, a low-level library used by binutils
    to handle various object file formats.
- term: GAS
  definition: The GNU Assembler, part of binutils, responsible for translating assembly
    language code into machine code.
- term: opcodes
  definition: The module within binutils responsible for disassembling machine code
    back into assembly language.
- term: trunk
  definition: The main development branch in a version control system like Git.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/fd48d485-ac3b-44a9-849c-a025ad1e9125@gjlay.de
bugzilla_url: null
date: '2026-07-04'
is_stub: false
stub_reason: ''
---

This patch, now applied to trunk, rectifies several style nits in the binutils codebase related to the AVR target. Changes include fixing indentations, utilizing tabs for indentation, breaking long lines, and removing superfluous semicolons after closing braces in code blocks across various binutils components like BFD, GAS, opcodes, and include files.
