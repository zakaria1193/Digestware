---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- floating-point
- rounding mode
- opcode table
discussion_id: bdfcf3d2-18bf-4e3a-98c6-cd0ebbf4b7d2@suse.com
source_type: public_inbox
title: '[PATCH 09/19] RISC-V: make FP rounding mode an optional argument'
headline: 'Risc-V: Make FP rounding mode an optional argument'
tldr: Makes the floating-point rounding mode argument optional in RISC-V assembler
  syntax, reducing opcode table size.
stakes: Simplifies assembler syntax and reduces code duplication in the opcode table,
  potentially improving performance and maintainability.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- The change introduces additional complexity in the assembler and disassembler to
  handle the optional argument.
- May break existing assembly code that relies on the rounding mode being a mandatory
  argument (though unlikely).
- Reduces opcode table size, which could improve lookup performance.
exchanges: []
primer_expert: The RISC-V instruction set architecture (ISA) includes floating-point
  instructions that can specify a rounding mode. This patch modifies the assembler
  (`gas/config/tc-riscv.c`) and disassembler (`opcodes/riscv-dis.c`) to treat the
  rounding mode as an optional argument for some instructions. This reduces the size
  of the `riscv_opcodes` table in `opcodes/riscv-opc.c` by merging entries with and
  without the rounding mode.
primer_general: When writing assembly code for RISC-V, floating-point operations often
  require specifying a rounding mode. This patch makes the rounding mode optional
  for some instructions, allowing the assembler to infer the default rounding mode
  if not explicitly specified. This simplifies the assembly syntax and reduces redundancy
  in the toolchain's internal tables.
series_id: 'binutils:risc-v: make fp rounding mode an optional argument'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/bdfcf3d2-18bf-4e3a-98c6-cd0ebbf4b7d2@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies the RISC-V assembler to allow the floating-point rounding mode argument to be optional for certain instructions.  By making the rounding mode optional, the number of entries in the opcode table can be reduced. The patch adjusts the assembler and disassembler to handle the optional rounding mode.
