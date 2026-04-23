---
project: glibc
subsystem: tests
patch_id: null
tags:
- glibc
- tests
- misc
- tunables
- makefile
discussion_id: 20260421143804.3933020-5-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 4/8] tests: misc: Use new tunable handling'
headline: 'Tests: Misc: Use new tunable handling'
tldr: Updates the misc tests to use the new tunable handling mechanism.
stakes: Using a consistent approach to handling tunables improves the maintainability
  and readability of glibc tests.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Modernizes the tunable handling in the `misc` tests.
- Ensures consistency with other parts of the glibc test suite.
- May require adjustments to test infrastructure if it relies on the old tunable handling
  method.
exchanges: []
primer_expert: This patch updates `misc/Makefile` and `sysdeps/unix/sysv/linux/Makefile`
  to use the new tunable handling mechanism.  Specifically, it changes how the `GLIBC_TUNABLES`
  environment variable is set for the `tst-syslog-long-progname` and `tst-rseq-disable`
  tests.  This is part of a larger effort to standardize how tunables are managed
  in glibc tests.
primer_general: glibc tunables are runtime configuration options that allow users
  to adjust the behavior of the library without recompilation. Tests often need to
  manipulate these tunables to ensure proper function under different configurations.
  This patch updates the way those tunables are set in the `misc` directory's tests
  using the new `TUNABLES +=` syntax instead of the older `GLIBC_TUNABLES` assignment
  in the Makefile.
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

This patch updates the `misc/Makefile` and `sysdeps/unix/sysv/linux/Makefile` files to use the new tunable handling mechanism. It replaces the direct assignment of `GLIBC_TUNABLES` with the `TUNABLES +=` syntax for setting tunables in the `tst-syslog-long-progname` and `tst-rseq-disable` tests.
