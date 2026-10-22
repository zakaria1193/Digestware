---
project: gcc
subsystem: fold-const
patch_id: null
tags:
- optimization
- floating-point
- fold-const
commit_hash: a327f4cf83765f53e54c93523bbdb3cebec9d1fc
source_type: github
author: Roger Sayle
headline: Constant fold pow(-Inf, 0.5) and other infinite/NaN cases
tldr: Improves constant folding for pow() with infinite or NaN arguments.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `fold_const_pow` function in `fold-const-call.cc` has been enhanced
  to handle constant folding of `pow(base, exponent)` where `base` or `exponent` are
  IEEE 754 infinity or NaN values. This required introducing `real_isoddinteger` in
  `real.cc` to correctly identify odd integer exponents, particularly for binary floating-point
  formats. The implementation conservatively checks for a base of 2 in the floating-point
  representation to ensure correctness, and the `real_isinteger` function was also
  updated for efficiency.
primer_glossary:
- term: constant folding
  definition: An optimization technique where expressions with constant operands are
    evaluated at compile time rather than runtime.
- term: NaN
  definition: Not a Number. An IEEE 754 floating-point value representing an undefined
    or unrepresentable numerical result.
- term: IEEE 754
  definition: The standard for floating-point arithmetic, defining formats, operations,
    and exception handling.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a327f4cf83765f53e54c93523bbdb3cebec9d1fc
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

GCC can now constant fold `pow()` operations involving infinite or NaN arguments, such as `pow(-Inf, 0.5)`. Previously, it only handled finite arguments. This enhancement required adding `real_isoddinteger` and improving `real_isinteger` in `real.cc`. A new test case ensures correctness.
