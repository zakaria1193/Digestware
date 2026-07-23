---
project: gcc
subsystem: gcc/frange
patch_id: null
tags:
- gcc
- floating-point
- optimization
commit_hash: d284bf3a1349c1bb5e57a71b5d6b46de36f4db13
source_type: github
author: Aldy Hernandez
headline: Consolidate signed-zero canonicalization of floating-point range endpoints.
tldr: Standardizes how +0.0 and -0.0 are represented in floating-point ranges.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The frange library's canonicalization of zero endpoints in floating-point
  ranges was inconsistent between `set()` and `flush_denormals_to_zero()`. This commit
  consolidates this logic to ensure a single, unified representation, which is a prerequisite
  for upcoming changes like implementing frange sub-ranges and correctly handling
  signed zeros in comparisons via `frange_cmp()`.
primer_glossary:
- term: signed zero
  definition: In floating-point arithmetic, zero can have a sign, represented as +0.0
    and -0.0. While numerically equal, they can arise from different operations and
    may have implications for comparisons and behavior in certain mathematical functions.
- term: frange
  definition: A GCC internal data structure representing a range of floating-point
    values. It is used in optimization passes to track possible values of expressions.
- term: canonicalization
  definition: The process of converting an expression or data structure into a standard
    or canonical form. In this context, it means ensuring that representations of
    floating-point zero are consistent.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d284bf3a1349c1bb5e57a71b5d6b46de36f4db13
date: '2026-07-15'
is_stub: false
stub_reason: ''
---

This change unifies the signed-zero canonicalization for floating-point range endpoints within the frange library. Previously, `set()` and `flush_denormals_to_zero()` handled zero endpoints differently, potentially leading to inconsistencies. By ensuring a single representation for zero endpoints, this commit lays the groundwork for more robust handling of signed zeros and simplifies range comparisons.
