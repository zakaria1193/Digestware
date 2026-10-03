---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop
- bugfix
commit_hash: 2ae9740dde8225371d3791a71b99d52ef686e2cc
source_type: github
author: Richard Biener
headline: 'tree-optimization: Fix missed FRE in loop'
tldr: Improves loop optimizations by ensuring FRE does not abort prematurely on PHI
  nodes in CFG cycles.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `ssa-fre.cc` pass, specifically `maybe_skip_until`, was too aggressive
  in aborting traversals when encountering PHI nodes in CFG cycles due to a PR54498
  fix. This commit refines the logic to correctly handle re-visiting a PHI node within
  a loop, preventing premature aborts and enabling further optimizations like constant
  propagation for `__builtin_constant_p`.
primer_glossary:
- term: FRE
  definition: Free Register Elimination, a compiler optimization pass that identifies
    and removes unnecessary register allocations.
- term: PHI node
  definition: In SSA (Static Single Assignment) form, a PHI node is used to merge
    values from different control flow paths. It selects one of its incoming values
    based on which path was taken to reach it.
- term: CFG
  definition: Control Flow Graph, a representation of a program's execution flow where
    nodes are basic blocks and edges represent possible transfers of control.
- term: SSA
  definition: Static Single Assignment, an intermediate representation property where
    every variable is assigned exactly once. PHI nodes are used to resolve merges
    at join points.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2ae9740dde8225371d3791a71b99d52ef686e2cc
date: '2026-10-02'
is_stub: false
stub_reason: ''
---

This commit fixes a missed optimization in the Free Register Elimination (FRE) pass for loops. A previous correctness fix caused FRE to incorrectly abort when encountering a loop PHI node within a control flow graph (CFG) cycle. The change modifies the `maybe_skip_until` function to stop the traversal when it revisits the original PHI node, allowing constant propagation and avoiding the bug.
