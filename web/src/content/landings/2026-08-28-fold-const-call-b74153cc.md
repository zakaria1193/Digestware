---
project: gcc
subsystem: fold-const-call
patch_id: null
tags:
- optimization
- floating-point
- fold-const-call
- NaN
commit_hash: b74153cc071f4bbedb76f2b72800b2c9467ce996
source_type: github
author: Kyrylo Tkachov
headline: Clarify handling of singleton sNaN in constant folding
tldr: Constant folding optimization now includes an explanation for its handling of
  singleton sNaN encodings.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `fold_const_call.cc` file's `fold_const_reduction` function now
  contains a comment explaining the reason for using the element-count fallback when
  encountering singleton sNaN encodings. This addresses PR127039.
primer_glossary:
- term: constant folding
  definition: A compiler optimization technique that evaluates constant expressions
    at compile time rather than at runtime.
- term: sNaN
  definition: Signaling Not-a-Number is a special floating-point value that, when
    used in an operation, generates an exception and typically propagates as a NaN.
    Unlike quiet NaN (qNaN), sNaN signals an invalid operation.
- term: singleton sNaN encoding
  definition: A specific representation of a signaling Not-a-Number value where all
    bits except the sign bit are zero, and the exponent and mantissa fields encode
    the signaling nature. Its handling in reductions can be complex.
- term: fallback
  definition: A secondary method or process used when the primary method fails or
    is not applicable. In this context, it refers to a different way of handling sNaN
    that ensures correctness.
- term: element-count
  definition: In the context of vector operations or reductions, this refers to the
    number of elements being processed or aggregated.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b74153cc071f4bbedb76f2b72800b2c9467ce996
date: '2026-08-28'
is_stub: true
stub_reason: low_score
---

The constant folding optimization pass has been updated to clarify why it uses an exact element-count fallback for singleton sNaN (signaling Not-a-Number) encodings. This explanation is added to the `fold_const_reduction` function in `fold-const-call.cc` to provide better understanding of this specific floating-point behavior within the optimization context.
