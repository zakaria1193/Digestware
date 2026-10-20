---
project: gcc
subsystem: ada
patch_id: null
tags:
- ada
- optimization
- floating-point
commit_hash: abefc2ab85bd64dfda068347ad3bbfe307b5ce51
source_type: github
author: Liam Powell
headline: 'Ada: Improve ''Valid for floating point with obsolete targets'
tldr: Improved the implementation of Ada's 'Valid attribute for floating-point types,
  benefiting all targets.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The change in `gcc/ada/libgnat/s-fatgen.adb` concerns the `Valid` attribute
  for Ada floating-point types. For obsolete targets without denormal support, the
  existing implementation was questionable. This fix improves the code by importing
  `Rep` (the representation of the FP number) as a constant and masking out the sign
  bit when checking the Most Significant Word. This approach is more robust and also
  yields better code for targets that do support denormals.
primer_glossary:
- term: Ada 'Valid attribute
  definition: In Ada, the 'Valid attribute for a floating-point type checks whether
    a given representation corresponds to a normal or subnormal number, excluding
    NaNs and infinities.
- term: denormals
  definition: Denormalized numbers (or subnormals) are floating-point numbers with
    a smaller magnitude than the smallest normalized number. Support for them can
    affect performance and precision.
- term: Most Significant Word
  definition: In the context of floating-point representation, this refers to the
    part of the number's binary representation that holds the sign bit and the exponent.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/abefc2ab85bd64dfda068347ad3bbfe307b5ce51
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This commit refactors the implementation of the Ada 'Valid attribute for floating-point types. While the change primarily addresses an issue with obsolete targets that do not support denormalized numbers, it also results in improved generated code for other targets. The fix involves treating the representation of the floating-point number as an imported constant and masking out the sign bit for the test on its most significant word, leading to more accurate and potentially more efficient checks.
