---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- vector instructions
- assembler
- insn directive
- gas
discussion_id: baea3bec-bbed-483d-bef0-d9c59116f2e4@suse.com
source_type: public_inbox
title: '[PATCH 03/19] RISC-V: add dedicated vector arithmetic .insn forms'
headline: 'RISC-V: add dedicated vector arithmetic .insn forms'
tldr: Adds dedicated `.insn` forms for RISC-V vector arithmetic instructions to simplify
  their use in assembly code.
stakes: Simplifies the use of RISC-V vector arithmetic instructions in assembly code,
  making it easier for developers to write and maintain code using these instructions.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Simplifies the use of vector arithmetic instructions in assembly.
- Potential ambiguities with future OP_VE instructions.
- Consideration of adding forms with immediate values.
exchanges: []
primer_expert: This patch modifies `gas/config/tc-riscv.c` to add new `.insn` forms
  for RISC-V vector instructions (OP_V). It introduces new forms utilizing `FUNCT6`
  and aims to simplify the encoding of vector arithmetic instructions. The patch also
  discusses potential ambiguities with OP_VE instructions and considers the addition
  of forms with immediate values for encoding unary vector instructions.
primer_general: The `.insn` directive in assembly allows developers to specify instructions
  using their numeric representation. This patch enhances the RISC-V assembler by
  adding more user-friendly `.insn` forms specifically for vector arithmetic instructions.
  This makes it easier to directly encode vector operations within assembly code.
  The patch improves the usability of vector instructions and opens discussions about
  further enhancements, such as handling immediates and potential future extensions.
series_id: 'binutils:risc-v: add dedicated vector arithmetic .insn forms'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/baea3bec-bbed-483d-bef0-d9c59116f2e4@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch adds dedicated `.insn` forms for RISC-V vector arithmetic instructions. The `.insn` directive allows specifying instructions numerically, but its usage can be challenging. This patch provides more specific forms for vector instructions to simplify their use. The patch also explores options for future OP_VE instructions and considers the potential for forms with immediates.
