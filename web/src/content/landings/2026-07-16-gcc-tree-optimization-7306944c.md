---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- optimization
commit_hash: 7306944cffc49249c4947e6f9b13130986f24f5a
source_type: github
author: Andrew MacLeod
headline: Logical AND and OR operations now better infer operand ranges.
tldr: Improved range analysis for logical AND/OR operations to infer more precise
  constraints on operands.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `range-op.cc` implementation for logical operations like AND and
  OR has been augmented. Specifically, `operator_logical_and::op1_range` now handles
  the case where the result is `[0, 0]` and the operator is AND with `[1, 1]` (TRUE),
  correctly inferring that the first operand must also be `[0, 0]`. Likewise, `operator_logical_or::op1_range`
  handles the case for OR with `[0, 0]` (FALSE) yielding `[1, 1]`. This refines the
  bounds propagation capabilities of the value-range optimization pass.
primer_glossary:
- term: rangeops
  definition: A component within GCC's optimization framework that computes and propagates
    possible value ranges for variables and expressions.
- term: op1_range
  definition: A function or method within rangeops that calculates the possible range
    of values for the first operand of an operation, given the operation and the range
    of the second operand.
- term: 'TRUE'
  definition: In this context, TRUE likely represents a bitmask or value where all
    relevant bits are set, often equivalent to -1 or UINT_MAX depending on the type.
- term: 'FALSE'
  definition: In this context, FALSE likely represents a bitmask or value where all
    relevant bits are clear, equivalent to 0.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7306944cffc49249c4947e6f9b13130986f24f5a
date: '2026-07-16'
is_stub: false
stub_reason: ''
---

This update enhances GCC's `rangeops` to more accurately infer value ranges for operands involved in logical AND and OR operations. For example, it now recognizes that if `op1 & TRUE` results in `[0, 0]`, then `op1` must be `[0, 0]`. Similarly, for `op1 | FALSE` resulting in `[1, 1]`, `op1` must be `[1, 1]`. These improvements allow for tighter value range propagation, potentially enabling further optimizations.
