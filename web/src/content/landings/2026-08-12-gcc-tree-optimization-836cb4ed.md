---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- range-analysis
commit_hash: 836cb4ed48c987a4a9027cb14e6b6e1edeebcaf3
source_type: github
author: Andrew MacLeod
headline: Set current query in fold_using_range
tldr: Ensures correct range context is maintained during folding operations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `fold_using_range::fold_stmt` in `gimple-range-fold.cc`, the current
  range query is temporarily replaced with the query provided to the function. This
  ensures that any folding operations performed within this scope operate under the
  intended range constraints, which is crucial for the correctness of range analysis
  and subsequent optimizations. This fixes a potential issue where the global or previously
  established range query might be used incorrectly.
primer_glossary:
- term: fold_using_range
  definition: A function or method within GCC's tree optimizer that attempts to simplify
    expressions or statements by using range information.
- term: range query
  definition: A request to the range analysis system to determine the possible values
    or bounds of an expression or variable.
- term: folding
  definition: An optimization technique where constant expressions or known properties
    of variables are used to simplify code at compile time.
- term: GIMPLE
  definition: GCC's Internal Machine-Independent Optimizations. A three-address intermediate
    representation used by GCC for optimization passes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/836cb4ed48c987a4a9027cb14e6b6e1edeebcaf3
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

This commit updates `fold_using_range` to set the current query for range analysis. This ensures that the folding operation correctly uses the specified range context, preventing potential inaccuracies. A new test case is added to verify this fix.
