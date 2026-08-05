---
project: gcc
subsystem: gcc/sched-deps
patch_id: null
tags:
- optimization
- scheduler
- compile-time
- gcc
commit_hash: 789d24cd259e0e1e8e5af512565fa59daae5307d
source_type: github
author: Kyrylo Tkachov
headline: Improves scheduler efficiency by reusing register dependency arrays.
tldr: Reduces scheduler setup time by pooling and reusing register dependency data
  structures.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The region scheduler's initialization of `deps_desc` for each basic
  block involved allocating and zeroing `max_reg` `deps_reg_entries`. This resulted
  in O(max_reg * sum(blocks)) complexity, which could be quadratic in function size.
  This commit introduces a `reg_last_pool` to `sched-deps.cc`. After `free_deps` empties
  an entry, the array is returned to this pool, keyed by `max_reg`. Reused arrays
  have their list length fields reset. This optimization targets the scheduler's setup
  time, providing a compile-time performance improvement. A selftest verifies the
  pooling mechanism.
primer_glossary:
- term: region scheduler
  definition: A phase in the compiler scheduler that groups basic blocks into regions
    to perform scheduling optimizations across block boundaries.
- term: deps_desc
  definition: A data structure within GCC's scheduler that describes dependencies
    between instructions.
- term: deps_reg_entries
  definition: An array of structures used by the scheduler to track register dependencies.
- term: max_reg
  definition: The maximum number of registers available on the target architecture,
    used to size certain data structures in the compiler.
- term: free_deps
  definition: A function within the scheduler that cleans up and releases dependency
    information.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/789d24cd259e0e1e8e5af512565fa59daae5307d
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

The GCC region scheduler previously allocated and zeroed new dependency descriptor arrays for each basic block within a region, leading to quadratic complexity in large functions. This commit introduces a pool for these `deps_reg_entries` arrays. After use, arrays are returned to the pool and reused for subsequent regions, significantly reducing allocation and zeroing overhead. This optimization improves compiler performance, particularly for large functions, with no impact on the generated code.
