---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- optimization
- middle-end
- division
- register allocation
commit_hash: 87c2f1ce7ce4b3e1792d4acdc98fc7132c7ab9c7
source_type: github
author: Christopher Bazley
headline: 'middle-end: Improve division check for divisors larger than dividends'
tldr: Enhanced division check correctly handles cases where the divisor is larger
  than the dividend, improving register allocation accuracy.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `can_div_away_from_zero_p` function, used in middle-end analysis
  to determine properties of division operations, is enhanced to correctly handle
  cases where `abs(divisor) > abs(dividend)`. Previously, it conservatively failed
  if `can_div_trunc_p` failed, inhibiting its use for determining register occupancy.
  The new implementation directly checks the condition `|b * Q| >= |a|` and correctly
  deduces the quotient (1 or -1) based on operand signs, independent of `can_div_trunc_p`'s
  limitations with symbolic values.
primer_general: This commit improves a specific check within the GCC compiler that
  analyzes division operations. The function `can_div_away_from_zero_p` helps determine
  properties of division results, particularly when a divisor is larger in magnitude
  than the dividend. The previous implementation was too conservative and could incorrectly
  report that a division was problematic, even when it wasn't. This update makes the
  check more robust, ensuring it correctly identifies that the quotient will be 1
  or -1 in such cases. This is important for optimizing code that uses scalable vector
  types, as it allows the compiler to more accurately predict how much space a value
  will occupy, preventing potential performance issues and internal errors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/87c2f1ce7ce4b3e1792d4acdc98fc7132c7ab9c7
date: '2026-06-12'
is_stub: false
stub_reason: ''
---

The `can_div_away_from_zero_p` function has been significantly improved to correctly handle division scenarios where the divisor's magnitude is larger than the dividend's. Previously, it relied too heavily on `can_div_trunc_p`, leading to incorrect results when the divisor was larger. This fix ensures the function accurately determines the quotient (1 or -1 based on signs) and is crucial for accurate register allocation for scalable vector types, preventing potential performance regressions or internal compiler errors.
