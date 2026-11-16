---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop optimization
- gcc
commit_hash: 19a2172b22961d74074fb602e9b82d44ef6e1fc7
source_type: github
author: Jiawei
headline: 'tree-optimization: Fix LIM dependence cache indexing'
tldr: Corrected indexing for LIM dependence cache improves reuse of cached results.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-loop-im.cc`, the `record_loop_dependence` function's logic
  for computing the cache index was flawed. The dependence-state comparison was not
  properly parenthesized, leading to an incorrect index calculation that did not account
  for both the loop number and the dependence kind. This change corrects the expression
  to ensure the cache index accurately reflects these factors, enabling the reuse
  of previously computed dependence information for subsequent loop optimizations.
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC optimization that operates on an intermediate representation
    called GENERIC trees, which are higher-level than GIMPLE.
- term: LIM
  definition: Loop Invariant Motion, an optimization technique that moves computations
    out of loops if their results do not change within the loop.
- term: dependence cache
  definition: A data structure used by the compiler to store and quickly retrieve
    information about data dependencies between loop iterations or program statements.
- term: Loop Invariant Motion (LIM)
  definition: An optimization technique that identifies computations within a loop
    whose results are constant across all iterations and moves them outside the loop.
- term: tree-ssa
  definition: A GCC optimization framework that uses the SSA (Static Single Assignment)
    form on the GENERIC tree intermediate representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/19a2172b22961d74074fb602e9b82d44ef6e1fc7
date: '2026-11-15'
is_stub: false
stub_reason: ''
---

This commit fixes an issue with the LIM (Loop Invariant Motion) dependence cache indexing within GCC's tree optimization passes. By correctly parenthesizing the dependence-state comparison, the cache index now accurately includes the loop number and dependence kind. This allows for more effective reuse of cached dependence results, improving optimization efficiency.
