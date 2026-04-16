---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260415205905.1257892-3-samuel.thibault@ens-lyon.org
source_type: public_inbox
title: '[hurd,commited 2/3] hurd: __adjtime(): struct timeval and time_value_t are
  not identical.'
proposer: Samuel Thibault <samuel.thibault@ens-lyon.org>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260415205905.1257892-3-samuel.thibault@ens-lyon.org
bugzilla_url: null
date: '2026-04-15'
---

From: Michael Kelly <mike@weatherwax.co.uk>

'struct timeval' and 'struct time_value' have different types for the
microseconds component: int and long int. Casting one to the other
leads to negative 
