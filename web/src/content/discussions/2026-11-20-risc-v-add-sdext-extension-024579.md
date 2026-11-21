---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- linker
- isa
- extensions
discussion_id: 20261120134220.3804350-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[committed] RISC-V: Add Sdext extension'
headline: 'RISC-V: Add Sdext extension'
tldr: Adds the Sdext extension to binutils, which implies Zicsr and is related to
  RISC-V debug.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Committed
outcome: committed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Adds support for the RISC-V Sdext extension.
- Ensures correct implication handling with Zicsr.
- Maintains compatibility with the RISC-V debug specification.
exchanges: []
primer_expert: This patch integrates the RISC-V Sdext extension into binutils. Sdext,
  related to the RISC-V debug specification, implies the Zicsr extension. The modifications
  are made in `bfd/elfxx-riscv.c` to include Sdext in the list of supported extensions
  and define its implication, and in `gas/testsuite/gas/riscv/imply.d` and `march-help.l`
  to add corresponding test cases.
primer_glossary:
- term: RISC-V
  definition: An open standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles.
- term: Sdext
  definition: A RISC-V standard extension related to debug functionality, implying
    the Zicsr extension.
- term: Zicsr
  definition: A RISC-V standard extension for Control and Status Register access.
- term: BFD
  definition: Binary File Descriptor library, a core component of GNU Binutils used
    for reading and writing various object file formats.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils suite.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120134220.3804350-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This commit introduces support for the RISC-V Sdext extension in binutils. Sdext is part of the RISC-V debug specification and implies the Zicsr extension. The change updates BFD and GAS to recognize this extension, ensuring correct handling of debug-related features.
