---
project: binutils
subsystem: binutils
patch_id: null
tags:
- bugfix
- elf
- symbol-table
- binutils
discussion_id: auJ4JAZmt6cnWlJI@squeak.grove.modra.org
source_type: public_inbox
title: Correct test for valid use of .dynsym
headline: Correct test for valid use of .dynsym
tldr: Improves the validation logic for using the dynamic symbol table (.dynsym) in
  ELF objects.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improves the correctness of handling dynamic symbol tables, potentially fixing issues
  with certain ELF file structures. No performance impact.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes a more robust check for using the dynamic symbol table (.dynsym)
    in ELF objects.
  quote: '* elf.c (bfd_elf_get_elf_syms): Allow partial use of .dynsym

    when using the dynamic symbol table.'
primer_expert: The patch modifies `bfd/elf.c`'s `bfd_elf_get_elf_syms` function. When
  `elf_use_dt_symtab_p(ibfd)` is true, the original check `elf_tdata(ibfd)->dt_symtab_count
  != symcount + symoffset` was too strict. The new condition `symoffset >= elf_tdata(ibfd)->dt_symtab_count
  || symcount > elf_tdata(ibfd)->dt_symtab_count - symoffset` correctly validates
  that the requested symbol range (`symoffset` to `symoffset + symcount`) is contained
  within the available dynamic symbol table entries.
primer_glossary:
- term: .dynsym
  definition: The dynamic symbol table section in an ELF object file. It contains
    symbols that are visible to the dynamic linker and are used for dynamic linking.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for object files,
    executables, shared libraries, and core dumps on many Unix-like systems.
- term: Symbol Table
  definition: A data structure within an object file or executable that maps symbol
    names to their addresses and other attributes, used by linkers and debuggers.
- term: Dynamic Linker
  definition: A program that resolves symbols and performs relocations for dynamically
    linked executables and libraries at runtime.
- term: bfd_elf_get_elf_syms
  definition: A BFD library function that likely retrieves symbol table information
    from an ELF object file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ4JAZmt6cnWlJI@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch revises the validation logic within `bfd_elf_get_elf_syms` when the dynamic symbol table (`.dynsym`) is used. Previously, it checked for an exact match between `dt_symtab_count` and the sum of `symcount` and `symoffset`. The updated check correctly handles cases where only a portion of `.dynsym` is relevant by ensuring `symoffset` is within bounds and that `symcount` does not exceed the available entries remaining in `dt_symtab_count` after `symoffset`.
