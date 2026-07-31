---
project: gcc
subsystem: gcc/frange
patch_id: null
tags:
- optimization
- memory
commit_hash: 80ade12f5384a27fbed0717fcee9c39427f9f989
source_type: github
author: Aldy Hernandez
headline: Store sub-ranges in a variable-length trailing array.
tldr: Value range storage now uses variable-length arrays for sub-ranges, optimizing
  memory use from O(MAX_PAIRS) to O(actual_pairs).
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: frange_storage::m_pairs, formerly a fixed-size array, is now a variable-length
  trailing array.  alloc() is sized to the range's num_pairs(), and m_max_ranges tracks
  capacity. This mirrors irange_storage and reduces per-range overhead when num_pairs()
  << MAX_PAIRS. Tested on ppc64le.
primer_glossary:
- term: frange_storage
  definition: A data structure within GCC used for caching and managing value ranges,
    potentially including multiple sub-ranges.
- term: sub-range
  definition: A portion of a larger range of possible values, used to represent more
    precise information about a variable's values.
- term: MAX_PAIRS
  definition: A compile-time constant defining the maximum number of sub-ranges that
    could be stored in the older frange_storage implementation.
- term: variable-length trailing array
  definition: A C++ pattern where an array is allocated dynamically at the end of
    a struct or class, allowing the size to vary based on runtime needs.
- term: irange_storage
  definition: Another GCC data structure, similar to frange_storage, likely for managing
    interval ranges.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/80ade12f5384a27fbed0717fcee9c39427f9f989
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

The frange_storage mechanism has been optimized for memory efficiency. Previously, it allocated space for the maximum possible number of sub-ranges (MAX_PAIRS), even if only one was used. This change revises frange_storage to use a variable-length trailing array, similar to irange_storage, so that memory is allocated only for the actual number of sub-ranges needed. This reduces memory overhead for the majority of cached ranges.
