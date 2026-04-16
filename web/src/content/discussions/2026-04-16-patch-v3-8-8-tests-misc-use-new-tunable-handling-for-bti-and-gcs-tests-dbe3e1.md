---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416143027.1881673-9-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v3 8/8] tests: misc: Use new tunable handling for BTI and GCS tests'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416143027.1881673-9-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

Use new way of handling test tunables for BTI and GCS tests.
---
 sysdeps/unix/sysv/linux/aarch64/Makefile | 129 ++++++++++++-----------
 1 file changed, 65 insertions(+), 64 deletions(-)

diff --git 
