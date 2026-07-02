---
project: gcc
subsystem: gcc/vectorization
patch_id: null
tags:
- gcc
- vectorization
- x86
- optimization
commit_hash: bab20a370641484fffa5ac5bb30b7d19f5d3fe92
source_type: github
author: Richard Biener
headline: Improve x86 epilogue loop selection with cost comparison.
tldr: The compiler now prefers existing epilogues unless a new candidate offers optimal
  vectorization, resolving a test failure.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch introduces a new override for `vector_costs::better_epilogue_loop_than_p`
  within the `ix86_vector_costs` class. The override addresses suboptimal epilogue
  selection when cost comparison is enabled. The logic prefers the currently prevailing
  epilogue unless the new candidate offers a vectorization factor of one (indicating
  an optimal vector epilogue). This change mitigates regressions related to target-specific
  epilogue usage and interactions with the cost model.  The `vinfo` accessor in `tree-vectorizer.h`
  might also be relevant.
primer_general: Vectorization improves performance by processing multiple data elements
  simultaneously.  When a loop's iteration count is not a multiple of the vector length,
  an epilogue loop handles the remaining elements.  This commit refines the selection
  of epilogue loops in GCC, particularly when cost comparison is enabled, to avoid
  performance regressions and ensure the optimal vectorization strategy is chosen
  for x86 architectures. The compiler's cost model estimates the performance impact
  of different vectorization choices.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bab20a370641484fffa5ac5bb30b7d19f5d3fe92
date: '2026-04-28'
---

This commit resolves a failure in `gcc.target/i386/vect-epilogues-3.c` when `--param ix86-vect-compare-costs=1` is specified. The change modifies the `better_epilogue_loop_than_p` function to favor the existing epilogue when the target requests multiple epilogues, unless the new candidate uses a vectorization factor of one. This prevents regressions in `gcc.dg/vect/costmodel/x86_64/costmodel-pr122573.c`.
