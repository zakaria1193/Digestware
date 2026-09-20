---
project: binutils
subsystem: bfd
patch_id: null
tags:
- linker
- loongarch
- relocation
- optimization
- rfc
discussion_id: mailman.4.1789819201.2699126.binutils@sourceware.org
source_type: public_inbox
title: 'Re: : [RFC PATCH] LoongArch: Use local anchors for relocatable section symbols'
headline: 'LoongArch: Use local anchors for relocatable section symbols'
tldr: Gopi Kumar Bulusu questions whether linker defects map section start to section
  offset and asks about desired behavior.
proposer: Gopi Kumar Bulusu <gopi@sankhya.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 6
technical_tradeoffs:
- Ensuring the correct handling of section offsets and their interaction with relocations
  under LoongArch's relaxation constraints.
- Potential impact on incremental linking and assembler behavior when input and output
  sections differ.
exchanges:
- author: Gopi Kumar Bulusu <gopi@sankhya.com>
  role: reviewer
  position: Asks clarifying questions about section mapping and desired behavior,
    suggesting an investigation into potential linker defects.
  quote: The basic difference between input section and output section should not
    impact assembler. Ideally it should not impact an incremental link that does not
    alter input/output section mapping. I would start by checking the desired documented
    behavior when a section is accessed and then ask the question what it should be.
    Is there a linker defect that makes it map section start to a section offset -…
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Provides context on the RFC patch and its implications for LoongArch relaxation.
  quote: For ld -r, when an input STT_SECTION symbol is redirected to the output section
    symbol, elf_link_input_bfd() folds sec->output_offset into the RELA addend. LoongArch
    relaxation does not allow symbols to be optimized into section symbol plus offset
    form.
primer_expert: This exchange discusses a LoongArch RFC patch for binutils that proposes
  using local anchors for relocatable section symbols. The core issue is how the linker
  (`ld -r`) handles `STT_SECTION` symbols when redirected to output section symbols,
  specifically how `sec->output_offset` is folded into RELA addends. LoongArch's relaxation
  constraints prevent optimization into section symbol plus offset, necessitating
  this change. The reviewer questions the fundamental interaction between input/output
  sections and linker behavior.
primer_glossary:
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
- term: ld -r
  definition: An option for the GNU linker (ld) that performs a partial link, similar
    to an incremental link, producing an intermediate object file.
- term: bfd
  definition: Binary File Descriptor library, used by GNU Binutils to handle various
    object file formats.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CAL1P33xkQYHjbQKBoE-2b9SMgJBVtB+gAy7xSNF0zs4kLujvMA@mail.gmail.com
bugzilla_url: null
date: '2026-09-19'
is_stub: false
stub_reason: ''
---

Gopi Kumar Bulusu responds to an RFC patch regarding LoongArch local anchors, questioning the impact of input vs. output section differences on the assembler and incremental linking. He suggests examining the documented behavior for section access and understanding if the current mapping of section start to section offset is by design or a linker defect.
