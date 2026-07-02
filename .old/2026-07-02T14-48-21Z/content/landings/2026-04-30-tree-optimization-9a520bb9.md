---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- slp
- code quality
commit_hash: 9a520bb987d3944ed9bb09f29b0f38f319817759
source_type: github
author: Richard Biener
headline: Tree-optimization/125088 - some TLC to the new vect_bb_slp_scalar_cost
tldr: The SLP vectorization cost estimation code is refactored for clarity and to
  avoid Coverity warnings.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR tree-optimization/125088 by refactoring the
  `vect_bb_slp_scalar_cost` function in `tree-vect-slp.cc`. The changes primarily
  focus on improving the structure of the code and removing a potentially confusing
  loop construct. Additionally, `vect_nop_conversion_p` in `tree-vect-stmts.cc` is
  modified to exclude copies with memory accesses, which may impact vectorization
  decisions.
primer_general: Vectorization is a compiler optimization technique that allows multiple
  operations to be performed simultaneously on multiple data elements. SLP (Superword
  Level Parallelism) is a specific type of vectorization that looks for similar independent
  operations within a basic block. This commit improves the cost estimation logic
  used during SLP vectorization, making the code more robust and easier to understand,
  which can lead to better optimization decisions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9a520bb987d3944ed9bb09f29b0f38f319817759
date: '2026-04-30'
---

The `vect_bb_slp_scalar_cost` function, used in SLP (Superword Level Parallelism) vectorization, has been refactored to improve code clarity and avoid confusion reported by Coverity.  The refactoring simplifies the control flow around cost recording and removes a `do { } while (false)` loop that contained `continue` statements. Additionally, copies involving memory accesses are now excluded from `vect_nop_conversion_p`.
