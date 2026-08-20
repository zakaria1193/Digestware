---
project: gcc
subsystem: gcc/optimization
patch_id: null
tags:
- gcc
- optimization
- forwprop
- long-multiply
- ladder
commit_hash: 91cca3ac45e7f286e770536030da982d65615d4f
source_type: github
author: Konstantinos Eleftheriou
headline: 'forwprop: Add long-multiply ladder variants'
tldr: Extends long-multiply optimization to recognize and fold 'ladder' variants involving
  shifted intermediate sums.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `forwprop` pass now recognizes and optimizes several 'ladder' variants
  of long multiplication, including `mul_ladder_sum1`, `mul_ladder_sum2`, `mul_ladder_sum3`,
  and `mul_ladder_part_sum`. These patterns involve carry propagation through shifted
  intermediate sums. The `match.pd` file is updated with new atom recognizers, and
  `tree-ssa-forwprop.cc` incorporates new GIMPLE functions and logic to handle these
  ladder forms. The `long_mul_classify_plus_kinds` function is adjusted to prioritize
  more constrained ladder forms. This addresses PR tree-optimization/107090 by enabling
  the fold of the…
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
- term: match.pd
  definition: A file within GCC that contains pattern-matching definitions for various
    intermediate code constructs, used by optimization passes to identify and transform
    specific code sequences.
- term: GIMPLE
  definition: GCC's Internal Manipulation-code Generator and Evaluator. It is an intermediate
    representation (IR) used within GCC after the parsing and initial tree building,
    designed to be simpler and more amenable to optimization than the original AST.
- term: atom recognizers
  definition: In GCC's pattern matching system (used by passes like `match.pd`), an
    atom recognizer defines a basic building block or operation that can be part of
    a larger pattern.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/91cca3ac45e7f286e770536030da982d65615d4f
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This commit enhances the `forwprop` optimization pass by adding support for 'ladder' variants of long multiplication. These variants propagate carries through a series of mask, shift, and add operations on intermediate sums. The optimization now recognizes patterns like `mul_ladder_sum1`, `mul_ladder_sum2`, and `mul_ladder_sum3`, allowing the compiler to fold these complex multiplication sequences into more efficient code. This improves optimization for targets supporting these patterns and addresses a reported issue (PR tree-optimization/107090).
