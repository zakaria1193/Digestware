---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler
- SSA
commit_hash: 7b5a05667c8e40bec5e070b1638d3b3882f7c78e
source_type: github
author: Richard Biener
headline: tree-optimization/125040 - fix sorted_array_from_bitmap_set
tldr: Improves expression sorting in SSA pre pass by computing value graph entries
  first.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Fixes PR tree-optimization/125040 by modifying `tree-ssa-pre.cc:sorted_array_from_bitmap_set`.
  The function now computes the set of entries to the value graph prior to building
  the final sorted expression set, addressing issues where the topological sort was
  incomplete due to missing graph entry information. This change aims to reduce redundant
  iterations in subsequent analyses.
primer_general: During compiler optimization, the tool transforms code into an intermediate
  representation called Static Single Assignment (SSA) form. The SSA pre-pass optimizes
  this form. This change fixes a function responsible for sorting expressions within
  a data structure (bitmap set) used by the SSA pass. By ensuring the function first
  correctly identifies all relevant parts (entries) of the code's value graph, it
  improves the accuracy of the sorting process, potentially leading to more effective
  optimizations and faster compilation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/7b5a05667c8e40bec5e070b1638d3b3882f7c78e
date: '2026-06-26'
is_stub: false
stub_reason: ''
---

The `sorted_array_from_bitmap_set` function in the SSA pre-pass has been corrected to first compute the entries of the value graph. This ensures a more accurate topological sorting of expressions within a bitmap set, reducing the overall iteration count needed for this process and potentially improving optimization performance.
