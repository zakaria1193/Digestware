---
project: binutils
subsystem: x86-64
patch_id: null
tags:
- binutils
- assembler
- x86-64
- relocation
- PIC
discussion_id: CAMe9rOpFTW9DN_0ZjSEaL6rN0QM+RsKg7PAmwrys1gRgEoLzpA@mail.gmail.com
source_type: public_inbox
title: '[PATCH] x86-64: Generate R_X86_64_PLT32 for ".long foo@PLT - .L4"'
headline: 'x86-64: Generate R_X86_64_PLT32 for ".long foo@PLT - .L4"'
tldr: Adds a new relocation type R_X86_64_PLT32 to binutils for specific PIC scenarios
  involving PLT entries.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Introducing a new relocation type adds complexity to the binutils codebase but enables
  support for specific PIC optimizations.
- Correctly handling PLT-relative relocations is essential for the performance and
  correctness of dynamically linked executables.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Submits a patch to introduce and utilize the R_X86_64_PLT32 relocation
    type for specific directives involving PLT entries.
  quote: 'Add BFD_RELOC_X86_64_PLT32 and use it to generate R_X86_64_PLT32 for

    directives like ".long foo@PLT - .L4" so that PLT entries are used to

    resolve the PC32 relocation against function symbols for such directives.'
primer_expert: This patch enhances binutils' handling of x86-64 relocations, particularly
  for Position Independent Code (PIC). It introduces a new relocation type, `R_X86_64_PLT32`,
  which is a PC-relative 32-bit relocation specifically designed for accessing Procedure
  Linkage Table (PLT) entries. This is necessary for constructs like `.long symbol@PLT
  - offset`, ensuring that the linker correctly resolves the address using the PLT
  mechanism rather than a direct symbol lookup, which is crucial for shared library
  calls in PIC.
primer_glossary:
- term: x86-64
  definition: A 64-bit microarchitecture and instruction set extension of the x86
    instruction set, commonly used in modern desktop and server CPUs.
- term: PLT
  definition: Procedure Linkage Table. A table used in dynamically linked executables
    on systems like Linux to resolve external function calls at runtime. It helps
    achieve Position Independent Code (PIC).
- term: R_X86_64_PLT32
  definition: A specific relocation type for the x86-64 architecture, indicating a
    32-bit PC-relative offset to a Procedure Linkage Table entry.
- term: Position Independent Code (PIC)
  definition: Code that can run correctly regardless of where it is loaded in memory.
    Essential for shared libraries.
- term: gas
  definition: The GNU Assembler, a component of the GNU Binutils package that translates
    assembly language code into machine code.
- term: BFD
  definition: Binary File Descriptor. A library within GNU Binutils that provides
    a consistent interface for reading and writing various object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOpFTW9DN_0ZjSEaL6rN0QM+RsKg7PAmwrys1gRgEoLzpA@mail.gmail.com
bugzilla_url: null
date: '2026-07-25'
is_stub: false
stub_reason: ''
---

This patch introduces the `BFD_RELOC_X86_64_PLT32` relocation type and uses it in the gas assembler for x86-64 targets. This addresses PR gas/34423 by generating the `R_X86_64_PLT32` relocation for directives like `.long foo@PLT - .L4`. The intention is to ensure that relocations against function symbols in such directives are correctly resolved using PLT entries, specifically for PC32 relative relocations.
