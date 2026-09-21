---
project: gcc
subsystem: widening_mul
patch_id: null
tags:
- widening_mul
- optimization
- PR127042
- tree-ssa
commit_hash: 2d2e355b89367711f549b1277a537e2c0a4de58d
source_type: github
author: Philipp Tomsich
headline: Emit zero high-half partials for operands that fit in `widening_mul`.
tldr: Optimizes `widening_mul` by skipping unnecessary calculations for operands that
  fit within half the width.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `build_long_mul_partials` function previously split both operands
  regardless of their known size. This commit modifies it to use the recognizer's
  `fits` test. If an operand fits within the lower half-width, its high-half partial
  products are emitted as zeros, and the subsequent carry arithmetic folds correctly.
  This avoids redundant shifts and multiplies for operands known to be small.
primer_glossary:
- term: widening_mul
  definition: An optimization pass in GCC that performs multiplication of two numbers
    where the result may exceed the standard integer type, often by using multiple
    machine instructions.
- term: high-half partials
  definition: In a wider multiplication, the results of multiplying the most significant
    bits of one operand with the least significant bits of the other. 'High-half'
    refers to the more significant portion of the result.
- term: recognizer
  definition: A component within GCC that analyzes the intermediate representation
    (like RTL) to identify patterns that can be optimized or mapped to specific machine
    instructions.
- term: tree-ssa
  definition: Static Single Assignment form, an intermediate representation used by
    GCC that simplifies many optimizations by ensuring each variable is assigned exactly
    once.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2d2e355b89367711f549b1277a537e2c0a4de58d
date: '2026-08-24'
is_stub: false
stub_reason: ''
---

The `widening_mul` optimization pass now correctly handles operands that provably fit within half the width of the multiplication. Previously, it performed unnecessary shift and multiply operations even when the high half of such operands was zero. This change reuses the recognizer's 'fits' test to emit literal zeros for the high-half partial products, simplifying the generated code and improving efficiency.
