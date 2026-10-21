---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- optimization
- SSA
commit_hash: f5af5512d34fbf5c30b1f450fb199cf73515f4df
source_type: github
author: Richard Biener
headline: SSA corruption fixed for SLP vectorization of abnormal vectors
tldr: Fixes SSA corruption in SLP vectorization by excluding abnormal vector definitions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit revises `vect_build_slp_tree_3` in `tree-vect-slp.cc` to
  prevent SLP (Superword Level Parallelism) from processing certain abnormal vector
  definitions. These definitions, if included, can lead to new uses that interfere
  with vector coalescing, causing SSA corruption. The change ensures that such cases
  are excluded, maintaining SSA invariants during vectorization. This is relevant
  for loop vectorization passes, particularly when dealing with non-standard vector
  types or operations.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f5af5512d34fbf5c30b1f450fb199cf73515f4df
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

This change prevents SSA corruption that could occur during SLP (Straight-Line-Pattern) vectorization. By excluding existing abnormal vector definitions from the SLP processing, the compiler avoids introducing new uses that might prevent vector coalescing. This resolves a specific issue identified in PR tree-optimization/128013 and ensures correct vectorization for certain code patterns.
