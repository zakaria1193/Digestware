---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- disassembler
- spacemit
discussion_id: 20260503143354.142807-2-zhuangqiubin@linux.spacemit.com
source_type: public_inbox
title: '[PATCH v5 1/2] RISC-V: Add SpacemiT vendor extension xsmtvdot'
headline: 'RISC-V: Add SpacemiT vendor extension xsmtvdot'
tldr: This patch adds support for the SpacemiT Vector Dot Product (XsmtVdot) extension
  to the RISC-V assembler and disassembler.
proposer: Mark Zhuang <zhuangqiubin@linux.spacemit.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds support for a new vendor extension, enabling developers to utilize the new
  instructions.
- Increases the complexity of the assembler and disassembler.
- Requires updates to the toolchain to recognize the new extension.
- The code changes include updates to the assembler, disassembler, ELF handling, and
  adds new test cases.
exchanges: []
primer_expert: This patch adds support for the xsmtvdot extension to the RISC-V toolchain.  This
  involves modifying the assembler, disassembler, and linker to recognize and handle
  the new instructions and associated metadata. The changes primarily affect the `gas`,
  `opcodes`, and `bfd` directories.
primer_general: This patch extends the RISC-V assembler and disassembler to support
  a new hardware feature from SpacemiT called XsmtVdot.  The assembler translates
  human-readable assembly code into machine code, and the disassembler does the reverse.  By
  adding support for this new extension, developers can use the new SpacemiT instructions
  in their code.
series_id: 'binutils:risc-v: add spacemit vendor extension xsmtvdot'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260503143354.142807-2-zhuangqiubin@linux.spacemit.com
bugzilla_url: null
date: '2026-05-03'
---

This patch adds the SpacemiT Vector Dot Product Extension (XsmtVdot v1.0) to the RISC-V assembler and disassembler within binutils. This extension is a subset of the SpacemiT Intrinsic Matrix Extension (IME) specification and is implemented in the SpacemiT X60 processor. The patch includes updates to the assembler, disassembler, ELF handling, and adds new test cases.
