---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- SLP
commit_hash: d47f2b280cb4aaf4368d79bd52d03c1056b536a9
source_type: github
author: Richard Biener
headline: tree-optimization/128132 - induction SLP with different induction kinds
tldr: Fixes SLP vectorization to reject groups with differing induction kinds.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch provides a minimal fix for PR128132 by addressing how `vect_get_and_check_slp_defs`
  handles differing induction kinds. The `vectorizable_induction` function now explicitly
  rejects SLP groups where the induction subtypes are effectively different. This
  prevents the SLP vectorizer from incorrectly grouping instructions that rely on
  distinct induction patterns, ensuring more accurate vectorization of loops.
primer_glossary:
- term: SLP
  definition: Superword-Level Parallelism. A compiler optimization technique that
    finds consecutive, independent instructions operating on different data elements
    and combines them into a single vector instruction.
- term: vectorization
  definition: The process of transforming scalar code (operating on single data items)
    into vector code (operating on multiple data items simultaneously using SIMD instructions).
- term: induction variable
  definition: A variable in a loop whose value changes by a constant amount in each
    iteration, commonly used for loop control and array indexing.
- term: tree-optimization
  definition: A phase in the GCC compiler pipeline where optimizations are performed
    on the GIMPLE intermediate representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d47f2b280cb4aaf4368d79bd52d03c1056b536a9
date: '2026-10-26'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in Superword-Level Parallelism (SLP) vectorization where groups of instructions with different induction types were incorrectly processed. The `vectorizable_induction` function now rejects SLP groups that exhibit varying induction subtypes, preventing potential misvectorization. This change ensures that SLP vectorization correctly handles induction variables within loops and improves the robustness of the vectorization pass.
