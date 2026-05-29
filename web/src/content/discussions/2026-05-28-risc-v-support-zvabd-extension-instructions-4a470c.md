---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- riscv
- zvabd
- vector
- extension
- assembler
discussion_id: 20260528100602.475331-1-jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH] RISC-V: Support Zvabd extension instructions.'
headline: 'RISC-V: Support Zvabd extension instructions'
tldr: This patch adds support for the RISC-V Zvabd extension, which provides vector
  integer absolute difference operations.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adding new instructions increases the complexity of the toolchain and requires additional
  testing and maintenance.
- The patch assumes that the current specification of the Zvabd extension is stable
  and will not change in the future.
exchanges: []
primer_expert: The patch adds support for the Zvabd extension to the RISC-V toolchain.
  This involves modifying the BFD library (`bfd/elfxx-riscv.c`) to recognize the new
  extension and its implications on other extensions like zve32x. The assembler (`gas`)
  is updated with new instructions and corresponding tests. The `opcode` directory
  is modified to include the instruction encodings. This enables the toolchain to
  assemble, link, and disassemble code that uses the Zvabd extension.
primer_general: This patch extends the RISC-V toolchain to support a new set of instructions
  called the Zvabd extension. RISC-V is a modular instruction set architecture, and
  extensions add new capabilities to the processor. The Zvabd extension provides instructions
  for performing absolute difference operations on vectors of integers, which can
  be useful in signal processing, image processing, and other applications. The patch
  modifies the assembler, linker, and other tools to understand and handle these new
  instructions, allowing developers to use them in their code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260528100602.475331-1-jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-05-28'
is_stub: false
---

This patch introduces support for the RISC-V Zvabd extension instructions, which provide vector integer absolute difference operations. The patch includes updates to bfd, gas, include files, and opcodes to recognize and handle the new instructions. The widening accumulate mnemonics `vwabda.vv` and `vwabdau.vv` are implemented according to the current specification, and new tests are added to ensure correct assembly and disassembly.
