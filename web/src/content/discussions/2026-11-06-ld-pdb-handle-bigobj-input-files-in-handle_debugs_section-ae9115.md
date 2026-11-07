---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- linker
- binutils
- pdb
- pe
- bigobj
discussion_id: 20261106203339.272-6-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH v2] ld/pdb: Handle bigobj input files in handle_debugs_section'
headline: 'ld/pdb: Handle bigobj input files in handle_debugs_section'
tldr: Linker patch to correctly handle symbol table entries in PE bigobj files for
  PDB debugging information.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Proposes using `bfd_coff_symesz` to handle 20-byte symbol table entries
    in PE bigobj files, fixing PDB generation.
  quote: 'symbol table entries in

    pe-bigobj files are 20 bytes rather than 18.  Use bfd_coff_symesz

    instead.'
primer_expert: This patch for the GNU linker (`ld`) fixes symbol table processing
  for PDB debugging information when dealing with PE 'bigobj' files. The issue arises
  because `struct external_syment` is 18 bytes, but PE bigobj files use 20-byte entries.
  The fix uses `bfd_coff_symesz` to get the correct entry size and updates a test
  case to include `-mbig-obj` for x86.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into executables or other binary formats.
- term: PDB
  definition: Program Database, a file format used by Microsoft Visual C++ for storing
    debugging and project information.
- term: bigobj
  definition: A compiler and linker option that increases the size of object file
    structures, such as the symbol table, to support larger numbers of symbols.
- term: PE file
  definition: Portable Executable, the file format used for executables, DLLs, and
    object files in Windows. 'bigobj' is an extension to this format.
- term: COFF
  definition: Common Object File Format, a file format for object files and executables.
    PE is a derivative of COFF.
- term: symbol table
  definition: A data structure within an object file that lists the symbols (e.g.,
    function names, variable names) defined or referenced by the code.
- term: bfd_coff_symesz
  definition: A function within the BFD library that returns the size of a COFF symbol
    table entry for a given BFD, accounting for platform variations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261106203339.272-6-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the GNU linker (`ld`) where it incorrectly processes symbol table entries for PE 'bigobj' files when generating PDB debugging information. Standard COFF symbol entries are 18 bytes, but 'bigobj' files use 20-byte entries. The patch updates the `handle_debugs_section` function to use `bfd_coff_symesz` to determine the correct size, ensuring compatibility with larger object files. A test case is also updated to use `-mbig-obj`.
