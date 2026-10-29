---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- elf
- cleanup
- type safety
commit_hash: dc3dffcccc1585e74e8535b7b9e92d5eb63f107e
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Constify Elf_Internal_Sym pointers in ELF processing
tldr: Makes Elf_Internal_Sym pointers const in ELF relocation and section processing
  functions.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch constifies `Elf_Internal_Sym *` parameters and variables
  within BFD's `check_relocs` and `relocate_section` functions. The author notes this
  work was a leftover from an attempt to improve handling of relocations against `STN_UNDEF`
  when no `.symtab` is present. While that larger goal was dropped, this change improves
  type correctness by marking symbols that are only read, not written, during these
  operations.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU Binutils
    to parse and manipulate various object file formats.
- term: ELF
  definition: Executable and Linkable Format. A common standard for object file formats
    on Unix-like systems.
- term: Elf_Internal_Sym
  definition: An internal structure used by BFD to represent a symbol within an ELF
    object file.
- term: const
  definition: A qualifier in C/C++ that indicates a variable or pointer cannot be
    modified after initialization.
- term: relocation
  definition: The process of updating symbolic references (like function or variable
    addresses) in relocatable object files to their final addresses when linked into
    an executable or shared library.
- term: STN_UNDEF
  definition: A special symbol table index in ELF indicating an undefined symbol,
    meaning its definition is expected in another object file.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261028223700.A330F4BA2E3B@sourceware.org
date: '2026-10-28'
is_stub: true
stub_reason: low_score
---

This commit enhances type safety in BFD's ELF handling by making `Elf_Internal_Sym` pointers `const` in the `check_relocs` and `relocate_section` functions. This change originated from an attempt to support relocations against STN_UNDEF without a `.symtab` section, but that broader effort was abandoned. The current change improves code hygiene by correctly reflecting that these symbols are not modified.
