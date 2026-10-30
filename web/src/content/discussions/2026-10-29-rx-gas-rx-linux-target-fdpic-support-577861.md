---
project: binutils
subsystem: rx
patch_id: null
tags:
- binutils
- rx
- gas
- fdpic
- position-independent code
discussion_id: 20261029120303.1987315-3-yoshinori.sato@nifty.com
source_type: public_inbox
title: 'RX: gas rx-linux target FDPIC support'
headline: 'RX: gas rx-linux target FDPIC support'
tldr: Adds FDPIC support to the RX gas assembler for the rx-linux target, enabling
  position-independent code generation.
proposer: Yoshinori Sato <yoshinori.sato@nifty.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the gas configuration and implementation for the RX backend to
  support FDPIC.
- Requires careful handling of new relocation types and assembly options to ensure
  correctness.
exchanges: []
primer_expert: This patch series targets the GNU Assembler's RX backend to add support
  for FDPIC (Fully Distributable Position-Independent Code) on the `rx-linux` target.
  Changes span gas configuration files (`rx-parse.y`, `tc-rx.c`, `tc-rx.h`, `rx-defs.h`)
  and include new relocations, options (`--fdpic`), and logic to handle FDPIC requirements
  for code generation and assembly. This enables the creation of position-independent
  binaries for the RX architecture on Linux.
primer_glossary:
- term: RX
  definition: A family of 32-bit microcontrollers developed by Renesas Electronics.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    language code into machine code.
- term: FDPIC
  definition: Fully Distributable Position-Independent Code. A system for generating
    position-independent code that can be loaded and executed at any memory address
    without modification, including support for shared libraries and position-independent
    data sections.
- term: rx-linux
  definition: A target triplet indicating the RX architecture combined with the Linux
    operating system.
- term: Relocation
  definition: The process by which the linker or loader adjusts memory addresses in
    code or data to their final locations in memory. This is necessary for position-independent
    code and linking object files.
- term: PIC
  definition: Position-Independent Code. Code that can be loaded and executed at any
    memory address without modification. This is essential for shared libraries.
series_id: 'binutils:rx: gas rx-linux target fdpic support'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261029120303.1987315-3-yoshinori.sato@nifty.com
bugzilla_url: null
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This patch series introduces support for FDPIC (Fully Distributable PIC) to the RX gas assembler, specifically for the rx-linux target. It modifies the assembler's configuration files, including parse definitions, C source files, and header files, to recognize and handle FDPIC-specific relocations and options, facilitating the creation of position-independent executables and shared libraries.
