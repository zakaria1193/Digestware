---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260415233038.1875006-1-samuel.thibault@ens-lyon.org
source_type: public_inbox
title: '[hurd,commited] mach: Fix tst-default-domain link'
proposer: Samuel Thibault <samuel.thibault@ens-lyon.org>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260415233038.1875006-1-samuel.thibault@ens-lyon.org
bugzilla_url: null
date: '2026-04-15'
---

It links nisdomain.os directly, which uses __libc_lock_lock, thus
__gsync_wait from libmachuser
---
 sysdeps/mach/Makefile | 1 +
 1 file changed, 1 insertion(+)

diff --git a/sysdeps/mach/Makefile b/s
