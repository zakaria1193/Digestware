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
discussion_id: 20261120134234.3804649-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[committed] RISC-V: Add Ziccid extension'
headline: 'RISC-V: Add Ziccid extension'
tldr: Adds the Ziccid extension to binutils, which implies Ziccif and has no specific
  instructions.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Committed
outcome: committed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Adds support for a new, albeit minimal, RISC-V extension.
- Ensures consistency with the RISC-V ISA manual for Ziccid.
exchanges: []
primer_expert: This patch updates binutils' BFD and GAS components to recognize the
  RISC-V Ziccid extension. Ziccid is a draft extension that, according to the ISA
  manual, has no instructions or CSRs of its own but implies Ziccif. The changes involve
  adding Ziccid to the supported extensions list and defining its implication to Ziccif
  in `bfd/elfxx-riscv.c`, along with adding a test case in `gas/testsuite/gas/riscv/attribute-ziccid.d`.
primer_glossary:
- term: RISC-V
  definition: An open standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles.
- term: Ziccid
  definition: A draft RISC-V standard extension related to cache control, which implies
    the Ziccif extension.
- term: Ziccif
  definition: A RISC-V standard extension related to cache flushing.
- term: CSR
  definition: Control and Status Register. Special-purpose registers used in CPUs
    to control system behavior or report status.
- term: BFD
  definition: Binary File Descriptor library, a core component of GNU Binutils used
    for reading and writing various object file formats.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils suite.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120134234.3804649-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This commit adds support for the RISC-V Ziccid extension in binutils. The Ziccid extension itself does not introduce new instructions or CSRs, but it implies the Ziccif extension. The change involves updating BFD and gas test suites to recognize and correctly handle this new extension.
