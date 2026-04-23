---
project: glibc
subsystem: tests
patch_id: null
tags:
- glibc
- tests
- nptl
- makefile
- dead code
discussion_id: 20260421143804.3933020-7-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 6/8] tests: nptl: Remove unused code from makefile'
headline: 'Tests: nptl: Remove unused code from makefile'
tldr: Removes unused code related to a non-existent test from the nptl Makefile.
stakes: Removing dead code simplifies the glibc build system and reduces the risk
  of future errors or confusion.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Removes dead code, improving maintainability.
- No functional impact as the code was already unused.
- Reduces the size and complexity of the Makefile.
exchanges: []
primer_expert: This patch removes the unused test `tst-pthread-proc-maps` and its
  associated environment variables (`tst-pthread-proc-maps-ENV`) and arguments (`tst-pthread-proc-maps-ARGS`)
  from `nptl/Makefile`. The removed code configures the `glibc.malloc.arena_max` and
  `glibc.malloc.mmap_threshold` tunables. The file in question is `nptl/Makefile`.
primer_general: The `nptl` (Native POSIX Thread Library) in glibc provides the standard
  C interface for creating and managing threads. The `nptl/Makefile` defines how the
  tests for this library are built and executed.  This patch removes code related
  to a test that no longer exists. The removed code also configured glibc tunables,
  which are runtime options that affect how glibc behaves.
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

This patch removes unused code related to a test named `tst-pthread-proc-maps` from the `nptl/Makefile`. The test does not exist, and the corresponding environment variable and arguments are no longer needed. Removing this dead code cleans up the Makefile and prevents potential issues.
