---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- testing
- .insn
discussion_id: 20261005153947.363053-88-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 40/46] s390: Improve test for .insn pseudo-mnemonic ssf'
headline: 's390: Improve test for .insn pseudo-mnemonic ssf'
tldr: Update gas tests for s390 .insn ssf pseudo-mnemonic.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch updates gas testsuite files for s390 to improve test coverage
  for the '.insn ssf' pseudo-mnemonic. It modifies the disassembly definition and
  assembly source files to match expected output for the 'mvcos' instruction.
primer_glossary: []
series_id: 'binutils:s390: improve test for .insn pseudo-mnemonic ssf'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-88-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch improves the test cases for the .insn pseudo-mnemonic ssf in the s390 gas assembler. It adds comments and updates the operand tests in the gas/s390/zarch-operands.d and gas/s390/zarch-operands.s files to better reflect the expected behavior.
