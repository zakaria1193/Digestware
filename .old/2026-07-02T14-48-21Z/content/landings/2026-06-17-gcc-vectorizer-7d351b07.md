---
project: gcc
subsystem: gcc/vectorizer
patch_id: null
tags:
- vectorization
- optimization
- cost model
- performance
commit_hash: 7d351b07e5b85c518b5cbe06a6a57cb653911195
source_type: github
author: Richard Biener
headline: Vectorizer gains a dedicated costing kind for vector decomposition.
tldr: A new costing mechanism for vector decomposition improves the vectorizer's ability
  to estimate costs for operations like emulated gather/scatter.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In GCD's `tree-vectorizer`, the `vect_cost_for_stmt` now includes a
  `vec_deconstruct` kind. This change moves away from a simplistic `nunits * vec_to_scalar`
  cost model for vector breakdown, providing finer-grained cost analysis, particularly
  for `VMAT_STRIDED_SLP` load/store patterns and emulated gather/scatter. The widespread
  target updates (across AArch64, x86, ARM, RISC-V, etc.) demonstrate the integration
  of this new costing into the existing `builtin_vectorization_cost` hook, ensuring
  consistent handling alongside `vec_construct` to avoid ICEs.
primer_general: Compilers often try to speed up your code by using 'vectorization,'
  which means performing operations on multiple data items at once, similar to how
  a graphics card processes many pixels simultaneously. To decide if this is a good
  idea, the compiler has to guess how much time different ways of doing things will
  take. This is called 'costing.' This change adds a new, more precise way for the
  compiler to estimate the cost of 'deconstructing' vectors—that is, breaking them
  down into smaller pieces. This is important for tasks like rearranging data efficiently
  for certain processor instructions (like "gather/scatter") or when dealing with
  data that isn't perfectly aligned in memory ('strided loads/stores'). By having
  a better cost model, the compiler can make smarter decisions about when to use these
  vector optimizations, potentially leading to faster code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7d351b07e5b85c518b5cbe06a6a57cb653911195
date: '2026-06-17'
is_stub: false
---

This commit introduces a new `vec_deconstruct` costing kind to the vectorizer, replacing the less precise `nunits * vec_to_scalar` method. This allows for a more accurate cost assessment when the vectorizer needs to break down vectors into smaller pieces, such as during emulated gather/scatter operations or for strided loads and stores. Target-specific implementations are updated to handle `vec_deconstruct` similarly to `vec_construct` to prevent internal compiler errors.
