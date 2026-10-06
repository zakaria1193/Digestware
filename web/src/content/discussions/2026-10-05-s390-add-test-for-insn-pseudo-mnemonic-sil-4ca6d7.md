---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- tests
- assembler
discussion_id: 20261005153947.363053-83-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 35/46] s390: Add test for .insn pseudo-mnemonic sil'
headline: 's390: Add test for .insn pseudo-mnemonic sil'
tldr: Adds gas test cases for the .insn sil pseudo-mnemonic on s390.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Submits patches to add test cases for the .insn sil pseudo-mnemonic in
    the s390 gas assembler.
  quote: "gas/testsuite/\n\t* gas/s390/zarch-operands.d: Add test for .insn sil.\n\
    \t* gas/s390/zarch-operands.s: Likewise."
primer_expert: This patch adds tests for the '.insn sil' pseudo-mnemonic in the s390
  GNU Assembler (gas). It extends the zarch-operands test suite by adding definitions
  and expected outputs for this specific instruction format, ensuring correct assembly
  and disassembly.
primer_glossary: []
series_id: 'binutils:s390: add test for .insn pseudo-mnemonic sil'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-83-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch adds test cases for the .insn sil pseudo-mnemonic to the gas assembler's test suite for the s390 architecture. The changes update the disassembly and assembly test files to include specific examples for this mnemonic, ensuring proper assembly and disassembly behavior.
