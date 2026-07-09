---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- dataflow analysis
commit_hash: c31cb13628593fc57779419a806170b6ef2c3b81
source_type: github
author: Richard Biener
headline: tree-optimization/126159 - Handle unions in data dependence analysis
tldr: Improves data dependence analysis to handle non-aggregate union field accesses.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch adds minimal handling for union accesses within the `dr_analyze_indices`
  function in `tree-data-ref.cc`. Specifically, it addresses accesses to non-aggregate
  fields of unions, especially those where additional subsetting is not performed.
  The `access_fn_component_p` function is adjusted accordingly. The goal is to improve
  the accuracy of data reference analysis, particularly for vectorization, by correctly
  modeling disjoint accesses within unions.
primer_glossary:
- term: data dependence analysis
  definition: A compiler analysis that determines if one instruction's result is used
    by a subsequent instruction. This is crucial for instruction scheduling and parallelization,
    including vectorization.
- term: union
  definition: A composite data type in C/C++ that can hold values of different data
    types at the same memory location. Only one member of a union can hold a value
    at any given time.
- term: vectorization
  definition: An optimization technique where a single instruction operates on multiple
    data elements simultaneously, often by using special CPU instructions (SIMD).
- term: tree-data-ref.cc
  definition: A GCC source file likely containing code for analyzing data references
    within the compiler's intermediate representation (tree).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c31cb13628593fc57779419a806170b6ef2c3b81
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This commit enhances GCC's data dependence analysis pass to correctly handle accesses to non-aggregate fields within unions. Previously, such accesses could be misinterpreted, potentially leading to incorrect optimization decisions. The changes ensure that accesses to union members, particularly when subsetting is not applied, are properly accounted for, improving the accuracy of data flow analysis.
