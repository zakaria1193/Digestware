---
project: gcc
subsystem: gcc/tree-vectorizer
patch_id: null
tags:
- gcc
- vectorization
- optimization
commit_hash: 3bdefbacdf4798a7f38876740855115f7d986c3b
source_type: github
author: Richard Biener
headline: Optimize SLP reduction group discovery with new matches[]
tldr: SLP vectorization now uses all discovered isomorphic groups for more efficient
  reduction discovery.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The SLP vectorizer in GCC identifies opportunities for loop vectorization
  by looking for independent instructions that can be combined. This commit refactors
  `vect_analyze_slp_reductions` in `tree-vect-slp.cc` to use an enhanced `matches[]`
  representation, which stores isomorphic groups discovered from `match_elt_t` instances.
  This optimization aims to improve the efficiency of finding reduction patterns within
  basic blocks, potentially enabling more aggressive vectorization.
primer_glossary:
- term: SLP
  definition: Slanted Line Processor. A compiler optimization technique that finds
    vectorization opportunities by identifying identical or similar sequences of scalar
    instructions that can be executed in parallel on vector hardware. It operates
    on the intermediate representation after loop optimizations.
- term: Reduction
  definition: In the context of loops or vectorization, a reduction operation is one
    that combines elements of a sequence into a single value, such as sum, product,
    minimum, or maximum. These patterns are common targets for optimization.
- term: Vectorizer
  definition: A compiler component responsible for transforming scalar code into vector
    code, allowing multiple data elements to be processed simultaneously using SIMD
    (Single Instruction, Multiple Data) instructions. GCC has both loop vectorizers
    and SLP vectorizers.
- term: Intermediate Representation (IR)
  definition: A data structure or code format used internally by a compiler to represent
    the source code during various stages of translation. GCC uses multiple IRs, including
    GENERIC and GIMPLE.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3bdefbacdf4798a7f38876740855115f7d986c3b
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This change enhances the SLP (Slanted Line Processor) vectorizer's ability to discover reduction groups. By utilizing all isomorphic groups found, the process becomes more efficient. The implementation includes operator overloading for match_elt_t and integer comparisons, and updates the `vect_analyze_slp_reductions` function to leverage the improved `matches[]` representation.
