---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- ivopts
- ssa
- uninitialized memory
commit_hash: d84a91bbd60bfabc1cd2dac6aae10a427a770627
source_type: github
author: Richard Biener
headline: Tree-optimization/124947 - IVOPTs emits uninit use
tldr: GCC's IVOPTs pass now avoids using induction variables based on undefined SSA
  variables, preventing uninitialized memory access.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit fixes a bug in GCC's IVOPTs pass, specifically when dealing
  with comparisons involving induction variables. The ``may_eliminate_iv`` function
  is modified to ensure that the candidate induction variable does not involve undefined
  SSA variables. This prevents the generation of code that could lead to undefined
  behavior due to the use of uninitialized memory.
primer_general: Compilers use various optimization techniques to improve the performance
  of generated code.  Induction variable optimization is one such technique, where
  the compiler identifies variables that change in a predictable way within a loop
  and replaces them with more efficient calculations. This commit fixes a bug where
  the optimization could lead to the use of uninitialized values. The fix ensures
  that the compiler only uses valid, defined variable values during this optimization,
  preventing potential issues.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d84a91bbd60bfabc1cd2dac6aae10a427a770627
date: '2026-04-21'
---

The IVOPTs (Induction Variable Optimization) pass in GCC could previously generate code that used uninitialized SSA variables when rewriting a comparison using an induction variable. This commit prevents IVOPTs from using candidate induction variables that involve undefined SSA variables.  This avoids potential uninitialized memory access and improves code reliability.
