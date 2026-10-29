---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- elf
- linking
- bfd
- validation
- relocations
commit_hash: d5be6936384246ca15bc330288e4fe0d24f93068
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Validate sym_hashes when reading relocations for ELF files
tldr: Binutils BFD now performs stricter validation of symbol hashes when processing
  ELF relocations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `elf_link_read_relocs_from_section` in `elflink.c`
  to enforce stricter checks on ELF relocation processing. A new flag, `sym_hashes_valid`,
  is introduced in `struct elf_obj_tdata` and set in `elf_link_input_bfd`. The validation
  now includes ensuring `STN_UNDEF` is present and that `elf_sym_hashes` entries are
  not NULL, addressing PR 9934. This makes the linker less tolerant of malformed object
  files where relocations might reference invalid symbol hash entries.
primer_glossary:
- term: sym_hashes
  definition: An array of hash table entries for symbols, used by BFD's ELF linker
    to efficiently look up symbol information during relocation processing.
- term: relocation
  definition: Information in an object file that describes how to modify certain addresses
    or symbols when linking. For example, a relocation entry might indicate that a
    specific address needs to be updated with the actual address of a function.
- term: STN_UNDEF
  definition: A special symbol table index in ELF that represents an undefined symbol,
    typically a function or variable that is defined in another object file or shared
    library.
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
url: https://inbox.sourceware.org/binutils-cvs/20261028223634.EEEDA4BA23D9@sourceware.org
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This update enhances the robustness of BFD's ELF linker by introducing stricter validation when reading relocations. It ensures that the `STN_UNDEF` symbol is present when required and verifies that the `elf_sym_hashes` array entries referenced by relocations are not NULL. This change addresses issues related to malformed object files and improves the reliability of the linking process.
