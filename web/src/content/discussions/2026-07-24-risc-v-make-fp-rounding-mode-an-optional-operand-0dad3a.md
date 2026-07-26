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
discussion_id: 34185d40-e19d-48e3-a6a5-f48ef4a54ebd@suse.com
source_type: public_inbox
title: '[PATCH v4 05/12] RISC-V: make FP rounding mode an optional operand'
headline: 'RISC-V: make FP rounding mode an optional operand'
tldr: Allow optional FP rounding mode operand for RISC-V instructions.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Reduces opcode table size and complexity by making the rounding mode optional.
- Introduces slightly more complex parsing logic in the assembler to handle optional
  operands.
exchanges: []
primer_expert: This change refactors the RISC-V assembler's instruction parsing for
  floating-point operations. It makes the rounding mode specifier ('m' or 'M') optional
  for most FP instructions, similar to how it's handled for 'Vm' and 'VM' instructions,
  reducing opcode table entries. The rounding mode is now implicitly determined if
  not provided, except for specific instructions like FCVTMOD.W.D that require explicit
  rounding mode specification.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is gaining popularity
    for its modularity and extensibility.
- term: FP
  definition: Floating-point. Refers to numbers with fractional parts, handled by
    dedicated hardware units in most processors.
- term: Rounding Mode
  definition: Specifies how to handle the result of a floating-point operation when
    it cannot be represented exactly. Common modes include round-to-nearest, round-to-zero,
    etc.
- term: Opcode table
  definition: A data structure used by assemblers and disassemblers to map instruction
    mnemonics to their binary representations.
series_id: 'binutils:risc-v: make fp rounding mode an optional operand'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/34185d40-e19d-48e3-a6a5-f48ef4a54ebd@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch modifies the RISC-V assembler to make the floating-point rounding mode operand optional for most instructions. This change simplifies the opcode table by reducing redundant entries and aligns the handling with similar ARM Vm and VM counterparts. The rounding mode is now implicitly handled unless explicitly specified, with an exception for FCVTMOD.W.D where 'M' is still required.
