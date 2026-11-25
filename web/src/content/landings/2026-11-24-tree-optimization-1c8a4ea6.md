---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- restrict
- alias analysis
commit_hash: 1c8a4ea630bfbf15a0b2f41a970c09fb38e68fdc
source_type: github
author: Richard Biener
headline: 'tree-optimization: Avoid incorrect restrict info on vectorized references'
tldr: Ensures restrict qualifiers are correctly handled for vectorized memory references.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The vectorizer's data reference handling in `tree-vect-data-refs.cc`
  and `tree-vect-stmts.cc` has been updated to ensure consistency of `restrict` qualifiers
  within a data reference (DR) group before copying. The `vect_copy_ref_info` function
  now takes `stmt_vec_info` as a source and verifies that the `restrict` properties
  are uniform across the group. This addresses PR128714, where incorrect `restrict`
  information could lead to faulty vectorization decisions. The changes align with
  existing practices for handling TBAA information and are designed for backporting.
primer_glossary:
- term: restrict
  definition: A C/C++ qualifier that provides a promise to the compiler that a pointer
    is the sole initial means of accessing a particular object, aiding optimization
    by improving alias analysis.
- term: vectorizer
  definition: A GCC optimization pass that transforms scalar code into vector code,
    utilizing SIMD instructions to process multiple data elements in parallel.
- term: data reference
  definition: In the context of vectorization, a representation of a memory access
    (load or store) that the vectorizer analyzes.
- term: alias analysis
  definition: The process by which a compiler determines whether different memory
    references might point to the same memory location.
- term: TBAA
  definition: Type-Based Alias Analysis, an optimization technique that uses type
    information to infer whether different pointers can alias.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1c8a4ea630bfbf15a0b2f41a970c09fb38e68fdc
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This commit enhances the vectorizer's handling of `restrict` qualifiers for memory references. It introduces a check to compare `restrict` information across data reference groups before copying it to a vector reference. This prevents incorrect `restrict` information from being propagated when vectorizing memory accesses, ensuring more accurate alias analysis and potentially better optimization. The approach mirrors how type-based alias analysis (TBAA) information is handled.
