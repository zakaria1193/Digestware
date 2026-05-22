---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- deprecation
- c++23
- numeric_limits
commit_hash: 6a4cfad20b7f7eacb352aed01b6159baa9935f2a
source_type: github
author: Jonathan Wakely
headline: Deprecates numeric_limits::has_denorm for C++23.
tldr: Deprecates `numeric_limits::has_denorm` and related features in libstdc++ for
  C++23, following the P2614R2 paper.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: '`numeric_limits` is a template class that provides information about
  the properties of arithmetic types, such as the minimum and maximum representable
  values, precision, and whether the type supports denormalized values.  `float_denorm_style`
  is an enumeration that indicates how denormalized floating-point values are handled.
  Deprecating `has_denorm` and `has_denorm_loss` means that these members should no
  longer be used in new code, as they may be removed in a future version of the standard.
  This is part of a larger effort to modernize the C++ standard library.'
primer_general: In floating-point arithmetic, denormalized numbers (also called subnormal
  numbers) are used to represent values closer to zero than the smallest normal floating-point
  number. This allows for a more gradual loss of precision as numbers approach zero.
  The C++ standard library provides the `numeric_limits` class to query properties
  of numeric types. This commit deprecates the `has_denorm` member of `numeric_limits`,
  indicating whether a floating-point type supports denormalized values. This change
  is part of ongoing evolution of the C++ language.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6a4cfad20b7f7eacb352aed01b6159baa9935f2a
date: '2026-05-19'
is_stub: false
---

The C++ standard is evolving, and some features are being deprecated. This commit marks `float_denorm_style`, its enumerators, and `numeric_limits::has_denorm` and `numeric_limits::has_denorm_loss` as deprecated in libstdc++ for C++23. This change aligns with the approved paper P2614R2. The commit adds `dg-warning` directives to test files to ensure that deprecation warnings are generated as expected.
