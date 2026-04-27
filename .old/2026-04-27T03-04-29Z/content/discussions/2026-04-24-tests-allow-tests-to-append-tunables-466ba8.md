---
project: glibc
subsystem: tests
patch_id: null
tags:
- glibc
- tests
- tunables
- environment variable
discussion_id: 63fd81e1-b789-4a82-89db-a2f868aaa541@linaro.org
source_type: public_inbox
title: 'Re: [PATCH v4 1/8] tests: Allow tests to append tunables'
headline: 'tests: Allow tests to append tunables'
tldr: Introduces a new `tst-foo-TUNABLES` mechanism in glibc's test suite to allow
  tests to append or override GLIBC_TUNABLES values.
proposer: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
consensus: Under Review
outcome: ready
sentiment_score: null
technical_tradeoffs:
- Increased complexity of the test infrastructure.
- Potential for subtle interactions between ambient and test-specific tunables.
exchanges:
- author: Yury Khrustalev
  role: proposer
  position: Proposes a new `tst-foo-TUNABLES` mechanism to allow tests to append tunables,
    override ambient values, and simplify Makefile code.
  quote: "To address all of this, in this commit we add support for using\nconstructs\
    \ like\n\n  tst-foo-TUNABLES += tunable=value"
- author: Adhemerval Zanella Netto
  role: reviewer
  position: Acknowledges the patch.
  quote: null
primer_expert: This patch modifies glibc's test infrastructure to introduce `tst-foo-TUNABLES`
  and `tst-foo-TUNABLES-only` constructs in Makefiles. These constructs affect how
  the `GLIBC_TUNABLES` environment variable is managed for each test.  The goal is
  to allow tests to modify the environment without completely overwriting existing
  values.  This change affects the test harness rather than core glibc functionality.
primer_general: Glibc's behavior can be customized at runtime using tunables, which
  are set via the `GLIBC_TUNABLES` environment variable.  This patch changes how the
  glibc test suite sets these tunables for individual tests.  The new approach lets
  tests modify existing tunable settings instead of replacing them entirely, providing
  better control and isolation.  This makes the test suite more flexible and robust
  when dealing with different tunable configurations.
series_id: 'glibc:tests: allow tests to append tunables'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/63fd81e1-b789-4a82-89db-a2f868aaa541@linaro.org
bugzilla_url: null
date: '2026-04-24'
---

This patch introduces a new mechanism for handling GLIBC tunables in glibc's test suite.  The new `tst-foo-TUNABLES` construct allows tests to append to or override the `GLIBC_TUNABLES` environment variable, addressing limitations with the existing `tst-foo-ENV` method. This change improves test isolation and makes it easier to manage tunable values for individual tests, and allows ambient GLIBC_TUNABLES to be used unless overridden.
