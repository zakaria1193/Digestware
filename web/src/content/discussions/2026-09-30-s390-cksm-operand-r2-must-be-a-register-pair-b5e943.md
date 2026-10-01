---
project: binutils
subsystem: s390/opcodes
patch_id: null
tags:
- s390
- architecture
- opcodes
- linker
- assembler
discussion_id: 20260930081834.2948939-25-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 03/20] s390: cksm operand R2 must be a register pair'
headline: 's390: cksm operand R2 must be a register pair'
tldr: Updates S/390 opcode definitions for `cksm` to enforce that R2 must be an even-numbered
  register forming a pair.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Introduces a new instruction format definition.
exchanges: []
primer_expert: This patch modifies the S/390 opcode definitions to correctly represent
  the constraints of the `cksm` instruction. The `cksm R1,R2` instruction requires
  that `R2` refers to an even-numbered register, which implicitly defines an even-odd
  register pair (e.g., R8 and R9). A new instruction format, `INSTR_RRE_RRE` and `MASK_RRE_RRE`,
  is introduced in `s390-opc.c` to enforce this requirement. The test cases in `gas/testsuite/gas/s390/esa-g5.d`
  and `esa-g5.s` are updated to use an even register for `R2` (`%r8` instead of `%r9`)
  to pass validation.
primer_glossary:
- term: s390
  definition: IBM's 31-bit and 64-bit mainframe architecture.
- term: opcode
  definition: A machine language instruction.
- term: cksm
  definition: An S/390 instruction for checksum calculation.
- term: register pair
  definition: In S/390 architecture, certain instructions operate on two consecutive
    registers, where the first register must have an even number.
series_id: 'binutils:s390: cksm operand r2 must be a register pair'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930081834.2948939-25-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch modifies the S/390 opcode definitions for the `cksm` instruction. It introduces a new instruction format, RRE_RRE, which correctly enforces that the second operand (R2) must be an even-numbered register, as `cksm` operates on an even-odd register pair. The test suite is updated to reflect this constraint, ensuring correct assembly and disassembly.
