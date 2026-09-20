---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- linker
- loongarch
- relocation
- optimization
- rfc
discussion_id: 20260919085650.2568760-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[RFC PATCH] LoongArch: Use local anchors for relocatable section symbols'
headline: 'LoongArch: Use local anchors for relocatable section symbols'
tldr: RFC patch to use local anchors for relocatable section symbols in LoongArch
  to handle linker's folding of output_offset into RELA addends.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces local anchors to manage section offsets, potentially increasing symbol
  table size.
- Ensures compatibility with LoongArch's relaxation constraints that prevent standard
  section symbol + offset optimizations.
exchanges: []
primer_expert: This RFC patch for binutils targets the LoongArch architecture, specifically
  how the linker handles relocatable section symbols with `ld -r`. The problem arises
  because `elf_link_input_bfd()` folds `sec->output_offset` into the RELA addend when
  an input `STT_SECTION` symbol is redirected to an output section symbol. LoongArch's
  relaxation process, which optimizes code by potentially adjusting instruction encodings
  based on symbol positions, does not support the 'section symbol + offset' form.
  The proposed solution is to use local `STT_NOTYPE` anchors per referenced input
  section symbol. The `…
primer_glossary:
- term: ld -r
  definition: An option for the GNU linker (ld) that performs a partial link, similar
    to an incremental link, producing an intermediate object file.
- term: STT_SECTION
  definition: A symbol table entry type indicating a section symbol.
- term: RELA
  definition: A type of relocation entry that includes an addend.
- term: LoongArch relaxation
  definition: A feature in the LoongArch architecture that allows for code optimization,
    potentially by adjusting instruction encoding based on symbol positions.
- term: local anchors
  definition: A mechanism to create stable references within sections that can be
    updated during linking or relaxation without altering relocation addends.
- term: st_value
  definition: The value associated with a symbol table entry, often representing an
    offset or address.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260919085650.2568760-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-09-19'
is_stub: false
stub_reason: ''
---

This RFC patch addresses an issue in LoongArch where the linker, when performing a partial link (ld -r), folds the output section offset into the RELA addend for STT_SECTION symbols. LoongArch's relaxation mechanism does not support optimizing symbols into a section symbol plus offset form, necessitating the use of local STT_NOTYPE anchors. These anchors will store the input section's output offset, allowing subsequent relaxation or section movement to update the anchor without modifying relocation addends.
