---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop-optimization
- signed-arithmetic
commit_hash: e90e0f66051d338c1950d2cc9e36967552d75c3a
source_type: github
author: Shivam Gupta
headline: 'tree-optimization: Recognize CLZ loop for signed non-negative values.'
tldr: Compiler now recognizes CLZ (count leading zeros) optimization for loops involving
  signed non-negative values.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-loop-niter.cc` pass, specifically `number_of_iterations_cltz`
  and `number_of_iterations_cltz_complement`, now correctly identifies opportunities
  for CLZ optimization when signed arithmetic right shifts operate on non-negative
  values. This is achieved by relaxing the `TYPE_UNSIGNED` restriction in `is_rshift_by_1`
  and introducing range analysis (`range_on_edge`) to verify the non-negativity of
  the loop's preheader input. This fixes PR tree-optimization/125734.
primer_glossary:
- term: CLZ
  definition: Count Leading Zeros. An instruction that counts the number of zero bits
    from the most significant bit to the first set bit.
- term: arithmetic right shift
  definition: A right bit shift operation that preserves the sign bit of the value.
    For non-negative numbers, it is equivalent to a logical right shift.
- term: GENERIC
  definition: GCC's first intermediate representation, a tree-based representation
    of the program.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned exactly once, simplifying many analyses and optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e90e0f66051d338c1950d2cc9e36967552d75c3a
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

The compiler's loop iteration counting has been improved to recognize Count Leading Zeros (CLZ) optimizations for loops that use signed arithmetic right shifts on non-negative values. Previously, a strict unsigned type check prevented this optimization. The change modifies the `is_rshift_by_1` function and adds non-negativity checks to loop iteration counting, enabling more efficient code generation for these cases.
