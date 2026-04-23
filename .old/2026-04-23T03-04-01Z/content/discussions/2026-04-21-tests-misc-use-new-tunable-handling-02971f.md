---
project: glibc
subsystem: tests
patch_id: null
tags:
- tests
- misc
- tunables
discussion_id: 20260421143804.3933020-5-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 4/8] tests: misc: Use new tunable handling'
headline: 'Tests: misc: Use new tunable handling'
tldr: Migrates the misc tests to use the new tunable handling mechanism.
stakes: Standardizes the tunable handling across the misc tests.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges:
- author: Yury Khrustalev <yury.khrustalev@arm.com>
  role: proposer
  position: States that new way of handling test tunables are used in the misc folder.
  quote: Use new way of handling test tunables in the misc folder.
primer_expert: This patch migrates the `misc/` tests to use the new tunable handling
  mechanism.  The key change is in the `Makefile`s, where the `GLIBC_TUNABLES` environment
  variable assignment is replaced with the `*_TUNABLES +=` syntax.
primer_general: This patch updates the way the `misc` tests are configured in glibc.
  It uses a new method for setting test parameters (tunables), bringing the `misc`
  tests in line with other parts of the glibc test suite.
series_id: 'glibc:tests: misc: use new tunable handling'
series_role: reply
series_parts:
- title: 'tests: misc: Use new tunable handling'
  url: https://inbox.sourceware.org/libc-alpha/c505509c-7c8a-4dad-bf59-03ac6be6913a@linaro.org
  n: 4
  total: 8
url: https://inbox.sourceware.org/libc-alpha/20260421143804.3933020-5-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-21'
---

This patch updates the `misc` tests to use the new tunable handling mechanism, by replacing the `GLIBC_TUNABLES` environment variable assignment with the `*_TUNABLES +=` syntax in `misc/Makefile` and `sysdeps/unix/sysv/linux/Makefile`.
