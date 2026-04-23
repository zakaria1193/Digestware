---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- instruction set
- rounding mode
discussion_id: 925c74e1-ee4d-4ab4-b293-e373b6910f26@suse.com
source_type: public_inbox
title: '[PATCH 08/19] RISC-V: drop FCVT.Q.L{,U} forms with rounding mode operand'
headline: 'Risc-V: Drop fcvt.q.l{,u} forms with rounding mode operand'
tldr: Removes the rounding mode operand from FCVT.Q.L and FCVT.Q.LU instructions as
  it has no effect.
stakes: Simplifies the instruction set and reduces potential confusion by removing
  meaningless operands.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Simplified instruction set and reduced potential for confusion.
- No performance impact.
exchanges: []
primer_expert: The patch removes the rounding mode operand from `FCVT.Q.L` and `FCVT.Q.LU`
  in `opcodes/riscv-opc.c`. As these instructions are integer-to-float conversions,
  the rounding mode has no effect. Removing the unnecessary operand simplifies the
  opcode table and reduces potential ambiguity.
primer_general: The binutils tools include information on the RISC-V instruction set.
  This patch removes an option from certain instructions that doesn't actually do
  anything. This simplifies the instruction set definition, making the tools easier
  to maintain.
series_id: 'binutils:risc-v: drop fcvt.q.l{,u} forms with rounding mode operand'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/925c74e1-ee4d-4ab4-b293-e373b6910f26@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch removes the rounding mode operand from the `FCVT.Q.L` and `FCVT.Q.LU` RISC-V instructions within binutils. These instructions are unaffected by the rounding mode, making the operand redundant. Removing the operand simplifies the instruction set and avoids potential confusion.
