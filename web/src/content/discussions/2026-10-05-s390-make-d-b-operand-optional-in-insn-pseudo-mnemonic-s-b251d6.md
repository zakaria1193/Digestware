---
project: binutils
subsystem: s390
patch_id: null
tags:
- binutils
- gas
- s390
- assembler
- instruction format
discussion_id: 20261005153947.363053-81-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 33/46] s390: Make D(B) operand optional in .insn pseudo-mnemonic s'
headline: 's390: Make D(B) operand optional in .insn pseudo-mnemonic s'
tldr: Makes the D(B) operand optional for the s390 .insn pseudo-mnemonic 's', aligning
  it with the instruction format.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Better alignment between assembler syntax and hardware instruction format.
- Improved usability for specific s390 instructions.
exchanges: []
primer_expert: This patch targets `opcodes/s390-opc.c` and testsuite files to update
  the `.insn` pseudo-mnemonic for the s390 's' instruction. The 'S' instruction format
  includes optional Base (B) and Displacement (D) fields, which are represented as
  a D(B) composite operand in the `.insn` pseudo-mnemonic. This change makes that
  composite operand optional, reflecting the actual instruction encoding. It also
  involves updating documentation and adding test cases for both ESA/390 and z/Architecture
  variants.
primer_glossary:
- term: .insn
  definition: An assembler pseudo-mnemonic that allows embedding raw machine instructions
    using their format and opcode.
- term: pseudo-mnemonic
  definition: An assembler directive that represents a machine instruction or a sequence
    of instructions using a symbolic name.
- term: s390
  definition: IBM's mainframe and enterprise server architecture.
- term: optional operands
  definition: Operands for an instruction or pseudo-mnemonic that are not required
    and can be omitted, often controlled by the instruction format or specific flags.
- term: D(B)
  definition: In s390 assembly, a composite operand representing a displacement (D)
    relative to a base register (B).
series_id: 'binutils:s390: make d(b) operand optional in .insn pseudo-mnemonic s'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-81-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch makes the D(B) composite operand optional in the s390 assembler's `.insn` pseudo-mnemonic for the 's' instruction. This change aligns the assembler's behavior with the S instruction format, which specifies optional B and D fields. The commit also adds comments to existing tests for ESA/390 and includes new tests for z/Architecture `s` instructions.
