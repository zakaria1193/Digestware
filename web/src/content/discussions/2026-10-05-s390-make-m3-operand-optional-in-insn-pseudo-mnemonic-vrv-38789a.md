---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- .insn
- instruction-format
discussion_id: 20261005153947.363053-92-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 44/46] s390: Make M3 operand optional in .insn pseudo-mnemonic vrv'
headline: 's390: Make M3 operand optional in .insn pseudo-mnemonic vrv'
tldr: Make the M3 operand optional for s390 .insn vrv pseudo-mnemonic.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch modifies the s390 GNU Assembler (gas) to support an optional
  M3 mask field in the VRV instruction format, accessible via the '.insn vrv' pseudo-mnemonic.
  Changes include updating opcodes/s390-opc.c, gas/doc/c-s390.texi to reflect the
  optionality (denoted by '[M3]'), and adding new test cases in gas/testsuite/gas/s390/zarch-operands.d/.s.
primer_glossary:
- term: .insn
  definition: A GNU assembler directive that allows embedding raw instruction bytes
    or defining pseudo-mnemonics for specific instruction formats.
- term: pseudo-mnemonic
  definition: An assembly language construct that represents a machine instruction,
    potentially with operands that are not direct encodings of machine code but are
    processed by the assembler.
- term: operand
  definition: A value or symbol that an instruction operates on.
- term: VRV
  definition: A specific instruction format in the s390 architecture.
series_id: 'binutils:s390: make m3 operand optional in .insn pseudo-mnemonic vrv'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-92-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch makes the M3 mask operand optional for the '.insn vrv' pseudo-mnemonic in the s390 gas assembler. It updates the opcode definitions, documentation, and adds test cases for this instruction format.
