---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- elf
- linking
- cleanup
- bfd
- relocations
commit_hash: 9dff5cb1aa18a779d952bffee9177590603ec394
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Remove redundant upper bound checks for relocation symbol indices
tldr: Multiple ELF backends in BFD no longer check the upper bound of relocation symbol
  indices, as this is handled by a central function.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `_bfd_elf_link_read_relocs` function in `elflink.c` is responsible
  for reading relocations. It performs essential validation, including ensuring that
  `r_symndx` values are within the valid range of the symbol table. Various architecture-specific
  `check_relocs` or `scan_relocs` functions previously duplicated this check. This
  commit removes these redundant checks from the listed backends, relying solely on
  the central validation in `_bfd_elf_link_read_relocs` for consistency and code reduction.
primer_glossary:
- term: r_symndx
  definition: The symbol table index field within an ELF relocation entry. It indicates
    which symbol the relocation refers to.
- term: relocation
  definition: Information in an object file that describes how to modify certain addresses
    or symbols when linking. For example, a relocation entry might indicate that a
    specific address needs to be updated with the actual address of a function.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: BFD
  definition: Binary File Descriptor library. A library used by GNU Binutils to provide
    a generic interface for reading and writing various binary file formats, including
    ELF.
discussion_id_link: public_inbox:binutils#9934
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261028223640.3477B4BA23D7@sourceware.org
date: '2026-10-28'
is_stub: true
stub_reason: low_score
---

Several ELF backend implementations in BFD have been updated to remove redundant checks for the upper bound of relocation symbol indices (`r_symndx`). The central function `_bfd_elf_link_read_relocs` already performs these necessary boundary checks, making the per-backend checks unnecessary. This change simplifies the code across various architectures.
