---
project: glibc
subsystem: sysdeps
patch_id: null
tags:
- glibc
- LA32
- compiler warning
- termios
discussion_id: 20260323071657.1505765-1-mengqinggang@loongson.cn
source_type: public_inbox
title: 'Re: [PATCH] Fix ''cbaud_to_speed'' defined but not used on LA32'
headline: Fix 'cbaud_to_speed' defined but not used on LA32
tldr: The patch fixes a compiler warning on LA32 by conditionally defining cbaud_to_speed.
stakes: Addresses a code quality issue, potentially improving maintainability and
  preventing unexpected behavior in specific configurations.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Ready to Land
outcome: ready
sentiment_score: 9
sentiment_rationale: Patch has been reviewed and approved, author is requesting it
  be pushed.
technical_tradeoffs:
- Condition definition avoids the warning under certain compilation flags.  No runtime
  performance impact.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/e3d206ec-aabe-4803-9f96-abf71fbe3eeb@loongson.cn
bugzilla_url: null
date: '2026-04-20'
---

A patch was submitted to fix a 'defined but not used' warning for the `cbaud_to_speed` function on the LA32 architecture. The function is now conditionally defined based on `TEST_COMPAT`. Adhemerval Zanella reviewed and approved the patch, and the author is requesting it be pushed to the master branch.
