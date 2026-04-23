---
project: glibc
subsystem: io
patch_id: null
tags:
- io
- fts
- consolidation
- code cleanup
discussion_id: 7ce6d247-0538-4860-90be-5788e1b70782@redhat.com
source_type: public_inbox
title: 'Re: [PATCH 1/3] io: Consolidate fts implementation'
headline: 'io: Consolidate fts implementation'
tldr: This patch consolidates the fts implementation by removing wordsize-64 and arch-specific
  implementations where off_t matches off64_t.
stakes: Reduces code duplication and simplifies maintenance of the fts implementation.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 9
sentiment_rationale: The patch is described as mechanical and has received explicit
  approval from upstream, suggesting a high level of confidence and agreement, pending
  confirmation of its origin.
series_id: 'glibc:io: consolidate fts implementation'
series_role: reply
series_parts:
- title: 'io: Consolidate fts implementation'
  url: https://inbox.sourceware.org/libc-alpha/a4d6a525-ed41-48c1-a08d-c7ee981e9472@linaro.org
  n: 1
  total: 3
- title: 'io: Consolidate fts implementation'
  url: https://inbox.sourceware.org/libc-alpha/20260417132808.235562-2-adhemerval.zanella@linaro.org
  n: 1
  total: 3
url: https://inbox.sourceware.org/libc-alpha/7ce6d247-0538-4860-90be-5788e1b70782@redhat.com
bugzilla_url: null
date: '2026-04-17'
---

This patch consolidates the fts implementation by removing wordsize-64 and arch-specific implementations for ABIs where off_t is the same as off64_t. The fts.c implementation is moved to fts-common.c to simplify the __OFF_T_MATCHES_OFF64_T usage. Upstream has approved the patch and requests that it be pushed if it is a mechanical sync from gnulib.
