---
project: gcc
subsystem: match/forwprop
patch_id: null
tags:
- optimization
- gcc
- match
- forwprop
commit_hash: a8677a123a62db69fbde06c7530fb2c0ee3e09c4
source_type: github
author: Andrea Pinski
headline: 'match/forwprop: Remove unused shift capture from mul_carry_cross_sum'
tldr: Unused shift capture removed from match/forwprop's mul_carry_cross_sum pattern.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In GCC's `tree-ssa-forwprop.cc`, pattern matching is used to identify
  and transform arithmetic operations. The `mul_carry_cross_sum` pattern in `match.pd`
  previously included a shift capture that was not utilized in validity checks. Removing
  this capture simplifies the pattern and is intended to facilitate the optimization
  of operations like `cond^` versions of `mul_carry_cross_sum`, potentially allowing
  earlier optimization passes like `forwprop1` to trigger for relevant test cases
  such as `long-mul-two-carry.c`.
primer_glossary:
- term: match/forwprop
  definition: Refers to pattern matching and forward propagation optimizations within
    the GCC compiler, specifically within the tree-ssa (Static Single Assignment)
    framework.
- term: mul_carry_cross_sum
  definition: A specific pattern or operation identified by the GCC match-compile
    system, likely related to multiplication with carry-out and sum calculation, possibly
    for large integer arithmetic.
- term: Shift capture
  definition: In the context of GCC's pattern matching (match.pd), this refers to
    capturing a specific shift operand or value associated with an operation.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation in compilers
    where every variable is assigned exactly once, simplifying many optimization passes.
- term: forwprop1
  definition: Likely refers to the first iteration or stage of the forward propagation
    optimization pass within the GCC compiler's SSA framework.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a8677a123a62db69fbde06c7530fb2c0ee3e09c4
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This change removes an unused shift capture from the `mul_carry_cross_sum` pattern in the `match/forwprop` subcomponent. This cleanup is a step towards enabling earlier optimization of specific patterns, like those found in `long-mul-two-carry.c`, by simplifying the pattern matching logic and allowing for `cond^` versions of such operations.
