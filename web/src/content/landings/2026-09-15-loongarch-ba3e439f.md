---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- binutils
- linker
- code sharing
- ELF
commit_hash: ba3e439f17aabdb5b1a9ca61646f9c22604ab259
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: 'loongarch: Use linker stubs bfd instead of linker aligns bfd'
tldr: LoongArch now uses the generic linker stubs BFD, improving code sharing and
  enabling dynamic section support.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The LoongArch backend is updated to use `elf_backend_want_stub_bfd`
  and related common linker stub code, replacing its custom "linker aligns" BFD logic.
  The `align_file` function in `loongarchelf.em` is replaced by `stub_file`, and the
  `LDEMUL_AFTER_OPEN_OUTPUT` hook is removed. This change enables the "linker stubs"
  BFD in all linker modes, not just relocatable linking, providing support for dynamic
  sections. Testsuite adjustments were necessary for orphan section placement.
primer_glossary:
- term: LoongArch
  definition: A 64-bit RISC instruction set architecture developed in China, used
    in various processors and embedded systems.
- term: linker stubs bfd
  definition: A generic mechanism within the Binary File Descriptor (BFD) library
    used by the linker to handle specific types of sections or symbols, particularly
    those related to dynamic linking or internal linker operations. Replaces architecture-specific
    implementations.
- term: linker aligns bfd
  definition: An older, architecture-specific BFD mechanism used by the linker, likely
    for managing alignment requirements of sections.
- term: BFD
  definition: Binary File Descriptor library, a low-level library used by binutils
    and GDB to support various object file formats (like ELF, COFF, a.out).
- term: dynamic sections
  definition: Sections within an executable or shared library that contain information
    needed for dynamic linking at runtime, such as symbol tables for shared objects
    and relocation entries.
- term: relocatable linking
  definition: The process of creating an object file that is not yet a complete executable
    program but contains information (relocations) that allows the linker to adjust
    addresses when it is combined with other object files or loaded into memory.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of the software.
    In this case, it's the set of tests for the binutils linker.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260915081005.77C954BAE7C6@sourceware.org
date: '2026-09-15'
is_stub: false
stub_reason: ''
---

This change switches the LoongArch backend to use the common "linker stubs" BFD instead of its previous "linker aligns" BFD. This allows LoongArch to leverage more shared code within binutils. Additionally, the linker stubs BFD is now created for all linker modes, not just relocatable linking, making it available for dynamic sections and improving its utility. The testsuite has been updated to accommodate these changes.
