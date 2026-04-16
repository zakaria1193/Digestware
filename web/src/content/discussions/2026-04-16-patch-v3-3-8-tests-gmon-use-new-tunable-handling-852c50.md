---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416143027.1881673-4-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v3 3/8] tests: gmon: Use new tunable handling'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416143027.1881673-4-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

Use new way of handling test tunables in the gmon folder.
---
 gmon/Makefile | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)

diff --git a/gmon/Makefile b/gmon/Makefile
index 7a8acda4fe..2a1
