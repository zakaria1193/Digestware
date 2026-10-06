---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- .insn
- instruction-set
- mainframe
discussion_id: 20261005153947.363053-80-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 32/46] s390: Add .insn pseudo-mnemonics rxy_a/b/c'
headline: 's390: Add .insn pseudo-mnemonics rxy_a/b/c'
tldr: Add support for s390 RXY instruction variants using .insn.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch adds support for three variants of the RXY instruction format
  (rxy_a, rxy_b, rxy_c) to the s390 GNU Assembler (gas) using the '.insn' pseudo-mnemonic.
  It defines these formats in opcodes/s390-opc.c and provides corresponding test cases
  in gas/testsuite/gas/s390/zarch-operands.d/.s, noting their introduction on specific
  IBM z/Architecture processors.
primer_glossary:
- term: .insn
  definition: A GNU assembler directive that allows embedding raw instruction bytes
    or defining pseudo-mnemonics for specific instruction formats.
- term: pseudo-mnemonic
  definition: An assembly language construct that represents a machine instruction,
    potentially with operands that are not direct encodings of machine code but are
    processed by the assembler.
- term: RXY
  definition: A specific instruction format in the s390 architecture, with variants
    introduced across different processor generations.
- term: z990, z10, z17
  definition: IBM mainframe processor generations that introduced different versions
    of the RXY instruction format.
series_id: 'binutils:s390: add .insn pseudo-mnemonics rxy_a/b/c'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-80-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch adds support for three variants of the RXY instruction format (rxy_a, rxy_b, rxy_c) to the s390 gas assembler via the '.insn' pseudo-mnemonic. These variants were introduced in different IBM processor generations (z990, z10, z17). The changes include updates to opcode definitions and test cases.
