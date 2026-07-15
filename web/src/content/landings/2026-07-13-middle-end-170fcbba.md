---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- vectorization
- optimization
commit_hash: 170fcbba4c97ea40750cc5c2fd0eb787311085f0
source_type: github
author: Hu, Lin1
headline: Use correct mode for masked cbranch operand
tldr: Fixes an assertion failure related to vector boolean constants in masked operations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The function `emit_cmp_and_jump_insns` in `optabs.cc` previously used
  `GET_MODE(expand_normal(masked_op))` to determine the mode for masked operations.
  When `masked_op` expanded to a `CONST_INT` representing a vector boolean constant,
  this could lead to `VOIDmode`. The fix changes this to `TYPE_MODE(TREE_TYPE(masked_op))`,
  correctly using the mode of the operand's type, which resolves the assertion `mode
  != VOID_mode` in `maybe_legitimize_operand`.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/170fcbba4c97ea40750cc5c2fd0eb787311085f0
date: '2026-07-13'
is_stub: false
stub_reason: ''
---

This change corrects how the mode for masked cbranch operands is determined. Previously, it used GET_MODE on an expanded masked operation, which could incorrectly result in VOIDmode for vector boolean constants. The fix adjusts this to use TYPE_MODE of the operand, ensuring constants are materialized in the correct mask mode and preventing an assertion failure.
