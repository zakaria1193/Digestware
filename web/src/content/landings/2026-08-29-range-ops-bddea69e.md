---
project: gcc
subsystem: range-ops
patch_id: null
tags:
- optimization
- range analysis
- compile time
commit_hash: bddea69ee406a0f68aed8f42ea7efba2d8b5883c
source_type: github
author: Aldy Hernandez
headline: 'range-ops: Infer operand equality from zero MINUS_EXPR'
tldr: Improves optimization by deducing operand equality from subtraction-equals-zero
  expressions.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `operator_minus` in `range-op-mixed.h` now exposes `op1_op2_relation`,
  enabling `register_outgoing_edges` in `gimple-range-fold.cc` to derive relations
  from any integral export, not just booleans. This allows the inference of `a ==
  b` from `a - b == 0`, even when the difference is not single-use, improving VRP
  and DOM optimizations at the cost of a 36% increase in `register_outgoing_edges`
  runtime.
primer_glossary:
- term: range-ops
  definition: A GCC optimization pass that reasons about the possible ranges of values
    for variables.
- term: MINUS_EXPR
  definition: GCC's internal representation for a subtraction operation in the GIMPLE
    intermediate language.
- term: VRP
  definition: Value Range Propagation, an optimization pass that narrows down the
    possible range of values for variables.
- term: DOM
  definition: Dominator analysis, a program analysis technique used in optimizations
    to understand control flow.
- term: GIMPLE
  definition: GCC's internal three-address intermediate representation, used after
    parsing and before optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bddea69ee406a0f68aed8f42ea7efba2d8b5883c
date: '2026-08-29'
is_stub: false
stub_reason: ''
---

This commit enhances the range-ops optimization pass by allowing it to infer operand equality from `a - b == 0` expressions. Previously, this was only possible for single-use differences, but now it supports a wider range of cases, leading to a slight increase in compile times but improved optimization in passes like VRP and DOM.
