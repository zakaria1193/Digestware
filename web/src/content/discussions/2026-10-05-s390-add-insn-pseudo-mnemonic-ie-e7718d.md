---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- .insn
- instruction-set
discussion_id: 20261005153947.363053-61-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 13/46] s390: Add .insn pseudo-mnemonic ie'
headline: 's390: Add .insn pseudo-mnemonic ie'
tldr: Add support for the s390 'ie' instruction format using .insn.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch adds support for the z/Architecture Instruction Execution
  (IE) format to the s390 GNU Assembler (gas). It defines the '.insn ie' pseudo-mnemonic
  in opcodes/s390-opc.c, documents its operand structure (I1, I2) in gas/doc/c-s390.texi,
  and provides test cases in gas/testsuite/gas/s390/zarch-operands.d/.s.
primer_glossary:
- term: .insn
  definition: A GNU assembler directive that allows embedding raw instruction bytes
    or defining pseudo-mnemonics for specific instruction formats.
- term: pseudo-mnemonic
  definition: An assembly language construct that represents a machine instruction,
    potentially with operands that are not direct encodings of machine code but are
    processed by the assembler.
- term: zEC12
  definition: IBM's 12th generation z/Architecture mainframe processor.
series_id: 'binutils:s390: add .insn pseudo-mnemonic ie'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-61-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch introduces the '.insn ie' pseudo-mnemonic to the s390 gas assembler, supporting the IE instruction format introduced with the zEC12 processor. It adds the new format to the opcode definitions, updates the documentation, and includes test cases.
