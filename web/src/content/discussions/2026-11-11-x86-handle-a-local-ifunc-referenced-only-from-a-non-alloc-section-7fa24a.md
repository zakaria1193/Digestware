---
project: binutils
subsystem: x86
patch_id: null
tags:
- linker
- x86
- ELF
- IFUNC
- DWARF
discussion_id: 20261111110350.3761956-3-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 2/7] x86: handle a local IFUNC referenced only from a non-alloc section'
headline: 'x86: handle a local IFUNC referenced only from a non-alloc section'
tldr: Fixes binutils to correctly handle local IFUNC symbols when referenced only
  from non-alloc sections on x86 architectures.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Applies a generic solution to specific architectures, potentially requiring architecture-specific
  error messages.
- Adds test cases to cover new scenarios, increasing test suite size and complexity.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes to use the common `_bfd_elf_ifunc_nonalloc_reloc` function to
    handle local STT_GNU_IFUNC symbols referenced from non-alloc sections on x86,
    aligning behavior with global symbols and providing appropriate error reporting.
  quote: Handle the symbol with _bfd_elf_ifunc_nonalloc_reloc, like a global one,
    and use the existing "non-alloc section" error for the reject case. Master aborts
    for a global symbol there too; give it the same error.
primer_expert: This patch addresses a bug in the binutils linker for x86 architectures
  (i386 and x86-64) where local IFUNC symbols are mishandled if their only references
  originate from non-allocatable sections. The current relocation scan excludes these
  sections, leading to a failure to create essential symbol information. The fix leverages
  a new BFD-level helper function (`_bfd_elf_ifunc_nonalloc_reloc`) to uniformly process
  such IFUNC references, ensuring they either resolve correctly, are skipped, or generate
  a diagnostic error, mirroring the behavior established for global IFUNC symbols.
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
- term: IFUNC
  definition: Indirect Function. Similar to STT_GNU_IFUNC, it's a mechanism to select
    a function implementation at runtime based on certain criteria.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers. It stores
    information about variables, types, and source code locations.
series_id: 'binutils:x86: handle a local ifunc referenced only from a non-alloc section'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261111110350.3761956-3-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This patch series aims to resolve an issue in the x86 linker where local STT_GNU_IFUNC symbols, when referenced solely from non-allocatable sections, are not processed correctly. The linker aborts because the relocation scan bypasses these sections, preventing the necessary hash entry creation. The solution involves using a new common helper function, `_bfd_elf_ifunc_nonalloc_reloc`, to manage these symbols, providing a consistent error message for unresolvable relocations, similar to how global symbols are handled.
