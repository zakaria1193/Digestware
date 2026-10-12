---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- bugfix
commit_hash: 9514a728a62cb82fd05b2db97717525e98ebdd53
source_type: github
author: Richard Biener
headline: tree-optimization/127705 - access violation with SCC copy
tldr: Fixes an access violation in the SLP vectorization pass when copying the Strongly
  Connected Component (SCC) for scheduling.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch fixes PR tree-optimization/127705, related to the `vect_schedule_scc`
  function in `tree-vect-slp.cc`. The function is responsible for scheduling operations
  within a loop after SLP vectorization. The bug involved a botched attempt to save
  the SCC data structure for later use, leading to an access violation. The fix ensures
  that the SCC is correctly copied and preserved, allowing the scheduling of vectorized
  loop components to proceed without crashing.
primer_glossary:
- term: SLP vectorization
  definition: Short-Loop Parallelism vectorization, an optimization technique in GCC
    that identifies and vectorizes loops consisting of straight-line code (superwords).
- term: tree-optimization
  definition: The phase in GCC where optimizations are performed on the Tree Intermediate
    Representation (IR).
- term: SCC
  definition: Strongly Connected Component, a part of a graph where every vertex is
    reachable from every other vertex. In optimization, it can represent a loop or
    a set of mutually dependent operations.
- term: access violation
  definition: A runtime error that occurs when a program attempts to access a memory
    location that it is not allowed to access.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9514a728a62cb82fd05b2db97717525e98ebdd53
date: '2026-10-06'
is_stub: false
stub_reason: ''
---

This commit addresses a bug in the SLP (Short-Loop Parallelism) vectorization pass that caused an access violation. The issue occurred during the process of saving the Strongly Connected Component (SCC) for later setting of the scheduling result across all components. The fix corrects how the SCC is copied, resolving the crash and ensuring proper scheduling of vectorized code.
