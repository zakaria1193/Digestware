---
project: gcc
subsystem: gcc/optimization
patch_id: null
tags:
- gcc
- optimization
- forwprop
- long-multiply
- two-carry
commit_hash: 6c171ef2c1ba0b71505f1c6e93c8d3c8d90bdaca
source_type: github
author: Konstantinos Eleftheriou
headline: 'forwprop: Add long-multiply two-carry variant'
tldr: Improves long-multiply optimization by recognizing and folding a 'two-carry'
  variant with separate cross-sum and low-half carry propagations.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `forwprop` pass gains support for a 'two-carry' variant of long
  multiplication. This variant features separate carry propagation from both the cross-sum
  (`xh*yl + xl*yh`) and the low-half accumulation (`xl*yl + (cross_sum << N)`), each
  indicated by an unsigned overflow compare. A new `long_mul_check_two_carries` helper
  function validates these carry operands against the original multiplication inputs.
  This optimization targets the HIGH_PART of the result and is enabled by new recognizers
  in `match.pd` and logic in `tree-ssa-forwprop.cc`, addressing PR tree-optimization/107090.
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
- term: HIGH_PART
  definition: Refers to the higher half of a wide result produced by an operation
    like a long multiply. For instance, in a 128-bit result from a 64x64 multiplication,
    the HIGH_PART would be the upper 64 bits.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6c171ef2c1ba0b71505f1c6e93c8d3c8d90bdaca
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This commit extends the `forwprop` optimization pass to recognize a 'two-carry' variant of long multiplication. In this variant, the cross sum and the low-half accumulation each generate a separate unsigned overflow compare, contributing to the final result. The optimization now correctly folds this pattern, including an extra check to validate the carry operands against the canonical multiplication operands. This addresses PR tree-optimization/107090 by enabling the compiler to optimize these complex multiplication sequences.
