---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- gcc
- compiler
commit_hash: b484690a29147fa190ccb74e0253b2ac89a4ee6d
source_type: github
author: Andrew MacLeod
headline: Ranger stmt prefill processes dependencies first
tldr: Fixes deep recursion in the Ranger optimization pass by correctly ordering dependency
  processing.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The gimple_ranger::prefill_stmt_dependencies function in gimple-range.cc
  previously failed to account for PHI argument dependencies, leading to incorrect
  processing order and potential infinite recursion. This commit implements a DFS
  stack simulation to properly order operands, resolving PR tree-optimization/125758.
primer_glossary:
- term: Ranger
  definition: A GCC optimization pass that analyzes and transforms code based on value
    ranges, aiming to simplify expressions and improve performance.
- term: PHI argument
  definition: In SSA (Static Single Assignment) form, a PHI node represents a value
    that can come from multiple different control flow paths. It selects which predecessor's
    value to use based on the path taken.
- term: DFS
  definition: Depth-First Search, an algorithm for traversing or searching tree or
    graph data structures. It explores as far as possible along each branch before
    backtracking.
- term: gimple-range.cc
  definition: The GCC source file containing the implementation of the Ranger optimization
    pass and its related data structures and algorithms.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b484690a29147fa190ccb74e0253b2ac89a4ee6d
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

The Ranger optimization pass previously mishandled dependencies for PHI arguments, potentially leading to deep recursion and negating its intended benefits. This change revises the prefill logic to perform a Depth-First Search (DFS) on the dependency stack, ensuring all operands are processed correctly before proceeding. This resolves issues related to incorrect ordering and improves the pass's stability.
