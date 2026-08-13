---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- optimization
- SLP
commit_hash: adc20f13b60f90c6a55d46fc6be37dfb9f4b86a0
source_type: github
author: Richard Biener
headline: SLP subgraph merging handles overlapping vector parts
tldr: SLP vectorization now merges subgraphs that overlap in low/high parts or use
  VEC_PERM, fixing SSA verification failures.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch enhances SLP vectorization by improving subgraph merging.
  It introduces `vect_cse_gather_part_starts` and `vect_cse_slp_node_parts` to handle
  merging of SLP nodes that overlap in `lowpart` or `highpart` extractions, or through
  `VEC_PERM` nodes. The logic correctly identifies overlapping parts of SLP nodes
  without requiring full vector equality, addressing issues like those in PR126099
  where schedule verification would elide graph entries due to these overlaps. It
  specifically targets cases where `vectorizable_slp_permutation` restrictions would
  prevent merging.
primer_glossary:
- term: SLP
  definition: Superword Level Parallelism, a compiler optimization technique that
    finds instructions operating on scalars that can be vectorized to operate on multiple
    data elements simultaneously.
- term: VEC_PERM
  definition: A GIMPLE operation representing a vector permutation, used to rearrange
    elements within a vector.
- term: SSA
  definition: Static Single Assignment form, an intermediate representation where
    every variable is assigned exactly once, simplifying many compiler analyses and
    optimizations.
- term: lowpart/highpart
  definition: Refers to the lower or higher-order bits/elements of a larger data type
    or vector, often relevant in type promotions or vector element extraction.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/adc20f13b60f90c6a55d46fc6be37dfb9f4b86a0
date: '2026-08-03'
is_stub: false
stub_reason: ''
---

This commit enhances SLP (Superword Level Parallelism) vectorization by enabling the merging of subgraphs that overlap in their low or high parts, or through full vector copies using `VEC_PERM` nodes. It introduces mechanisms to build reverse mappings for scalar statements to SLP nodes and checks for containment within candidate subgraphs. This resolves issues in testcases like PR126053 and PR126099, preventing SSA verification failures by correctly handling overlapping vector data. New testcases are added to verify these improvements.
