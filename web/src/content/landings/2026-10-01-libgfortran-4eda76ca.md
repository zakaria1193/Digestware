---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- parallelism
- bugfix
commit_hash: 4eda76ca63df945f4c22d76aeca263bd9457887d
source_type: github
author: Jerry DeLisle
headline: 'libgfortran: SYNC IMAGES hang fixed when an image terminates'
tldr: SYNC IMAGES now correctly handles terminated images, preventing hangs.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The caf_shmem.c implementation of SYNC IMAGES now correctly handles
  image termination. Previously, it returned early for stopped/failed images, preventing
  statement pairing and leading to hangs. The fix ensures statements are counted for
  all active images, even if one terminates, and uses a new notify_image_terminated
  function to wake waiting images reliably. This addresses an issue where supervisor
  wakeups could be lost due to race conditions.
primer_glossary:
- term: SYNC IMAGES
  definition: A Fortran Coarray Programming (CAF) statement that synchronizes execution
    across all images (parallel processes) in a coarray. It ensures that all participating
    images reach a common synchronization point before proceeding.
- term: Coarray
  definition: A Fortran language feature that allows programs to express data-parallelism
    using arrays where elements can be accessed across different images (processes).
    It facilitates SPMD-style parallel programming.
- term: Image
  definition: In Fortran's Coarray Programming, an image refers to an individual process
    or execution context participating in the parallel execution of a coarray program.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4eda76ca63df945f4c22d76aeca263bd9457887d
date: '2026-10-01'
is_stub: false
stub_reason: ''
---

A hang in libgfortran&#39;s SYNC IMAGES statement has been fixed. Previously, if an image within a set terminated, other images waiting in SYNC IMAGES would not be released, causing a deadlock. This change ensures that terminated images are counted correctly, allowing SYNC IMAGES to complete even if some images have stopped or failed.
