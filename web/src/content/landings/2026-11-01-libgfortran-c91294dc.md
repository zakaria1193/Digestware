---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- performance
- concurrency
commit_hash: c91294dca7d29682c55c8b989c0197f84eb57e53
source_type: github
author: Jerry DeLisle
headline: libgfortran improves unit cache lookup performance
tldr: Libgfortran optimizes unit cache lookups by using atomic operations and a free
  list, significantly improving performance on Darwin.
impact_score: 8
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit refactors libgfortran's unit management to improve concurrency.
  The `unit_rwlock` is removed from `get_gfc_unit`, which now probes a direct-mapped,
  64-slot unit cache. Units are reused from a `unit_free_list` instead of being immediately
  freed by `close_unit_1`, ensuring cache pointers remain valid. This resolves a Darwin-specific
  performance regression (PR127893) where the previous mutex-based locking caused
  excessive contention. `check_for_recursive` now attempts a non-blocking probe of
  the cache before acquiring `unit_rwlock` for a full tree traversal. `find_file`
  and `flush_al…
primer_glossary:
- term: libgfortran
  definition: The GNU Fortran runtime library, providing functions and data structures
    necessary for executing Fortran programs compiled by GCC.
- term: unit
  definition: In Fortran I/O, a unit number is an identifier associated with a file
    or data stream.
- term: rwlock
  definition: A read-write lock, a synchronization primitive that allows multiple
    readers or a single writer to access a resource.
- term: Darwin
  definition: The name of the operating system that forms the core of macOS, iOS,
    and other Apple operating systems. It is an open-source Unix-like operating system.
- term: PR127893
  definition: Problem Report 127893, a bug report filed against libgfortran, indicating
    a performance issue with concurrent I/O operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c91294dca7d29682c55c8b989c0197f84eb57e53
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

Libgfortran has substantially improved the performance of unit cache lookups, particularly on Darwin systems, by eliminating contention on the `unit_rwlock`. Previously, every data transfer statement acquired this lock, leading to severe performance degradation under heavy parallel I/O loads. This change introduces a direct-mapped cache with 64 slots, accessed atomically. Closed units are now placed on a free list for reuse, preventing dangling pointers and allowing cache reads without the global lock. If a cached unit is found to be closed or doesn't match expectations, the lookup falls back to the tree search under the `unit_rwlock`.
