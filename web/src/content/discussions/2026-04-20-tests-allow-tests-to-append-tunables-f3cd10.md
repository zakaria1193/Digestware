---
project: glibc
subsystem: tests
patch_id: null
tags:
- tests
- glibc
- Makefile
- tunables
discussion_id: aeYvrv1oo9r1qN5I@arm.com
source_type: public_inbox
title: 'Re: [PATCH v3 1/8] tests: Allow tests to append tunables'
headline: 'tests: Allow tests to append tunables'
tldr: The author retracts a suggestion to introduce a new macro for joining strings
  with colons in Makefiles, opting to use existing methods instead.
stakes: Minor change to Makefile readability and maintainability within the glibc
  test suite.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Readability vs. conciseness of Makefiles.
- Consistency with existing code vs. introducing new patterns.
primer_expert: This thread discusses Makefile style within the glibc test suite. The
  specific point is whether to introduce a new macro (`colon-join`) to simplify joining
  strings with colons. The author ultimately decides against it, favoring the existing
  `$(subst $(empty) ,:,$(strip $(1)))` pattern for consistency. This reflects a micro-optimization
  of Makefile readability within the glibc testing infrastructure.
primer_general: The glibc test suite uses Makefiles to automate the process of building
  and running tests. Makefiles contain macros, which are named abbreviations for commonly
  used strings. This discussion revolves around the style and readability of those
  Makefiles, specifically how to join strings together using a colon as a separator.
  The author is considering whether to introduce a new macro to make this process
  more concise, but ultimately decides against it to maintain consistency with existing
  code.
series_id: 'glibc:tests: allow tests to append tunables'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/aeYvrv1oo9r1qN5I@arm.com
bugzilla_url: null
date: '2026-04-20'
---

The author discusses a suggestion made by Andreas Schwab to use an existing macro for joining strings with colons in Makefiles. The author initially proposed a new macro but now suggests sticking with the existing `$(subst $(empty) ,:,$(strip $(FOO)))` pattern for consistency.
