---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- gcc
- compiler
commit_hash: 604a45f74909987929eb77dfc1119fa94aedb1e1
source_type: github
author: Andrew MacLeod
headline: Ranger optimization cache uses two timestamps
tldr: Ranger optimization cache distinguishes between value storage and calculation
  times for better cache invalidation.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The temporal_cache in gcc/gimple-range-cache.cc used a single timestamp
  for cache invalidation. This commit splits it into stored and calculated timestamps,
  allowing for more precise cache management. This helps resolve PR tree-optimization/125758
  by improving the ranger's ability to track value staleness.
primer_glossary:
- term: Ranger
  definition: A GCC optimization pass that analyzes and transforms code based on value
    ranges, aiming to simplify expressions and improve performance.
- term: Cache invalidation
  definition: The process of marking cached data as invalid, forcing it to be re-fetched
    or recalculated from the original source. In compilers, this is crucial for ensuring
    that optimizations are based on up-to-date information.
- term: gimple-range-cache.cc
  definition: The GCC source file implementing the caching mechanism used by the Ranger
    optimization pass.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/604a45f74909987929eb77dfc1119fa94aedb1e1
date: '2026-06-18'
is_stub: false
stub_reason: ''
---

The Ranger optimization pass's caching mechanism has been updated to use two distinct timestamps: one for when a value was last stored and another for when it was last calculated. This allows the compiler to differentiate between a value that was recalculated but unchanged, and one that truly changed. This finer-grained tracking improves the cache's accuracy and efficiency by preventing unnecessary recalculations when a value's computed result remains the same.
