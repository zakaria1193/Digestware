---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416092751.11653-1-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH 0/2] malloc: introduce ifuncs for malloc functions'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416092751.11653-1-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

See commit message for details. In a nutshell, we want to add ifucs
for the functions related to the malloc API (on targets that support
ifuncs). This will allow to add alternative (e.g. target-specif
