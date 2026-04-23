---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- floating point
- instruction encoding
discussion_id: 925c74e1-ee4d-4ab4-b293-e373b6910f26@suse.com
source_type: public_inbox
title: '[PATCH 08/19] RISC-V: drop FCVT.Q.L{,U} forms with rounding mode operand'
headline: 'Risc-V: Drop fcvt.q.l{,u} forms with rounding mode operand'
tldr: Removes invalid rounding mode operands from FCVT.Q.L and FCVT.Q.LU instructions
  in the RISC-V assembler.
stakes: Ensures correct instruction encoding and prevents misinterpretation of floating-point
  conversion instructions.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Removes code from the opcode table.
- Ensures correct instruction encoding.
exchanges: []
primer_expert: The RISC-V opcode table (`riscv_opcodes`) maps instruction names and
  operands to their corresponding encodings. This patch removes the rounding mode
  operand ('m') from the `FCVT.Q.L` and `FCVT.Q.LU` entries, as these instructions
  do not use the rounding mode.  This ensures that the assembler generates the correct
  machine code.
primer_general: This patch fixes a small issue in the RISC-V assembler where certain
  floating-point conversion instructions were incorrectly allowed to have a rounding
  mode specified. Since the rounding mode has no effect on these instructions, the
  patch removes the unnecessary operand.
series_id: 'binutils:risc-v: drop fcvt.q.l{,u} forms with rounding mode operand'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/925c74e1-ee4d-4ab4-b293-e373b6910f26@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch removes the rounding mode operand from the `FCVT.Q.L` and `FCVT.Q.LU` instructions in the RISC-V assembler. These instructions are not affected by the rounding mode, so allowing a rounding mode operand is incorrect. This change ensures that the assembler generates the correct instruction encoding.
