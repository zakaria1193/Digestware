---
project: glibc
subsystem: tests
patch_id: null
tags:
- tests
- nptl
- tunables
discussion_id: 20260421143804.3933020-6-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 5/8] tests: nptl: Use new tunable handling'
headline: 'Tests: nptl: Use new tunable handling'
tldr: Migrates the nptl tests to use the new tunable handling mechanism.
stakes: Standardizes the tunable handling across the nptl tests.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges:
- author: Yury Khrustalev <yury.khrustalev@arm.com>
  role: proposer
  position: States that new way of handling test tunables are used in the nptl folder.
  quote: Use new way of handling test tunables in the nptl folder.
primer_expert: This patch converts the `nptl/` tests to use the new tunable handling
  mechanism.  The key change is in the `sysdeps/pthread/Makefile`, where the `GLIBC_TUNABLES`
  environment variable assignment is replaced with the `*_TUNABLES +=` syntax.
primer_general: This patch updates the way the `nptl` (Native POSIX Thread Library)
  tests are configured in glibc. It uses a new method for setting test parameters
  (tunables), bringing the `nptl` tests in line with other parts of the glibc test
  suite.
series_id: 'glibc:tests: nptl: use new tunable handling'
series_role: reply
series_parts:
- title: 'tests: nptl: Use new tunable handling'
  url: https://inbox.sourceware.org/libc-alpha/16a9aeea-6826-4f1c-8979-b21baa042ea0@linaro.org
  n: 5
  total: 8
url: https://inbox.sourceware.org/libc-alpha/20260421143804.3933020-6-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-21'
---

This patch updates the `nptl` tests to use the new tunable handling mechanism, by replacing the `GLIBC_TUNABLES` environment variable assignment with the `*_TUNABLES +=` syntax in `sysdeps/pthread/Makefile`.
