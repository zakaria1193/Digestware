---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- assembler
- relocations
- pc-relative
discussion_id: 20260813170736.1880481-4-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH 3/3] LoongArch: Fix md_pcrel_from'
headline: 'LoongArch: Fix md_pcrel_from'
tldr: Correctly calculates PC-relative offsets for LoongArch instructions.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Correctly calculates PC-relative offsets, ensuring accurate code generation.
- Fixes a bug that could lead to incorrect program behavior or link-time errors.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Changes `md_pcrel_from` to return `fixP->fx_frag->fr_address + fixP->fx_where`
    to correctly calculate PC-relative offsets on LoongArch.
  quote: null
primer_expert: This patch modifies the LoongArch assembler configuration in `gas/config/tc-loongarch.c`
  by correcting the `md_pcrel_from` function. On LoongArch, PC-relative addressing
  is calculated from the start of the instruction itself. The previous implementation
  incorrectly returned 0, leading to miscalculated offsets. This change ensures that
  `md_pcrel_from` now returns the correct base address (`fixP->fx_frag->fr_address
  + fixP->fx_where`), which is essential for generating accurate PC-relative relocations
  and ensuring correct program behavior, particularly in position-independent code.
primer_glossary:
- term: PC-relative
  definition: A type of address calculation where the offset is relative to the current
    program counter (PC). This is common for position-independent code.
- term: relocation
  definition: Information embedded in an object file that describes how to modify
    symbolic addresses and constants when linking. It tells the linker which parts
    of the code or data need to be adjusted based on the final memory layout.
- term: assembler
  definition: A program that translates assembly language into machine code. It also
    generates relocation information for the linker.
- term: LoongArch
  definition: A RISC ISA developed by China's Loongson Technology.
- term: fixP
  definition: A pointer to a 'fixup' structure, which holds information about a relocation
    to be applied.
- term: fr_address
  definition: Likely refers to the base address of a fragment, a contiguous chunk
    of code or data within an object file.
- term: fx_where
  definition: Likely indicates the offset within a fragment where the relocation needs
    to be applied.
series_id: 'binutils:loongarch: fix md_pcrel_from'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260813170736.1880481-4-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

This patch corrects the `md_pcrel_from` function for the LoongArch architecture. Previously, it incorrectly returned 0, which is not the correct base address for PC-relative calculations. The function is updated to return `fixP->fx_frag->fr_address + fixP->fx_where`, which accurately represents the start of the current instruction, ensuring correct PC-relative offset computation.
