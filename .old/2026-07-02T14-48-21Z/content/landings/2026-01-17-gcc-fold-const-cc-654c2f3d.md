---
project: gcc
subsystem: gcc/fold-const.cc
patch_id: null
tags:
- optimization
- constant folding
- overflow
commit_hash: 654c2f3d61ac7394eb85cacf6203b5a8a556bad9
source_type: github
author: Daniel Barboza
headline: Remove strict_overflow_p flag from extract_muldiv
tldr: The strict_overflow_p flag was removed from extract_muldiv, part of deprecating
  -Wstrict-overflow.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes the `strict_overflow_p` flag from the `extract_muldiv`
  function within `fold-const.cc`.  This function attempts to decompose an expression
  into multiplication and division components for constant folding. The removal is
  related to the deprecation of the `-Wstrict-overflow` flag, which warned about potential
  overflows detected during compile-time constant expression evaluation.  The impact
  is primarily within the constant folding logic itself.
primer_general: GCC optimizes code by performing constant calculations at compile
  time, known as constant folding. During this process, the `extract_muldiv` function
  identifies multiplication and division operations. The `-Wstrict-overflow` flag
  instructs the compiler to warn about potential integer overflows during such calculations.
  This commit removes the `strict_overflow_p` flag, which controlled overflow checking
  in `extract_muldiv`, as part of the broader effort to deprecate the `-Wstrict-overflow`
  warning.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/654c2f3d61ac7394eb85cacf6203b5a8a556bad9
date: '2026-01-17'
is_stub: false
---

The `strict_overflow_p` flag was removed from the `extract_muldiv` function.  This function is involved in extracting multiplication and division operations during constant folding.  Removing the flag is part of the larger effort to deprecate the `-Wstrict-overflow` warning. Consequently, a test case that specifically checked for `-Wstrict-overflow` warnings in `extract_muldiv` patterns was also removed.
