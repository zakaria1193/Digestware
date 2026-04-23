---
project: glibc
subsystem: tests
patch_id: null
tags:
- tests
- BTI
- GCS
- tunables
discussion_id: 20260421143804.3933020-9-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 8/8] tests: misc: Use new tunable handling for BTI and GCS tests'
headline: 'Tests: misc: Use new tunable handling for BTI and GCS tests'
tldr: Uses the new tunable handling mechanism for BTI and GCS tests, fixing failures
  when the ambient GLIBC_TUNABLES variable is used with the aarch64_gcs tunable.
stakes: Ensures correct behavior of BTI and GCS tests, particularly when used with
  ambient tunables, improving the reliability of these security features.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges: []
primer_expert: This patch converts the BTI/GCS tests in `misc/` to use the newly introduced
  tunable handling mechanism.  It resolves a bug where these tests would fail if the
  `GLIBC_TUNABLES` environment variable was set globally (ambiently) with the `aarch64_gcs`
  tunable. The changes primarily involve Makefile modifications.
primer_general: This patch updates the testing configuration for BTI (Branch Target
  Identification) and GCS (Guard Control Stack) features in glibc.  It uses a new
  system for managing test configurations (tunables).  The patch also fixes a problem
  where these tests would fail if the `GLIBC_TUNABLES` environment variable was set
  globally, ensuring that the tests run correctly in more environments.
series_id: 'glibc:tests: misc: use new tunable handling for bti and gcs tests'
series_role: reply
series_parts:
- title: 'tests: misc: Use new tunable handling for BTI and GCS tests'
  url: https://inbox.sourceware.org/libc-alpha/df59daa8-d09f-45d8-950d-84df481f41ae@linaro.org
  n: 8
  total: 8
url: https://inbox.sourceware.org/libc-alpha/20260421143804.3933020-9-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-21'
---

This patch updates the BTI and GCS tests in the `misc` directory to use the new tunable handling mechanism. It also fixes issues that caused tests to fail when the ambient `GLIBC_TUNABLES` variable was used with the `aarch64_gcs` tunable.
