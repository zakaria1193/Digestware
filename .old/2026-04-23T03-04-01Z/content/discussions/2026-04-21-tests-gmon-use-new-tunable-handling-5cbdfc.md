---
project: glibc
subsystem: tests
patch_id: null
tags:
- tests
- gmon
- tunables
discussion_id: 20260421143804.3933020-4-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 3/8] tests: gmon: Use new tunable handling'
headline: 'Tests: gmon: Use new tunable handling'
tldr: Updates the gmon tests to use the new tunable handling mechanism.
stakes: Standardizes the way tunables are handled in gmon tests.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges:
- author: Yury Khrustalev <yury.khrustalev@arm.com>
  role: proposer
  position: States that new way of handling test tunables are used in the gmon folder.
  quote: Use new way of handling test tunables in the gmon folder.
primer_expert: This patch migrates the `gmon/` tests to use the new tunable handling
  mechanism.  The key change is in the `gmon/Makefile`, where the `GLIBC_TUNABLES`
  environment variable assignment is replaced with the `*_TUNABLES +=` syntax.
primer_general: This patch updates how the `gmon` (profiling) tests are configured
  in glibc. It uses a new method for setting test parameters (tunables), bringing
  the `gmon` tests in line with other parts of the glibc test suite.
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

This patch modifies the `gmon` tests to use the new tunable handling mechanism introduced in the preceding patches. This involves replacing the `GLIBC_TUNABLES` environment variable assignment with the `*_TUNABLES +=` syntax in the `gmon/Makefile`.
