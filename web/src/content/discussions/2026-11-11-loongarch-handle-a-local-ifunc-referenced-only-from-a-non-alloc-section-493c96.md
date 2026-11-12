---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- linker
- ifunc
- relocations
- debugging sections
discussion_id: 20261111110350.3761956-7-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 6/7] LoongArch: handle a local IFUNC referenced only from a non-alloc
  section'
headline: 'LoongArch: handle a local IFUNC referenced only from a non-alloc section'
tldr: Fixes LoongArch linker to correctly handle local IFUNC symbols referenced from
  non-allocatable sections.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Ensures correct linking of local IFUNCs from non-allocatable sections on LoongArch.
- Adds test cases to cover this specific scenario.
- Prevents linker aborts in specific cases.
exchanges: []
primer_expert: This patch addresses a specific problem in the LoongArch linker's handling
  of `STT_GNU_IFUNC` symbols, particularly when they are local to an object file and
  only referenced from non-allocatable sections (e.g., `.debug_info`). The linker's
  standard relocation scan skips non-`SEC_ALLOC` sections. If an `IFUNC` symbol's
  only reference comes from such a section, the linker's `loongarch_elf_relocate_section`
  function fails to find a corresponding entry in its internal structures and aborts.
  This patch modifies the function to handle this scenario gracefully by treating
  the `IFUNC` as a regular fu…
primer_glossary:
- term: LoongArch
  definition: A RISC-ISA architecture developed in China.
- term: STT_GNU_IFUNC
  definition: A symbol type in the ELF format that represents an Indirect Function.
    IFUNCs allow for dynamic selection of function implementations at runtime, typically
    based on processor capabilities.
- term: Non-alloc section
  definition: A section in an object file that is not loaded into memory when the
    program runs (e.g., debugging information sections). Marked by `SEC_ALLOC` flag
    being unset.
- term: Relocation scan
  definition: The process by which the linker identifies and processes relocation
    entries in an object file to resolve symbolic addresses.
- term: STT_FUNC
  definition: A symbol type in ELF representing a function.
- term: SEC_ALLOC
  definition: A flag in BFD that indicates whether a section should be allocated memory
    when the program is loaded.
series_id: 'binutils:loongarch: handle a local ifunc referenced only from a non-alloc
  section'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261111110350.3761956-7-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This patch resolves an issue in the LoongArch linker where local `STT_GNU_IFUNC` symbols referenced solely from non-allocatable sections were causing link failures. Because the relocation scan bypasses these sections, `loongarch_elf_relocate_section` would not find an entry and abort. The fix aligns the behavior with global IFUNCs, relocating the symbol against itself (as STT_FUNC) when no hash entry is found, thereby preventing the abort. New test cases are included.
