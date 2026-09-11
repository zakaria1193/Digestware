---
project: gcc
subsystem: tree-ssa-threadbackward
patch_id: null
tags:
- optimization
- performance
- backthreader
commit_hash: cea04b88c16b25f0119062cc65db9ab778c4e24b
source_type: github
author: Aldy Hernandez
headline: 'backthreader: compute path profitability incrementally'
tldr: backthreader computes path profitability incrementally, improving performance
  by 7.8%.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The backthreader is a GCC optimization pass that aims to improve instruction-level
  parallelism by reordering instructions. This commit refactors the path profitability
  computation within `tree-ssa-threadbackward.cc`. Previously, path statistics were
  recomputed entirely for each node explored during path analysis. The new incremental
  approach uses `push_bb` and `pop_bb` to maintain accumulated statistics for the
  current path, significantly reducing overhead and boosting performance. This change
  primarily affects the `back_threader::find_paths_to_names` function and related
  profitability checks.
primer_glossary:
- term: backthreader
  definition: A GCC optimization pass that reorders instructions to improve parallelism.
    It analyzes execution paths to determine the most profitable reordering strategies.
- term: path profitability
  definition: A metric used by the backthreader pass to evaluate how beneficial reordering
    instructions along a particular execution path would be. It considers factors
    like instruction counts and potential for parallelism.
- term: incremental computation
  definition: A method of updating a value by applying changes based on the previous
    value, rather than recalculating it from scratch. This is often more efficient
    for complex calculations.
- term: instruction-level parallelism (ILP)
  definition: The ability of a processor to execute multiple instructions simultaneously
    within a single clock cycle. Optimization passes like the backthreader aim to
    expose and increase ILP.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cea04b88c16b25f0119062cc65db9ab778c4e24b
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

The backthreader pass now computes path profitability incrementally, avoiding expensive recomputation at each node. This change speeds up the threader by 7.8% while ensuring identical assembly output and identical path/stats compared to the previous version. The implementation was refined to use new push_bb and pop_bb functions and an accumulated stats mechanism.
