---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- bfd
- mach-o
- dwarf5
- debugging
discussion_id: 20261023133425.173952-1-tdevries@suse.de
source_type: public_inbox
title: '[PATCH] [bfd/mach-o] Add DWARF5 sections in dwarf_section_names_xlat'
headline: Add DWARF5 sections in dwarf_section_names_xlat
tldr: Adds support for DWARF5 debugging sections to binutils' Mach-O object file handling,
  fixing GDB errors.
proposer: Tom de Vries <tdevries@suse.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding new sections to the translation table increases its size.
- Ensuring the mapping is correct for all relevant DWARF5 sections and doesn't interfere
  with existing ones.
- Potential for GDB (or other tools) to misinterpret or incorrectly use the newly
  supported sections if their handling logic is also incomplete.
exchanges:
- author: Tom de Vries
  role: proposer
  position: Submitted a patch to add missing DWARF5 section names to the Mach-O handler
    in binutils.
  quote: 'This is because that and other DWARF5 sections are not supported in the

    dwarf_section_names_xlat table in bfd/mach-o.c.


    Fix this by adding the missing sections.'
primer_expert: This patch targets the Mach-O backend within binutils' BFD library,
  specifically addressing incomplete support for DWARF5 debugging information. The
  issue arises because the `dwarf_section_names_xlat` table in `bfd/mach-o.c` does
  not map all recognized DWARF5 section names (e.g., `.debug_addr`, `.debug_line_str`,
  `.debug_str_offsets`) to their corresponding internal BFD representations. This
  leads to errors when tools like GDB attempt to process DWARF5-compliant object files
  generated for Mach-O targets, particularly on macOS.
primer_glossary:
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about program variables, types, and structure.
- term: DWARF5
  definition: The fifth version of the DWARF debugging data format, introducing new
    features and sections for improved debugging capabilities.
- term: Mach-O
  definition: Mach Object file format, the standard executable file format used on
    macOS and iOS.
- term: bfd
  definition: Binary File Descriptor library, a low-level library used by GNU Binutils
    for handling various object file formats.
- term: dwarf_section_names_xlat
  definition: A translation table within binutils/bfd that maps section names (e.g.,
    '.debug_line') to internal BFD attributes for different object file formats.
- term: .debug_str_offsets
  definition: A DWARF5 section containing offset information for string data, used
    for efficient string lookup during debugging.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261023133425.173952-1-tdevries@suse.de
bugzilla_url: null
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

Tom de Vries proposes a patch to binutils to add support for several DWARF5 debugging sections, which were missing from the `dwarf_section_names_xlat` table in `bfd/mach-o.c`. This omission caused GDB to fail when processing Mach-O files containing these DWARF5 sections, specifically reporting errors related to missing `.debug_str_offsets` and other sections. The patch adds these missing sections, resolving the GDB errors and allowing successful debugging.
