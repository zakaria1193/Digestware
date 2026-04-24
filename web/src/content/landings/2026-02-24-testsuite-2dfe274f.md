---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- floating-point
commit_hash: 2dfe274f644292f59a224c4963f984ed9a2217e8
source_type: github
author: feedable
headline: 'Testsuite: Fix Invalid Float Test by Moving Declaration'
tldr: This commit fixes a floating-point test by moving a declaration to ensure compilation
  on platforms without FE_UPWARD.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The patch rearranges code in ``gcc.dg/torture/fp-double-convert-float-1.c``
  to ensure compilation on platforms lacking ``FE_UPWARD``. This involves moving a
  declaration to precede a conditional compilation block.
primer_general: This commit repairs a floating-point conversion test in GCC's testsuite.  The
  C standard allows floating-point operations to be rounded in different ways, and
  the ``FE_UPWARD`` macro indicates support for one particular rounding mode.  This
  change ensures that the test compiles correctly regardless of whether the target
  platform supports this feature.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2dfe274f644292f59a224c4963f984ed9a2217e8
date: '2026-02-24'
---

This commit addresses a compilation issue in a floating-point test (``gcc.dg/torture/fp-double-convert-float-1.c``) by moving a declaration before the ``#ifdef`` directive. This ensures that the test compiles correctly on platforms that do not define ``FE_UPWARD``.
