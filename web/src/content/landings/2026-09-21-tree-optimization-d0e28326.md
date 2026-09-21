---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-ssa
- floating-point
commit_hash: d0e28326d4254e4824096a7331c8600455c22f73
source_type: github
author: Naveen
headline: Fold redundant integer-float-integer conversions
tldr: Optimizes redundant int->float->int conversions when precision is maintained.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The pattern in `match.pd` has been extended to fold integer-float-integer
  conversions if the intermediate floating-point type's significand can exactly represent
  all values of the final integer type, provided `-fno-trapping-math` is in effect.
  This builds upon the existing pattern from PR66211, safely removing the intermediate
  floating-point conversion when precision is guaranteed, thus addressing PR98984.
primer_glossary:
- term: tree-optimization
  definition: A stage in GCC optimization where the code is represented in an intermediate
    form called GENERIC/GIMPLE (a three-address code representation) before being
    converted to RTL.
- term: folding
  definition: An optimization technique where constant expressions or redundant operations
    are evaluated or removed at compile time.
- term: significand
  definition: The fractional part of a floating-point number, also known as the mantissa.
- term: -fno-trapping-math
  definition: A compiler flag that modifies floating-point exception handling; when
    enabled, operations like division by zero or overflow do not raise exceptions
    but result in undefined or special values, allowing for more aggressive optimizations.
- term: PR
  definition: Problem Report, used to refer to specific bugs or feature requests filed
    against GCC.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d0e28326d4254e4824096a7331c8600455c22f73
date: '2026-09-21'
is_stub: false
stub_reason: ''
---

This optimization folds redundant integer-to-floating-point-to-integer conversions when the intermediate floating-point type can precisely represent all values of the final integer type. This improves code efficiency by eliminating unnecessary conversions, especially when the `-fno-trapping-math` option is enabled and the floating-point significand has sufficient precision.
