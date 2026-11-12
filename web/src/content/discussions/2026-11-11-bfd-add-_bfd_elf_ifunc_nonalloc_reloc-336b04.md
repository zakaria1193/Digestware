---
project: binutils
subsystem: bfd
patch_id: null
tags:
- linker
- BFD
- ELF
- IFUNC
- refactoring
discussion_id: 20261111110350.3761956-2-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 1/7] bfd: add _bfd_elf_ifunc_nonalloc_reloc'
headline: 'bfd: add _bfd_elf_ifunc_nonalloc_reloc'
tldr: Introduces a new BFD helper function to standardize handling of IFUNC symbols
  in non-allocatable sections.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Introduces a new API and implementation, increasing the complexity of the BFD library.
- Centralizes logic, reducing duplication across architecture-specific backends, which
  should improve maintainability.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Introduces a new BFD helper function `_bfd_elf_ifunc_nonalloc_reloc` to
    handle IFUNC symbol relocations in non-allocatable sections consistently across
    different architectures.
  quote: 'The relocation scan skips non-SEC_ALLOC sections (PR ld/26080), so an STT_GNU_IFUNC
    reference there has no PLT entry. For a global symbol, x86, AArch64, RISC-V and
    SPARC handle such a reference the same way: STT_FUNC in a SHT_NOTE section (PR
    ld/22929), unapplied in a debugging section (PR ld/18808), an error elsewhere.
    Put that rule in one function, so the local-symbol fixes that follow can shar…'
primer_expert: This patch introduces a common helper function within BFD to standardize
  the behavior of ELF linkers when encountering IFUNC (Indirect Function) symbols
  that are referenced only from non-allocatable sections. The relocation scan typically
  ignores these sections, which can lead to unresolved symbols or incorrect linking
  for IFUNCs. This new function encapsulates the logic previously duplicated across
  various architecture-specific ELF backend implementations for handling such scenarios
  (e.g., treating them as function symbols, skipping them, or rejecting them), paving
  the way for consistent app…
primer_glossary:
- term: BFD
  definition: Binary Descriptor Format. A library used by GNU binutils and GCC to
    provide a common interface to object file formats.
- term: STT_GNU_IFUNC
  definition: A symbol type in the ELF format that represents an indirect function.
    The linker and dynamic loader resolve this symbol to a specific function pointer
    at runtime, allowing for architecture-specific or version-specific function implementations.
- term: non-alloc section
  definition: An ELF section that is not loaded into memory when the program is executed.
    These sections are often used for debugging information, notes, or other metadata.
- term: relocation scan
  definition: The process by which the linker identifies and resolves references between
    different parts of an executable or library. This involves examining relocation
    entries in object files.
- term: PLT entry
  definition: Procedure Linkage Table entry. A table used in dynamically linked executables
    to resolve calls to shared library functions at runtime.
- term: IFUNC
  definition: Indirect Function. Similar to STT_GNU_IFUNC, it's a mechanism to select
    a function implementation at runtime based on certain criteria.
series_id: 'binutils:bfd: add _bfd_elf_ifunc_nonalloc_reloc'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261111110350.3761956-2-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This patch introduces a new function, `_bfd_elf_ifunc_nonalloc_reloc`, to the BFD library. This function consolidates the logic for handling relocations against STT_GNU_IFUNC symbols when they appear in non-allocatable sections. Previously, different architectures handled this scenario inconsistently, leading to issues. This change aims to provide a unified approach for these cases, reducing code duplication and improving the linker's robustness.
