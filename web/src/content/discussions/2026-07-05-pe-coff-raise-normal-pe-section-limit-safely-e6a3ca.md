---
project: binutils
subsystem: pe/coff
patch_id: null
tags:
- binutils
- pe/coff
- linker
- object-file-format
discussion_id: 20260705220703.1725-2-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: 'PE/COFF: raise normal PE section limit safely'
headline: 'PE/COFF: raise normal PE section limit safely'
tldr: Increase the maximum number of sections in PE/COFF objects from 32767 to 65279
  by using unsigned integers for section numbers.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increases the maximum section count, potentially improving compatibility with tools
  that generate large numbers of sections.
exchanges:
- author: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
  role: proposer
  position: Proposes to increase the normal PE section limit from 32767 to 65279 by
    using unsigned integers for section numbers, while maintaining correct handling
    of special section values and improving error checking.
  quote: PE/COFF stores symbol section numbers in a 16-bit field. Binutils used signed
    16-bit handling there, which limited normal PE objects to 32767 sections even
    though MSVC and Clang already accept a larger unsigned range.
primer_expert: This patch revises the PE/COFF object file parsing and writing logic
  within binutils to support more than 32767 sections. Previously, a signed 16-bit
  field for symbol section numbers imposed this limit. The change correctly uses unsigned
  values for normal section numbers up to 65279, while explicitly mapping the reserved
  section numbers (Undefined, Absolute, Debug) to ensure compatibility. It also adds
  input validation to catch malformed section numbers earlier and includes test cases
  in gas and binutils.
primer_glossary:
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, the file format used
    for executables, object code, and DLLs in 32-bit and 64-bit versions of Windows
    operating systems. It is based on the COFF format.
- term: section number
  definition: In PE/COFF files, a number within a symbol's entry that indicates which
    section of the object file the symbol belongs to. Special values are reserved
    for symbols not associated with a specific section.
- term: binutils
  definition: A collection of binary tools for GNU systems, including assemblers,
    linkers, and utilities for manipulating object files.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    language code into machine code.
- term: objdump
  definition: A utility from GNU Binutils that displays information from object files,
    including section contents and symbol tables.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260705220703.1725-2-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-07-05'
is_stub: false
stub_reason: ''
---

This patch addresses an limitation in the PE/COFF format where the number of sections in an object file was capped at 32767 due to signed 16-bit handling of section numbers. The proposal raises this limit to 65279 by properly decoding and encoding section numbers as unsigned values, while preserving special reserved values. It also enhances error handling by rejecting invalid reserved section numbers during input reading and includes new tests for gas and binutils to ensure the changes function correctly.
