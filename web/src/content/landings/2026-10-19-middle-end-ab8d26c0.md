---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- optimization
- aliasing
- stack analysis
commit_hash: ab8d26c0d68f49841a8225be53a7f947fb664476
source_type: github
author: Richard Biener
headline: Fix stack variable conflicts with addresses passed through PHI nodes.
tldr: Correctly handles stack variable conflicts when addresses are live via PHI nodes
  in control flow graphs.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `add_scope_conflicts_1` pass in GCC's middle-end analyzes stack
  variable aliasing. A recent change incorrectly used `visit_op` instead of `visit_conflict`
  for PHI results, causing conflicts to be missed if a variable's address only entered
  a block via a PHI argument. This commit reverts to using `visit` (which calls `visit_conflict`
  in conflict-generation mode) for PHI results, fixing a bug where variables in single-predecessor
  blocks with PHI inputs weren't properly checked against pre-existing live variables,
  leading to incorrect store operations.
primer_glossary:
- term: PHI node
  definition: A construct in Static Single Assignment (SSA) form that merges values
    from different control flow paths. It represents a variable that has multiple
    definitions depending on which path was taken to reach it.
- term: Stack variable
  definition: A variable allocated on the program's call stack, typically local variables
    within functions.
- term: Control flow graph (CFG)
  definition: A representation of all execution paths in a program, where nodes are
    basic blocks (sequences of code with no branches in or out except at the ends)
    and edges represent possible transfers of control.
- term: Live variable
  definition: A variable whose value might be used in the future before being redefined.
    In the context of conflict detection, it refers to variables whose memory locations
    are currently considered potentially active.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ab8d26c0d68f49841a8225be53a7f947fb664476
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This commit resolves an issue where stack variables could incorrectly conflict with other variables when their addresses were passed through PHI nodes. Previously, the analysis missed recording conflicts in certain single-predecessor blocks, leading to potential data corruption. The fix restores the correct conflict detection mechanism for PHI results, ensuring accurate aliasing information.
