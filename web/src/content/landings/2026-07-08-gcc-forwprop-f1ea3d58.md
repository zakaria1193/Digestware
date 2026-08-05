---
project: gcc
subsystem: gcc/forwprop
patch_id: null
tags:
- optimization
- performance
- aarch64
- x86-64
commit_hash: f1ea3d58f0caf819042b0ca3981af1219a8fb461
source_type: github
author: Konstantinos Eleftheriou
headline: Fold longhand wide-multiply idioms for improved performance
tldr: Optimize manual carry propagation in wide-multiply operations to use built-in
  widening multiply instructions.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `forwprop` and `widening_mul` passes now recognize and fold manual
  implementations of 2N-bit multiplication, which typically involve splitting operands
  into halves, computing four partial products, and manually propagating carries.
  This rewrite transforms such code into a `WIDEN_MULT_EXPR` or `MULT_HIGHPART_EXPR`
  for the high part and a `MULT_EXPR` for the low part. When 2N-bit operations are
  unsupported, `lower_long_mul_high_chain` resynthesizes the longhand at N precision.
  This optimization is gated by pattern matching in `match.pd` and a consistency check
  in `forwprop`.
primer_glossary:
- term: widening multiply
  definition: An arithmetic operation that computes a product of two N-bit integers,
    resulting in a 2N-bit integer. This is often implemented using specific instructions
    on hardware that support it.
- term: forwprop
  definition: Forward propagation is a compiler optimization pass that propagates
    constants and expressions through the intermediate representation (IR) to simplify
    computations and enable further optimizations.
- term: WIDEN_MULT_EXPR
  definition: An internal GCC representation for a widening multiply operation, indicating
    that the result of a multiplication is expected to occupy twice the number of
    bits as its operands.
- term: MULT_EXPR
  definition: An internal GCC representation for a multiplication operation.
- term: MULT_HIGHPART_EXPR
  definition: An internal GCC representation for an operation that computes only the
    high part of a widening multiplication result.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f1ea3d58f0caf819042b0ca3981af1219a8fb461
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This commit optimizes code that manually computes a 2N-bit product on an N-bit target by folding the longhand arithmetic into a single widening multiply and a shift. This transformation leverages built-in widening multiply instructions, improving performance significantly on specific architectures. The change affects the `forwprop` and `widening_mul` passes, with performance gains up to 59% observed on certain processors. Compile times are negligibly impacted.
