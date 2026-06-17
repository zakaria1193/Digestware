---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- loop-optimization
- range-analysis
- performance
commit_hash: 1fb998f8839b31e91fb154bbf052e9470f083ef6
source_type: github
author: Abhishek Kaushik
headline: 'Tree optimization: Query ranger for niter bound expressions on edge.'
tldr: GCC's loop optimizer now queries the range analyzer for integral expressions
  at loop preheader edges, improving precision of number-of-iterations analysis.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-loop-niter.cc` component, specifically `determine_value_range`
  in the number of iterations (niter) analysis, now consults the 'ranger' (range analysis
  pass) for integral expressions at the loop preheader edge, decoupled from the prior
  restriction to SSA_NAME operands. This addresses a limitation where `expand_simple_operations`
  on IV bases could obscure range information by exposing GENERIC expressions, including
  conversions, which ranger is capable of analyzing. By querying on the preheader
  edge, the compiler can now determine tighter bounds for value-preserving type conversion…
primer_general: Compilers try to make your code run faster by optimizing loops, as
  loops often consume a significant portion of execution time. One crucial optimization
  is determining how many times a loop will run, known as the 'number of iterations.'
  This commit improves how GCC's loop optimizer figures this out. Previously, the
  optimizer sometimes had trouble with expressions that determined loop bounds if
  they involved certain calculations or conversions that were expanded by prior optimization
  passes. The fix enables the optimizer to ask a special 'range analyzer' component
  for more precise information about these expressions, even after transformations.
  This allows the compiler to get a more accurate count of loop iterations, which
  can lead to better and more aggressive optimizations, resulting in faster code execution,
  especially for loops involving simple type conversions or calculations for their
  bounds.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1fb998f8839b31e91fb154bbf052e9470f083ef6
date: '2026-06-16'
is_stub: false
---

This commit enhances GCC's loop optimizer by making `determine_value_range` query the 'ranger' (range analyzer) for integral bound expressions regardless of whether they are SSA_NAMEs. Previously, it only queried for SSA_NAMEs, missing opportunities to analyze expressions that resulted from `expand_simple_operations` on IV bases. By querying on the loop preheader edge, the optimizer can now recover narrower, more accurate ranges for value-preserving conversions (e.g., `uint8_t` to `int`), leading to more effective loop optimizations while still conservatively handling non-value-preserving or wrapping conversions.
