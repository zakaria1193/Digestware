---
project: gcc
subsystem: gcc/vectorizer
patch_id: null
tags:
- vectorization
- x86
- performance
- cost model
commit_hash: 83a0f499108787a8e397c76530f5eae8b5512b82
source_type: github
author: Richard Biener
headline: Vectorizer costing now handles vector construction and decomposition directly.
tldr: The vectorizer's cost model now explicitly accounts for the expense of building
  and breaking down vectors, improving the accuracy of optimization decisions.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Within `gcc/vectorizer`, specifically the x86 backend's cost modeling
  (`ix86_default_vector_cost`), the logic for calculating the cost of vector construction
  and decomposition has been split out into `ix86_vector_cd_cost`. This is crucial
  for accurately valuing `VMAT_STRIDED_SLP` related memory operations, where vectors
  might be formed or broken down from smaller elements, influencing profitability
  heuristics for autovectorization. This re-organization lays groundwork for more
  granular costing, especially in scenarios like emulated gather/scatter or complex
  strided memory accesses.
primer_general: Compilers try to make your code run faster through a process called
  optimization. One such optimization is 'vectorization,' where the compiler transforms
  operations on individual data items into operations on entire arrays (vectors) of
  data, which modern processors can execute much more efficiently. To decide if vectorization
  is beneficial, the compiler uses a 'cost model' to estimate how expensive different
  operations are. This change refactors how the compiler for x86 processors calculates
  the cost of creating and breaking down these data vectors. By making this cost estimation
  more precise, especially for certain complex memory access patterns (like `VMAT_STRIDED_SLP`),
  the compiler can make better decisions about when to apply vectorization, potentially
  leading to faster programs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/83a0f499108787a8e397c76530f5eae8b5512b82
date: '2026-05-13'
is_stub: false
---

This change refactors the x86 vectorizer's cost calculation by extracting `ix86_vector_cd_cost` to specifically handle vector construction and decomposition. This enhancement provides a more precise cost assessment for operations involving `VMAT_STRIDED_SLP` loads and stores during vectorization. The improved costing helps the optimizer make better decisions about when to apply vectorization.
