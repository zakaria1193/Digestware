---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- instruction set
- opcode
- rounding mode
- assembler
discussion_id: 22f4c3a6-01a8-4ae4-8359-5d5ad3470b8b@suse.com
source_type: public_inbox
title: '[PATCH v2 07/16] RISC-V: drop FCVT.Q.L{,U} forms with rounding mode operand'
headline: 'RISC-V: drop FCVT.Q.L{,U} forms with rounding mode operand'
tldr: Removes the rounding mode operand from the `FCVT.Q.L` and `FCVT.Q.LU` RISC-V
  instructions as it has no effect.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Simplified instruction definitions.
- Removed a potentially confusing operand from the assembler syntax.
exchanges: []
primer_expert: The RISC-V opcode table in `opcodes/riscv-opc.c` defines the format
  of RISC-V instructions. This patch removes the rounding mode ('m') operand from
  the `FCVT.Q.L` and `FCVT.Q.LU` instruction definitions because these instructions
  are unaffected by the rounding mode. This change simplifies the opcode table and
  avoids potential confusion.
primer_general: The instruction set architecture (ISA) defines the instructions a
  CPU can execute. RISC-V is a modern open ISA designed for a wide range of applications.  Instructions
  can have operands that specify the data to be operated on.  Rounding modes specify
  how floating-point numbers should be rounded to fit within a certain precision.  This
  patch removes an unnecessary operand from certain RISC-V instructions, simplifying
  the instruction definition.
series_id: 'binutils:risc-v: drop fcvt.q.l{,u} forms with rounding mode operand'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/22f4c3a6-01a8-4ae4-8359-5d5ad3470b8b@suse.com
bugzilla_url: null
date: '2026-05-15'
is_stub: false
---

This patch removes the rounding mode operand from the `FCVT.Q.L` and `FCVT.Q.LU` RISC-V instructions in the opcode table. The rounding mode has no effect on these instructions, so allowing the operand is misleading. This change aligns these instructions with similar ones (`FCVT.D.W`, `FCVT.Q.W`) and simplifies the opcode definitions.
