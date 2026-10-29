---
project: binutils
subsystem: binutils
patch_id: null
tags:
- redundancy-removal
- refactoring
- binutils
discussion_id: auJ3fnJI0QrqMNto@squeak.grove.modra.org
source_type: public_inbox
title: Delete redundant check_relocs symndx upper bound checks
headline: Delete redundant check_relocs symndx upper bound checks
tldr: Removes unnecessary upper bound checks for symbol indices in check_relocs functions
  across multiple ELF backends.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes redundant code, improving clarity and slightly reducing binary size. Relies
  on the correctness of `_bfd_elf_link_read_relocs` for validation.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes removing redundant upper bound checks for relocation symbol indices
    (`r_symndx`) from various ELF backend `check_relocs` functions, as these checks
    are already performed by `_bfd_elf_link_read_relocs`.
  quote: '_bfd_elf_link_read_relocs does these checks, and the relocs processed

    by check_relocs always come via that function.'
primer_expert: This patch targets multiple BFD ELF backend files (e.g., `elf32-arm.c`,
  `elf64-x86-64.c`, `elfnn-loongarch.c`) to remove checks for `r_symndx >= nsyms`
  or similar conditions within their respective `check_relocs` functions. The rationale
  is that `_bfd_elf_link_read_relocs` is the primary function that reads relocations,
  and it already validates that `r_symndx` is within the bounds of the symbol table
  size. This eliminates redundant checks and simplifies the `check_relocs` logic.
primer_glossary:
- term: Relocation
  definition: A modification needed in an object file or shared library to resolve
    references to symbols or addresses that are not yet known at link time. This process
    is typically handled by the linker.
- term: Symbol Index
  definition: An integer that uniquely identifies a symbol within a symbol table.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for object files,
    executables, shared libraries, and core dumps on many Unix-like systems.
- term: _bfd_elf_link_read_relocs
  definition: A BFD library function that reads relocation entries from an ELF object
    file's section.
- term: check_relocs
  definition: A function within BFD's ELF backends responsible for validating relocation
    entries against symbol table information.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ3fnJI0QrqMNto@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch removes redundant checks for the upper bound of symbol indices (`r_symndx`) in the `check_relocs` function of numerous ELF backends. The `_bfd_elf_link_read_relocs` function, which is the source of relocations processed by `check_relocs`, already performs these upper bound checks. Therefore, duplicating this validation within `check_relocs` is unnecessary and has been removed to simplify the code.
