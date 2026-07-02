---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- undefined behavior
- count leading zeros
- DeBruijn
commit_hash: a66820ce3f5b298759042b6543a056b490370310
source_type: github
author: Philipp Tomsich
headline: 'Tree-optimization: Avoid Shift-by-64 Undefined Behavior'
tldr: The DeBruijn CLZ table validator now avoids undefined behavior by special-casing
  the MSB bit, resolving a long-standing issue.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The ``simplify_count_zeroes`` function validates DeBruijn CLZ tables
  using a bit-shifting approach. When validating 64-bit inputs, a shift by ``HOST_BITS_PER_WIDE_INT``
  (64) triggers undefined behavior, causing the check to fail. The fix special-cases
  ``data + 1 == HOST_BITS_PER_WIDE_INT`` to use ``HOST_WIDE_INT_M1U``, preventing
  the shift and ensuring correct validation.
primer_general: GCC uses various optimization techniques to improve the performance
  of compiled code. One such technique involves counting the number of leading zeros
  in a number.  This commit fixes a bug in the validation of a data structure used
  for this optimization, preventing it from rejecting valid data and potentially hindering
  performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a66820ce3f5b298759042b6543a056b490370310
date: '2026-04-09'
---

The DeBruijn CLZ (count leading zeros) table validator in GCC's tree-optimization pass had an issue where it would perform a shift by the number of bits in a `HOST_WIDE_INT`, resulting in undefined behavior. This affected 64-bit inputs, causing the validator to reject well-formed CLZ tables. The fix special-cases this scenario, ensuring correct validation and enabling optimizations relying on DeBruijn CLZ tables.
