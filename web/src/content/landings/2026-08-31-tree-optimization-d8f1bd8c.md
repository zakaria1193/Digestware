---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- bugfix
commit_hash: d8f1bd8c34a289de0810178d897cb246ce2033cf
source_type: github
author: Richard Biener
headline: Fixes incorrect lane calculation for vector reductions.
tldr: Corrects lane calculation in vectorizer to fix wrong code for reduction operations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The vectorizer's `vect_create_constant_vectors` and related functions
  were incorrectly computing the number of excess lanes for lane-reducing reductions.
  This commit adjusts the API of `vect_get_num_copies_for_invariant` to ensure its
  poly computation is constant and that it correctly outputs the number of excess
  lanes. This resolves PR126998.
primer_glossary:
- term: vectorizer
  definition: A compiler component that automatically transforms loops and other code
    constructs to use SIMD (Single Instruction, Multiple Data) instructions, which
    can operate on multiple data elements simultaneously for improved performance.
- term: lane-reducing reduction
  definition: A type of reduction operation within a vector loop where the results
    from multiple lanes (parallel computations) are combined into a single value.
    Examples include sum or dot product.
- term: poly computation
  definition: Refers to polynomial computations, often used in compiler optimizations
    to express relationships between variables or code transformations in a mathematical
    form.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d8f1bd8c34a289de0810178d897cb246ce2033cf
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This commit fixes an issue in the vectorizer where the calculation of excess lanes for lane-reducing reductions was incorrect. The poly computation for the number of copies for an invariant value is now ensured to be constant, resolving wrong code in vectorized reduction operations. A new test case is added to verify the fix.
