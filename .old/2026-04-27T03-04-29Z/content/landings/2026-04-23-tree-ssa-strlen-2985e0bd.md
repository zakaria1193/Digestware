---
project: gcc
subsystem: tree-ssa-strlen
patch_id: null
tags:
- optimization
- tree-ssa
- gimple
- string length
commit_hash: 2985e0bd9b2aee03a932e5ab406523a95c04de5f
source_type: github
author: Avinal Kumar
headline: Use gimple_build and gimple_convert_to_ptrofftype in strlen pass.
tldr: The strlen pass now uses gimple_build and gimple_convert_to_ptrofftype, modernizing
  the code.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The tree-ssa-strlen pass determines the lengths of strings at compile
  time. This commit refactors the code to use `gimple_convert_to_ptrofftype` and `gimple_build`
  instead of the older `convert_to_ptrofftype`, `force_gimple_operand_gsi`, and `gimple_build_assign`.  This
  simplifies the code and doesn''t directly impact performance. search_context: GCC
  tree-ssa-strlen inter-procedural string length'
primer_general: The strlen optimization pass attempts to determine the length of strings
  at compile time.  This allows the compiler to replace calls to `strlen` with constants,
  potentially improving performance. GIMPLE is the simplified intermediate representation
  (IR) used by GCC during compilation, after parsing and lowering the source code.
  This commit modernizes the code responsible for building GIMPLE statements within
  the strlen pass.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2985e0bd9b2aee03a932e5ab406523a95c04de5f
date: '2026-04-23'
---

This change replaces older functions like `convert_to_ptrofftype`, `force_gimple_operand_gsi`, and `gimple_build_assign` with `gimple_convert_to_ptrofftype` and `gimple_build` in the tree-ssa-strlen pass. This simplifies the code and improves maintainability by using more modern GIMPLE building functions.
