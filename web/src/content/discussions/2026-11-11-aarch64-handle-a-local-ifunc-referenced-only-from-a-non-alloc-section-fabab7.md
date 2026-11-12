---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- linker
- aarch64
- ELF
- IFUNC
discussion_id: 20261111110350.3761956-4-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 3/7] aarch64: handle a local IFUNC referenced only from a non-alloc
  section'
headline: 'aarch64: handle a local IFUNC referenced only from a non-alloc section'
tldr: Fixes binutils to correctly handle local IFUNC symbols when referenced only
  from non-alloc sections.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces a new helper function to centralize logic, potentially increasing code
  complexity but improving maintainability.
- Ensures consistent error reporting for local IFUNC symbols, improving user diagnostics.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes to handle local STT_GNU_IFUNC symbols referenced only from non-alloc
    sections by using _bfd_elf_ifunc_nonalloc_reloc, similar to global symbols, to
    provide a more consistent error message.
  quote: A local STT_GNU_IFUNC symbol gets its hash entry from the relocation scan,
    which skips non-SEC_ALLOC sections (PR ld/26080).  When only such a section, for
    example .debug_info, refers to it, elfNN_aarch64_relocate_section finds no entry
    and aborts.  Handle it with _bfd_elf_ifunc_nonalloc_reloc, like a global symbol,
    giving the same "unresolvable ... relocation" error in the reject case.
primer_expert: This patch series aims to fix a bug in the binutils linker where local
  IFUNC symbols (symbols that resolve to different function pointers at runtime) are
  not handled correctly when they are only referenced from sections that are not allocated
  in memory (e.g., debug sections). The existing relocation scan skips these non-alloc
  sections, leading to missing hash entries for IFUNC symbols. This series introduces
  a common helper function `_bfd_elf_ifunc_nonalloc_reloc` and applies it to various
  architectures (x86, aarch64, RISC-V, SPARC) to ensure these local IFUNCs are processed
  correctly, either…
primer_glossary:
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
- term: hash entry
  definition: A data structure within an ELF file that helps speed up symbol lookups,
    particularly for dynamic linking. For IFUNC symbols, a hash entry is important
    for runtime resolution.
- term: IFUNC
  definition: Indirect Function. Similar to STT_GNU_IFUNC, it's a mechanism to select
    a function implementation at runtime based on certain criteria.
series_id: 'binutils:aarch64: handle a local ifunc referenced only from a non-alloc
  section'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261111110350.3761956-4-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the aarch64 linker where local STT_GNU_IFUNC symbols are not handled correctly if they are only referenced from non-allocatable sections (like .debug_info). The linker previously aborted because the relocation scan skips these sections, preventing the creation of a hash entry. The fix introduces the use of _bfd_elf_ifunc_nonalloc_reloc to handle these cases, providing a more informative error message when resolution fails.
