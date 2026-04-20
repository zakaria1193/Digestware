---
project: glibc
subsystem: sysdeps
patch_id: null
tags:
- glibc
- LA32
- compiler warning
- code cleanup
discussion_id: 20260323071657.1505765-1-mengqinggang@loongson.cn
source_type: public_inbox
title: 'Re: [PATCH] Fix ''cbaud_to_speed'' defined but not used on LA32'
headline: 'Request to commit: Fix unused ''cbaud_to_speed'' on LA32'
tldr: Mengqinggang asks for commit of a patch fixing an unused `cbaud_to_speed` definition,
  which has already received LGTM and a review.
stakes: Resolving compiler warnings improves code quality and maintainability.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Ready to Land
outcome: ready
sentiment_score: 8
sentiment_rationale: Patch has been reviewed and approved, indicating a positive progression
  towards resolution.
technical_tradeoffs:
- Minor code rearrangement to eliminate a compiler warning.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/e3d206ec-aabe-4803-9f96-abf71fbe3eeb@loongson.cn
bugzilla_url: null
date: '2026-04-20'
---

Mengqinggang is requesting that a patch addressing the "cbaud_to_speed defined but not used" warning on LA32 architecture be pushed to the master branch. The patch has already received a "LGTM" (Looks Good To Me) and review from Adhemerval Zanella Netto.  The patch conditionally defines `cbaud_to_speed` to avoid the warning when `TEST_COMPAT (libc, GLIBC_2_0, GLIBC_2_42)` is false.
