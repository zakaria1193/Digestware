---
project: binutils
subsystem: s390
patch_id: null
tags:
- binutils
- gas
- s390
- assembler
- testing
discussion_id: 20261005153947.363053-94-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 46/46] s390: Add test for .insn pseudo-mnemonic vsi'
headline: 's390: Add test for .insn pseudo-mnemonic vsi'
tldr: Adds a test case for the VSI instruction format using the .insn pseudo-mnemonic
  in the s390 assembler.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves test coverage for VSI instructions.
- No functional change, only verification.
exchanges: []
primer_expert: This is a test-only patch for the s390 assembler's `.insn` directive
  support. It adds specific test cases in `gas/testsuite/gas/s390/zarch-operands.d`
  and `.s` to cover the VSI (Vector Scalar Integer) instruction format. This ensures
  that instructions using the VSI format can be correctly assembled and disassembled
  via the `.insn` pseudo-mnemonic, verifying the implementation's accuracy.
primer_glossary:
- term: .insn
  definition: An assembler pseudo-mnemonic that allows embedding raw machine instructions
    using their format and opcode.
- term: pseudo-mnemonic
  definition: An assembler directive that represents a machine instruction or a sequence
    of instructions using a symbolic name.
- term: s390
  definition: IBM's mainframe and enterprise server architecture.
- term: VSI format
  definition: A specific instruction encoding format for the s390 architecture, likely
    related to vector operations.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    component.
series_id: 'binutils:s390: add test for .insn pseudo-mnemonic vsi'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-94-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch adds new test cases to the s390 assembler's testsuite for the VSI instruction format when used with the `.insn` pseudo-mnemonic. The tests are added to `zarch-operands.d` and `zarch-operands.s` to verify correct assembly and disassembly of VSI instructions.
