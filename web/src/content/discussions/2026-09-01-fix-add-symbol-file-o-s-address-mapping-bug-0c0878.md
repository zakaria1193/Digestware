---
project: binutils
subsystem: gdb
patch_id: null
tags:
- gdb
- binutils
- debugging
- elf
- address mapping
discussion_id: CA+_Su2J4YNEx3Ox+Nt8Z_nqcuKEjHMQZp9D3S8YB8BU-9JHjFQ@mail.gmail.com
source_type: public_inbox
title: '[gdb] Fix `add-symbol-file -o ... -s ...` address mapping bug'
headline: Fix `add-symbol-file -o ... -s ...` address mapping bug
tldr: Fixes a bug in GDB's `add-symbol-file` command where section addresses are incorrectly
  mapped when using both `-o` and `-s` options.
proposer: Dragorn421 <dragorn421@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Ensuring correct handling of section offsets when multiple mapping options are used.
- Maintaining the integrity of symbol address information during debugging.
exchanges:
- author: Dragorn421 <dragorn421@gmail.com>
  role: proposer
  position: Identifies and explains a bug in GDB's `add-symbol-file` command concerning
    address mapping with `-o` and `-s` options, and proposes a fix.
  quote: This behavior boils down to the `set_objfile_default_section_offset` function
    assuming it can pass 0 as `objfile_relocate`'s `offsets` entries to not modify
    the `-s` mappings previously set by the `symbol_file_add` call in `add_symbol_file_command`.
primer_expert: This patch addresses a bug in GDB's `add-symbol-file` command, which
  is used to load symbol tables from ELF files at specific memory addresses. The problem
  occurs when the `-o` option (to set a default offset for unspecified sections) is
  used in conjunction with the `-s` option (to specify an address for a particular
  section). The `set_objfile_default_section_offset` function incorrectly handles
  the case where a section's address is explicitly set by `-s`, leading to incorrect
  address mappings in the `info files` output.
primer_glossary:
- term: add-symbol-file
  definition: A GDB command used to load symbol table information from an executable
    or shared library file, allowing it to be mapped to arbitrary memory addresses.
- term: ELF file
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps, used on many Unix-like systems.
- term: section mapping
  definition: The process of associating a section within an ELF file (e.g., .text,
    .data) with a specific memory address when loading it for debugging or execution.
- term: -o option
  definition: In `add-symbol-file`, this option sets a default offset for all sections
    not explicitly mapped by other options.
- term: -s option
  definition: In `add-symbol-file`, this option allows specifying a base address for
    a particular section.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+_Su2J4YNEx3Ox+Nt8Z_nqcuKEjHMQZp9D3S8YB8BU-9JHjFQ@mail.gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

Dragorn421 reports a bug in GDB's `add-symbol-file` command where the `-o` (offset) option interferes with specific section mappings provided by the `-s` option. The issue arises because `set_objfile_default_section_offset` incorrectly passes 0 to `objfile_relocate` for sections that should not be modified by the global offset. The proposed fix modifies this function to pass the current offset instead.
