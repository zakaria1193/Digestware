---
project: gcc
subsystem: gcc/vect
patch_id: null
tags:
- gcc/vect
- vectorization
- SLP
- aarch64
commit_hash: c3ceac8d1e1645cb5e7a2502ff17d9effce70699
source_type: github
author: Tamar Christina
headline: Simplify linear load checks using vector permutation utilities
tldr: Refactor `is_linear_load_p` to use `vec_perm_indices` for clearer and more robust
  checking of vector load patterns.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `is_linear_load_p` function in `tree-vect-slp-patterns.cc` determines
  if a load operation constitutes a "linear" access pattern, often involving permutations
  of vector elements, which is crucial for SLP (Superword Level Parallelism) vectorization.
  Previously implemented with a manual, iterative disqualification process, it was
  found to be complex and susceptible to errors, accepting invalid patterns. The rewrite
  leverages `vec_perm_indices` to directly construct and validate the permutation
  indices, using `series_p()` to check for linear sequences. This makes the logic
  more declarative an…
primer_glossary:
- term: Linear Load
  definition: A memory load operation in a vectorized loop where data elements are
    accessed in a sequential or predictable pattern, often with a constant stride
    or specific permutation.
- term: Vector Permutation
  definition: Rearranging the elements within a vector register according to a specified
    index pattern. This is a common operation in SIMD programming.
- term: vec_perm_indices
  definition: A function or utility within GCC that helps in constructing or analyzing
    the indices used for vector permutations.
- term: SLP (Superword Level Parallelism)
  definition: A compiler optimization technique that vectorizes sequences of independent
    scalar operations by grouping them into operations on wider data elements (vectors).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c3ceac8d1e1645cb5e7a2502ff17d9effce70699
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

This commit refactors the `is_linear_load_p` function within the vectorizer to use `vec_perm_indices` and the `series_p()` helper. This change simplifies the code, making it easier to verify correctness and preventing the acceptance of invalid permutation patterns, such as the `[0 2 2 2]` example cited in the bug report. The function now more reliably identifies valid linear load patterns involving complex arithmetic permutations. A new test case for AArch64 is included.
