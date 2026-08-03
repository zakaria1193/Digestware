---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- linker
- elf
- bugfix
commit_hash: 0cdae10e5786da5d9128c9faaeb640130b041513
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: 'bfd: Fix memory corruption in ELF relocation handling'
tldr: Fixes ELF relocation bug causing malloc/free corruption when linking objects
  with both REL and RELA relocations.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses a bug in `bfd/elflink.c` where the `_bfd_elf_link_info_read_relocs`
  function mishandled the case where both `rel.hdr` and `rela.hdr` were present for
  a section. The REL relocation buffer was being reused for RELA relocations, leading
  to corruption, often manifesting as `malloc`/`free` aborts during `ld -r` operations.
  The fix involves correcting buffer allocation/management and updating the function
  comment. A test in `ld-tic6x/pcrel-reloc-local-r-rel-rela.d` was also enhanced to
  include an extra `ld -r` stage to expose this bug.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU Binutils
    to provide a common interface for reading and writing various executable file
    formats.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: REL and RELA relocations
  definition: Types of relocation entries in ELF files. REL entries contain a symbol
    and an offset, while RELA entries also include an addend. They inform the linker
    or dynamic loader how to adjust addresses in the code or data sections.
- term: ld -r
  definition: A linker command-line option that produces a relocatable object file
    instead of a final executable. This is often used for intermediate linking steps.
- term: malloc/free corruption
  definition: An error condition where memory management functions like `malloc` (allocate
    memory) and `free` (deallocate memory) encounter corrupted internal data structures.
    This typically leads to program crashes or unpredictable behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260802234518.16E024B99F79@sourceware.org
date: '2026-08-02'
is_stub: false
stub_reason: ''
---

A bug in `_bfd_elf_link_read_relocs` could lead to memory corruption, specifically `malloc`/`free` errors, when linking objects containing both REL and RELA relocations for the same section. This was caused by the REL relocation buffer being incorrectly reused for RELA relocations. The fix corrects the buffer handling and updates the function's description, while also improving a test case to catch this issue.
