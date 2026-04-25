---
project: gcc
subsystem: gcc/bitintlower
patch_id: null
tags:
- bitint
- overflow
- bugfix
- middle-end
commit_hash: dcaa624319dc58ed8b1f51f6e0718cba94d7a3b9
source_type: github
author: Jakub Jelinek
headline: 'bitintlower: Fix padding bit handling for __builtin_{add,sub,mul}_overflow
  [PR123635].'
tldr: This commit fixes padding bit handling for `__builtin_{add,sub,mul}_overflow`
  for `_BitInt`, completing the padding bit fixes for extended bit integers.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch addresses PR123635 and PR124988 by fixing padding bit handling
  in `bitint_large_huge::finish_arith_overflow` and `bitint_large_huge::lower_addsub_overflow`
  within `gimple-lower-bitint.cc`. The fix ensures correct extension of padding bits
  for partial and full limbs when lowering `__builtin_{add,sub,mul}_overflow` operations
  on `_BitInt` types, especially `bitint_extended`. The patch also adds new test cases
  in `gcc.dg/torture`.
primer_general: GCC now supports arbitrarily sized integer types via the `_BitInt`
  keyword.  These integers might require padding bits to fit within machine words.  The
  `__builtin_{add,sub,mul}_overflow` functions detect integer overflows during arithmetic
  operations.  This commit fixes a bug in the compiler's internal logic that handles
  these overflow checks for `_BitInt` types, specifically ensuring the correct handling
  of padding bits. This fixes an obscure corner case in the relatively new `_BitInt`
  feature.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dcaa624319dc58ed8b1f51f6e0718cba94d7a3b9
date: '2026-04-24'
---

This commit addresses missing padding bit handling in `__builtin_{add,sub,mul}_overflow` for the `_BitInt` type within GCC.  The patch ensures proper extension of padding bits in partial and full limbs during overflow checks. This fix completes the efforts to correctly handle padding bits for extended bit integers, resolving issue PR123635 and PR124988. New test cases are added to verify the correct behavior.
