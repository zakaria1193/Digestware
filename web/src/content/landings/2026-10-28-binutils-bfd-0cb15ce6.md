---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- elf
- linking
- bfd
commit_hash: 0cb15ce61d9d777965bb2eb2086b77382d2caef6
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Allow partial use of .dynsym when using dynamic symbols
tldr: Binutils BFD now correctly handles partial use of .dynsym for dynamic symbol
  tables.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In BFD's ELF support, `bfd_elf_get_elf_syms` handles symbol table retrieval.
  When `elf_use_dt_symtab_p` is true, it uses the dynamic symbol table. The previous
  check `dt_symtab_count != symcount + symoffset` was too strict. This commit refines
  the check to `symoffset >= dt_symtab_count || symcount > dt_symtab_count - symoffset`,
  which correctly accounts for the available symbols within the dynamic symbol table,
  accommodating cases where the symbol count does not exactly match the dynamic table
  size.
primer_glossary:
- term: .dynsym
  definition: The dynamic symbol table section in an ELF file. It contains symbols
    that are needed for dynamic linking at runtime.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: BFD
  definition: Binary File Descriptor library. A library used by GNU Binutils to provide
    a generic interface for reading and writing various binary file formats, including
    ELF.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261028223655.89BC04BA2E33@sourceware.org
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This change adjusts the BFD library to correctly handle scenarios where the dynamic symbol table (.dynsym) is used partially. Previously, it enforced a strict equality check between the number of symbols and the dynamic symbol table count, which could lead to errors in valid use cases. The updated logic now allows for partial use, improving robustness when processing ELF files with dynamic linking.
