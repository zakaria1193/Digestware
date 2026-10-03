---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- coarray
- bugfix
commit_hash: bd2a164d7fdf1f109a8019aa2d32a2a2ad4893c4
source_type: github
author: Jerry DeLisle
headline: 'libgfortran: Fix coarray team size calculation'
tldr: libgfortran's coarray implementation now correctly determines team sizes using
  the image map, resolving issues with image termination and status reporting.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In libgfortran's coarray support, `caf_shmem.c` previously used `barrier->count`
  to determine `NUM_IMAGES`. This count decreases as images in a team terminate. This
  commit changes the source of `NUM_IMAGES` and related functions (`_gfortran_caf_image_status`,
  `_gfortran_caf_form_team`) to use `team->image_map.size()`, which is invariant to
  image termination. This resolves issues where `FORM TEAM` and collectives operated
  on an incorrect number of images.
primer_glossary:
- term: coarray
  definition: A Fortran language feature providing built-in support for parallel programming
    by allowing direct access to data on other processing units (images).
- term: image
  definition: In Fortran coarrays, an 'image' is an independent sequential execution
    stream, analogous to a process or thread.
- term: team
  definition: A subset of images within a coarray program, allowing for more flexible
    and structured parallel communication patterns.
- term: barrier
  definition: A synchronization primitive that halts all participating images until
    every image has reached the barrier.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bd2a164d7fdf1f109a8019aa2d32a2a2ad4893c4
date: '2026-09-19'
is_stub: false
stub_reason: ''
---

This commit addresses a bug in libgfortran's coarray implementation where team sizes were incorrectly derived from barriers. When images terminated, the barrier size decreased, leading to incorrect `NUM_IMAGES` counts and faulty team formation and collective operations. The fix ensures team sizes are consistently determined from the team's image map, which remains static.
