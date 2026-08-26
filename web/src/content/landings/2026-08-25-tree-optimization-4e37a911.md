---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
commit_hash: 4e37a91129de4dab6ef37a6b432c565def1ba9f4
source_type: github
author: Richard Biener
headline: Fix outer loop vectorization data reference analysis.
tldr: GCC's vectorizer now correctly analyzes data references for outer loop vectorization
  by using MEM_REF instead of INDIRECT_REF.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `vect_analyze_data_refs` function in `tree-vect-data-refs.cc` previously
  constructed an `INDIRECT_REF` to represent a data reference within the innermost
  loop for outer loop vectorization analysis. This led to issues with type and alignment
  analysis. This commit changes the construction to use `MEM_REF` while preserving
  the original `DR_REF` type, which is more appropriate for representing memory accesses
  and allows for better analysis of loop-carried dependencies relevant to vectorization.
primer_glossary:
- term: vectorization
  definition: An optimization technique that allows the compiler to use special SIMD
    (Single Instruction, Multiple Data) instructions to perform the same operation
    on multiple data elements simultaneously.
- term: outer loop vectorization
  definition: A vectorization strategy where the compiler attempts to vectorize an
    outer loop, potentially enabling more data parallelism than inner loop vectorization.
- term: MEM_REF
  definition: An RTX (representation RTX) code in GCC representing a memory reference,
    typically used for accesses to memory locations.
- term: INDIRECT_REF
  definition: An RTX code in GCC representing an indirect memory reference, often
    used when an address is computed dynamically.
- term: DR_REF
  definition: Likely refers to a data reference information structure used within
    GCC's data-reference analysis for loops.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4e37a91129de4dab6ef37a6b432c565def1ba9f4
date: '2026-08-25'
is_stub: false
stub_reason: ''
---

GCC's vectorizer has been fixed to correctly analyze data references for outer loop vectorization. The previous implementation used `build_fold_indirect_ref`, which led to incorrect type and alignment analysis. This change replaces it with a `MEM_REF` of the original `DR_REF` type, enabling more accurate analysis of the innermost loop's behavior. A new test case, `pr127049.C`, is included to verify the fix.
