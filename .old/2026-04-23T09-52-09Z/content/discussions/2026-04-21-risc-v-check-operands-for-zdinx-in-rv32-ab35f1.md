---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- zdinx
- rv32
- operand checking
- assembler
discussion_id: caa092f8-7262-44b3-b139-7478ba5fb2db@suse.com
source_type: public_inbox
title: '[PATCH 10/19] RISC-V: check operands for Zdinx in RV32'
headline: 'Risc-V: Check operands for Zdinx in RV32'
tldr: Adds operand checks for the Zdinx extension in RV32 to ensure register pairs
  have low bit clear.
stakes: Ensures correct code generation and prevents undefined behavior when using
  the Zdinx extension on RV32.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding operand checks may introduce a small performance overhead during assembly.
- The new flags increase code complexity.
exchanges: []
primer_expert: The Zdinx extension introduces new instructions that operate on register
  pairs.  In RV32, these register pairs must be aligned on even register numbers.  The
  patch adds checks in the assembler (`gas/config/tc-riscv.c`) and disassembler (`opcodes/riscv-dis.c`)
  to enforce this alignment constraint. The `INSN_RV32_EVEN_*` flags are introduced
  to propagate this constraint, since match functions lack XLEN access.
primer_general: RISC-V extensions add new instructions and features to the base architecture.
  The Zdinx extension introduces instructions that operate on pairs of registers.
  This patch ensures that when using the Zdinx extension on 32-bit RISC-V systems,
  the registers used in these instructions are correctly aligned, preventing potential
  errors and ensuring that the code executes as intended.
series_id: 'binutils:risc-v: check operands for zdinx in rv32'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/caa092f8-7262-44b3-b139-7478ba5fb2db@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch introduces checks for register pair operands in the Zdinx extension for RV32. It enforces that register pairs are encoded with the low bit clear, as required by the specification. The patch adds flags to be used in assembler and disassembler to facilitate these checks, since match functions don't have XLEN available.
