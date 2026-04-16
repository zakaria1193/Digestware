---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416143027.1881673-5-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v3 4/8] tests: misc: Use new tunable handling'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416143027.1881673-5-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

Use new way of handling test tunables in the misc folder.
---
 misc/Makefile                    | 4 ++--
 sysdeps/unix/sysv/linux/Makefile | 4 ++--
 2 files changed, 4 insertions(+), 4 deletions(-)

d
