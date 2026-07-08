---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- binutils
- assembler
- linker
- optimization
discussion_id: 20260707174719.1883721-3-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH v0 2/4] LoongArch: Do not emit relocation if addsy and subsy are in
  the same frag'
headline: 'LoongArch: Do not emit relocation if addsy and subsy are in the same frag'
tldr: Optimizes LoongArch assembly by consolidating relaxed instructions and alignment
  nops within a single fragment, thus avoiding redundant relocations for addsy/s…
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Consolidating instructions can improve code density and reduce relocation overhead.
- Requires careful management of fragment boundaries and instruction types to ensure
  correctness.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Proposes to group relaxed instructions and alignment nops into a single
    fragment for LoongArch, preventing relocation emission for addsy/subsy pairs within
    the same frag.
  quote: 'Let relaxed instructions and alignment nops in a single frag.

    Do not emit relocation if addsy and subsy are in the same frag.'
primer_expert: This patch for LoongArch's gas aims to reduce unnecessary relocations
  during linker relaxation. It achieves this by ensuring that 'relaxed' instructions
  and 'alignment nops' (no-operation instructions used for padding) are grouped together
  within the same assembler fragment. When `addsy` (likely 'add symbol') and `subsy`
  (likely 'subtract symbol') operations, which often involve address calculations,
  occur within such a consolidated fragment, the assembler now avoids generating relocations
  for them. This optimization simplifies the output and can improve linker performance.
primer_glossary:
- term: LoongArch
  definition: A RISC-V-based instruction set architecture developed by Loongson Technology.
- term: relaxed instructions
  definition: Instructions whose final encoding or address in the object file can
    change after the initial assembly pass, often due to linker relaxation.
- term: alignment nops
  definition: No-operation instructions used specifically to pad code or data to meet
    alignment requirements, which can affect instruction fetching and execution efficiency.
- term: frag
  definition: A 'fragment', a basic unit of code or data within an assembler's intermediate
    representation, which eventually forms part of an object file section.
- term: relocation
  definition: Information in an object file that describes how to modify addresses
    and references when the code is linked or loaded into memory.
- term: addsy/subsy
  definition: Assembly pseudo-instructions or directives used in LoongArch to define
    symbols or perform address calculations, likely related to 'add symbol' and 'subtract
    symbol' operations.
series_id: 'binutils:loongarch: do not emit relocation if addsy and subsy are in the
  same frag'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260707174719.1883721-3-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

This patch modifies the LoongArch assembler to place relaxed instructions and alignment nops within the same fragment. Consequently, if `addsy` and `subsy` (likely related to symbol address calculations) reside in the same fragment, the assembler will not emit relocations for them, reducing overhead.
