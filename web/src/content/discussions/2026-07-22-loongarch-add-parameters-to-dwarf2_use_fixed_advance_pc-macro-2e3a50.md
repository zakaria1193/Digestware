---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- gas
- dwarf
- loongarch
- debugging
discussion_id: 20260722032330.1310277-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[RFC PATCH] LoongArch: Add parameters to DWARF2_USE_FIXED_ADVANCE_PC macro'
headline: 'LoongArch: Add parameters to DWARF2_USE_FIXED_ADVANCE_PC macro'
tldr: Patch adds FROM and TO symbol parameters to DWARF2_USE_FIXED_ADVANCE_PC macro
  for LoongArch for finer DWARF debug info control.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Increased complexity in DWARF line number generation logic.
- Potential for more accurate or compact DWARF information.
- Added control for specific architectures like LoongArch.
exchanges: []
primer_expert: This patch introduces parameters (FROM, TO) to the `DWARF2_USE_FIXED_ADVANCE_PC`
  macro in the LoongArch backend of binutils' GAS. This macro controls how DWARF line
  number information is generated. Currently, it's a simple on/off switch. The change
  allows GAS to conditionally use `DW_LNS_fixed_advance_pc` (for advancing the program
  counter in DWARF .debug_line info) only when there are linker-relaxable instructions
  between the FROM and TO symbols. Otherwise, it falls back to using special opcodes,
  potentially leading to more compact or accurate line number debug info.
primer_glossary:
- term: LoongArch
  definition: A Chinese indigenous instruction set architecture.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about variables, types, and code structure.
- term: DW_LNS_fixed_advance_pc
  definition: A DWARF line number statement ('Line Number Statement') instruction
    used to advance the program counter by a fixed amount in the .debug_line section.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: linker-relaxable instructions
  definition: Instructions whose assembly addresses might change during the linking
    process, typically due to relocation or optimization.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260722032330.1310277-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-07-22'
is_stub: false
stub_reason: ''
---

This RFC patch for binutils' LoongArch support introduces parameters to the DWARF2_USE_FIXED_ADVANCE_PC macro. The goal is to allow finer-grained control over DWARF debug information generation, specifically by deciding whether to use the DW_LNS_fixed_advance_pc opcode or special opcodes based on the presence of linker-relaxable instructions between symbols.
