---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- omp
- vectorization
- bugfix
commit_hash: c06252ee5215bfb58ad97a8636234fc67318e052
source_type: github
author: Richard Biener
headline: Fix ICE with OMP SIMD clone mask types.
tldr: Resolves an ICE when SIMD clone mask arguments have BLKmode vector types.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch addresses an ICE in `tree-vect-stmts.cc` during the handling
  of SIMD clone mask arguments when the mask type has `BLKmode`. The `vectorizable_simd_clone_call`
  function previously failed to construct the correct mask type in such scenarios.
  For non-`VECTOR_BOOLEAN_TYPE_P` masks, it now uses `truth_type_for`, which correctly
  handles `BLKmode`. For `VECTOR_BOOLEAN_TYPE_P` masks, it reconstructs the mask type
  using a vector mode that matches the `aarch64` approach. Additionally, mask mode
  verification for inbranch clones used in not-inbranch contexts has been improved.
primer_glossary:
- term: tree-optimization
  definition: A phase in the GCC compiler where the intermediate representation (GIMPLE's
    'tree' format) is analyzed and transformed to improve code efficiency.
- term: ICE
  definition: Internal Compiler Error, indicating a bug within the compiler itself.
- term: OMP SIMD
  definition: OpenMP directives that allow loops to be vectorized, enabling SIMD (Single
    Instruction, Multiple Data) instructions for parallel execution on multiple data
    elements simultaneously.
- term: mask argument
  definition: In SIMD operations, a control vector that determines which elements
    of data vectors are operated on.
- term: BLKmode
  definition: A GCC internal mode representing a block of data, often used for complex
    types or unaligned memory access, distinct from standard vector types.
- term: VECTOR_BOOLEAN_TYPE_P
  definition: A macro or function predicate in GCC that checks if a given type is
    a vector boolean type, used for SIMD masks.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c06252ee5215bfb58ad97a8636234fc67318e052
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This commit corrects an internal compiler error (ICE) that occurred in GCC's tree-optimization passes when the mask argument for an OMP SIMD clone had a vector type in `BLKmode`. The compiler now correctly handles these cases by using `truth_type_for` for non-`VECTOR_BOOLEAN_TYPE_P` modes and by reconstructing mask types with a matching vector mode for `VECTOR_BOOLEAN_TYPE_P` cases, similar to how `aarch64` is handled. This ensures that SIMD vectorization with OMP directives remains robust.
