---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416143027.1881673-2-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v3 1/8] tests: Allow tests to append tunables'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416143027.1881673-2-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

Many tests use Glibc tunables, and the values of the tunables are
provided via the GLIBC_TUNABLES env variable. Tests set it in
makefiles using

  tst-foo-ENV = GLIBC_TUNABLES=tunable=value

This over
