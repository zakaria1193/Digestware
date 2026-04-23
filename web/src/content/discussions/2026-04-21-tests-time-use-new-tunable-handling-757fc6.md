---
project: glibc
subsystem: tests
patch_id: null
tags:
- glibc
- tests
- tunables
- makefile
discussion_id: 20260421143804.3933020-8-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 7/8] tests: time: Use new tunable handling'
headline: 'Tests: Time: Use new tunable handling'
tldr: Updates the time folder tests to use the new tunable handling mechanism.
stakes: This change simplifies the way tunables are handled in glibc tests, making
  them more consistent and easier to maintain.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Modernizes the tunable handling in the `time` tests.
- Ensures consistency with other parts of the glibc test suite.
- May require adjustments to test infrastructure if it relies on the old tunable handling
  method.
exchanges: []
primer_expert: This patch updates the `time/Makefile` to use the new tunable handling
  mechanism.  Specifically, it changes how the `GLIBC_TUNABLES` environment variable
  is set for the `tst-tzfile-fault` test.  This is part of a larger effort to standardize
  how tunables are managed in glibc tests. The relevant file is `time/Makefile`.
primer_general: glibc tunables are runtime configuration options that allow users
  to adjust the behavior of the library without recompilation. These tunables can
  affect various aspects of glibc, such as memory allocation, threading, and internationalization.  Tests
  often need to manipulate these tunables to ensure proper function under different
  configurations. This patch updates the way those tunables are set in the `time`
  directory's tests by using the new `TUNABLES +=` syntax instead of the older `GLIBC_TUNABLES`
  assignment in the Makefile.
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

The patch modifies the `time/Makefile` to use the new tunable handling mechanism. This involves replacing the `GLIBC_TUNABLES` assignment with the `TUNABLES +=` syntax. The change affects how test tunables are set for the `tst-tzfile-fault` test.
