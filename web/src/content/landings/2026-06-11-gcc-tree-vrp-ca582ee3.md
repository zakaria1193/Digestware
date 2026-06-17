---
project: gcc
subsystem: gcc/tree-vrp
patch_id: null
tags:
- optimization
- pointers
- gimple
- value-range-analysis
commit_hash: ca582ee36820a318fbc506928503282a5e35603a
source_type: github
author: Andrew MacLeod
headline: Pointer global ranges of nonzero are no longer invariant
tldr: GCC's value range analysis now correctly tracks pointer ranges that become non-zero,
  allowing more precise optimization based on points-to information.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's `prange` (pointer range) analysis is a crucial component of value
  range propagation (VRP) within the GIMPLE intermediate representation. The `ranger_cache`
  stores computed `prange` information to avoid re-computation. Prior to this change,
  if a pointer's range was determined to be non-zero (e.g., `p != NULL`), the cache
  would consider this fact invariant, and subsequent conditional checks (like `if
  (p)` before dereference) would not further refine its points-to set. This commit
  modifies `ranger_cache::set_global_range` to remove this invariant assumption for
  non-zero pointer ranges, all…
primer_general: Compilers like GCC analyze your code to make it more efficient; one
  way they do this is through 'value range propagation' (VRP). This technique tries
  to figure out the possible values a variable can hold at different points in your
  program. For pointers (variables that store memory addresses), the compiler also
  tracks 'pointer ranges' or `prange`, which are the possible memory addresses a pointer
  could point to. Previously, if the compiler determined a pointer couldn't be null
  (it had a non-zero range), it would stop tracking further details about what it
  *could* point to. This commit changes that. Now, even if a pointer is known to be
  non-null, the compiler continues to refine its understanding of what that pointer
  might be pointing to based on later parts of your code. This improved analysis can
  lead to more accurate optimizations, making your programs run faster and potentially
  avoiding certain bugs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ca582ee36820a318fbc506928503282a5e35603a
date: '2026-06-11'
is_stub: false
---

Previously, the GCC `ranger_cache` treated any pointer range that became non-zero as an invariant, effectively stopping further analysis of its points-to information. This approach is no longer valid because subsequent conditional operations might provide new points-to data, even for a non-zero range. The change updates the `set_global_range` method in `gimple-range-cache.cc` to ensure that nonzero pointer ranges are no longer considered invariant, allowing more fine-grained points-to analysis to continue for these types.
