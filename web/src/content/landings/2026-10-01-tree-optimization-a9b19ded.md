---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
commit_hash: a9b19ded78ca2dd8f66b355b05ebbbb149c2d320
source_type: github
author: Richard Biener
headline: Vector cost model heuristic misapplied when loop iteration count is constant
tldr: GCC's vectorizer will no longer wrongly assume vectorization is profitable for
  single-iteration loops when the iteration count is already known.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The vectorizer's cost model in `tree-vect-loop.cc` has a heuristic
  to promote vectorization of loops executing only once if the per-iteration vector
  cost is cheap. This commit corrects `vect_analyze_loop_costing` to disable this
  heuristic when the number of scalar iterations is constant, as profitability is
  already evaluated over the entire execution in that scenario. This prevents misoptimizations
  where the single-iteration heuristic overrides a more accurate constant-iteration
  cost assessment.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a9b19ded78ca2dd8f66b355b05ebbbb149c2d320
date: '2026-10-01'
is_stub: false
stub_reason: ''
---

GCC's vectorizer uses a cost model heuristic that assumes vectorization is profitable even for loops that execute only once, provided the vector cost is cheap. However, this heuristic was being applied even when the loop's iteration count was constant, a case already handled by a separate profitability assessment. This commit modifies the vector cost analysis to avoid applying the single-iteration heuristic when the iteration count is constant, preventing incorrect vectorization decisions.
