---
project: glibc
subsystem: tests
patch_id: null
tags:
- glibc
- tests
- makefile
- build system
- code style
discussion_id: aeYvrv1oo9r1qN5I@arm.com
source_type: public_inbox
title: 'Re: [PATCH v3 1/8] tests: Allow tests to append tunables'
headline: 'Tests: Use existing macro for joining with colons.'
tldr: The author decided to use the existing '$(subst $(empty) ,:,$(strip $(FOO)))'
  macro instead of introducing a new one for joining with colons.
stakes: Simplifies the patch by avoiding the introduction of a new macro, maintaining
  consistency with existing code.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Avoids introducing a new macro, reducing code complexity.
- Maintains consistency with existing code in the Makefiles.
- No functional changes to the tests themselves.
primer_expert: This patch series modifies the glibc test suite Makefiles.  The discussion
  revolves around joining lists of strings with colons.  The author initially considered
  introducing a new macro for this purpose but ultimately decided to reuse the existing
  `$(subst $(empty) ,:,$(strip $(FOO)))` pattern, which achieves the same result.
primer_general: 'Glibc includes a comprehensive test suite to ensure the correctness
  and stability of the library. These tests are often configured and run using Makefiles.  This
  discussion is about a stylistic choice in the test suite''s Makefiles: specifically,
  how to join a list of strings with colons to create a colon-separated string.  The
  author is simplifying the patch by sticking with an existing approach rather than
  introducing a new one.'
series_id: 'glibc:tests: allow tests to append tunables'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/aeYvrv1oo9r1qN5I@arm.com
bugzilla_url: null
date: '2026-04-20'
---

The author decided against introducing a new macro for joining elements with colons in the test suite Makefiles. They will instead use the existing '$(subst $(empty) ,:,$(strip $(FOO)))' macro, promoting code reuse and reducing complexity.
