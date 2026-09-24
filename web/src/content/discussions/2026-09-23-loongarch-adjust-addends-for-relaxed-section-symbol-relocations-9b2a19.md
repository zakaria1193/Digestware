---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- linker
- relocation
- relaxation
- loongarch
discussion_id: 20260923095431.2702807-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[RFC PATCH] LoongArch: Adjust addends for relaxed section-symbol relocations'
headline: 'LoongArch: Adjust addends for relaxed section-symbol relocations'
tldr: Fixes incorrect relocation targets after code relaxation on LoongArch by adjusting
  addends.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces a new function and logic to handle a specific relaxation edge case.
- Ensures correct relocation behavior for LoongArch targets when using `ld -r`.
exchanges: []
primer_expert: This change addresses an issue in `ld -r` on LoongArch where `elf_link_input_bfd`
  incorrectly folds `sec->output_offset` into relocation addends for input STT_SECTION
  symbols. The relaxation pass in `bfd/elfnn-loongarch.c` does not adjust these addends,
  causing incorrect jump targets after code shrinking. The fix introduces `loongarch_relax_adjust_reloc_addends`
  to re-evaluate and correct these addends based on instruction deletions.
primer_glossary:
- term: ld -r
  definition: A linker command-line option that performs a partial link, combining
    multiple object files into a single output file without resolving external symbols.
    This is often used for creating relocatable object files or libraries.
- term: STT_SECTION
  definition: A symbol type in the ELF file format that refers to a section. In this
    context, it's used for relocations related to section symbols.
- term: Relocation Addend
  definition: A value stored within a relocation entry that is added to the address
    of the symbol or the relocation itself to determine the final address. In this
    case, it's being incorrectly handled after relaxation.
- term: Relaxation
  definition: A process in linkers and assemblers where instructions are optimized
    or modified after initial assembly, often to shrink code size or adapt to specific
    hardware features. This can involve changing instruction lengths and addresses.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260923095431.2702807-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-09-23'
is_stub: false
stub_reason: ''
---

This patch introduces a fix for incorrect relocation targets on LoongArch when using `ld -r` with relaxed section-symbol relocations. Previously, the ELF linker would fold the section offset into the relocation addend, but LoongArch's relaxation process did not update these addends, leading to incorrect targets after code shrinking. The fix adds a new function `loongarch_relax_adjust_reloc_addends` to correct these addends based on deleted instructions during relaxation, specifically for sections with local STT_SECTION relocations and non-zero addends.
