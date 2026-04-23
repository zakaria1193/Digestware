---
project: glibc
subsystem: tests
patch_id: null
tags:
- glibc
- tests
- tunables
- makefile
discussion_id: 20260421143804.3933020-5-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 4/8] tests: misc: Use new tunable handling'
headline: 'Tests: Misc: Use new tunable handling'
tldr: Use the new mechanism for setting GLIBC tunables in Makefiles for misc tests.
stakes: Simplifies setting GLIBC tunables in Makefiles for tests.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Improved readability and maintainability of Makefiles.
- More explicit and consistent way of setting GLIBC tunables for tests.
exchanges: []
primer_expert: This patch updates Makefiles under the `misc` test suite to use the
  new `*TUNABLES` Make variable instead of the older `*ENV` form. The test suite uses
  Makefiles to set environment variables to configure the runtime loader and memory
  allocator. This change improves maintainability and consistency across the project.
primer_general: The GNU C Library (glibc) provides a way to tune its behavior through
  environment variables called "tunables". These tunables can control aspects like
  memory allocation, threading, and other low-level system behaviors. This patch modifies
  the Makefiles responsible for building and running tests for glibc, specifically
  in the `misc` directory. It changes the way these tunables are set for the tests,
  moving from a general environment variable (`ENV`) to a dedicated `TUNABLES` variable,
  for clarity and better organization.
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

This patch updates the Makefiles in the misc tests folder to use the new way of handling test tunables, changing from setting tunables in the ENV variable to using the TUNABLES variable.
