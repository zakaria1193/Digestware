---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- optimization
- boolean
- performance
commit_hash: 70f7c95333a5bbb085e6ad666250e03e819d1297
source_type: github
author: Richard Biener
headline: Enable vectorization of scalar bool inversions
tldr: GCC now vectorizes the inversion of scalar boolean values by rewriting the operation
  as a bitwise XOR.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The tree vectorizer transforms scalar operations into vector operations.  Scalar
  bool inversions (`BIT_NOT_EXPR`) are now rewritten as `BIT_XOR_EXPR` to enable vectorization.
  This involves adding a pattern recognition to `vect_recog_bool_pattern` in `tree-vect-patterns.cc`.  The
  interaction with other tree-level optimizations should be considered.
primer_general: Vectorization is a compiler optimization that transforms scalar operations
  (operating on single values) into vector operations (operating on multiple values
  simultaneously).  This commit improves GCC's ability to vectorize boolean logic
  by rewriting boolean inversions.  The tree vectorizer operates on the compiler's
  internal representation of the code (the "tree").  This optimization can improve
  performance for code that performs many boolean operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/70f7c95333a5bbb085e6ad666250e03e819d1297
date: '2026-04-15'
---

GCC's tree vectorizer now transforms scalar boolean inversions (using `!`) into bitwise XOR operations, enabling vectorization. Boolean types in GCC have a bit precision, which previously prevented vectorization of inversions.  This change allows the compiler to generate more efficient vector code for boolean logic, potentially improving performance in code that uses boolean arrays or performs many boolean operations.
