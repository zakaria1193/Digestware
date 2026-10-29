---
project: binutils
subsystem: binutils
patch_id: null
tags:
- elf
- relocations
- symbol table
- bugfix
discussion_id: auJ2_Wox0zewHJmO@squeak.grove.modra.org
source_type: public_inbox
title: Ignore empty symtab sections
headline: Ignore empty symtab sections
tldr: This patch prevents BFD from processing relocations in objects with empty symbol
  tables.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Disables a test case for rx-elf that requires modification to work with the new
  validation logic.
exchanges: []
primer_expert: This patch modifies `bfd/elf.c` to validate `sh_info` and `sh_size`
  for SHT_SYMTAB and SHT_DYNSYM sections. Previously, BFD might incorrectly process
  relocations when these sections were empty or malformed, leading to assertion failures
  or incorrect behavior in GNU ld. The change ensures that such sections are ignored
  if their size is less than the entry size, or if `sh_info` is zero, preventing downstream
  issues in relocation handling.
primer_glossary:
- term: .symtab
  definition: A section in an ELF object file that contains the symbol table, which
    maps symbol names to their addresses and other information.
- term: BFD
  definition: Binary File Descriptor library, a low-level interface used by binutils
    for manipulating object files.
- term: GNU ld
  definition: The GNU linker, responsible for combining object files into executables
    or libraries.
- term: relocations
  definition: Information in an object file that tells the linker how to adjust addresses
    when combining object files, especially in position-independent code.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: SHT_SYMTAB
  definition: A section header type in ELF that identifies a symbol table section.
- term: sh_info
  definition: A field in an ELF section header that provides information specific
    to the section type, such as the index of the associated string table for a symbol
    table.
- term: sh_size
  definition: A field in an ELF section header that indicates the size of the section
    in bytes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ2_Wox0zewHJmO@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch addresses issues where BFD and GNU ld encounter errors when an empty .symtab section is present in ELF objects. It prevents BFD from attempting to handle relocations in such cases, similar to how missing .symtab sections are handled. The changes also improve error reporting and disable a test case on rx-elf that previously failed due to the issue.
