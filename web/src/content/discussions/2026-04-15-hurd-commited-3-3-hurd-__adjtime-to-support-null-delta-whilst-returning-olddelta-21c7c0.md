---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260415205905.1257892-4-samuel.thibault@ens-lyon.org
source_type: public_inbox
title: '[hurd,commited 3/3] hurd: __adjtime() to support NULL delta whilst returning
  olddelta.'
proposer: Samuel Thibault <samuel.thibault@ens-lyon.org>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260415205905.1257892-4-samuel.thibault@ens-lyon.org
bugzilla_url: null
date: '2026-04-15'
---

From: Michael Kelly <mike@weatherwax.co.uk>

This is required to obtain the remaining time of day adjustment
without altering the required adjustment.
Message-ID: <20260415180318.109742-4-mike@weather
