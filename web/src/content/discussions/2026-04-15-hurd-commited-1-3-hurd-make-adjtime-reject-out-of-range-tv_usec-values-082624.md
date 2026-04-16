---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260415205905.1257892-2-samuel.thibault@ens-lyon.org
source_type: public_inbox
title: '[hurd,commited 1/3] hurd: Make adjtime reject out-of-range tv_usec values'
proposer: Samuel Thibault <samuel.thibault@ens-lyon.org>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260415205905.1257892-2-samuel.thibault@ens-lyon.org
bugzilla_url: null
date: '2026-04-15'
---

From: Michael Kelly <mike@weatherwax.co.uk>

---
 sysdeps/mach/hurd/adjtime.c | 7 +++++++
 1 file changed, 7 insertions(+)

diff --git a/sysdeps/mach/hurd/adjtime.c b/sysdeps/mach/hurd/adjtime.c
index
