---
project: glibc
subsystem: tests
patch_id: null
tags:
- glibc
- tests
- gmon
- tunables
- makefile
discussion_id: 20260421143804.3933020-4-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 3/8] tests: gmon: Use new tunable handling'
headline: 'Tests: Gmon: Use new tunable handling'
tldr: Updates the gmon tests to use the new tunable handling mechanism.
stakes: Consistent tunable handling improves test maintainability and reduces potential
  errors.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Modernizes the tunable handling in the `gmon` tests.
- Ensures consistency with other parts of the glibc test suite.
- May require adjustments to test infrastructure if it relies on the old tunable handling
  method.
exchanges: []
primer_expert: This patch updates `gmon/Makefile` to use the new tunable handling
  mechanism.  Specifically, it changes how the `GLIBC_TUNABLES` environment variable
  is set for the `tst-mcount-overflow` test.  This involves updating the way the minimum
  and maximum arc counts are configured for the gmon profiling tool. The file in question
  is `gmon/Makefile`.
primer_general: '`gmon` is a profiling tool included within glibc.  glibc tunables
  are runtime configuration options that allow users to adjust the behavior of the
  library.  Tests often need to manipulate these tunables to ensure proper function
  under different configurations. This patch updates the way those tunables are set
  in the `gmon` directory''s tests by using the new `TUNABLES +=` syntax.'
series_id: 'glibc:tests: gmon: use new tunable handling'
series_role: reply
series_parts:
- title: 'tests: gmon: Use new tunable handling'
  url: https://inbox.sourceware.org/libc-alpha/e68ed7f3-64ea-484d-bab4-bdb2cedd1345@linaro.org
  n: 3
  total: 8
url: https://inbox.sourceware.org/libc-alpha/20260421143804.3933020-4-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies the `gmon/Makefile` to use the new tunable handling mechanism. It replaces the direct assignment of `GLIBC_TUNABLES` with the `TUNABLES +=` syntax for setting the `glibc.gmon.minarcs` and `glibc.gmon.maxarcs` tunables in the `tst-mcount-overflow` test.
