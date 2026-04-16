---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416143027.1881673-8-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v3 7/8] tests: time: Use new tunable handling'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416143027.1881673-8-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

Use new way of handling test tunables in the time folder.
---
 time/Makefile | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/time/Makefile b/time/Makefile
index 43708b0856..b28471c
