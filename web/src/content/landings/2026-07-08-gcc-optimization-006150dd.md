---
project: gcc
subsystem: gcc/optimization
patch_id: null
tags:
- gcc
- optimization
- forwprop
- long-multiply
commit_hash: 006150ddc40844105eb99bc6514267314715f6dc
source_type: github
author: Konstantinos Eleftheriou
headline: 'forwprop: Add long-multiply low-plus variant'
tldr: Enhances long-multiply optimization by recognizing and folding a 'low-plus'
  variant involving cross-product and shifted low parts.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `forwprop` pass now recognizes a `LOW_PART` variant of long multiplication
  where the result is formed by `xl*yl + (cross_sum << N)`, with `cross_sum = xh*yl
  + xl*yh`. This pattern is part of a two-carry long multiply. The fold is deferred
  if any comparison uses (`GT`, `LT`, `GE`, `LE`) share an operand with the `PLUS`
  expression, ensuring that necessary intermediate values are not destroyed. Once
  the high-part fold is complete, a subsequent `forwprop` pass can complete the remaining
  fold. This addresses PR tree-optimization/107090.
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
- term: LOW_PART
  definition: Refers to the lower half of a wide result produced by an operation like
    a long multiply. For instance, in a 128-bit result from a 64x64 multiplication,
    the LOW_PART would be the lower 64 bits.
- term: cross_sum
  definition: In the context of long multiplication, the cross sum typically refers
    to the sum of the products of the high part of one operand and the low part of
    the other, and vice versa (e.g., xh*yl + xl*yh).
- term: PLUS
  definition: Represents an addition operation within GCC's intermediate representation
    (GIMPLE).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/006150ddc40844105eb99bc6514267314715f6dc
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This commit extends the `forwprop` optimization pass to recognize a 'low-plus' variant of long multiplication. This variant involves the cross-product of high and low parts of the operands, combined with a shifted low partial product. The optimization now correctly folds this pattern, especially when it's part of a two-carry long multiplication, deferring the fold if conditional comparisons still require intermediate values. This improves code generation for specific multiplication scenarios.
