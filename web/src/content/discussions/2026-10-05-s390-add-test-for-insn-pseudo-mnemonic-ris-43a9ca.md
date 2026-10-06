---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- testing
- assembler
discussion_id: 20261005153947.363053-66-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 18/46] s390: Add test for .insn pseudo-mnemonic ris'
headline: 's390: Add test for .insn pseudo-mnemonic ris'
tldr: Adds a test case for the .insn ris pseudo-mnemonic in the s390 assembler.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Adds test cases for the .insn ris pseudo-mnemonic in gas/testsuite/gas/s390/zarch-operands.d
    and gas/testsuite/gas/s390/zarch-operands.s.
  quote: null
primer_expert: This patch adds a test for the `.insn ris` pseudo-mnemonic in the GNU
  Assembler for the s390 architecture. It verifies the correct disassembly and assembly
  of the `cib` instruction using the RIS format, ensuring consistency with the instruction
  set architecture.
primer_glossary: []
series_id: 'binutils:s390: add test for .insn pseudo-mnemonic ris'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-66-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch adds test cases for the .insn ris pseudo-mnemonic to the s390 assembler's test suite. It specifically targets the zarch-operands.d and zarch-operands.s files, including a new test for the 'cib' instruction.
