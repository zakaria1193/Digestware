---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416143027.1881673-7-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v3 6/8] tests: nptl: Remove unused code from makefile'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416143027.1881673-7-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

There is no test named tst-pthread-proc-maps.
---
 nptl/Makefile | 4 ----
 1 file changed, 4 deletions(-)

diff --git a/nptl/Makefile b/nptl/Makefile
index 85f95dd0cf..02862d1c04 100644
--- a/nptl/Mak
