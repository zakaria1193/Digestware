---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- loongarch
- debugging
- dwarf
discussion_id: 20260819034135.4182729-1-mengqinggang@loongson.cn
source_type: public_inbox
title: 'Re: [PATCH v1] LoongArch: Use less DW_LNS_fixed_advance_pc'
headline: 'LoongArch: Use less DW_LNS_fixed_advance_pc'
tldr: Patch to use less DW_LNS_fixed_advance_pc for LoongArch debugging information
  is ready for merge.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: 10
technical_tradeoffs:
- Potentially reduces the size of DWARF debug info.
- May increase complexity in the code generation logic.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Confirms that the patch is ready to be merged and asks for confirmation.
  quote: Thanks! Just to confirm, can this patch be merged?
- author: Alan Modra <amodra@gmail.com>
  role: maintainer
  position: Approves the patch for merging.
  quote: Yes.
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Reports that the patch has been applied.
  quote: Thanks, applied.
primer_expert: This patch modifies gas to conditionally use DW_LNS_fixed_advance_pc
  for generating DWARF debugging information on LoongArch. It refines the logic to
  use this opcode only when linker-relaxable instructions exist between symbols, aiming
  to reduce the overhead of symbol value lookups.
primer_glossary:
- term: DW_LNS_fixed_advance_pc
  definition: A DWARF Instruction Set (DIS) opcode used to advance the program counter
    (PC) by a fixed amount, typically for generating location lists.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about variables, types, and program structure.
- term: LoongArch
  definition: A RISC-based instruction set architecture developed in China.
- term: linker-relaxable instructions
  definition: Instructions whose machine code representation can be modified by the
    linker during optimization (relaxation) to improve code density or performance.
- term: symbol_get_value_expression
  definition: A function likely involved in retrieving the value or address of a symbol,
    potentially involving complex expressions.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/5f682482-2d96-4a31-a196-8958e2ae03d7@loongson.cn
bugzilla_url: null
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This patch, previously reviewed and revised based on feedback, optimizes the generation of debugging information for LoongArch by judiciously using DW_LNS_fixed_advance_pc. The author inquires if the patch can now be merged, and the maintainer confirms it can be applied.
