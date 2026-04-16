---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260416143027.1881673-3-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v3 2/8] tests: elf: Use new tunable handling'
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260416143027.1881673-3-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-16'
---

Use new way of handling test tunables in the elf folder.
---
 elf/Makefile | 8 ++++----
 1 file changed, 4 insertions(+), 4 deletions(-)

diff --git a/elf/Makefile b/elf/Makefile
index 7f039b5563..c83
