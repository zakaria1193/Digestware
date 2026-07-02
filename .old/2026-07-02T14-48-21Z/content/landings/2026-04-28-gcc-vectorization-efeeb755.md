---
project: gcc
subsystem: gcc/vectorization
patch_id: null
tags:
- gcc
- vectorization
- x86
- optimization
commit_hash: efeeb755192cb03e5b24b44cb4fb563c11626a8e
source_type: github
author: Richard Biener
headline: Improve masked main loop selection for x86 vectorization.
tldr: The compiler now prefers masked main loops when they reduce epilogue iterations
  on x86, preventing performance regressions.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch introduces a new override for `vector_costs::better_main_loop_than_p`
  within the `ix86_vector_costs` class. The override addresses a regression related
  to masked main loop selection in the presence of cost comparison.  The logic prefers
  a masked main loop if it can eliminate enough vector and scalar epilogue loop iterations,
  particularly when a non-masked main loop cannot be vectorized effectively. This
  change highlights the trade-offs between masking costs, epilogue costs, and icache
  footprint. The `vinfo` accessor in `tree-vectorizer.h` is used to gather vectorization
  information.
primer_general: Vectorization enhances performance by processing multiple data elements
  concurrently.  Masking allows vector operations to be applied selectively to elements
  within a vector.  Epilogue loops handle remaining elements when the loop count isn't
  a multiple of the vector length.  This commit refines GCC's decision-making process
  for choosing between masked and non-masked main loops in vectorization, considering
  the costs of masking and epilogue iterations to optimize performance, especially
  on x86 architectures where icache performance is significant.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/efeeb755192cb03e5b24b44cb4fb563c11626a8e
date: '2026-04-28'
---

This commit overrides `vector_costs::better_main_loop_than_p` to prevent regressions in `gcc.target/i386/vect-partial-vectors-2.c` when `--param ix86-vect-compare-costs=1` is enabled. The change prioritizes masked main loops (where AVX masking is used) if they minimize the need for vector and scalar epilogue iterations, specifically when a non-masked main loop cannot be vectorized.  This is a heuristic that favors smaller icache footprint on x86 for loops with few iterations.
