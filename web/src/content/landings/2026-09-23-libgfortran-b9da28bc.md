---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- coarray
- fortran
- deadlock
- bugfix
commit_hash: b9da28bcd9af4053544f191f2393a0c79e3d30ae
source_type: github
author: Jerry DeLisle
headline: 'libgfortran: Prevent waiting for terminated images in caf_shmem'
tldr: Ensures that Fortran coarray operations do not indefinitely block when an image
  has terminated.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch, part of the ongoing F2023 coarray conformance effort for
  `libgfortran`'s `caf_shmem`, prevents deadlocks caused by terminated images. Previously,
  images executing `STOP` or `FAIL IMAGE` would remain in team barrier counts, causing
  subsequent `SYNC ALL` operations to block indefinitely. The fix introduces `leave_teams`
  to remove terminated images from all their team barriers before they exit. Additionally,
  it refines `SYNC IMAGES` to correctly handle table indexing when the image count
  changes due to termination.
primer_glossary:
- term: Coarray Fortran (CAF)
  definition: An extension to the Fortran language that provides parallel programming
    capabilities through a syntax for accessing components of distributed memory arrays
    (called 'corray' components) on other images (processes).
- term: image
  definition: In Coarray Fortran, an image represents an independent unit of execution,
    typically a process or thread, that can communicate with other images.
- term: SYNC ALL
  definition: Coarray Fortran synchronization primitive. SYNC ALL synchronizes all
    images in the current team.
- term: FAIL IMAGE
  definition: A Fortran coarray statement that initiates abnormal termination for
    a specific image.
- term: team barrier
  definition: A synchronization point within a team of coarray images where all participating
    images must arrive before any can proceed.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b9da28bcd9af4053544f191f2393a0c79e3d30ae
date: '2026-09-23'
is_stub: false
stub_reason: ''
---

This commit improves the robustness of Fortran's coarray shared memory implementation by preventing indefinite blocking on terminated images. When an image stops or fails, it now properly withdraws from team barriers. This allows other waiting images to proceed once barrier counts reach zero, avoiding deadlocks that previously occurred with synchronization statements like `SYNC ALL`.
