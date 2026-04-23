---
project: glibc
subsystem: io
patch_id: null
tags:
- io
- ftw
- consolidation
- code cleanup
discussion_id: a7163076-2196-4180-bbef-da7bc94c119e@redhat.com
source_type: public_inbox
title: 'Re: [PATCH 2/3] io: Consolidate ftw implementation'
headline: 'io: Consolidate ftw implementation'
tldr: This patch consolidates the ftw implementation by removing wordsize-64 and arch-specific
  implementations where off_t matches off64_t.
stakes: Reduces code duplication and simplifies maintenance of the ftw implementation.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 9
sentiment_rationale: The patch is described as mechanical and has received explicit
  approval from upstream, suggesting a high level of confidence and agreement.
series_id: 'glibc:io: consolidate ftw implementation'
series_role: reply
series_parts:
- title: 'io: Consolidate ftw implementation'
  url: https://inbox.sourceware.org/libc-alpha/3aa40b5a-25c2-4640-aef2-17722fe59154@linaro.org
  n: 2
  total: 3
- title: 'io: Consolidate ftw implementation'
  url: https://inbox.sourceware.org/libc-alpha/20260417132808.235562-3-adhemerval.zanella@linaro.org
  n: 2
  total: 3
url: https://inbox.sourceware.org/libc-alpha/a7163076-2196-4180-bbef-da7bc94c119e@redhat.com
bugzilla_url: null
date: '2026-04-17'
---

This patch consolidates the ftw implementation by removing wordsize-64 and arch-specific implementations for ABIs where off_t is the same as off64_t. The ftw.c implementation is moved to ftw-common.c to simplify the __OFF_T_MATCHES_OFF64_T usage.  Upstream has approved the patch and requests that it be pushed.
