---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gdb
- dwarf
- mach-o
- debugging
discussion_id: 53b97082-1f96-48a2-99c5-f5c55557ef50@suse.de
source_type: public_inbox
title: Add DWARF5 sections in dwarf_section_names_xlat
headline: Add DWARF5 sections in dwarf_section_names_xlat
tldr: Patch adds missing DWARF5 section names to binutils' Mach-O support to fix GDB
  debug info issues.
proposer: Tom de Vries <tdevries@suse.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch modifies the `bfd` library's Mach-O object file parser to
  recognize new DWARF5 debugging sections. The `dwarf_section_names_xlat` table maps
  DWARF section names to internal BFD representations. The issue arises when GDB,
  which relies on BFD, encounters DWARF5 sections not present in this table, preventing
  it from correctly processing debug information on macOS.
primer_glossary:
- term: DWARF
  definition: A standardized debugging data format used by many compilers to store
    information about variables, types, and code structure for debuggers.
- term: DWARF5
  definition: The fifth version of the DWARF debugging data format, introducing new
    features and sections for improved debugging capabilities.
- term: Mach-O
  definition: The executable file format used by macOS and iOS, analogous to ELF on
    Linux or PE on Windows.
- term: bfd
  definition: The Binary File Descriptor library, part of GNU Binutils, providing
    a common interface for reading and writing various object file formats.
- term: .debug_str
  definition: A DWARF section containing null-terminated strings, often used for C++
    mangled names or other string literals.
- term: .debug_str_offsets
  definition: A DWARF section that provides offsets into the .debug_str section, allowing
    for more efficient string lookup.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/53b97082-1f96-48a2-99c5-f5c55557ef50@suse.de
bugzilla_url: null
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

A patch adds DWARF5 section names like .debug_addr and .debug_line_str to the `dwarf_section_names_xlat` table in `bfd/mach-o.c`. This addresses a bug where GDB could not find necessary DWARF5 sections on macOS, leading to incorrect debug information parsing for executables. The fix was tested by rebuilding GDB and confirming that the previous error message no longer appears.
