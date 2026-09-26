---
project: gcc
subsystem: gcc/cselim
patch_id: null
tags:
- optimization
- regression
- libgomp
commit_hash: bfdd3d3d8b6877435898c89393177bbcbd713309
source_type: github
author: Thomas Schwinge
headline: 'cselim: Skip store replacement for certain conditional stores'
tldr: Fixes a regression in conditional store optimization that incorrectly reduced
  loop dependency counts.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `cond_if_else_store_replacement_limited` optimization in cselim
  was too aggressive in factoring out stores in conditional branches. This commit
  adjusts the optimization to skip factoring when stores occur on both sides of an
  if-else, preventing a regression in loop dependency analysis seen in `libgomp.graphite/force-parallel-8.c`.
primer_glossary:
- term: cselim
  definition: The conditional select elimination optimization pass in GCC, responsible
    for simplifying conditional assignments.
- term: libgomp
  definition: GCC's OpenMP implementation, providing parallel execution support.
- term: loop dependency
  definition: A situation where one iteration of a loop depends on the result of a
    previous iteration, affecting parallelization potential.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bfdd3d3d8b6877435898c89393177bbcbd713309
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

This commit reverts a change in the cselim pass that affected conditional store optimizations. The previous change caused a regression in a libgomp test case by incorrectly reducing the number of loops carrying no dependency. The fix re-enables the previous behavior for certain conditional stores, ensuring correct analysis of loop dependencies.
