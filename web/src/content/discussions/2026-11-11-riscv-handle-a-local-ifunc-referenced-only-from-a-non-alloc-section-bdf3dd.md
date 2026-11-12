---
project: binutils
subsystem: riscv
patch_id: null
tags:
- riscv
- linker
- ifunc
- relocations
- debugging sections
discussion_id: 20261111110350.3761956-5-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 4/7] riscv: handle a local IFUNC referenced only from a non-alloc section'
headline: 'riscv: handle a local IFUNC referenced only from a non-alloc section'
tldr: Fixes RISC-V linker to correctly handle local IFUNC symbols referenced from
  non-allocatable sections.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Ensures correct linking of local IFUNCs from non-allocatable sections on RISC-V.
- Adds test cases to cover this specific scenario.
- Prevents linker aborts in specific cases.
exchanges: []
primer_expert: This patch tackles a linking problem on RISC-V concerning local `STT_GNU_IFUNC`
  symbols that are only referenced within non-allocatable sections (like `.debug_info`).
  The linker's relocation process, which typically skips `SEC_ALLOC`-free sections,
  means `riscv_elf_relocate_section` won't find the necessary information and will
  abort. This fix applies the generic `_bfd_elf_ifunc_nonalloc_reloc` handler to these
  symbols, ensuring they are processed correctly even without a PLT entry. It also
  aligns the error reporting with that for global symbols in similar unsupported sections.
  New linker tes…
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on RISC principles.
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
series_id: 'binutils:riscv: handle a local ifunc referenced only from a non-alloc
  section'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261111110350.3761956-5-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the RISC-V linker where local `STT_GNU_IFUNC` symbols referenced only from non-allocatable sections were causing link failures. The relocation scan skips these sections, and `riscv_elf_relocate_section` would not find an entry and abort. The fix utilizes `_bfd_elf_ifunc_nonalloc_reloc` for these cases, similar to how global symbols are handled, and reports a defined `STT_GNU_IFUNC` symbol in an unsupported non-alloc section. New test cases are provided.
