---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- assembler
- instruction-formats
- documentation
discussion_id: 20261005153947.363053-62-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 14/46] s390: Add .insn pseudo-mnemonic mii'
headline: 's390: Add .insn pseudo-mnemonic mii'
tldr: Adds support for the .insn mii pseudo-mnemonic in the s390 assembler, corresponding
  to the MII instruction format introduced with IBM zEC12.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Requires specifying the minimum architecture level (IBM zEC12) for this instruction
  format.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Adds the .insn mii pseudo-mnemonic to opcodes/s390-opc.c and gas/doc/c-s390.texi,
    with corresponding tests in gas/testsuite/gas/s390/zarch-operands.
  quote: null
primer_expert: This patch introduces support for the MII instruction format and its
  associated '.insn mii' pseudo-mnemonic in the s390 GNU Assembler. The MII format
  was introduced in the IBM zEC12 architecture. The changes involve updating the opcode
  definitions and documentation, and adding test cases to verify correct assembly
  and disassembly.
primer_glossary:
- term: .insn
  definition: An assembler directive that allows direct insertion of machine instructions
    using their opcode and operands, often used for undefined or specialized instructions.
- term: pseudo-mnemonic
  definition: A symbolic name used in assembly language that corresponds to a machine
    instruction or a sequence of instructions, often used for convenience or to represent
    complex operations.
- term: MII format
  definition: A specific s390 instruction format introduced with the IBM zEC12 processor,
    characterized by its structure and intended use.
series_id: 'binutils:s390: add .insn pseudo-mnemonic mii'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-62-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch adds the '.insn mii' pseudo-mnemonic to the GNU Assembler for the s390 architecture. It reflects the MII instruction format, which was introduced with the IBM zEC12 processor. The changes include updates to the opcode definitions and documentation, along with new test cases for z/Architecture.
