---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- floating-point
- assembler
- opcode
discussion_id: e790534c-6de5-4595-bcd3-34ab3c243cab@suse.com
source_type: public_inbox
title: '[PATCH v4 04/12] RISC-V: drop FCVT.Q.L{,U} forms with rounding mode operand'
headline: 'RISC-V: drop FCVT.Q.L{,U} forms with rounding mode operand'
tldr: Remove redundant floating-point conversion instructions from RISC-V assembler.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Simplifies the opcode table by removing incorrect instruction forms.
- Removes the possibility of users incorrectly specifying a rounding mode for these
  instructions.
exchanges: []
primer_expert: This patch cleans up the RISC-V opcode table by removing forms of `fcvt.q.l`
  and `fcvt.q.lu` that incorrectly included a rounding mode operand. These particular
  conversions operate on floating-point values being converted to integers, and the
  rounding mode specifier is not relevant. This cleanup ensures the assembler adheres
  to the RISC-V ISA specification for these instructions.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is gaining popularity
    for its modularity and extensibility.
- term: FCVT.Q.L
  definition: A RISC-V floating-point instruction for converting a quad-precision
    floating-point value to a long integer.
- term: FCVT.Q.LU
  definition: A RISC-V floating-point instruction for converting a quad-precision
    floating-point value to a long unsigned integer.
- term: Rounding Mode
  definition: Specifies how to handle the result of a floating-point operation when
    it cannot be represented exactly. Common modes include round-to-nearest, round-to-zero,
    etc.
- term: Opcode table
  definition: A data structure used by assemblers and disassemblers to map instruction
    mnemonics to their binary representations.
series_id: 'binutils:risc-v: drop fcvt.q.l{,u} forms with rounding mode operand'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/e790534c-6de5-4595-bcd3-34ab3c243cab@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch removes redundant forms of the RISC-V `FCVT.Q.L` and `FCVT.Q.LU` instructions from the assembler's opcode table. These forms incorrectly allowed a floating-point rounding mode operand, which is not applicable to these specific conversions. The removal simplifies the opcode definitions and prevents incorrect instruction usage.
