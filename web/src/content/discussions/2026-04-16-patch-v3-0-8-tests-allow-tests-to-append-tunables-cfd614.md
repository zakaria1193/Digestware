---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416143027.1881673-1-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v3 0/8] tests: Allow tests to append tunables'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416143027.1881673-1-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

The commit message in the 1st patch explains why and how. We plan
to use ability to combine test tunables to validate memory tagging
implementation in malloc: this will required added existing test
tu
