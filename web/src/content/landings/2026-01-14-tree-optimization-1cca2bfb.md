---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- performance
commit_hash: 1cca2bfbdaa4433002d321b580b173294ee88460
source_type: github
author: Zhongyao Chen
headline: SLP vectorizer now skips reduction subgroups of size one.
tldr: GCC’s SLP vectorizer now explicitly avoids creating size-one reduction subgroups,
  improving code generation quality.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Within GCC's tree-optimization pass, specifically in `tree-vect-slp.cc`,
  the SLP (Superword Level Parallelism) vectorizer's reduction subgroup analysis is
  refined. The `vect_analyze_slp_reduction_group` function now explicitly checks `group_size`
  and returns `false` if it is less than or equal to one. This prevents the vectorizer
  from attempting SLP on trivial, single-element reductions. While such groups might
  technically 'succeed' in the analysis, their vectorization typically leads to worse
  code than scalar execution, often introducing unnecessary shuffle or extract operations.
  By making r…
primer_general: 'Compilers like GCC try to make your code run faster by using special
  processor features, one of which is called vectorization. This means performing
  the same operation on multiple pieces of data simultaneously, often by grouping
  them into ''vectors.'' A particular technique called SLP (Superword Level Parallelism)
  looks for patterns in your code that can be vectorized, especially for operations
  that combine many values into a single result, known as reductions (like summing
  an array). This update in GCC improves how its SLP vectorizer handles these reductions.
  Previously, if the compiler found a ''group'' of just one item to reduce, it would
  still try to vectorize it. This often made the code slower because the overhead
  of setting up the vector operation outweighed any benefit. Now, the compiler is
  smarter: if a reduction group only has one element, it skips the vectorization attempt
  and reverts to a simpler, more efficient single-item operation. This leads to better
  performance for such…'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1cca2bfbdaa4437b45c6bc87bc3ad3b1
date: '2026-01-14'
is_stub: false
---

GCC's SLP vectorizer now requires reduction subgroups to have a size greater than one. Previously, size-one groups were analyzed, leading to inefficient code generation. The `vect_analyze_slp_reduction_group` function now returns false for groups of size one or less, ensuring these cases correctly fall back to single-lane reductions and avoiding suboptimal output.
