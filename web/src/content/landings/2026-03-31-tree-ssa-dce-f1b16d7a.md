---
project: gcc
subsystem: tree-ssa-dce
patch_id: null
tags:
- optimization
- tree-ssa
- dce
- atomic
commit_hash: f1b16d7a17bf2cd8f5071e94384a0893c124e7bf
source_type: github
author: Eikansh Gupta
headline: Eliminates dead relaxed atomic loads with no LHS.
tldr: Dead relaxed atomic loads without a left-hand side are now eliminated by the
  tree-ssa-dce pass.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'This commit modifies `mark_stmt_if_obviously_necessary` in `tree-ssa-dce.cc`
  to avoid marking relaxed atomic loads (BUILT_IN_ATOMIC_LOAD_1/2/4/8/16) with no
  LHS as necessary, enabling their removal by the dead code elimination pass. The
  memory order must be compile-time-constant relaxed. search_context: GCC tree-ssa-dce
  relaxed atomic loads'
primer_general: The Dead Code Elimination (DCE) optimization pass removes code that
  does not affect the program's outcome. Atomic operations are used for thread synchronization,
  but a relaxed atomic load with no side effects can be safely removed without affecting
  program behavior. This commit optimizes code by eliminating such unnecessary atomic
  loads.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f1b16d7a17bf2cd8f5071e94384a0893c124e7bf
date: '2026-03-31'
---

Relaxed atomic loads whose results are unused have no observable effect because they provide no inter-thread synchronization guarantees. This commit adds a check to the tree-ssa-dce pass to identify and eliminate these dead atomic loads, improving code cleanliness and potentially reducing unnecessary memory traffic.
