---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler bug
commit_hash: 7da4eb256f169fdc6bf3849b247d81f2e9404eb3
source_type: github
author: Philipp Tomsich
headline: Perform inverse converted +- lookup in Value Numbering
tldr: Fixes incorrect code generation for arithmetic operations in Value Numbering.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The value numbering pass (VN) in GCC normalizes expressions. Previously,
  it performed a rewrite for (T)a +- X to (T)(a +- X') assuming no overflow, which
  was incorrect if the original program didn't execute the narrow operation. This
  commit reverts that rewrite and instead implements the equivalence by looking up
  the narrow operation `a +- X'` in `visit_nary_op` and converting its result. This
  ensures the equivalence is established regardless of expression order and is valid
  for sign changes and widening conversions where the narrow operation dominates.
primer_glossary:
- term: Value Numbering (VN)
  definition: A compiler optimization pass that identifies and merges equivalent expressions.
    It assigns a unique number (value number) to each distinct expression, enabling
    the reuse of computed values and the elimination of redundant calculations.
- term: Intermediate Representation (IR)
  definition: A representation of the program used internally by the compiler during
    various optimization and transformation stages. GCC uses several forms, including
    GIMPLE.
- term: ILP32
  definition: A data model where integers and pointers are 32 bits wide. This contrasts
    with LP64 where pointers are 64 bits and integers can be 32 or 64 bits.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7da4eb256f169fdc6bf3849b247d81f2e9404eb3
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

This commit corrects an issue in Value Numbering where an arithmetic operation was assumed to not overflow, leading to incorrect code generation for certain conversions. The fix adjusts how these operations are processed to ensure they are handled correctly, regardless of the order they appear in the intermediate representation. This change also broadens the applicability of the optimization to include sign changes and targets like ILP32.
