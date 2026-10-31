---
project: binutils
subsystem: binutils
patch_id: null
tags:
- DWARF
- Mach-O
- debugging
- BFD
discussion_id: ba44aab1-438d-469a-905b-588ed67a6823@suse.com
source_type: public_inbox
title: 'Re: [PATCH] [bfd/mach-o] Add DWARF5 sections in dwarf_section_names_xlat'
headline: Add DWARF5 sections in dwarf_section_names_xlat
tldr: Adds support for new DWARF5 debug sections in the Mach-O object file format.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds support for DWARF5 sections, improving debugging capabilities on macOS, by
  expanding the section name translation table.
exchanges:
- author: Tom de Vries
  role: proposer
  position: Identified an issue where GDB fails to load DWARF5 debug information on
    macOS AArch64 due to missing section name translations in binutils' Mach-O parser.
    Submitted a patch to add these missing DWARF5 sections.
  quote: 'The error message is actually wrong, it''s the .debug_str_offsets section
    that

    gdb can''t find.


    This is because that and other DWARF5 sections are not supported in the

    dwarf_section_names_xlat table in bfd/mach-o.c.


    Fix this by adding the missing sections.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the patch and its adherence to existing patterns, without
    further comments on the technical details.
  quote: 'Okay. This looks to follow an existing pattern, and I guess it doesn''t
    make

    much sense for me to ask where that model of translation is specified.'
primer_expert: This patch modifies `bfd/mach-o.c` to update the `dwarf_section_names_xlat`
  table. This table maps DWARF section names (e.g., `.debug_info`) to their Mach-O
  specific representations (e.g., `__debug_info`). The original table lacked entries
  for several DWARF5 sections like `.debug_addr`, `.debug_line_str`, `.debug_str_offsets`,
  etc. This omission caused tools like GDB to fail when processing DWARF5 debug info
  on Mach-O binaries, as they couldn't locate these essential sections. The patch
  adds these missing entries, ensuring proper DWARF5 section discovery.
primer_glossary:
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to represent
    information about source code, variables, and types.
- term: DWARF5
  definition: The fifth version of the DWARF debugging data format, introducing new
    features and sections for more efficient and detailed debugging information.
- term: Mach-O
  definition: Mach Object file format. The standard executable file format used on
    macOS and iOS.
- term: BFD
  definition: Binary File Descriptor library. A part of GNU Binutils that provides
    a common interface for reading and writing various object file formats.
- term: section
  definition: A distinct part of an object file or executable, such as code (.text),
    initialized data (.data), or uninitialized data (.bss).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ba44aab1-438d-469a-905b-588ed67a6823@suse.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where the Mach-O object file parser in binutils' BFD library was missing support for several DWARF5 debug sections. This prevented tools like GDB from correctly loading debug information from DWARF5-enabled executables on macOS, particularly on AArch64. The fix adds the missing section names to the `dwarf_section_names_xlat` table, enabling GDB to find and parse these sections.
