---
project: binutils
subsystem: binutils
patch_id: null
tags:
- bugfix
- elf
- validation
- binutils
discussion_id: auJ3N7ehAJpRqhds@squeak.grove.modra.org
source_type: public_inbox
title: Validate sym_hashes when reading relocs
headline: Validate sym_hashes when reading relocs
tldr: Enhances ELF relocation reading to validate sym_hashes and ensure STN_UNDEF
  is present with a non-empty symbol table.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Increases the strictness of ELF file parsing, potentially rejecting malformed files
  earlier and preventing subtle bugs. This might also reject some unusual but previously
  tolerated inputs.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a patch to make ELF relocation reading more strict by validating
    `sym_hashes` and checking for `STN_UNDEF` with a non-empty symbol table.
  quote: 'This patch makes elf_link_read_relocs more strict.  STN_UNDEF is no

    longer allowed with an empty .symtab, and the function also verifies

    that the elf_sym_hashes array entries are non-NULL.'
primer_expert: This patch modifies `bfd/elflink.c` and `bfd/elf-bfd.h` to enhance
  the robustness of relocation processing. `elf_link_read_relocs_from_section` now
  explicitly checks that `STN_UNDEF` is associated with a valid symbol table (specifically,
  that `sym_hashes` is non-NULL and populated). This addresses issues like those in
  PR 9934 where relocations might reference undefined symbols incorrectly in malformed
  ELF files. A new `sym_hashes_valid` flag is introduced in `elf_obj_tdata` to track
  the state of the symbol hash array.
primer_glossary:
- term: sym_hashes
  definition: Likely an array or hash table containing symbol information, used for
    efficient symbol lookup during linking.
- term: Relocation
  definition: A modification needed in an object file or shared library to resolve
    references to symbols or addresses that are not yet known at link time. This process
    is typically handled by the linker.
- term: STN_UNDEF
  definition: A special symbol type in ELF representing an undefined symbol, typically
    a reference to a symbol defined in another object file or library.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for object files,
    executables, shared libraries, and core dumps on many Unix-like systems.
- term: PR 9934
  definition: Likely refers to Problem Report 9934, a bug filed against the binutils
    project, which this patch aims to fix.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ3N7ehAJpRqhds@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch introduces stricter validation in `elf_link_read_relocs_from_section` to address PR 9934. It now ensures that `STN_UNDEF` symbols are present when the dynamic symbol table is used and verifies that the `elf_sym_hashes` array entries are non-NULL. A new `sym_hashes_valid` flag is added to `elf_obj_tdata` to track the validity of the `sym_hashes` array after it's assigned. This aims to catch malformed ELF files earlier in the linking process.
