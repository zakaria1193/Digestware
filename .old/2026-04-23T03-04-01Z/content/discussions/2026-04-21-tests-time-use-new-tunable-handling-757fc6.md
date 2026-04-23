---
project: glibc
subsystem: tests
patch_id: null
tags:
- tests
- time
- tunables
discussion_id: 20260421143804.3933020-8-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 7/8] tests: time: Use new tunable handling'
headline: 'Tests: time: Use new tunable handling'
tldr: Updates the time tests to use the new tunable handling mechanism.
stakes: Modernizes the time tests' configuration, ensuring consistency with other
  test suites.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges:
- author: Yury Khrustalev <yury.khrustalev@arm.com>
  role: proposer
  position: States that new way of handling test tunables are used in the time folder.
  quote: Use new way of handling test tunables in the time folder.
primer_expert: This patch migrates the `time/` tests to use the new tunable handling
  mechanism.  The key change is in the `Makefile`, where the `GLIBC_TUNABLES` environment
  variable assignment is replaced with the `*_TUNABLES +=` syntax.
primer_general: This patch updates the way the `time` tests are configured in glibc.
  It uses a new method for setting test parameters (tunables), bringing the `time`
  tests in line with other parts of the glibc test suite.
series_id: 'glibc:tests: time: use new tunable handling'
series_role: reply
series_parts:
- title: 'tests: time: Use new tunable handling'
  url: https://inbox.sourceware.org/libc-alpha/25442f68-860a-48ad-be97-57346a39a5a2@linaro.org
  n: 7
  total: 8
url: https://inbox.sourceware.org/libc-alpha/20260421143804.3933020-8-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies the `time` tests to utilize the new tunable handling mechanism introduced in the preceding patches. This involves changes to the `Makefile` to define tunables using the new syntax.
