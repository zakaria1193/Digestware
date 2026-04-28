---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- bitint
- target guard
commit_hash: a2d74fe9c932874aa0a295f6c2b95410186c98a2
source_type: github
author: Jakub Jelinek
headline: Testsuite Fixed bitint-95.c Test.
tldr: The bitint-95.c test now includes necessary guards for bitint features, preventing
  failures on targets without full `_BitInt` support.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR124988 by adding target-specific guards to
  `gcc.dg/torture/bitint-95.c`. The test uses `_BitInt(192)`, which may not be supported
  on all targets, depending on the value of `__BITINT_MAXWIDTH__`. The missing guards
  caused failures on targets lacking full `_BitInt` support.
primer_general: The `_BitInt` type in GCC allows developers to define integer types
  with a specific number of bits. However, not all targets support arbitrarily large
  `_BitInt` types. The testsuite includes tests for `_BitInt` functionality, and these
  tests need to be guarded to ensure they only run on targets that support the required
  bit widths. This commit adds the necessary guards to `bitint-95.c`, preventing it
  from failing on targets with limited `_BitInt` support.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a2d74fe9c932874aa0a295f6c2b95410186c98a2
date: '2026-04-27'
---

The `bitint-95.c` test was missing the standard guards used in other bitint tests. This commit adds these guards, which check for bitint effective targets and ensure that parts of the test requiring `_BitInt(192)` support are only executed when `__BITINT_MAXWIDTH__ >= 192`. Without these guards, the test would fail on targets without sufficient `_BitInt` support.  This resolves PR124988.
