---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- gas
- testing
- assembler
discussion_id: 20261005153947.363053-59-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 11/46] s390: Add test for .insn pseudo-mnemonic e'
headline: 's390: Add test for .insn pseudo-mnemonic e'
tldr: Adds a test case for the .insn e pseudo-mnemonic in the s390 assembler and comments
  existing tests.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Adds a test for .insn e in gas/testsuite/gas/s390/zarch-operands and adds
    comments to existing tests in gas/testsuite/gas/s390/esa-operands.
  quote: null
primer_expert: This patch enhances the test coverage for the s390 GNU Assembler by
  adding a new test case for the `.insn e` pseudo-mnemonic in the z/Architecture test
  suite (`zarch-operands.d/s`). Additionally, it adds comments to the existing ESA/390
  tests for the `.insn e` instruction in `esa-operands.d/s` to clarify their purpose.
primer_glossary:
- term: .insn
  definition: An assembler directive that allows direct insertion of machine instructions
    using their opcode and operands, often used for undefined or specialized instructions.
- term: pseudo-mnemonic
  definition: A symbolic name used in assembly language that corresponds to a machine
    instruction or a sequence of instructions, often used for convenience or to represent
    complex operations.
- term: ESA/390
  definition: Enterprise Systems Architecture/370, an earlier architecture from IBM
    that evolved into z/Architecture.
- term: z/Architecture
  definition: IBM's 64-bit enterprise architecture, an evolution of the System/360
    and System/370 lineage.
series_id: 'binutils:s390: add test for .insn pseudo-mnemonic e'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-59-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch adds a new test case for the '.insn e' pseudo-mnemonic in the s390 GNU Assembler, specifically for the z/Architecture. It also adds comments to the existing tests for the '.insn e' pseudo-mnemonic in the ESA/390 assembler test suite, improving clarity and maintainability of the test suite.
