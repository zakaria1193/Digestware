---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- ld
- pdb
- debug info
- bigobj
- coff
discussion_id: d071adcc-0a19-447d-b80f-d76622d28dd4@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2] ld/pdb: Handle bigobj input files in handle_debugs_section'
headline: 'ld/pdb: Handle bigobj input files in handle_debugs_section'
tldr: Patch corrects ld/pdb to use bfd_coff_symesz for stepping through COFF symbol
  tables, accommodating bigobj files.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Proposes to use `bfd_coff_symesz` for stepping through symbol table entries
    in `handle_debugs_section` to correctly handle bigobj files, and suggests running
    a C13 line info test with -mbig-obj on x86.
  quote: 'handle_debugs_section stepped through the raw COFF symbol table using

    sameof (struct external_syment), but symbol table entries in

    pe-bigobj files are 20 bytes rather than 18.  Use bfd_coff_symesz

    instead.


    Run the C13 line info test a second time with objects assembled with

    -mbig-obj on x86.'
- author: Jan Beulich
  role: reviewer
  position: Acknowledges and approves the proposed change.
  quote: Okay.
primer_expert: This patch in binutils's linker (ld) component addresses the PDB debug
  format handling. It corrects an issue where the linker incorrectly assumed a fixed
  size for COFF symbol table entries when processing `bigobj` files, which use larger
  entries. The change ensures correct parsing by using `bfd_coff_symesz`.
primer_glossary:
- term: ld/pdb
  definition: The linker (ld) component responsible for handling the Program Database
    (PDB) format, a proprietary Microsoft symbol file format used by the Visual C++
    compiler.
- term: bigobj
  definition: A file format that supports symbol tables larger than 2^32 entries,
    overcoming limitations of older COFF formats.
- term: COFF
  definition: Common Object File Format, a file format used for object files, executables,
    and core dumps on Unix-like systems. It is a precursor to PE (Portable Executable)
    format.
- term: bfd_coff_symesz
  definition: A function or value within the Binary File Descriptor (BFD) library
    that provides the correct size for COFF symbol table entries, accounting for variations
    like those in bigobj files.
series_id: d071adcc-0a19-447d-b80f-d76622d28dd4@suse.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/d071adcc-0a19-447d-b80f-d76622d28dd4@suse.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in ld/pdb where the COFF symbol table was incorrectly processed for bigobj input files. The original code used a fixed size for symbol table entries, but bigobj files use larger entries. The fix involves using `bfd_coff_symesz` to correctly determine the size of symbol table entries, ensuring proper handling of debug information.
