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
discussion_id: 20260701175852.1111-2-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH v2] PE/COFF: raise normal PE section limit safely'
headline: 'PE/COFF: raise normal PE section limit safely'
tldr: Safely increases the maximum number of sections allowed in PE/COFF files processed
  by binutils.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Enables support for larger PE/COFF files with more sections, improving compatibility
  with modern toolchains.
- Adds complexity to section number handling and error checking.
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Proposes a change to safely increase the PE/COFF section limit by properly
    handling unsigned 16-bit section numbers and adding related tests.
  quote: 'PE/COFF stores symbol section numbers in a 16-bit field.  Binutils used

    signed 16-bit handling there, which limited normal PE objects to 32767

    sections even though MSVC and Clang already accept a larger unsigned

    range.


    Raise the normal PE section limit to 65279, while keeping the PE/COFF

    special section-number values for undefined, absolute and debug symbols

    working correctly.  Do this by decodi…'
primer_expert: This patch raises the limit for the number of sections supported in
  PE/COFF files within binutils from 32,767 to 65,279. The prior limitation stemmed
  from treating the 16-bit symbol section number as signed, whereas modern compilers
  like MSVC and Clang support the full unsigned range. The solution correctly decodes
  and encodes these numbers as unsigned, while explicitly preserving special reserved
  values (undefined, absolute, debug). Additionally, it enhances input validation
  by rejecting malformed reserved section numbers earlier in the process and includes
  new test cases for gas and binutil…
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
url: https://inbox.sourceware.org/binutils/20260701175852.1111-2-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This patch addresses a limitation in binutils' handling of PE/COFF files, where symbol section numbers were treated as signed 16-bit integers, restricting normal PE objects to 32,767 sections. The change raises this limit to 65,279 by correctly decoding and encoding section numbers as unsigned values, while preserving special reserved values. It also improves error handling by rejecting invalid reserved section numbers during symbol reading and includes new gas and binutils tests to verify the changes.
