---
project: glibc
subsystem: tests
patch_id: null
tags:
- tests
- nptl
- makefile
- cleanup
discussion_id: 20260421143804.3933020-7-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 6/8] tests: nptl: Remove unused code from makefile'
headline: 'Tests: nptl: Remove unused code from makefile'
tldr: Removes unused code related to the non-existent tst-pthread-proc-maps test from
  the nptl Makefile.
stakes: Simplifies the build system by removing unnecessary definitions, improving
  maintainability.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges:
- author: Yury Khrustalev <yury.khrustalev@arm.com>
  role: proposer
  position: States that there is no test named tst-pthread-proc-maps.
  quote: There is no test named tst-pthread-proc-maps.
primer_expert: This patch cleans up the `nptl/Makefile` by removing stale definitions
  related to a test, `tst-pthread-proc-maps`, that no longer exists.  This removes
  associated `GLIBC_TUNABLES` and argument settings that were no longer used.
primer_general: This patch cleans up the `nptl` (Native POSIX Thread Library) build
  configuration in glibc by removing settings for a test that doesn't exist anymore.
  This simplifies the build process and makes the configuration easier to understand.
series_id: 'glibc:tests: nptl: remove unused code from makefile'
series_role: reply
series_parts:
- title: 'tests: nptl: Remove unused code from makefile'
  url: https://inbox.sourceware.org/libc-alpha/b426b244-d2a5-4275-ad95-c66c7e8f2189@linaro.org
  n: 6
  total: 8
url: https://inbox.sourceware.org/libc-alpha/20260421143804.3933020-7-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-21'
---

This patch removes unused code from the `nptl/Makefile`. The removed code was related to a test named `tst-pthread-proc-maps`, which does not exist.
