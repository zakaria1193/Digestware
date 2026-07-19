---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- gcc
commit_hash: ddeb9b30a26ce61c836efe70893c77a67f7b737e
source_type: github
author: Andrew MacLeod
headline: Use vrp_operand_equal_p for prange comparisons.
tldr: Optimized comparisons for prange objects by using a specialized function.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch modifies value-range analysis in GCC's IPA passes. It replaces
  raw pointer equality checks for `prange_storage` objects with `vrp_operand_equal_p`.
  This is necessary because IPA's reassociation and unsharing of `prange` objects
  can lead to different physical pointers for semantically identical objects. Direct
  pointer comparison would break optimizations like hash table lookups, while `vrp_operand_equal_p`
  correctly handles semantic equality.
primer_glossary:
- term: IPA
  definition: Inter-procedural Analysis, a phase in GCC that analyzes code across
    function boundaries to enable optimizations.
- term: prange
  definition: A data structure used in GCC's value-range analysis to represent a range
    of possible values for a variable or expression.
- term: vrp_operand_equal_p
  definition: A function within GCC's value-range analysis that compares two operands
    for equality, considering their value ranges and potential aliasing.
- term: unsharing
  definition: In GCC's internal representation, unsharing refers to creating distinct
    copies of data structures that were previously shared, often to allow independent
    modification or optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ddeb9b30a26ce61c836efe70893c77a67f7b737e
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This commit changes how prange objects are compared for equality. Previously, raw pointer comparisons were used, which could lead to incorrect results when objects were unshared. The change introduces `vrp_operand_equal_p` for prange comparisons, ensuring that unshared objects are correctly identified as equal, which is crucial for data structures like hash tables.
