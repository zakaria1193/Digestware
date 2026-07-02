---
project: gcc
subsystem: gcc
patch_id: null
tags:
- optimization
- rtl
- aarch64
commit_hash: ddacdb8b37ce268cac26e594e8f84b530b4f85b4
source_type: github
author: Richard Sandiford
headline: Simplifies vec_duplicates of vec_duplicates
tldr: This commit simplifies nested `vec_duplicate` operations in GCC's RTL, folding
  them into a single `vec_duplicate` to improve optimization.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `simplify_context::simplify_unary_operation_1` function in `simplify-rtx.cc`
  now handles nested `vec_duplicate` RTL expressions. Previously, a `VEC_DUPLICATE`
  from a source that was itself a `VEC_DUPLICATE` might not be optimally represented.
  This patch explicitly folds such nested structures into a single `VEC_DUPLICATE`
  operation, leveraging the fact that `vec_duplicate_p` was initially designed for
  scalar elements. This simplification affects patterns like `*aarch64_vec_duplicate_subvector`
  and contributes to cleaner RTL prior to subsequent optimization passes.
primer_general: Inside GCC, code is represented using an intermediate language called
  RTL. When you have code that creates a vector by copying a single value multiple
  times, and then another operation that copies that entire vector multiple times
  to make an even larger vector, the compiler might represent this inefficiently as
  two separate "duplicate vector" operations. This change teaches the compiler to
  recognize these nested duplication operations and combine them into a single, more
  efficient "duplicate vector" operation. This makes the internal representation of
  the code simpler, which can help the compiler generate faster and smaller machine
  code, especially for vectorized operations like those found in AArch64 SVE.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ddacdb8b37ce268cac26e594e8f84b530b4f85b4
date: '2026-06-08'
is_stub: false
---

GCC's RTL simplifier now optimizes expressions that involve duplicating replicated vectors. Previously, a `vec_duplicate` of another `vec_duplicate` could occur unnecessarily. This change modifies `simplify_context::simplify_unary_operation_1` to detect and fold these nested operations into a single `vec_duplicate`, improving the efficiency of the intermediate representation and potentially affecting downstream optimizations. This was primarily observed and fixed in AArch64 SVE specific patterns.
