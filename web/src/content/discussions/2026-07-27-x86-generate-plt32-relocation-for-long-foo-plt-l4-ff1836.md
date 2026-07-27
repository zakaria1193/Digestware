---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- relocation
- assembler
- linker
- patch
discussion_id: CAMe9rOoQR-AGCqWqfL5vHw45bBVZ03MQhQygKf-AvULkZ2p65w@mail.gmail.com
source_type: public_inbox
title: '[PATCH v2] x86: Generate PLT32 relocation for ".long foo@PLT - .L4"'
headline: 'x86: Generate PLT32 relocation for .long foo@PLT - .L4'
tldr: Adds support for generating PLT32 relocations for x86 and x86-64, mirroring
  LLVM assembler's behavior for directives like '.long foo@PLT - .L4'.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Aligns binutils behavior with LLVM, improving consistency across different toolchains.
- Resolves a specific bug (PR gas/34423) related to how certain function calls are
  resolved.
- Introduces new relocation types and handling logic into the assembler and linker.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Submits a v2 patch to add PLT32 relocation generation for x86 and x86-64,
    mirroring LLVM assembler and addressing PR gas/34423.
  quote: 'Add i386 support like LLVM assembler in the v2 patch.


    LLVM assembler supports directives like ".long foo@PLT - .L4" for i386

    and x86-64.  Implement the same feature to generate PLT32 relocation

    for directives like ".long foo@PLT - .L4" so that PLT entries are used

    to resolve the PC32 relocation against function symbols.'
primer_expert: This patch series (v2) introduces support for the `BFD_RELOC_X86_64_PLT32`
  relocation type in the binutils, specifically for the x86-64 and i386 architectures.
  It enables the assembler (gas) to generate `R_X86_64_PLT32` for expressions like
  `.long foo@PLT - .L4`, which involves calculating a PC-relative offset to a PLT
  entry. This behavior mirrors that of the LLVM assembler. The changes span BFD (by
  adding the new relocation type), gas (by modifying the assembler's logic to recognize
  and generate this relocation), and ld (with test cases). The goal is to ensure that
  indirect function calls us…
primer_glossary:
- term: PLT
  definition: Procedure Linkage Table. A table used in executable files and shared
    libraries to resolve indirect function calls to functions that are not defined
    in the current module, typically used for dynamic linking.
- term: PLT32 / R_X86_64_PLT32
  definition: A specific type of ELF relocation used on x86-64 architectures. It indicates
    that a 32-bit PC-relative offset to an entry in the Procedure Linkage Table (PLT)
    needs to be calculated and patched into the code at link time.
- term: PC32 relocation
  definition: A type of relocation that calculates an offset relative to the current
    Program Counter (PC). On x86-64, R_X86_64_PC32 is used for 32-bit PC-relative
    addressing.
- term: BFD
  definition: Binary File Descriptor library. A library used by GNU Binutils to provide
    a common interface for reading and writing various object file formats.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils, responsible for translating
    assembly language code into machine code.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: PR gas/34423
  definition: Problem Report number 34423 filed against the GNU Assembler, likely
    related to the functionality addressed by this patch.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOoQR-AGCqWqfL5vHw45bBVZ03MQhQygKf-AvULkZ2p65w@mail.gmail.com
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This patch introduces support for generating PLT32 relocations for x86 and x86-64 architectures, aligning with the functionality of the LLVM assembler. It enables the handling of directives such as ".long foo@PLT - .L4" by generating R_X86_64_PLT32 relocations, which utilize PLT entries to resolve PC32 relocations against function symbols. This addresses PR gas/34423 and includes updates to BFD, gas, and ld components, along with new test cases.
