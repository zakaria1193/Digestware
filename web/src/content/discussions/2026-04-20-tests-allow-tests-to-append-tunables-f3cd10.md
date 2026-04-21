---
project: glibc
subsystem: tests
patch_id: null
tags:
- glibc
- tests
- tunables
- makefile
- macro
discussion_id: aeYvrv1oo9r1qN5I@arm.com
source_type: public_inbox
title: 'Re: [PATCH v3 1/8] tests: Allow tests to append tunables'
headline: 'tests: Allow tests to append tunables'
tldr: Decides against introducing new macros for string concatenation in Makefiles
  and will instead use the existing `$(subst $(empty) ,:,$(strip $(FOO)))` construct.
stakes: This affects how test tunables are configured and managed, potentially impacting
  test execution and results.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Avoiding new macros reduces code complexity but may result in less readable Makefiles.
- Using the existing method ensures consistency but may be less efficient.
- The decision impacts the maintainability and clarity of the test infrastructure.
exchanges:
- author: Yury Khrustalev <yury.khrustalev@arm.com>
  role: proposer
  position: States that no new macros will be added and the existing method, '$(subst
    $(empty) ,:,$(strip $(FOO)))', will be used.
  quote: 'Actually, after looking into it I think that we shouldn''t add any new

    macros and instead use ''$(subst $(empty) ,:,$(strip $(FOO)))'' in this

    patch series.'
primer_expert: This patch modifies the glibc test infrastructure to allow appending
  tunables to test configurations.  Tunables are parameters that can be adjusted to
  modify the behavior of a test. The discussion concerns Makefile macro usage for
  string manipulation, specifically how to join a list of strings with a colon separator,
  and the decision to avoid introducing new macros for this purpose.
primer_general: glibc, the GNU C Library, has an extensive test suite to ensure its
  correctness and stability. Tests often require specific configurations, which can
  be adjusted using 'tunables'. This patch allows tests to append to existing tunables,
  providing more flexibility in test configuration. The discussion focuses on how
  this is implemented in the Makefiles that control the build and execution of the
  tests, and a design choice was made to avoid introducing new Makefile macros.
series_id: 'glibc:tests: allow tests to append tunables'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/aeYvrv1oo9r1qN5I@arm.com
bugzilla_url: null
date: '2026-04-20'
---

The patch series aims to allow tests to append tunables. The discussion revolves around the best way to concatenate elements in a list using a colon within the Makefiles. The author initially proposed introducing a new macro but ultimately decided against it, opting to use the existing method.
