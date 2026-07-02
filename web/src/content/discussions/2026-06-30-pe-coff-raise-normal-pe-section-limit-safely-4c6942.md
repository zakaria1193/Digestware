---
project: binutils
subsystem: pe/coff
patch_id: null
tags:
- pe/coff
- windows
- linker
- symbols
- bugfix
discussion_id: 20260630205916.1179-3-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH] PE/COFF: raise normal PE section limit safely'
headline: 'PE/COFF: raise normal PE section limit safely'
tldr: Safely increases the maximum number of sections allowed in PE/COFF files processed
  by binutils.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: 8
technical_tradeoffs:
- Improves compatibility with modern toolchains and allows for larger PE/COFF files.
- Introduces more complex handling of section number encoding/decoding.
- Adds new test cases to ensure the increased limit is handled correctly.
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Submits a patch to safely increase the PE/COFF section limit by handling
    unsigned 16-bit section numbers and preserving reserved constants, along with
    new tests.
  quote: 'PE/COFF stores symbol section numbers in a 16-bit field.  Binutils used

    signed 16-bit handling there, which limited normal PE objects to 32767

    sections even though MSVC and Clang already accept a larger unsigned

    range.


    Raise the normal PE section limit to 65279, while keeping the PE/COFF

    special section-number values for undefined, absolute and debug symbols

    working correctly.  Do this by decodi…'
- author: Jan Beulich
  role: reviewer
  position: Suggests formatting improvements for long lines in the code and a potential
    consolidation of related manifest constants.
  quote: 'Okay, albeit preferably with ...


    ... this line split for each part to remain within 80 columns (no matter

    that other such long lines exist). Perhaps they all should be consolidated

    into the checking of a single (new) manifest constant, such that mistakes

    like the one being fixed here are easier to avoid. But that''s for later.'
primer_expert: This patch modifies binutils to support a larger number of sections
  (up to 65,279) in PE/COFF files, overcoming a previous limit of 32,767 imposed by
  signed 16-bit interpretation of symbol section numbers. The change ensures compatibility
  with modern toolchains like MSVC and Clang, which support the full unsigned range.
  It involves correctly decoding and encoding section numbers as unsigned values while
  preserving special reserved values. The patch also adds input validation for reserved
  section numbers and includes new test cases to cover scenarios with a high section
  count.
primer_glossary:
- term: PE/COFF
  definition: An object file format used by Windows, combining aspects of the COFF
    format with PE (Portable Executable) headers.
- term: section number
  definition: An identifier for a section within an object file. In PE/COFF symbol
    tables, this number refers to the section to which a symbol belongs.
- term: symbol table
  definition: A data structure within an object file that stores information about
    symbols (e.g., function and variable names, their addresses, and types).
- term: MSVC
  definition: Microsoft Visual C++, a suite of programming tools for the Microsoft
    Windows platform, including a compiler and debugger.
- term: Clang
  definition: A compiler front-end for the C, C++, Objective-C, and Objective-C++
    languages, part of the LLVM project.
- term: gas
  definition: The GNU Assembler, the default assembler used by the GNU Compiler Collection
    (GCC).
- term: objdump
  definition: A utility that displays information from object files, including disassembly
    and symbol tables.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260630205916.1179-3-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This patch increases the limit for the number of sections in PE/COFF files handled by binutils from 32,767 to 65,279. It achieves this by correctly treating symbol section numbers as unsigned 16-bit values, aligning with modern compiler practices, while preserving special reserved section number constants. Additionally, it introduces a new gas test to verify the handling of objects with a high section count and improves input validation for reserved section numbers.
