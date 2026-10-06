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
discussion_id: 20261005153947.363053-90-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 42/46] s390: Add .insn pseudo-mnemonics vrr_a/b/c/d/e/f/g/h/i/j/k'
headline: 's390: Add .insn pseudo-mnemonics vrr_a/b/c/d/e/f/g/h/i/j/k'
tldr: Add support for s390 VRR instruction variants using .insn.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch introduces support for eleven variations of the VRR instruction
  format (vrr_a through vrr_k) in the s390 GNU Assembler (gas) using the '.insn' pseudo-mnemonic.
  It defines these formats in opcodes/s390-opc.c and adds corresponding tests to gas/testsuite/gas/s390/zarch-operands.d/.s,
  referencing their introduction on various IBM z/Architecture processors and noting
  optional fields like M4 and I2 introduced in later models.
primer_glossary:
- term: .insn
  definition: A GNU assembler directive that allows embedding raw instruction bytes
    or defining pseudo-mnemonics for specific instruction formats.
- term: pseudo-mnemonic
  definition: An assembly language construct that represents a machine instruction,
    potentially with operands that are not direct encodings of machine code but are
    processed by the assembler.
- term: VRR
  definition: A specific instruction format in the s390 architecture, with various
    sub-types introduced across different processor generations.
- term: z13, z14, z15, z16, z17
  definition: IBM mainframe processor generations that introduced different versions
    or optional fields of the VRR instruction format.
series_id: 'binutils:s390: add .insn pseudo-mnemonics vrr_a/b/c/d/e/f/g/h/i/j/k'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-90-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch adds support for eleven variants of the VRR instruction format (vrr_a through vrr_k) to the s390 gas assembler using the '.insn' directive. These variants were introduced across different IBM processor generations (z13, z14, z15, z16, z17). The changes include updates to opcode definitions, documentation, and test suites.
