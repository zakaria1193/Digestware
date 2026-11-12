---
project: binutils
subsystem: sparc
patch_id: null
tags:
- sparc
- linker
- ifunc
- relocations
- debugging sections
discussion_id: 20261111110350.3761956-6-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 5/7] sparc: handle a local IFUNC referenced only from a non-alloc section'
headline: 'sparc: handle a local IFUNC referenced only from a non-alloc section'
tldr: Fixes the SPARC linker to correctly handle local IFUNC symbols referenced from
  non-allocatable sections.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Ensures correct linking of local IFUNCs from non-allocatable sections on SPARC.
- Improves error reporting for unresolvable relocations.
- Adds test cases to cover this specific scenario.
exchanges: []
primer_expert: This patch addresses the linking behavior for local `STT_GNU_IFUNC`
  symbols on SPARC when they are only referenced from non-allocatable sections (like
  `.debug_info`). The standard linker relocation process, which skips non-`SEC_ALLOC`
  sections, means that `_bfd_sparc_elf_relocate_section` cannot find the necessary
  information for these symbols. This leads to a linker abort. The solution applies
  the generic `_bfd_elf_ifunc_nonalloc_reloc` handler, which is designed for such
  scenarios, ensuring that the symbol is processed appropriately even without a PLT
  entry. Additionally, the patch enhances…
primer_glossary:
- term: SPARC
  definition: A RISC instruction set architecture developed by Sun Microsystems.
- term: STT_GNU_IFUNC
  definition: A symbol type in the ELF format that represents an Indirect Function.
    IFUNCs allow for dynamic selection of function implementations at runtime, typically
    based on processor capabilities.
- term: Non-alloc section
  definition: A section in an object file that is not loaded into memory when the
    program runs (e.g., debugging information sections). Marked by `SEC_ALLOC` flag
    being unset.
- term: Relocation
  definition: The process of updating symbolic references in an object file to absolute
    addresses when linking. Relocations contain information about which parts of the
    code need to be modified and how.
- term: _bfd_elf_ifunc_nonalloc_reloc
  definition: A generic BFD helper function for handling relocations of IFUNC symbols
    located in non-allocatable sections.
- term: SEC_ALLOC
  definition: A flag in BFD that indicates whether a section should be allocated memory
    when the program is loaded.
series_id: 'binutils:sparc: handle a local ifunc referenced only from a non-alloc
  section'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261111110350.3761956-6-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This patch addresses an issue on the SPARC architecture where local `STT_GNU_IFUNC` symbols referenced exclusively from non-allocatable sections caused the linker to abort. The relocation scan skips these sections, and `_bfd_sparc_elf_relocate_section` would not find the symbol. The fix implements `_bfd_elf_ifunc_nonalloc_reloc` for these cases, mirroring how global symbols are handled, and improves the error message to include the symbol's name when a relocation is unresolvable. New test cases are added.
