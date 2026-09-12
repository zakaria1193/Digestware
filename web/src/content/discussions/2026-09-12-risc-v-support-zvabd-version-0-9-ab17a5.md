---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- vector
- extension
discussion_id: cd4ddfbc-1e9b-4829-bc22-343db066a2cb@oss.qualcomm.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Support Zvabd version 0.9'
headline: 'RISC-V: Support Zvabd version 0.9'
tldr: Patch to update RISC-V Zvabd extension support to version 0.9 has been pushed.
proposer: Jeff Law <jeffrey.law@oss.qualcomm.com>
consensus: Proposed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jeff Law <jeffrey.law@oss.qualcomm.com>
  role: reviewer
  position: Approved the patch and pushed it to the repository, noting it saved him
    time.
  quote: LGTM. I went ahead and pushed this to the repo -- I was going to have do
    this myself, so you just saved me a meaningful amount of time. Thanks!
primer_expert: This patch updates binutils' assembler and disassembler support for
  the RISC-V 'Zvabd' (absolute difference) vector extension to its 0.9 specification.
  This involves changes to the instruction encodings and variants within BFD, GAS,
  and the opcode tables, reflecting updates in the RISC-V ISA manual.
primer_glossary:
- term: Zvabd
  definition: A RISC-V vector extension that provides instructions for calculating
    the absolute difference between vector elements.
- term: BFD
  definition: Binary File Descriptor library, a component of binutils that provides
    a portable interface to object file formats like ELF.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    converting assembly language code into machine code.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer principles.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/cd4ddfbc-1e9b-4829-bc22-343db066a2cb@oss.qualcomm.com
bugzilla_url: null
date: '2026-09-12'
is_stub: false
stub_reason: ''
---

This patch updates the binutils support for the RISC-V Zvabd extension to version 0.9, incorporating changes to instruction variants and encodings as approved in the RISC-V ISA manual. The changes affect BFD, GAS, and opcodes components. The reviewer LGTM'd and pushed the patch, saving the author time.
