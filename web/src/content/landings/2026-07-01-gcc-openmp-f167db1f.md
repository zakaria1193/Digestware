---
project: gcc
subsystem: gcc/openmp
patch_id: null
tags:
- openmp
- OMPT
- compiler internals
- runtime
commit_hash: f167db1fa47db24fdb93e9ef75c2786245702e09
source_type: github
author: Paul-Antoine Arras
headline: Pass iteration count to static worksharing builtins for OMPT
tldr: OpenMP static worksharing builtins now receive loop iteration count for future
  OMPT integration.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `GOMP_loop_static_worksharing`, `GOMP_loop_static_worksharing_start`,
  `GOMP_distribute_static_worksharing`, and `GOMP_distribute_static_worksharing_start`
  builtins have been updated to include a `long niter` parameter. In `omp-expand.cc`,
  the calls to these builtins are moved after the loop iteration count is computed,
  allowing this count to be passed. This lays the groundwork for OMPT instrumentation,
  which may utilize the iteration count for runtime analysis and control.
primer_glossary:
- term: OpenMP
  definition: An API for shared-memory multiprocessing programming that supports a
    common, scalable model of shared-memory and mandated memory consistency models.
- term: OMPT
  definition: OpenMP Tools Interface, a standard interface for developing tools that
    interact with and profile OpenMP applications at runtime.
- term: static worksharing
  definition: A type of loop parallelization in OpenMP where iterations are divided
    among threads statically before execution begins, typically in chunks.
- term: builtins
  definition: Special functions recognized by the compiler that perform specific,
    often low-level or optimized, operations.
- term: niter
  definition: An argument representing the total number of iterations in a loop, added
    to OpenMP worksharing builtins in this commit.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f167db1fa47db24fdb93e9ef75c2786245702e09
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This commit modifies OpenMP's static worksharing builtins to accept the total number of loop iterations as a new argument, `niter`. While `niter` is currently unused, this change prepares the compiler for forthcoming integration with the OpenMP Tools Interface (OMPT) by ensuring the iteration count is available when the worksharing constructs are expanded.
