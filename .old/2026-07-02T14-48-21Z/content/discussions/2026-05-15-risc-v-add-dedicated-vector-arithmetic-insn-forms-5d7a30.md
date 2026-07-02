---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- vectorization
- .insn
discussion_id: 81972842-e7b8-460b-aea7-3e8511c3f26b@suse.com
source_type: public_inbox
title: '[PATCH v2 03/16] RISC-V: add dedicated vector arithmetic .insn forms'
headline: 'RISC-V: Add dedicated vector arithmetic .insn forms'
tldr: Adds more dedicated .insn forms for RISC-V vector arithmetic instructions to
  simplify their use in assembly.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Potential ambiguity with future OP_VE instructions if naming conventions are not
  carefully considered.
- The current parsing logic may not support both signed and unsigned immediates for
  OPIVI instructions.
- Adding forms with immediates for V*UNARY* instructions could increase code complexity.
exchanges: []
primer_expert: The RISC-V GNU assembler uses `.insn` directives to define custom assembly
  instructions.  This patch extends the existing instruction definitions in `gas/config/tc-riscv.c`
  to include more specific forms for vector arithmetic operations (`OP_V`). The goal
  is to simplify the use of these instructions by providing more intuitive operand
  combinations.
primer_general: The GNU assembler translates human-readable assembly code into machine
  code that a computer can execute.  Assembler directives like `.insn` allow developers
  to define custom instructions with specific operand types and encodings. This patch
  enhances the RISC-V assembler by adding new instruction forms for vector operations,
  making it easier to write assembly code that utilizes RISC-V's vector processing
  capabilities.
series_id: 'binutils:risc-v: add dedicated vector arithmetic .insn forms'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/81972842-e7b8-460b-aea7-3e8511c3f26b@suse.com
bugzilla_url: null
date: '2026-05-15'
is_stub: false
---

This patch adds dedicated `.insn` forms for RISC-V vector arithmetic instructions, aiming to make assembly code easier to write and read. The patch introduces new forms for the `OP_V` opcode. The author is seeking feedback on naming conventions for future `OP_VE` instructions and on the possibility of adding forms with immediates for encoding V*UNARY* instructions.
