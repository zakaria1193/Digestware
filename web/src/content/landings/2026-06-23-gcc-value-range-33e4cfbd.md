---
project: gcc
subsystem: gcc/value-range
patch_id: null
tags:
- optimization
- bugfix
- value-range-analysis
- compiler-internals
commit_hash: 33e4cfbd9495a23ffe4639c217442a5459b9e400
source_type: github
author: Andrew MacLeod
headline: Prange zero_p() should never have points to
tldr: The value range analysis in GCC now correctly handles `zero_p` ranges, ensuring
  they do not contain pointer information and fixing a bug that could lead to inc…
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch targets a specific invariant violation within GCC's value
  range analysis, specifically related to the `prange` data structure in `value-range.cc`
  and `value-range.h`. The core issue was that a `zero_p` (empty or zero-width) range
  could implicitly retain 'points-to' information, which is semantically incorrect
  because a zero-width range cannot point to anything meaningful. The fix involves
  modifying `prange::set_pt` and `prange::intersect` to explicitly clear points-to
  data whenever a range becomes `zero_p`, and introducing a verification check in
  `prange::verify_range` to enforce t…
primer_general: Compilers perform many optimizations to make programs run faster.
  One such optimization technique is 'value range analysis,' which tries to determine
  the possible range of values a variable can hold during program execution. This
  information helps the compiler make smarter decisions. This change fixes an internal
  bug in how GCC's value range analysis handled a specific type of range called `zero_p`,
  which essentially means a variable has no possible values or its range is empty.
  The bug was that this 'empty' range could still somehow hold information indicating
  it 'points to' a memory location, which doesn't make sense. The fix ensures that
  if a range becomes `zero_p`, any associated 'points-to' information is correctly
  cleared, preventing the compiler from making incorrect assumptions that could lead
  to subtle programming errors or less effective optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/33e4cfbd9495a23ffe4639c217442a5459b9e400
date: '2026-06-23'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in GCC's value range analysis where a `zero_p` (zero-width) program range could sometimes incorrectly acquire 'points-to' information. This could lead to miscompilations or incorrect optimizations. The corrections ensure that if `prange::set_pt` is called or `prange::intersect` results in a `zero_p` range, any associated points-to data is cleared. A new verification step in `prange::verify_range` further validates this invariant.
