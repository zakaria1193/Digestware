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
headline: Fixes Invalid Float Test for Platforms Without FE_UPWARD.
tldr: This commit fixes a floating-point test compilation error on platforms lacking
  FE_UPWARD.
why_it_matters: Ensures that floating-point tests are portable across different hardware
  and software configurations, preventing false negatives during testing.
impact_score: 4
impact_rationale: Fixes a test compilation issue, improving testsuite robustness.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit touches `gcc.dg/torture/fp-double-convert-float-1.c`, a
  part of the GCC testsuite. The FE_UPWARD macro relates to floating-point rounding
  modes as defined by the IEEE 754 standard.  This fix ensures that the test case
  is conditionally compiled based on the availability of this specific rounding mode,
  avoiding compilation errors on systems that don't provide it.
primer_general: 'Floating-point arithmetic requires careful handling of rounding,
  where a real number is approximated by a representable floating-point number. The
  IEEE 754 standard defines several rounding modes, including FE_UPWARD, which rounds
  towards positive infinity.  Compilers use preprocessor macros like #ifdef to conditionally
  compile code based on the target platform''s capabilities. This commit ensures that
  a specific floating-point test only runs when the target platform supports the FE_UPWARD
  rounding mode, avoiding compilation errors.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2dfe274f644292f59a224c4963f984ed9a2217e8
date: '2026-02-24'
---

The commit directly addresses a compilation failure in a floating-point test on platforms where the FE_UPWARD macro is not defined. By moving a variable declaration before the #ifdef directive, the code now compiles correctly regardless of the platform's floating-point environment support.
