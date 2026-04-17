---
project: glibc
subsystem: stdio-common
patch_id: null
tags:
- stdio
- scanf
- vfscanf
- regression test
- security
discussion_id: 520d0e06-a5c4-49ec-a5cc-f8057d8f89f9@redhat.com
source_type: public_inbox
title: 'Re: [PATCH v5 1/3] stdio-common: Add regression test [BZ #34008]'
headline: Add regression test for scanf %mc buffer overflow
tldr: This patch adds a regression test for a buffer overflow vulnerability in scanf's
  %mc format specifier.
stakes: This test ensures that a previously identified buffer overflow vulnerability
  is not reintroduced in future glibc versions.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 7
sentiment_rationale: Adding a regression test is a positive step, but copyright and
  code style feedback prevent a higher score.
technical_tradeoffs:
- Adds a new test case to the test suite.
- Requires additional dependencies for the test environment (MALLOC_CHECK_, LD_PRELOAD).
series_id: 'glibc:stdio-common: add regression test [bz #34008]'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/520d0e06-a5c4-49ec-a5cc-f8057d8f89f9@redhat.com
bugzilla_url: null
date: '2026-04-17'
---

A regression test is being added to `stdio-common` to verify the fix for bug #34008, which involves a buffer overflow in `vfscanf` with the `%Nmc` format specifier. The test is confirmed to fail before the fix and pass after. A copyright correction is requested.
