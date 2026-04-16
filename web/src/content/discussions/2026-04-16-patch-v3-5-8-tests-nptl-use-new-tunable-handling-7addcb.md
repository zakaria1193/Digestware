---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416143027.1881673-6-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v3 5/8] tests: nptl: Use new tunable handling'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416143027.1881673-6-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

Use new way of handling test tunables in the nptl folder.
---
 sysdeps/pthread/Makefile | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/sysdeps/pthread/Makefile b/sysdeps/pthread/M
