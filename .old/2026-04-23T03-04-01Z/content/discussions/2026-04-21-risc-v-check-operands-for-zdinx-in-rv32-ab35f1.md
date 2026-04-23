---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- Zdinx
- RV32
discussion_id: caa092f8-7262-44b3-b139-7478ba5fb2db@suse.com
source_type: public_inbox
title: '[PATCH 10/19] RISC-V: check operands for Zdinx in RV32'
headline: 'Risc-V: Check operands for Zdinx in RV32'
tldr: Adds operand checks for the Zdinx extension in RV32 to ensure correct register
  pairing.
stakes: Ensures correct code generation and execution when using the Zdinx extension
  on RV32 architectures.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds additional checks to the assembler, potentially increasing assembly time slightly.
- Ensures correct code generation for Zdinx on RV32.
exchanges: []
primer_expert: The Zdinx extension introduces new instructions that operate on register
  pairs.  On RV32, these register pairs must be encoded such that the least significant
  bit of the register number is zero. The patch adds checks in the assembler to validate
  this encoding. It also introduces the `RV32_EVEN_CHECK` macro for easier checking.
primer_general: The RISC-V Zdinx extension adds instructions that operate on pairs
  of registers. This patch ensures that when using these instructions on 32-bit RISC-V
  systems, the registers are correctly specified as pairs. This ensures code correctness.
series_id: 'binutils:risc-v: check operands for zdinx in rv32'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/caa092f8-7262-44b3-b139-7478ba5fb2db@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch introduces checks for register operands when the Zdinx extension is used in RV32 mode. Like Zilsd, Zdinx requires register pairs to be encoded with the low bit clear. The patch adds flags to indicate whether these checks should be performed, as the availability of XLEN is not guaranteed in match functions.
