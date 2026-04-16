---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416092751.11653-3-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH 2/2] malloc: introduce ifuncs for malloc functions'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416092751.11653-3-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

Introduce ifuncs and resolvers for functions pertinent to the
malloc interface.

In order to do this, we first rename all core implementations by
adding the '_core' suffix. These functions are suppose
