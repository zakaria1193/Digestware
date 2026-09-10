---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- compiler-error
- optimization
commit_hash: 388aada52115970d85926c07072aeb7fce4498e7
source_type: github
author: Richard Biener
headline: Fix ICE with switch statement uninitialized variable warnings
tldr: GCC now correctly converts switch label types to match the switch index type,
  resolving an internal compiler error.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `predicate::init_from_control_deps` function in `gimple-predicate-analysis.cc`
  incorrectly assumed switch indices and case labels would have compatible types.
  This commit forces a conversion of the case label values to match the switch index's
  type, preventing an ICE that occurred during analysis of control dependencies, especially
  when warnings about uninitialized variables were active.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/388aada52115970d85926c07072aeb7fce4498e7
date: '2026-09-09'
is_stub: false
stub_reason: ''
---

An internal compiler error (ICE) occurred when the type of switch indices and case labels differed, particularly when uninitialized variable warnings were enabled. This change modifies `gimple-predicate-analysis.cc` to convert case label values to the type of the switch index, thus ensuring type consistency. A new test case `pr127262.c` is added to verify the fix.
