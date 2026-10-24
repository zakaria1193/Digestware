---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- nanomips
- mips
- architecture
- gas
discussion_id: 20261023101053.2756793-1-lei.wang@oss.cipunited.com
source_type: public_inbox
title: '[PATCH v4 0/7] Add-support-for-nanoMIPS-architecture'
headline: Add-support-for-nanoMIPS-architecture
tldr: Adds support for the nanoMIPS architecture to GNU Binutils (Gas, BFD, Opcodes).
proposer: Tsing <lei.wang@oss.cipunited.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Adding support for a new architecture increases the complexity and maintenance burden
  of Binutils.
- Ensuring the variable-length instruction encoding is handled correctly by the assembler
  and disassembler.
- Validating the correctness of the ISA and ABI implementations across various toolchain
  components.
exchanges:
- author: Tsing
  role: proposer
  position: Submitted a seven-patch series (v4) to add support for the nanoMIPS architecture
    to Binutils.
  quote: 'This set of patches provides support for the nanomips architecture

    in the Gas, BFD and Opcodes. nanoMIPS is a code-size-optimized,

    variable-length-encoding ISA from MIPS Technologies.

    nanoMIPS has 16, 32, and 48-bit instructions.'
primer_expert: This patch series introduces support for the nanoMIPS architecture
  into GNU Binutils, encompassing the assembler (Gas), Binary File Descriptor (BFD)
  library, and the Opcodes module. nanoMIPS is an MIPS Technologies ISA variant optimized
  for code size, featuring variable-length instructions (16, 32, and 48 bits). The
  submission includes modifications to assembler configuration, instruction encoding,
  object file handling, linking, documentation, and test cases, verified on a nanomips-mti-elf
  toolchain.
primer_glossary:
- term: nanoMIPS
  definition: A code-size-optimized instruction set architecture (ISA) from MIPS Technologies,
    characterized by variable-length instructions (16, 32, and 48 bits).
- term: Gas
  definition: The GNU Assembler, part of GNU Binutils, which translates assembly code
    into machine code.
- term: BFD
  definition: Binary File Descriptor library, a part of GNU Binutils that provides
    a consistent interface to various object file formats.
- term: Opcodes
  definition: A module within Binutils that defines and handles instruction encodings
    for different architectures.
- term: ISA
  definition: Instruction Set Architecture, the set of commands a processor understands.
- term: ABI
  definition: Application Binary Interface, defines how low-level code is written,
    how functions are called, and how data is laid out in memory.
- term: variable-length encoding
  definition: An instruction encoding scheme where instructions can occupy different
    numbers of bytes, allowing for denser code representation.
series_id: binutils:add-support-for-nanomips-architecture
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261023101053.2756793-1-lei.wang@oss.cipunited.com
bugzilla_url: null
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

Tsing (lei.wang@oss.cipunited.com) presents a seven-patch series (v4) to add support for the nanoMIPS architecture to GNU Binutils. This includes modifications to the Gas assembler, BFD library, and Opcodes module, along with updates to readelf, ld, documentation, and test suites. The nanoMIPS architecture, from MIPS Technologies, is a code-size-optimized ISA with variable-length instructions (16, 32, and 48 bits). The patches have been tested on a nanomips-mti-elf target.
