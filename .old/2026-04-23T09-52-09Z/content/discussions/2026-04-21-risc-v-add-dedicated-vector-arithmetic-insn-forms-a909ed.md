---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- .insn directive
- vector instructions
discussion_id: baea3bec-bbed-483d-bef0-d9c59116f2e4@suse.com
source_type: public_inbox
title: '[PATCH 03/19] RISC-V: add dedicated vector arithmetic .insn forms'
headline: 'RISC-V: Add dedicated vector arithmetic .insn forms'
tldr: Adds more dedicated .insn forms for vector arithmetic instructions to simplify
  their use.
stakes: Improves the usability of the .insn directive for specifying vector arithmetic
  instructions, potentially leading to more readable and maintainable assembly code.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds complexity to the assembler's instruction parsing logic.
- May increase the size of the assembler binary.
- Potential ambiguity with existing instruction forms (OP_VE).
exchanges: []
primer_expert: This patch modifies `gas/config/tc-riscv.c` to add new instruction
  forms for RISC-V vector instructions.  `.insn` is a directive that allows specifying
  instructions numerically. The changes improve the usability of `.insn` for `OP_V`
  instructions by adding more specific forms. The patch also discusses potential extensions
  to `OP_VE` and `OPCFG` opcodes, and handling immediate values in vector instructions.
primer_general: The RISC-V architecture has a `.insn` assembler directive, which allows
  embedding raw instruction encodings directly into assembly code. This is useful
  for defining custom or less common instructions. This patch focuses on improving
  the usability of the `.insn` directive for vector instructions in RISC-V. Vector
  instructions perform the same operation on multiple data elements simultaneously.
  By providing dedicated `.insn` forms, the patch aims to make it easier to specify
  these instructions numerically, improving code readability and maintainability.
series_id: 'binutils:risc-v: add dedicated vector arithmetic .insn forms'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/baea3bec-bbed-483d-bef0-d9c59116f2e4@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch introduces dedicated `.insn` forms for RISC-V vector arithmetic instructions, specifically for the `OP_V` opcode. The goal is to simplify the use of the `.insn` directive, which can be challenging with existing forms. The patch adds new forms, and seeks feedback on extending this approach to other vector instructions, like those using the `OP_VE` and `OPCFG` opcodes, and instructions with immediate values.
