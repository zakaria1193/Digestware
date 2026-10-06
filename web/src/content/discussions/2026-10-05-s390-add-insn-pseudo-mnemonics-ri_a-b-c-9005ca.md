---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- pseudo-mnemonic
- instruction-format
discussion_id: 20261005153947.363053-63-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 15/46] s390: Add .insn pseudo-mnemonics ri_a/b/c'
headline: 's390: Add .insn pseudo-mnemonics ri_a/b/c'
tldr: Adds support for RI-a, RI-b, and RI-c pseudo-mnemonics for s390 architecture.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Expands the assembler's instruction set for s390.
- Maintains consistency by using the existing minimum architecture level for RI.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Adds support for RI-a, RI-b, and RI-c pseudo-mnemonics, sharing the base
    RI minimum architecture level and including tests.
  quote: 'Instruction format RI, including its variants RI-a/b/c, predate

    IBM z900.  Therefore use the .insn ri minimum architecture/CPU level

    for all variants.'
primer_expert: This patch extends the s390 assembler's support for the `.insn` directive
  by adding pseudo-mnemonics for RI-a, RI-b, and RI-c instruction formats. These are
  variants of the Relative ISTRUCTION (RI) format, which has existed since before
  the IBM z900. Consequently, these variants do not impose stricter architecture level
  requirements than the base RI format. The changes include updates to `s390-opc.c`
  and `gas/testsuite/gas/s390/`.
primer_glossary:
- term: RI
  definition: A s390 instruction format, typically involving register and immediate
    operands.
- term: RI-a/b/c
  definition: Variants of the RI instruction format.
- term: .insn
  definition: An assembler directive used to specify machine instructions directly,
    often with pseudo-mnemonics.
series_id: 'binutils:s390: add .insn pseudo-mnemonics ri_a/b/c'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-63-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch adds support for the RI-a, RI-b, and RI-c instruction formats on the s390 architecture using the `.insn` pseudo-mnemonic. These formats predate the IBM z900, so they share the same minimum architecture/CPU level as the base RI format. The changes include updating opcode definitions, adding comments to ESA/390 tests, and new test cases for z/Architecture.
