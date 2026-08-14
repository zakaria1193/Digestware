---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- assembler
- relocations
- optimization
- code generation
discussion_id: 20260813170736.1880481-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH 0/3] LoongArch: Optimize ADD/SUB and PC-relative relocations handling'
headline: 'LoongArch: Optimize ADD/SUB and PC-relative relocations handling'
tldr: Series optimizes LoongArch relocation handling for ADD/SUB and PC-relative types.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves efficiency and correctness of relocation handling for LoongArch.
- Adds complexity to assembler logic for handling various relocation types and expressions.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Submits a three-part patch series to optimize ADD/SUB and PC-relative
    relocation handling on LoongArch by enhancing symbolic expression support, reducing
    fixups, and correcting PC-relative base address calculation.
  quote: null
primer_expert: This cover letter introduces a three-part series for the LoongArch
  assembler (`gas`). Patch 1 enables `R_LARCH_ADD/SUB` relocations for expressions
  like `constant - symbol` by correctly setting `fx_addsy`. Patch 2 optimizes `TC_FORCE_RELOCATION_SUB_LOCAL`
  to prefer PC-relative relocations over ADD/SUB relocations when linker relaxation
  is not fully applicable, reducing fixup counts. Patch 3 fixes `md_pcrel_from` to
  return the correct instruction start address for PC-relative calculations, which
  was previously hardcoded to 0. These changes collectively improve relocation efficiency
  and accurac…
primer_glossary:
- term: LoongArch
  definition: A RISC ISA developed by China's Loongson Technology.
- term: relocation
  definition: Information embedded in an object file that describes how to modify
    symbolic addresses and constants when linking. It tells the linker which parts
    of the code or data need to be adjusted based on the final memory layout.
- term: assembler
  definition: A program that translates assembly language into machine code. It also
    generates relocation information for the linker.
- term: ADD/SUB relocations
  definition: Specific relocation types used by the assembler/linker to represent
    the result of an addition or subtraction between symbols or constants.
- term: PC-relative
  definition: A type of address calculation where the offset is relative to the current
    program counter (PC). This is common for position-independent code.
- term: linker relaxation
  definition: A linker optimization that allows it to substitute shorter, faster instructions
    for longer ones if the target address is known to be close enough. This can involve
    changing instruction opcodes and relocation types.
series_id: 'binutils:loongarch: optimize add/sub and pc-relative relocations handling'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260813170736.1880481-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

This patch series introduces several improvements to LoongArch relocation handling in the GNU Assembler. It adds support for emitting relocations for symbolic subtraction expressions, optimizes the `TC_FORCE_RELOCATION_SUB_LOCAL` mechanism to reduce fixup overhead, and corrects the `md_pcrel_from` function for accurate PC-relative offset calculations. These changes collectively aim to improve the efficiency and correctness of code generation for LoongArch.
