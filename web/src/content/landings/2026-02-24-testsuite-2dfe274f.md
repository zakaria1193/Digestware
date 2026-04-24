---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- floating-point
- portability
commit_hash: 2dfe274f644292f59a224c4963f984ed9a2217e8
source_type: github
author: feedable
headline: 'Testsuite: Fix floating-point test compilation on platforms without FE_UPWARD.'
tldr: A floating-point test now compiles correctly on platforms lacking `FE_UPWARD`
  by moving the declaration before the `#ifdef`.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses a conditional compilation issue in `gcc.dg/torture/fp-double-convert-float-1.c`.
  The fix involves moving a declaration outside the scope of an `#ifdef FE_UPWARD`
  block.  The macro `FE_UPWARD` relates to floating-point rounding modes. This ensures
  the code compiles even when `FE_UPWARD` is not defined, improving testsuite portability.
primer_general: This commit fixes a compilation error in a GCC test program. The test
  involves floating-point number conversions. The error occurred because the test
  used a feature (`FE_UPWARD`, related to floating-point rounding) that is not available
  on all systems. The fix rearranges the code so that it compiles correctly even on
  systems without this feature, making the test more portable.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2dfe274f644292f59a224c4963f984ed9a2217e8
date: '2026-02-24'
---

A floating-point test, `gcc.dg/torture/fp-double-convert-float-1.c`, failed to compile on platforms that do not define `FE_UPWARD`. This commit fixes the issue by moving a declaration before the `#ifdef` directive, ensuring that the declaration is always visible regardless of whether `FE_UPWARD` is defined. This makes the test more portable.
