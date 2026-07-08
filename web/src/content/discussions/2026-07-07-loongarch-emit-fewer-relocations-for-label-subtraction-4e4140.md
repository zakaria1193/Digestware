---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- binutils
- linker
- optimization
- compiler
discussion_id: 20260707174719.1883721-4-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH v0 3/4] LoongArch: Emit fewer relocations for label subtraction'
headline: 'LoongArch: Emit fewer relocations for label subtraction'
tldr: Optimizes LoongArch instruction emission by not generating relocations for label
  subtraction when no relaxed instructions are present between addsy and subsy.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Reduced relocations can lead to smaller object files and faster linking, but requires
  accurate tracking of instruction states.
- The logic for identifying 'relaxed' instructions needs to be comprehensive and correct
  for the optimization to be safe.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Proposes to reduce relocations for LoongArch label subtraction by marking
    relaxed instructions and avoiding relocation emission if addsy and subsy are in
    the same frag.
  quote: 'Mark the frag and section to indicate if they have a relaxed instruction.


    For label subtraction, if there are no relaxed instructions between addsy

    and subsy, do not emit relocations.'
primer_expert: This LoongArch-specific patch for binutils optimizes linker relaxation
  by reducing the number of relocations generated for label subtraction. It introduces
  logic to track whether a fragment or section contains 'relaxed' instructions. If
  the sequence 'addsy' and 'subsy' (likely related to calculating a symbol's address
  or offset) occurs within the same fragment without intervening relaxed instructions,
  the associated relocations are omitted. This optimization aims to improve code density
  and potentially linker performance.
primer_glossary:
- term: LoongArch
  definition: A RISC-V-based instruction set architecture developed by Loongson Technology.
- term: linker relaxation
  definition: A process where the linker adjusts addresses and offsets of code and
    data after initial assembly, often to optimize for space or speed, especially
    in position-independent code.
- term: relocations
  definition: Information in an object file that describes how to modify addresses
    and references when the code is linked or loaded into memory.
- term: label subtraction
  definition: An assembly operation where the difference between two labels (addresses)
    is calculated, typically used for offset calculations.
- term: addsy/subsy
  definition: Assembly pseudo-instructions or directives used in LoongArch to define
    symbols or perform address calculations, likely related to the 'add symbol' and
    'subtract symbol' operations.
- term: frag
  definition: A 'fragment', a basic unit of code or data within an assembler's intermediate
    representation, which eventually forms part of an object file section.
series_id: 'binutils:loongarch: emit fewer relocations for label subtraction'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260707174719.1883721-4-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

This patch for the LoongArch binutils component optimizes relocation emission for label subtraction. It introduces flags to mark fragments and sections with relaxed instructions, preventing the generation of relocations when `addsy` and `subsy` occur within the same fragment and no relaxed instructions are interspersed.
