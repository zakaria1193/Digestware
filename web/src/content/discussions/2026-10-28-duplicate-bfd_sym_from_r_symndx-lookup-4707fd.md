---
project: binutils
subsystem: binutils
patch_id: null
tags:
- refactoring
- code-duplication
- binutils
discussion_id: auJ4bvQSeduo3CXX@squeak.grove.modra.org
source_type: public_inbox
title: Duplicate bfd_sym_from_r_symndx lookup
headline: Duplicate bfd_sym_from_r_symndx lookup
tldr: Removes redundant local symbol lookups in multiple ELF backend's check_relocs
  functions and cleans up old comments.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Reduces code duplication and improves maintainability by removing redundant logic.
  No functional changes or performance impacts are expected.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Identifies and removes duplicated local symbol lookup logic in multiple
    ELF backends' `check_relocs` functions, also cleaning up comments.
  quote: 'elf32-csky.c, elf32-i386.c, elf32-s390.c, elf64-s390.c, elf64-x86-64.c,

    elfnn-aarch64.c, elfnn-kvx.c and elfnn-riscv.c all repeat a local sym

    lookup in their check_relocs function.  Fix that, and trim an old

    comment in the other files touched here.'
primer_expert: The patch refactors the `check_relocs` function in several BFD ELF
  backends (e.g., `elf32-csky.c`, `elf64-x86-64.c`, `elfnn-aarch64.c`). It removes
  a repeated `bfd_sym_from_r_symndx` lookup within the `else` block that handles non-local
  symbols, consolidating this logic. This likely stems from an earlier attempt to
  support relocations against local symbols more directly, as hinted by the removed
  comments, but has since been simplified or refactored.
primer_glossary:
- term: Relocation
  definition: A modification needed in an object file or shared library to resolve
    references to symbols or addresses that are not yet known at link time. This process
    is typically handled by the linker.
- term: Symbol
  definition: An identifier (name) associated with a memory location or value in a
    program, such as a variable, function, or constant.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for object files,
    executables, shared libraries, and core dumps on many Unix-like systems.
- term: bfd_sym_from_r_symndx
  definition: A BFD library function that likely retrieves symbol information based
    on its index in the relocation entry.
- term: check_relocs
  definition: A function within BFD's ELF backends responsible for validating relocation
    entries against symbol table information.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ4bvQSeduo3CXX@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch consolidates duplicated code by removing redundant lookups of local symbols using `bfd_sym_from_r_symndx` within the `check_relocs` function across various ELF backends. It also trims outdated comments in the affected files. The goal is to eliminate code duplication and improve maintainability.
