---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416092751.11653-2-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH 1/2] misc: fix lint-makefiles failures'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416092751.11653-2-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

---
 sysdeps/aarch64/Makefile | 39 ++++++++++++++++++++++++++++-----------
 sysdeps/generic/Makefile | 24 ++++++++++++++++++------
 2 files changed, 46 insertions(+), 17 deletions(-)

diff --git a/sys
