---
project: gcc
subsystem: gcc/value-range
patch_id: null
tags:
- optimization
- value-range analysis
- refactoring
commit_hash: bbf71b94fc1af926cb9dfe3934e716ced755dc8b
source_type: github
author: Aldy Hernandez
headline: Prepare value-range analysis to handle multiple sub-ranges.
tldr: Value-range analysis data structure refactored to support multiple sub-ranges
  per slot.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `frange` and `frange_storage` classes in `value-range.cc` have
  been modified to accommodate future support for multiple disjoint value ranges per
  analyzed variable. The existing `m_min` and `m_max` members, representing a single
  contiguous range, are replaced by an array of pairs (`m_pairs`) and a count (`m_num_ranges`).
  Consumers of the `frange` class that iterated over sub-ranges have been updated
  to loop `m_num_ranges` times. Single-range specific functions now include a `m_num_ranges
  == 1` guard.
primer_glossary:
- term: value-range analysis
  definition: A compiler optimization technique that determines the possible range
    of values a variable can hold at different points in the program. This information
    can be used to perform optimizations like constant folding or dead code elimination.
- term: sub-range
  definition: A contiguous portion of the possible values a variable can take. In
    value-range analysis, a variable might be known to fall within multiple disjoint
    sub-ranges.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bbf71b94fc1af926cb9dfe3934e716ced755dc8b
date: '2026-07-19'
is_stub: false
stub_reason: ''
---

The internal data structure for value-range analysis has been refactored to prepare for supporting multiple sub-ranges efficiently. The current implementation, limited to one sub-range per slot, now stores endpoints in a one-element array. This change modifies various functions to iterate over a new `m_num_ranges` field and adds guards for single-range operations, laying the groundwork for future enhancements.
