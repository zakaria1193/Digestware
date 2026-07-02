---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- optimization
- compiler
commit_hash: 5b0da09f0ed5da80734c143d3ce2bacd78dc0c28
source_type: github
author: Thomas Koenig
headline: GCC optimizes `(-1.0)**n` to an efficient intrinsic for all integer types.
tldr: The Fortran front end of GCC now optimizes `(-1.0)**n` into an efficient intrinsic
  that handles all integer exponent types, reducing calls to slower library fu…
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change in `gcc/fortran/trans-expr.cc` modifies how `gfc_conv_power_op`
  handles the specific Fortran power operation `(-1.0)**n`. Previously, an optimization
  relying on `__builtin_powi` only applied to default integer exponents, leaving larger
  integer types to potentially slower library function calls. This patch introduces
  a direct bitwise calculation that is efficient across all integer kinds, avoiding
  the performance pitfalls of converting larger integers to default integers. It interacts
  with the existing `__builtin_powi` framework by offering a more globally optimal
  approach for this…
primer_general: When you write code like `x**n` in Fortran, the compiler needs to
  figure out the most efficient way to calculate that power. For simple cases, the
  compiler often has built-in, highly optimized instructions or sequences of instructions
  (called intrinsics) that are much faster than calling a general-purpose math library
  function. This change specifically targets cases where the base is exactly -1.0
  and the exponent `n` is an integer. Previously, if `n` was a very large integer
  (a 'kind=8' integer in Fortran), the compiler would call a slower library function
  instead of using an optimized intrinsic. This update teaches the compiler a clever
  trick to calculate `(-1.0)**n` directly using bitwise operations on the exponent,
  making it fast for all integer sizes. This helps your Fortran programs run quicker
  by avoiding unnecessary overhead for a common mathematical pattern.
discussion_id_link: github:gcc-mirror/gcc#57073
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5b0da09f0ed5da80734c143d3ce2bacd78dc0c28
date: '2026-06-22'
is_stub: false
---

The Fortran front end of GCC now optimizes expressions like `(-1.0)**n` by replacing them with an intrinsic calculation: `(real) (1 - ((n & 1) << 1))`. This optimization applies correctly to all integer exponent types, including those of kind=8, which previously bypassed an existing optimization due to reliance on a library function. The change avoids suboptimal code generation associated with conversions to default integer types.
