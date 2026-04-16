---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260415205905.1257892-1-samuel.thibault@ens-lyon.org
source_type: public_inbox
title: '[hurd,commited 0/3] hurd: Support for adjtime(NULL, &olddelta)'
proposer: Samuel Thibault <samuel.thibault@ens-lyon.org>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260415205905.1257892-1-samuel.thibault@ens-lyon.org
bugzilla_url: null
date: '2026-04-15'
---

This adds support for passing NULL as first argument of adjtime.

Michael Kelly (3):
  hurd: Make adjtime reject out-of-range tv_usec values
  hurd: __adjtime(): struct timeval and time_value_t are no
