---
project: gcc
subsystem: gcc/vectorizer
patch_id: null
tags:
- vectorization
- x86
- data types
- optimization
commit_hash: cb0849d0facad53ccabf5b18ef2a3dd71a54e565
source_type: github
author: Richard Biener
headline: Vectorizer now tracks element type for complex loads and stores.
tldr: The vectorizer now records the element type for strided loads and stores, allowing
  for more accurate vector type reconstruction.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Within `gcc/vectorizer`, specifically `tree-vectorizer.h` and `tree-vect-stmts.cc`,
  the `vect_load_store_data` structure now records `ls_eltype`. This is a refinement
  to the internal representation of vector load/store operations, particularly for
  `VMAT_STRIDED_SLP`. The realization was that `ls_type` alone does not retain enough
  information about the *constituent* element types when a vector is effectively built
  from smaller, possibly vector, components (e.g., combining `V2SI` elements into
  a `V4SI` vector on x86). This detail is crucial for the vectorizer's correctness
  in identifying opport…
primer_general: Compilers use 'vectorization' to make your code run faster by processing
  multiple data items at once. To do this effectively, the compiler needs a precise
  understanding of how data is arranged in memory and how it's being accessed. This
  change improves the compiler's internal tracking of data types, specifically for
  complex ways of reading and writing data in 'vectors.' Previously, the compiler
  might only record the final type of a vector (e.g., a vector of four integers),
  but not the type of the smaller pieces it was built from (e.g., two-integer vectors).
  By recording this 'element type,' the compiler can more accurately understand how
  vectors are being constructed and decomposed, leading to better optimization decisions,
  especially for specific patterns of data access like 'strided loads.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cb0849d0facad53ccabf5b18ef2a3dd71a54e565
date: '2026-05-13'
is_stub: false
---

This update adds an `ls_eltype` field to `vect_load_store_data` in the vectorizer, addressing situations where recording only the load/store type (`ls_type`) is insufficient to understand vector composition. On x86, for instance, a `V4SI` (vector of four 32-bit integers) might be constructed from `V2SI` (vector of two 32-bit integers) elements. This more detailed information improves the vectorizer's ability to recognize and optimize such complex memory accesses.
