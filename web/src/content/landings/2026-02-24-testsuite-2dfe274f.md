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
headline: 'Testsuite: Fix floating-point test compilation on systems without FE_UPWARD'
tldr: 'A floating-point test in the GCC testsuite now compiles correctly on platforms
  lacking FE_UPWARD by moving a declaration before an #ifdef.'
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The commit modifies `gcc.dg/torture/fp-double-convert-float-1.c` to
  ensure it compiles correctly even when `FE_UPWARD` is not defined. `FE_UPWARD` is
  a floating-point rounding mode macro. Correctly handling platform-specific differences
  in the testsuite avoids spurious test failures.
primer_general: The GCC testsuite contains a variety of tests to verify the compiler's
  behavior, including floating-point operations. To ensure these tests work correctly
  on different systems, they need to handle platform-specific differences, such as
  the availability of certain floating-point features or macros. This commit addresses
  one such difference, ensuring the test compiles and runs correctly across more platforms.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2dfe274f644292f59a224c4963f984ed9a2217e8
date: '2026-02-24'
---

This commit addresses a compilation issue in a floating-point test within the GCC testsuite.  The test, `gcc.dg/torture/fp-double-convert-float-1.c`, failed to compile on platforms that do not define `FE_UPWARD`. To resolve this, a declaration was moved to ensure it is always visible, regardless of the `#ifdef` condition.
