---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- linker
- relocation
- relaxation
- ld -r
discussion_id: 20261112111617.86372-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH v2] LoongArch: Adjust addends of relocations with STT_SECTION symbol'
headline: 'LoongArch: Adjust addends of relocations with STT_SECTION symbol'
tldr: Fixes incorrect relocation addends in LoongArch when using ld -r, caused by
  folding section offsets during relaxation.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Ensures correctness of relocations with STT_SECTION symbols in `ld -r` mode at the
  cost of increased complexity in the relaxation process.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Submits a v2 patch to fix incorrect relocation addends in LoongArch during
    `ld -r` relaxation.
  quote: For ld -r, when an input STT_SECTION symbol is redirected to the output section
    symbol, elf_link_input_bfd() folds sec->output_offset into the RELA addend. LoongArch
    relaxation does not update these relocation addends, leaving the relocated target
    incorrect. ... The fix adds loongarch_relax_adjust_reloc_addends() to adjust relocation
    addends according to the instructions deleted during relaxation.
primer_expert: The LoongArch linker's behavior with `ld -r` and section relaxation
  is flawed. When `sec->output_offset` is folded into a RELA addend for STT_SECTION
  symbols, the subsequent relaxation pass fails to update these addends. This results
  in incorrect target addresses for relocated instructions. The patch introduces a
  new function, `loongarch_relax_adjust_reloc_addends`, which corrects these addends
  by considering deleted instructions, ensuring that relocations targeting section
  symbols remain accurate after relaxation.
primer_glossary:
- term: STT_SECTION symbol
  definition: A symbol of type 'section' in an object file. It represents an entire
    section and is often used in relocations to refer to the section itself.
- term: RELA addend
  definition: An additional value used in relocation entries (RELA) that is added
    to the base address of the relocation target to determine the final address.
- term: linker relaxation
  definition: A linker optimization that allows the linker to adjust the size and
    addresses of instructions after the initial assembly. This can improve code density
    and performance but requires careful handling of relocations.
- term: ld -r
  definition: A linker command-line option that produces a relocatable output file
    instead of an executable. This is often used for combining multiple object files
    before final linking.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261112111617.86372-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in LoongArch where the linker, when operating with `ld -r` (relocatable mode), incorrectly adjusts relocation addends. Specifically, when an input section's symbol is redirected to an output section symbol, the `sec->output_offset` is folded into the RELA addend. LoongArch's relaxation process does not update these addends, leading to incorrect target addresses after code is shrunk. The fix introduces `loongarch_relax_adjust_reloc_addends` to correct these addends during relaxation.
