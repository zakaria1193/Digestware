---
project: glibc
subsystem: tests
patch_id: null
tags:
- tests
- tunables
- memory tagging
- GCS
- BTI
discussion_id: 20260421143804.3933020-1-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 0/8] tests: Allow tests to append tunables'
headline: 'Tests: Allow tests to append tunables'
tldr: Allows tests to append tunables, enabling validation of memory tagging and increasing
  testing coverage for GCS and BTI support.
stakes: Extends testing capabilities, improving code quality and enabling testing
  for new features like memory tagging and GCS/BTI support.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in makefiles due to new tunable handling logic.
- Potential for conflicts if different parts of the test setup try to modify the same
  tunables in incompatible ways.
exchanges: []
primer_expert: Glibc's testing framework utilizes "tunables" to modify runtime behavior
  during tests. This series enhances the framework by allowing tests to append to
  existing tunables.  Specifically, it supports combining test-specific tunables with
  the `memtag` tunable for memory tagging validation, and enables broader testing
  of GCS/BTI features by combining ambient tunables. This involves modifications to
  Makefiles and test configurations.
primer_general: Glibc's testing framework uses configurable parameters called "tunables"
  to control how tests are executed. This allows developers to test different scenarios
  and configurations. This patch series extends this functionality by making it possible
  for tests to add their own tunables to the existing set, rather than replacing them.
  This is useful for testing new features like memory tagging, which requires combining
  multiple tunable settings. It also improves testing coverage for security features
  like GCS and BTI by making it easier to enable them during tests.
series_id: 'glibc:tests: allow tests to append tunables'
series_role: cover
series_parts:
- title: 'tests: Allow tests to append tunables'
  url: https://inbox.sourceware.org/libc-alpha/20260421143804.3933020-2-yury.khrustalev@arm.com
  n: 1
  total: 8
- title: 'tests: Allow tests to append tunables'
  url: https://inbox.sourceware.org/libc-alpha/aeeMLAbiZ2VPFBDO@arm.com
  n: 1
  total: 8
- title: 'tests: Allow tests to append tunables'
  url: https://inbox.sourceware.org/libc-alpha/f44915c8-d07e-4a3d-b722-2a886c1010b2@linaro.org
  n: 1
  total: 8
- title: 'tests: Allow tests to append tunables'
  url: https://inbox.sourceware.org/libc-alpha/aeYvrv1oo9r1qN5I@arm.com
  n: 1
  total: 8
url: https://inbox.sourceware.org/libc-alpha/20260421143804.3933020-1-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-21'
---

This patch series allows tests to append tunables, facilitating the validation of memory tagging implementation in malloc. It also significantly increases testing coverage for GCS (Guard Control Stack) and BTI (Branch Target Identification) support by enabling the addition of existing test tunables to the memtag tunable. The changes include makefile modifications to support the new tunable handling.
