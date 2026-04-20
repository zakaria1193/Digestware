---
project: glibc
subsystem: sysdeps
patch_id: null
tags:
- glibc
- sysdeps
- la32
- compiler warning
- termios
discussion_id: 20260323071657.1505765-1-mengqinggang@loongson.cn
source_type: public_inbox
title: 'Re: [PATCH] Fix ''cbaud_to_speed'' defined but not used on LA32'
headline: Fix 'cbaud_to_speed' defined but not used on LA32
tldr: Fixes a compiler warning on LA32 by conditionally defining 'cbaud_to_speed'
  based on compatibility requirements.
stakes: Resolves a compiler warning, improving code quality and maintainability.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: ready
sentiment_score: 9
sentiment_rationale: The patch received a LGTM, indicating strong approval.
technical_tradeoffs:
- The fix is a simple conditional definition, with minimal impact on performance or
  code complexity.
- It only affects the LA32 architecture.
primer_expert: This patch involves a fix in the `sysdeps` directory, specifically
  addressing a compiler warning related to conditional compilation. The `cbaud_to_speed`
  function is related to terminal settings and compatibility with older glibc versions.
  The surrounding code likely deals with termios and ioctl functions.
primer_general: The `sysdeps` directory in glibc contains system-specific implementations
  of functions. Conditional compilation is used to include or exclude code based on
  the target platform or compatibility requirements.  Compiler warnings indicate potential
  issues in the code that may lead to unexpected behavior or errors. This patch addresses
  a warning by ensuring a function is only defined when it's actually used.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/e3d206ec-aabe-4803-9f96-abf71fbe3eeb@loongson.cn
bugzilla_url: null
date: '2026-04-20'
---

This patch fixes a 'defined but not used' warning for the `cbaud_to_speed` function on the LA32 architecture. The function is now conditionally defined based on the `TEST_COMPAT` macro. The patch has received a LGTM and the author is requesting it be pushed to the master branch.
