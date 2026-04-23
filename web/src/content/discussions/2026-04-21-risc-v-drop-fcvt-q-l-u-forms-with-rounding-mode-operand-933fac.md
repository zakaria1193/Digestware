---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- opcode table
- redundancy
- floating-point
discussion_id: 925c74e1-ee4d-4ab4-b293-e373b6910f26@suse.com
source_type: public_inbox
title: '[PATCH 08/19] RISC-V: drop FCVT.Q.L{,U} forms with rounding mode operand'
headline: 'Risc-V: Drop fcvt.q.l{,u} forms with rounding mode operand'
tldr: Removes the rounding mode operand from `fcvt.q.l` and `fcvt.q.lu` instructions
  as it has no effect, simplifying the opcode table.
stakes: Reduces redundancy and potential confusion by removing an unnecessary operand,
  leading to a cleaner and more efficient assembler.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- May break existing assembly code that incorrectly uses the rounding mode operand
  with these instructions (though the code was already behaving incorrectly).
- Reduces the size of the opcode table, slightly improving assembler performance.
exchanges: []
primer_expert: The RISC-V assembler (`gas/config/tc-riscv.c`) uses an opcode table
  (`opcodes/riscv-opc.c`) to map instruction names to their binary encodings. This
  patch simplifies the table by removing entries for `fcvt.q.l` and `fcvt.q.lu` that
  incorrectly included a rounding mode operand. The instructions themselves don't
  use the rounding mode, so the operand is redundant.
primer_general: In RISC-V assembly, some instructions convert between different data
  types. This patch removes an unnecessary option from certain conversion instructions
  (`fcvt.q.l` and `fcvt.q.lu`). The option, called "rounding mode", doesn't actually
  affect how these instructions work, so removing it makes the assembly code cleaner
  and less confusing.
series_id: 'binutils:risc-v: drop fcvt.q.l{,u} forms with rounding mode operand'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/925c74e1-ee4d-4ab4-b293-e373b6910f26@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch removes the floating-point rounding mode operand from the `fcvt.q.l` and `fcvt.q.lu` instructions in the RISC-V opcode table. These instructions are unaffected by the rounding mode, so allowing the operand is misleading. Removing the operand simplifies the opcode table and avoids potential misinterpretations.
