---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- testing
- regression
commit_hash: d9171eae3d69fe2a63ef8f03a5792c04e9d14271
source_type: github
author: Tamar Christina
headline: 'middle-end: Add bitmask to default POLY_INT_CST ranges.'
tldr: Restored bitmask to POLY_INT_CST ranges in value-query.cc to fix test failures.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `value-query.cc`, the `range_query::get_tree_range` function handles
  the determination of value ranges for constants. A recent change, possibly during
  the AArch64 extraction, omitted setting the bitmask in the `VARYING` return case.
  This bitmask is essential for accurately representing the valid subset of values
  within a varying range. Its absence caused test failures related to range interpretation,
  which this commit fixes by reintroducing the bitmask.
primer_glossary:
- term: POLY_INT_CST
  definition: Represents a constant integer value that may involve symbolic constants
    or polynomial expressions, used in GCC's intermediate representation.
- term: VARYING
  definition: A status indicating that a value or range can vary, often used in range
    analysis where precise bounds cannot be determined statically.
- term: bitmask
  definition: A value used to manipulate or check specific bits within a larger value.
    In this context, it likely encodes information about the valid values within a
    `POLY_INT_CST` range.
- term: value-query.cc
  definition: A GCC source file containing logic for querying and determining properties
    of constant values and their ranges within the compiler's intermediate representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d9171eae3d69fe2a63ef8f03a5792c04e9d14271
date: '2026-08-21'
is_stub: true
stub_reason: low_score
---

A regression in GCC's middle-end value-query logic caused test failures by failing to set the bitmask on `POLY_INT_CST` ranges when returning `VARYING`. This bitmask is crucial because even when a range is considered varying, it doesn't imply all values within it are possible. The change restores the bitmask, ensuring correct range evaluation and passing CI tests.
