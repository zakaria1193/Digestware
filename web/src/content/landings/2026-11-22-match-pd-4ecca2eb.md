---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- optimization
- floating-point
- GIMPLE
commit_hash: 4ecca2eba5a6932251248195cb4b2c348b240a01
source_type: github
author: Igor Shevlyakov
headline: Fold sign-bit operations on reinterpreted floats
tldr: Optimizes floating-point sign bit manipulation by folding them into standard
  absolute value and negation operations.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit introduces a new optimization in the `match.pd` pass for
  GCC. It targets GIMPLE expressions where floating-point values are cast to integers,
  their sign bit is manipulated (cleared, flipped, or set using bitwise operations),
  and then cast back to floating-point. The optimization recognizes these patterns
  as equivalent to `fabs`, negation, or negation of `fabs`. It canonicalizes these
  into `ABS_EXPR` and `NEGATE_EXPR` at the GIMPLE level, enabling further optimization
  by downstream passes and target-specific lowering, especially when targets lack
  direct hardware support or have spe…
primer_glossary:
- term: GIMPLE
  definition: GCC's internal representation of code between the front-end and the
    back-end. It's a three-address, low-level representation that facilitates optimizations.
- term: VIEW_CONVERT_EXPR
  definition: An expression in GCC's internal representation indicating a conversion
    between types, often used when reinterpreting the bits of one type as another,
    like casting a float to an integer to access its bit pattern.
- term: ABS_EXPR
  definition: An expression in GCC's internal representation representing the absolute
    value of an operand.
- term: NEGATE_EXPR
  definition: An expression in GCC's internal representation representing the negation
    of an operand.
- term: copysign
  definition: A function that returns a value with the magnitude of the first argument
    and the sign of the second argument.
- term: NaN
  definition: Not a Number. A special floating-point value used to represent undefined
    or unrepresentable results, such as the result of 0/0.
- term: signed zero
  definition: Floating-point numbers can have both a positive zero (+0.0) and a negative
    zero (-0.0). While they compare as equal, their bit representations differ.
- term: bfloat16
  definition: A 16-bit floating-point format with a similar exponent range to IEEE
    754 single-precision but lower precision.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4ecca2eba5a6932251248195cb4b2c348b240a01
date: '2026-11-22'
is_stub: false
stub_reason: ''
---

This change optimizes code that manipulates the sign bit of floating-point numbers using integer reinterpretations. Previously, such operations would involve moving values between floating-point and integer registers, leading to inefficiencies. The compiler now recognizes these patterns and canonicalizes them to ABS_EXPR or NEGATE_EXPR, allowing them to be lowered to native target instructions and combine better with surrounding code. This improves performance by reducing register pressure and leveraging efficient hardware instructions, particularly for operations like fabs, negation, and copysign.
