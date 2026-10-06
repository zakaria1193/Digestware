---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- testing
- testability
discussion_id: 20261005153947.363053-55-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 07/46] s390: Position independent .insn test verification patterns'
headline: 's390: Position independent .insn test verification patterns'
tldr: Makes s390 .insn test verification patterns position independent and adds tests
  for optional padding NOPs.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves test suite maintainability by enabling alphabetical ordering.
- Adds coverage for padding NOPs, increasing robustness.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Modifies s390 .insn test patterns to be position-independent and adds
    tests for optional padding NOPs.
  quote: 'This enables to insert new .insn pseudo-mnemonic tests in alphabetical

    order.


    While at it also test for an optional trailing padding nop.'
primer_expert: This change focuses on improving the test suite for the s390 assembler's
  `.insn` directive. By making the disassembly verification patterns in `esa-operands.d`
  and `zarch-operands.d` position-independent (using regex like `.*:` instead of fixed
  offsets), it simplifies test maintenance and organization. Additionally, it introduces
  tests to cover the scenario where a padding NOP instruction might follow an instruction
  encoded via `.insn`.
primer_glossary:
- term: .insn
  definition: An assembler directive used to specify machine instructions directly,
    often with pseudo-mnemonics.
- term: position independent
  definition: Code or data that can run or be loaded at any memory address without
    modification. In this context, it refers to test patterns that do not rely on
    specific byte offsets.
- term: NOP
  definition: No Operation instruction, which performs no meaningful operation and
    is often used for padding or timing.
series_id: 'binutils:s390: position independent .insn test verification patterns'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005153947.363053-55-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch makes the verification patterns in the s390 `.insn` test suites position-independent, allowing new tests to be inserted alphabetically. It also adds tests to verify the handling of an optional trailing padding NOP (No Operation) instruction. The changes affect the `esa-operands.d` and `zarch-operands.d` files within the gas test suite.
