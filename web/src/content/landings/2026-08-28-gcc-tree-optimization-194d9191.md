---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- vectorization
- optimization
commit_hash: 194d91912cb3fc86dcce7d13d2239f46ab988b03
source_type: github
author: Richard Biener
headline: Simplify BB reduction group splitting for vectorization
tldr: Vectorizer now picks the largest isomorphic subset for BB reduction, improving
  efficiency.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change in `tree-vect-slp.cc` modifies `vect_build_slp_instance`
  to select the largest isomorphic subset for BB reduction vectorization. Previously,
  it might not have picked the optimal group. This leverages improvements in `matches[]`
  to directly vectorize larger, more suitable instruction groups, simplifying the
  overall BB vectorization strategy.
primer_glossary:
- term: BB reduction
  definition: A basic block (BB) reduction refers to a pattern of straight-line code
    within a function. Vectorization aims to replace these sequences with a single
    instruction that operates on multiple data elements simultaneously.
- term: isomorphic
  definition: In this context, isomorphic means that a group of instructions has the
    same structure and can be mapped to a vector operation. The vectorizer looks for
    such patterns to replace scalar operations with vector ones.
- term: vectorization
  definition: The process of converting scalar operations (operating on single data
    elements) into vector operations (operating on multiple data elements simultaneously)
    to improve performance on suitable hardware.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/194d91912cb3fc86dcce7d13d2239f46ab988b03
date: '2026-08-28'
is_stub: false
stub_reason: ''
---

The GCC vectorizer simplifies the process of splitting basic blocks (BBs) for loop vectorization. It now identifies and selects the largest isomorphic subset of instructions within a BB reduction, allowing for more direct vectorization. This change enhances the efficiency of code generation by improving how instruction groups are chosen for vector processing.
