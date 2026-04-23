---
project: glibc
subsystem: tests
patch_id: null
tags:
- glibc
- tests
- nptl
- tunables
- makefile
discussion_id: 20260421143804.3933020-6-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 5/8] tests: nptl: Use new tunable handling'
headline: 'Tests: nptl: Use new tunable handling'
tldr: Updates the nptl tests to use the new tunable handling mechanism.
stakes: Consolidating tunable handling makes glibc tests more consistent and easier
  to manage.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Modernizes the tunable handling in the `nptl` tests.
- Ensures consistency with other parts of the glibc test suite.
- May require adjustments to test infrastructure if it relies on the old tunable handling
  method.
exchanges: []
primer_expert: This patch updates `sysdeps/pthread/Makefile` to use the new tunable
  handling mechanism.  Specifically, it changes how the `GLIBC_TUNABLES` environment
  variable is set for the `tst-stack2` test. This is part of a larger effort to standardize
  how tunables are managed in glibc tests. The file is `sysdeps/pthread/Makefile`.
primer_general: glibc tunables are runtime configuration options that allow users
  to adjust the behavior of the library without recompilation. These tunables can
  affect various aspects of glibc, such as memory allocation, threading, and internationalization.  Tests
  often need to manipulate these tunables to ensure proper function under different
  configurations. This patch updates the way those tunables are set in the `nptl`
  (Native POSIX Thread Library) directory's tests.
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

This patch modifies the `sysdeps/pthread/Makefile` to use the new tunable handling mechanism. It replaces the direct assignment of `GLIBC_TUNABLES` with the `TUNABLES +=` syntax for setting the `glibc.rtld.execstack` tunable in the `tst-stack2` test.
