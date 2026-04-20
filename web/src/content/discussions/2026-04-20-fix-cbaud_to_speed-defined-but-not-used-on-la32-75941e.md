---
project: glibc
subsystem: sysdeps
patch_id: null
tags:
- compiler warning
- LA32
- sysdeps
- compatibility
- glibc
discussion_id: 20260323071657.1505765-1-mengqinggang@loongson.cn
source_type: public_inbox
title: 'Re: [PATCH] Fix ''cbaud_to_speed'' defined but not used on LA32'
headline: Fix 'cbaud_to_speed' defined but not used on LA32
tldr: Fixes a compiler warning on LA32 architecture where 'cbaud_to_speed' was defined
  but not used under certain compatibility conditions.
stakes: Resolves a compiler warning, improving code quality and maintainability on
  the LA32 architecture.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Ready to Land
outcome: ready
sentiment_score: 10
sentiment_rationale: The patch received a LGTM and is awaiting commit, indicating
  strong approval.
technical_tradeoffs:
- None
- Code cleanup
primer_expert: This patch fixes a "defined but not used" warning for `cbaud_to_speed`
  in `sysdeps/unix/sysv/linux/tst-termios-linux.c`.  The function's definition was
  not guarded by the same `TEST_COMPAT` macro that controlled its usage. The fix ensures
  the function is only defined when it's actually needed. This is specific to the
  LA32 architecture due to its compatibility requirements.
primer_general: In large projects like glibc, compatibility with older systems is
  often maintained using conditional compilation. This means certain code sections
  are only included when building for specific system configurations or compatibility
  levels. This patch deals with such a compatibility issue where a function, `cbaud_to_speed`,
  was defined even when it wasn't used, triggering a compiler warning. By making the
  definition conditional, the patch cleans up the code and avoids unnecessary baggage
  for systems where the function isn't required.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/e3d206ec-aabe-4803-9f96-abf71fbe3eeb@loongson.cn
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses a compiler warning on the LA32 architecture related to the `cbaud_to_speed` function. The function was being defined unconditionally but only used when `TEST_COMPAT (libc, GLIBC_2_0, GLIBC_2_42)` was true, leading to a "defined but not used" warning. The patch modifies the definition to be conditional, resolving the warning. The patch has been reviewed and is awaiting commit.
