---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- floating-point
- precision
commit_hash: 95decbde1acc0c9a459d39e806106ab4e232085a
source_type: github
author: Kyrylo Tkachov
headline: Improve float conversion folding safety
tldr: Float conversion folding now requires intermediate types to exactly represent
  the input type, preventing precision loss.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `two conversions in a row` pattern in `match.pd` previously used
  `element_precision` to determine if an intermediate float-to-float conversion could
  be eliminated. This commit replaces that with `real_exact_conversion_p`, which performs
  a more robust check comparing radix, precision, exponent range, and special value
  support. This prevents folding chains like `(float) (_Decimal32) f16` or `(double)
  (_Float16) (__bf16) x` where the intermediate type (`_Decimal32`, `_Float16`) cannot
  exactly represent the input type (`f16`, `__bf16`), thus avoiding precision loss
  and incorrect results due t…
primer_glossary:
- term: match.pd
  definition: A file containing pattern matching rules for the GCC middle-end, used
    to identify and optimize sequences of operations.
- term: folding
  definition: An optimization technique where constant expressions or predictable
    operations are evaluated at compile time rather than runtime.
- term: _Decimal32
  definition: A IEEE 754-2008 decimal floating-point format with 32 bits of precision.
- term: _Float16
  definition: A 16-bit floating-point format, often used for machine learning and
    graphics, with limited precision and range.
- term: __bf16
  definition: Bfloat16, a 16-bit floating-point format primarily used in deep learning,
    prioritizing dynamic range over precision.
- term: element_precision
  definition: A property of floating-point types indicating the number of representable
    digits.
- term: radix
  definition: The base of a number system; for floating-point types, this is typically
    2 (binary) or 10 (decimal).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/95decbde1acc0c9a459d39e806106ab4e232085a
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This patch enhances the floating-point conversion folding in `match.pd` by introducing `real_exact_conversion_p`. This new check ensures that the intermediate floating-point type in a conversion chain can precisely represent all values of the preceding type. Previously, folding could occur based solely on bit-width, leading to precision loss and incorrect results, particularly with formats like _Decimal32, _Float16, and __bf16.
