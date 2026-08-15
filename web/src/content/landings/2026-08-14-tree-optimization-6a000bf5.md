---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- PHI nodes
commit_hash: 6a000bf53e6f42cff3774822227f47e39d2b76d5
source_type: github
author: Richard Biener
headline: Verify SLP schedule also for PHIs
tldr: Ensures SLP vectorizer correctly handles PHI nodes in scheduled code.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect_schedule_slp_node` function in `tree-vect-slp.cc` is responsible
  for scheduling basic blocks for SLP vectorization. This change adds a verification
  step to ensure that the scheduled position dominates all incoming edges to PHI nodes
  within the block. This is crucial because PHI nodes merge values from different
  control flow paths, and their operands must be available at the point of the PHI.
primer_glossary:
- term: SLP
  definition: Sliding Window Parallelization, a compiler optimization technique that
    identifies and vectorizes independent instructions within a basic block by treating
    them as a 'sliding window'.
- term: PHI node
  definition: In SSA (Static Single Assignment) form, a PHI node is used to merge
    values from different control flow paths. It represents a value that could have
    come from one of several predecessors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6a000bf53e6f42cff3774822227f47e39d2b76d5
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This commit enhances the SLP (Sliding Window Parallelization) vectorizer to correctly verify scheduling for PHI nodes. It ensures that the insertion place of the schedule dominates the PHI argument edges. This fix prevents potential issues with vectorization when PHI nodes are involved and includes a new test case.
