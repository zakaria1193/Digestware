---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- gcc
commit_hash: b85f2169fb3b0a25b5e53974775df3086d900376
source_type: github
author: Andrew MacLeod
headline: range_of_phi unconditionally unions ranges of all arguments.
tldr: GCC's range_of_phi optimization now unconditionally unions ranges of all arguments,
  improving precision and performance.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `fold_using_range::range_of_phi` function in `gimple-range-fold.cc`
  computes the range of values a PHI node can take. Previously, it handled equivalences
  separately. This change modifies it to always union the range of every argument,
  simplifying the logic and improving precision, particularly for floating-point ranges.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b85f2169fb3b0a25b5e53974775df3086d900376
date: '2026-11-17'
is_stub: false
stub_reason: ''
---

The range_of_phi optimization in GCC previously accumulated ranges of equivalences separately and combined them conditionally. This could lead to loss of precision, such as +/- 0.0 ranges, and potential incorrectness. The change simplifies the process by unconditionally unioning the range of each argument, which is also reported to be 0.025% faster.
