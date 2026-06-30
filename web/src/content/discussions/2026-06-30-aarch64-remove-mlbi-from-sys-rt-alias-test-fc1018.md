---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- testing
- gas
- ARM
- instructions
discussion_id: 20260630094203.2328048-4-rearnsha@arm.com
source_type: public_inbox
title: '[PATCH v3 3/7] aarch64: remove MLBI from sys-rt-alias test.'
headline: 'aarch64: remove MLBI from sys-rt-alias test.'
tldr: Removes MLBI instruction tests from aarch64 sys-rt-alias test suite.
proposer: Richard Earnshaw <rearnsha@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Removes MLBI instructions from `gas/testsuite/gas/aarch64/sys-rt-alias.d`
  and `.s`. This aligns with the reversion of MLBI support, ensuring tests do not
  cover withdrawn functionality.
primer_general: This change removes specific test cases for the 'MLBI' instruction
  from the binutils test suite for the aarch64 architecture. This is part of an effort
  to clean up or correct the tests, likely related to previous changes concerning
  the MLBI instruction itself. It ensures that the tests accurately reflect what the
  assembler currently supports.
series_id: 'binutils:aarch64: remove mlbi from sys-rt-alias test'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260630094203.2328048-4-rearnsha@arm.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This patch removes references to the MLBI instruction from the `sys-rt-alias.d` and `sys-rt-alias.s` test files for the aarch64 architecture. This is likely related to the broader effort of reverting or reconsidering the inclusion of MLBI instructions, ensuring the test suite accurately reflects the current state of instruction support.
