---
project: gcc
subsystem: gcc/ssa_operands
patch_id: null
tags:
- optimization
- ssa
- gimple
- switch
commit_hash: 8c8f688fd8d936859dda5cd2eea88f0b22b6c189
source_type: github
author: Andrew Pinski
headline: 'ssa_operands: Speed up GIMPLE_SWITCH handling'
tldr: GCC's SSA operand scanner now processes only the index operand of GIMPLE_SWITCH
  statements, improving performance.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit optimizes the ``operands_scanner::parse_ssa_operands``
  function in ``tree-ssa-operands.cc`` by only processing the index operand of a ``GIMPLE_SWITCH``
  statement. The cases within the switch statement are represented as ``CASE_LABEL_EXPR``
  nodes, which are already skipped by the ``get_expr_operands`` method. By avoiding
  redundant scanning of these case labels, the commit improves the performance of
  the SSA operand scanner. This is a localized optimization that is also a step towards
  future changes to the representation of ``GIMPLE_SWITCH``.
primer_general: GCC's internal representation of code, GIMPLE, uses Single Static
  Assignment (SSA) form during optimization.  The ``ssa_operands`` pass analyzes the
  operands of GIMPLE statements to identify optimization opportunities. ``GIMPLE_SWITCH``
  statements are used to implement switch statements in C/C++.  This commit optimizes
  the scanning of ``GIMPLE_SWITCH`` operands by skipping the case labels, as they
  are already handled elsewhere.  This optimization improves the performance of the
  SSA analysis, potentially leading to faster compilation times.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8c8f688fd8d936859dda5cd2eea88f0b22b6c189
date: '2026-05-15'
is_stub: false
---

The ``operands_scanner::parse_ssa_operands`` function now only processes the index operand of ``GIMPLE_SWITCH`` statements, skipping the case labels.  Since the case labels are skipped anyway, this change reduces the amount of work performed by the operand scanner, leading to faster compilation times. This change is also presented as a preliminary step in modifying ``GIMPLE_SWITCH`` slightly.
