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
discussion_id: 20261005153947.363053-91-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 43/46] s390: Add .insn pseudo-mnemonics vrs_a/b/c/d'
headline: 's390: Add .insn pseudo-mnemonics vrs_a/b/c/d'
tldr: Add support for s390 VRS instruction variants using .insn.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch introduces support for four variations of the VRS instruction
  format (vrs_a through vrs_d) in the s390 GNU Assembler (gas) using the '.insn' pseudo-mnemonic.
  It defines these formats, including operand orderings, in opcodes/s390-opc.c and
  adds corresponding tests to gas/testsuite/gas/s390/zarch-operands.d/.s, referencing
  their introduction on specific IBM z/Architecture processors.
primer_glossary:
- term: .insn
  definition: A GNU assembler directive that allows embedding raw instruction bytes
    or defining pseudo-mnemonics for specific instruction formats.
- term: pseudo-mnemonic
  definition: An assembly language construct that represents a machine instruction,
    potentially with operands that are not direct encodings of machine code but are
    processed by the assembler.
- term: VRS
  definition: A specific instruction format in the s390 architecture, with variants
    introduced across different processor generations.
- term: z13, z14
  definition: IBM mainframe processor generations that introduced different versions
    of the VRS instruction format.
series_id: 'binutils:s390: add .insn pseudo-mnemonics vrs_a/b/c/d'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-91-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch adds support for four variants of the VRS instruction format (vrs_a, vrs_b, vrs_c, and vrs_d) to the s390 gas assembler using the '.insn' pseudo-mnemonic. These variants were introduced in IBM processor generations z13 and z14. The changes include updates to opcode definitions, documentation, and test suites.
