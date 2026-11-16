---
project: binutils
subsystem: loongarch/ld
patch_id: null
tags:
- loongarch
- linker
- relocation
- relaxation
commit_hash: c98a77f14787760c308352d2f6800ebe5254563b
source_type: public_inbox
author: liu zhensong
headline: 'LoongArch: Adjust addends of relocations with STT_SECTION symbol'
tldr: LoongArch linker now correctly adjusts relocation addends for STT_SECTION symbols
  during relaxation.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses an issue in `bfd/elfnn-loongarch.c` where `ld
  -r` incorrectly handled STT_SECTION symbols. During linking of relocatable objects,
  `elf_link_input_bfd()` folded `sec->output_offset` into the RELA addend. LoongArch's
  relaxation pass, which shrinks instructions, did not account for this, causing relocated
  call sites to be misaligned. The fix adds `loongarch_relax_adjust_reloc_addends()`
  to correct these addends based on bytes removed during relaxation, specifically
  for sections flagged by `loongarch_elf_check_relocs` when their STT_SECTION symbol
  is referenced with a non-ze…
primer_glossary:
- term: LoongArch
  definition: A RISC instruction set architecture developed by Loongson Technology,
    primarily for server and workstation processors.
- term: Relocation
  definition: The process of updating symbolic references in machine code to absolute
    addresses or offsets. This is typically performed by the linker after assembly.
- term: STT_SECTION symbol
  definition: A symbol table entry of type STT_SECTION, which represents a section
    in an object file. It is used by the linker to refer to specific code or data
    segments.
- term: Addend
  definition: A constant value added to a symbol's address during relocation. It is
    part of the relocation entry and contributes to the final calculated address.
- term: ld -r
  definition: A linker option that produces a relocatable output file. It combines
    multiple input object files into a single relocatable file, allowing further linking.
- term: Relaxation
  definition: A linker optimization technique where instructions that occupy variable
    space (e.g., conditional branches, calls) are adjusted to occupy the minimum possible
    space after all code has been laid out. This often involves replacing larger instructions
    with smaller ones and updating related relocations.
- term: RELA
  definition: A type of relocation entry in the ELF (Executable and Linkable Format)
    standard that includes an addend, alongside the symbol, offset, and type of relocation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261115093748.411454B99F4E@sourceware.org
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

A bug in the LoongArch linker's handling of relocations with STT_SECTION symbols has been fixed. When using `ld -r` (relocatable output), the linker previously folded the output section offset into the relocation addend. LoongArch's relaxation process did not update these addends, leading to incorrect target addresses for relocated code. This change introduces a new function to adjust relocation addends based on instructions deleted during relaxation, ensuring accurate positioning of relocated code.
