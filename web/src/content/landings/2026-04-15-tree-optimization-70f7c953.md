---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- optimization
- bool
commit_hash: 70f7c95333a5bbb085e6ad666250e03e819d1297
source_type: github
author: Richard Biener
headline: Tree-optimization Vectorizes Inversion of Scalar Bools
tldr: The tree-optimization pass now vectorizes the inversion of scalar bools by rewriting
  it to a `BIT_XOR_EXPR` operation.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR tree-optimization/124843 by enabling vectorization
  of scalar bool inversions. The `vect_recog_bool_pattern` function in `tree-vect-patterns.cc`
  is modified to recognize `BIT_NOT_EXPR` operations on scalar bools and rewrite them
  as `BIT_XOR_EXPR`. The vectorizer can then process the latter. This transformation
  is necessary because bools have bit precision, which prevents direct vectorization
  of `BIT_NOT_EXPR`.
primer_general: Compilers often include a tree-optimization phase. Vectorization is
  a compiler optimization technique that transforms code to perform the same operation
  on multiple data elements simultaneously, using vector instructions. A `BIT_NOT_EXPR`
  represents a bitwise NOT operation. `BIT_XOR_EXPR` represents a bitwise XOR operation.
  This commit enables the compiler to vectorize boolean inversions by transforming
  the `BIT_NOT_EXPR` into a `BIT_XOR_EXPR`, which improves performance when working
  with arrays of boolean values.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/70f7c95333a5bbb085e6ad666250e03e819d1297
date: '2026-04-15'
---

The tree-optimization pass now vectorizes the inversion of scalar bools. Due to bools having bit precision, direct vectorization of the `BIT_NOT_EXPR` operation is not possible. This commit adds a pattern to rewrite the inversion of scalar bools to the corresponding `BIT_XOR_EXPR` operation, which can be vectorized effectively, leading to performance improvements in code that uses boolean arrays.
