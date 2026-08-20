---
project: gcc
subsystem: gcc/optimization
patch_id: null
tags:
- gcc
- optimization
- forwprop
- long-multiply
- carry-low-sum
commit_hash: 6c598e2be7d0adf937d3390bb8f6a16b39603016
source_type: github
author: Konstantinos Eleftheriou
headline: 'forwprop: Add long-multiply carry-low-sum variant'
tldr: Improves long-multiply optimization by recognizing and folding a 'carry-low-sum'
  variant where cross-sum and low partial products are combined.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `forwprop` pass now recognizes a 'carry-low-sum' variant of long
  multiplication, characterized by `low_sum = cross_sum + (xl*yl >> N)`, where `cross_sum
  = xh*yl + xl*yh`. The outer chain then uses an overflow compare against this `low_sum`
  for carry propagation. New atom recognizers (`mul_low_sum`, `mul_carry_low_sum`)
  are added to `match.pd`, and `tree-ssa-forwprop.cc` is updated to handle these `LMK_LOW_SUM`
  and `LMK_CARRY_LOW_SUM` kinds. The `long_mul_classify_carry` function prioritizes
  `mul_carry_low_sum`, and `long_mul_classify_plus_kinds` is adjusted for `mul_low_sum`.
  This address…
primer_glossary:
- term: forwprop
  definition: Forward propagation is an optimization pass in GCC that attempts to
    simplify expressions by replacing variables with their definitions as early as
    possible in the program flow. It's part of the SSA (Static Single Assignment)
    based optimization framework.
- term: long-multiply
  definition: A multiplication operation where the result's bit-width is twice that
    of the operands (e.g., multiplying two 64-bit integers to produce a 128-bit result).
    Optimizing these operations is crucial for performance on platforms that may not
    have native hardware support for such wide multiplications.
- term: cross_sum
  definition: In the context of long multiplication, the cross sum typically refers
    to the sum of the products of the high part of one operand and the low part of
    the other, and vice versa (e.g., xh*yl + xl*yh).
- term: match.pd
  definition: A file within GCC that contains pattern-matching definitions for various
    intermediate code constructs, used by optimization passes to identify and transform
    specific code sequences.
- term: LOW_PART
  definition: Refers to the lower half of a wide result produced by an operation like
    a long multiply. For instance, in a 128-bit result from a 64x64 multiplication,
    the LOW_PART would be the lower 64 bits.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6c598e2be7d0adf937d3390bb8f6a16b39603016
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This commit enhances the `forwprop` optimization pass to recognize a 'carry-low-sum' variant of long multiplication. This variant combines the cross sum and the low partial product into a single `low_sum`, and then uses an overflow compare against this `low_sum` to generate the carry for the higher part. The optimization now folds this pattern, which has three summands in its outer chain, improving code generation for these specific multiplication scenarios and addressing PR tree-optimization/107090.
