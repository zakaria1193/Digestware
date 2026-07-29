---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- optimization
- vectorization
commit_hash: 3cd23c9fd60854cd9d160ce3b341a819025bfeb8
source_type: github
author: Richard Biener
headline: Improve conversion detection in vector reduction chains.
tldr: Fixes detection of conversions in vector reduction chains to accurately skip
  them when needed.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Within the `vect-slp.cc` file, the `vect_analyze_slp_reduc_chain` function
  is responsible for analyzing Superword (Vector) Level Parallelism in reduction chains.
  This commit updates the pattern matching logic to distinguish between a statement
  that *is* a conversion and a statement that *mismatches* the expected conversion,
  ensuring correct analysis for vectorizable reduction chains.
primer_glossary:
- term: vector reduction chain
  definition: A sequence of operations where data is accumulated using a binary operation
    across vector elements. This allows for parallel computation of sums, products,
    or other cumulative results.
- term: conversion detection
  definition: The process by which the compiler identifies and analyzes type conversions
    within the code to determine if they can be optimized or if they interfere with
    other optimizations like vectorization.
- term: SLP (Superword Level Parallelism)
  definition: A compiler optimization technique that identifies and vectorizes sequences
    of identical scalar operations that operate on consecutive memory locations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3cd23c9fd60854cd9d160ce3b341a819025bfeb8
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This commit refines the detection of conversion statements within vector reduction chains. It ensures that the analysis correctly identifies and skips conversion patterns that do not match the original statement, preventing misinterpretations during optimization. A new test case is included to validate this improvement.
