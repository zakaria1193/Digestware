---
project: binutils
subsystem: binutils/elf
patch_id: null
tags:
- elf
- linker
- revert
commit_hash: 6d18e0b2e8c579c76b94ffbc56d5bb58a8017dea
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Revert hiding of DT_INIT and DT_FINI symbols
tldr: The linker will no longer hide the `_init` and `_fini` symbols by default, reverting
  a previous change.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The linker (`ld`) previously implemented logic to hide the `_init`
  and `_fini` functions by marking them as hidden symbols. This change reverts that
  behavior. The motivation was that `ld` automatically hiding these symbols could
  be unexpected, and that control over symbol visibility for initialization and finalization
  routines should primarily rest with the source code. The impact of leaving them
  visible is considered small.
primer_glossary:
- term: DT_INIT
  definition: A dynamic section tag in an ELF file that specifies the address of the
    initialization function called when a shared object is loaded or initialized.
    Corresponds to the `_init` symbol.
- term: DT_FINI
  definition: A dynamic section tag in an ELF file that specifies the address of the
    finalization function called when a shared object is unloaded or finalized. Corresponds
    to the `_fini` symbol.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps, primarily used on Unix-like operating
    systems.
- term: symbol visibility
  definition: Controls whether a symbol (like a function or variable) defined in one
    object file is visible or accessible from other object files. 'Hidden' visibility
    means the symbol is not exported and cannot be directly referenced externally.
- term: linker
  definition: A program that combines various pieces of code and data (object files
    and libraries) into a single executable file or library. It resolves symbol references
    between different modules.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260914234501.C3F924BAE7E7@sourceware.org
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

This commit reverts the decision to automatically hide the `_init` and `_fini` symbols in ELF binaries. The linker's previous behavior of hiding these symbols was found to be surprising and can be achieved through source code if needed, with minimal performance impact from leaving them visible.
