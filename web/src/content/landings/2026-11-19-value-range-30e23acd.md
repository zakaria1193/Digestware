---
project: gcc
subsystem: value-range
patch_id: null
tags:
- code cleanup
- api
commit_hash: 30e23acd03e9e675b1fb30e8d70d4d53a576b581
source_type: github
author: Andrew MacLeod
headline: Remove unused prange pointer-query API.
tldr: Unused API for querying pointer ranges (base, offset, size) in `prange` has
  been removed.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `prange` class in `value-range.h` represents ranges of values.
  This commit removes a specific API that allowed setting and querying pointer-like
  ranges by explicitly providing the base address, offset, and size. Since no existing
  compiler passes or features utilize this representation, it is being pruned.
primer_glossary:
- term: prange
  definition: A data structure within GCC used to represent a range of possible values
    for a variable or expression, aiding in optimization and analysis.
- term: API
  definition: Application Programming Interface. A set of functions, procedures, and
    protocols that allows different software components to communicate with each other.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/30e23acd03e9e675b1fb30e8d70d4d53a576b581
date: '2026-11-19'
is_stub: true
stub_reason: low_score
---

The `prange` API for representing pointer ranges with explicit base, offset, and size information is currently not used by any part of GCC. This commit removes the API to reduce code complexity and maintenance overhead until a concrete use case arises.
