---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- opcode
- refactoring
discussion_id: 0916417e-863e-90ac-8c0a-f64284866afb@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 04/28] aarch64: Use F_OPD0_OPT to combine two gcspopm entries'
headline: 'aarch64: Use F_OPD0_OPT to combine two gcspopm entries'
tldr: Consolidates two aarch64 gcspopm opcode entries into one using F_OPD0_OPT for
  cleaner representation.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Simplifies opcode table representation.
- Aligns with canonical representation for optional operands.
exchanges: []
primer_expert: This patch modifies the AArch64 opcode table (`aarch64-tbl-2.h` and
  `aarch64-dis-2.c`) to use the `F_OPD0_OPT` and `F_DEFAULT` flags to represent the
  `gcspopm` instruction. Previously, this instruction was represented by two separate
  entries in the table. The change aims to streamline the opcode definition and decoding
  process within binutils.
primer_glossary:
- term: F_OPD0_OPT
  definition: A flag used in the AArch64 opcode table to indicate that an operand
    is optional. This allows a single opcode table entry to represent variations of
    an instruction based on operand presence.
- term: F_DEFAULT
  definition: A flag used in the AArch64 opcode table, often in conjunction with optional
    operands, to specify default values or behaviors when an operand is omitted.
- term: gcspopm
  definition: A specific AArch64 instruction related to stack operations, likely involving
    popping multiple registers from the stack.
- term: Opcode Table
  definition: A data structure used by disassemblers and assemblers to map instruction
    byte patterns to mnemonic names and vice-versa. In binutils, these tables define
    the instructions a specific architecture supports.
series_id: 'binutils:aarch64: use f_opd0_opt to combine two gcspopm entries'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/0916417e-863e-90ac-8c0a-f64284866afb@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch refactors the AArch64 opcode table by combining two 'gcspopm' entries into a single entry using the F_OPD0_OPT and F_DEFAULT flags. This change aligns with the canonical representation for opcodes with optional operands, simplifying the opcode table and potentially improving decoding efficiency.
