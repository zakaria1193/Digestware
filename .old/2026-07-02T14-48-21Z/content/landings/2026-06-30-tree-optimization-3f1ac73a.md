---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- dead code
commit_hash: 3f1ac73a476a9416ba8a623faf38190bb3b1acde
source_type: github
author: Richard Biener
headline: 'tree-optimization: Remove dead code in vectorizable_load'
tldr: Removes an unnecessary conditional branch in the vectorization pass, cleaning
  up dead code.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Within `tree-vect-stmts.cc`, the `vectorizable_load` function handles
  load operations for vectorization. This commit removes a redundant `else if` branch
  that became dead code after the elimination of non-SLP paths. The `vectorizer` pass
  no longer requires this conditional logic, simplifying the function.
primer_general: Compilers optimize code to make it run faster, and vectorization is
  one technique that allows the processor to perform the same operation on multiple
  data points simultaneously. This commit cleans up the code within GCC's vectorization
  pass. Specifically, in a function called `vectorizable_load` which handles loading
  data for vector operations, an unnecessary conditional check (`else if`) was removed.
  This branch of code was no longer reachable after previous changes, so its removal
  simplifies the compiler's internal workings without altering how user code is compiled.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3f1ac73a476a9416ba8a623faf38190bb3b1acde
date: '2026-06-30'
is_stub: true
stub_reason: low_score
---

This commit removes a dead `else if` statement from the `vectorizable_load` function within the `tree-vect-stmts.cc` file. The branch was mistakenly left in after non-SLP (Superword Level Parallelism) paths were removed from the vectorization logic. Its removal cleans up the code without affecting functionality.
