---
project: gcc
subsystem: tree-vectorizer
patch_id: null
tags:
- tree-vectorizer
- cleanup
- SLP
commit_hash: 53a96b6b6d35ab730b6f227370b8858b241fcc38
source_type: github
author: Richard Biener
headline: Remove unused max_nunits field from SLP tree.
tldr: Cleans up vectorizer code by removing an unused field and related functions.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The SLP vectorizer uses `slp_tree` to represent potential vectorization
  opportunities. The `max_nunits` field within `slp_tree` tracked the maximum number
  of vector units encountered. This commit removes `max_nunits` and related functions
  like `vect_update_max_nunits` and `vect_record_max_nunits` because they are unused.
  This cleanup streamlines the vectorizer's internal representation and reduces code
  complexity, as the relevant information is now managed through other means, primarily
  `SLP_TREE_VECTYPE`.
primer_glossary:
- term: SLP
  definition: Superword Level Parallelism, an optimization technique that enables
    the compiler to identify and vectorize sequences of identical operations on different
    data elements.
- term: slp_tree
  definition: A data structure used by the GCC SLP vectorizer to represent a sequence
    of operations that can potentially be vectorized.
- term: vectorizer
  definition: A compiler component responsible for identifying opportunities to use
    SIMD (Single Instruction, Multiple Data) instructions to speed up code execution.
- term: vector units
  definition: The individual data elements (lanes) within a SIMD register that can
    be processed in parallel by a single instruction.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/53a96b6b6d35ab730b6f227370b8858b241fcc38
date: '2026-08-20'
is_stub: true
stub_reason: low_score
---

This commit removes the `max_nunits` field from the `slp_tree` structure and associated internal APIs, as it is no longer used. The `max_nunits` field was related to tracking the maximum number of units (e.g., lanes) in vector types during SLP vectorization. Its removal simplifies the vectorizer's internal data structures and code by eliminating dead code and reducing maintenance overhead.
