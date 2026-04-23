---
project: glibc
subsystem: elf
patch_id: null
tags:
- ld.so.cache
- caching
- performance
- security
- tunables
discussion_id: d3f4110e0e542a0b045e278c07573775a4d5a412.1776449736.git.dj@redhat.com
source_type: public_inbox
title: '[PATCH v7 2/4] Add system-wide tunables: cache ld.so.cache'
headline: 'Add system-wide tunables: cache ld.so.cache'
tldr: Caches ld.so.cache in memory, re-reading only on changes, enabling more intensive
  security checks and handling cache corruption.
stakes: Improves performance and robustness by caching ld.so.cache, paving the way
  for more intensive security checks without impacting performance significantly.
proposer: DJ Delorie <dj@redhat.com>
consensus: Proposed
outcome: stalled
sentiment_score: 5
sentiment_rationale: This is a complex change with potential performance and security
  implications, so a neutral score is appropriate in the absence of further discussion.
series_id: 'glibc:add system-wide tunables: cache ld.so.cache'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/d3f4110e0e542a0b045e278c07573775a4d5a412.1776449736.git.dj@redhat.com
bugzilla_url: null
date: '2024-02-21'
---

This patch caches the ld.so.cache in memory, re-reading it only when it changes on disk. This allows for more intensive security checks without significantly impacting performance and provides resilience against cache corruption. The load/check logic is broken out to allow independent loading of the cache for purposes like examining extensions.
