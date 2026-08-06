---
project: gcc
subsystem: gcc/vectorizer
patch_id: null
tags:
- vectorizer
- optimization
- refactor
commit_hash: 28f2250ad1d37f49edb0efd1d88e3877257ab4a1
source_type: github
author: Richard Biener
headline: Simplify vect_get_vec_defs API.
tldr: Vectorizer's `vect_get_vec_defs` API is simplified to improve clarity and code
  cleanup.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect_get_vec_defs` function's signature in `tree-vectorizer.h`
  and `tree-vect-stmts.cc` is changed from taking a `tree` argument to a `bool`. This
  boolean indicates whether to populate the vector definitions vector for an operand,
  a step towards avoiding scalar operand access determined by `vect_is_simple_use`.
  This change simplifies several vectorizable routines like `vectorizable_bswap` and
  `vectorizable_conversion`.
primer_glossary:
- term: Vectorizer
  definition: A compiler component that transforms code to utilize vector instructions,
    performing multiple operations in parallel on data elements packed into wider
    registers.
- term: API (Application Programming Interface)
  definition: A set of definitions, protocols, and tools for building software. In
    this context, it refers to the functions and data structures used by different
    parts of the compiler.
- term: tree
  definition: GCC's internal representation of the program's abstract syntax tree,
    used during various optimization passes.
- term: Operand
  definition: A value or variable that an operator acts upon in an expression.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/28f2250ad1d37f49edb0efd1d88e3877257ab4a1
date: '2026-08-05'
is_stub: true
stub_reason: low_score
---

The `vect_get_vec_defs` function within the GCC vectorizer has been refactored to accept a boolean argument instead of a `tree` argument. This change clarifies its purpose: indicating whether to fill the vector definitions vector for an operand. The modification also simplifies related code in several vectorizable routines and cleans up the `tree-vectorizer.h` header.
