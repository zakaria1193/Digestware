---
project: binutils
subsystem: pe/coff
patch_id: null
tags:
- binutils
- pe/coff
- elf
- linker
- sections
discussion_id: 20260714202348.1105-2-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: 'PE/COFF: raise normal PE section limit safely'
headline: 'PE/COFF: raise normal PE section limit safely'
tldr: Increases the maximum number of sections in PE/COFF objects from 32767 to 65279
  by using unsigned 16-bit integers for section numbers.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increasing the section limit improves compatibility with modern toolchains but requires
  careful handling of existing code and special section values to avoid breaking existing
  functionality.
exchanges: []
primer_expert: The PE/COFF executable format has a limit on the number of sections,
  imposed by the 16-bit field used for section numbers in symbol table entries. Historically,
  binutils treated this as signed, limiting valid section numbers to 32767. This patch
  corrects this by interpreting and encoding these numbers as unsigned, aligning with
  the format's capability to support up to 65535 sections (minus reserved values),
  thus enabling the creation of objects with more sections.
primer_glossary:
- term: PE/COFF
  definition: Portable Executable / Common Object File Format. The standard file format
    for executables, object code, and DLLs used in Windows operating systems.
- term: section number
  definition: In the PE/COFF format, a symbol table entry refers to a section by its
    number (index).
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU binutils
    to handle various object file formats.
- term: gas
  definition: The GNU Assembler, part of the GNU binutils.
- term: objdump
  definition: A utility in GNU binutils that displays information from object files.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260714202348.1105-2-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

Oleg Tolmatcev proposes raising the section limit in PE/COFF objects from 32,767 to 65,279. This change is necessary because binutils currently uses signed 16-bit integers for symbol section numbers, whereas modern compilers like MSVC and Clang support a larger unsigned range. The patch modifies BFD to handle section numbers as unsigned values while preserving special constants, and includes a new gas test case to verify the functionality.
