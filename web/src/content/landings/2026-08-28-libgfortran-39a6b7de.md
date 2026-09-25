---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- coarray
- fortran
- error handling
- f2023
commit_hash: 39a6b7de56ebd7091c092a4b07fed3809f10544d
source_type: github
author: Jerry DeLisle
headline: 'libgfortran: Terminate all images on ERROR STOP in caf_shmem'
tldr: Ensures ERROR STOP in Fortran coarrays terminates all participating images,
  preventing deadlocks.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates `libgfortran`'s `caf_shmem` to align with F2023's
  `ERROR STOP` semantics. An `ERROR STOP` statement now triggers a coordinated error
  termination of all images within a team. Previously, only the image executing `ERROR
  STOP` terminated, leaving others blocked. The implementation records the error state
  before exiting and the supervisor is responsible for terminating the remaining images.
  This ensures that all images participate in the error termination, preventing potential
  deadlocks.
primer_glossary:
- term: Coarray Fortran (CAF)
  definition: An extension to the Fortran language that provides parallel programming
    capabilities through a syntax for accessing components of distributed memory arrays
    (called 'corray' components) on other images (processes).
- term: ERROR STOP
  definition: A Fortran statement that initiates abnormal termination of the program,
    typically indicating a runtime error.
- term: image
  definition: In Coarray Fortran, an image represents an independent unit of execution,
    typically a process or thread, that can communicate with other images.
- term: supervisor
  definition: In a distributed or parallel system, a process or component responsible
    for managing and coordinating other worker processes or images. In this context,
    it manages coarray image termination.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/39a6b7de56ebd7091c092a4b07fed3809f10544d
date: '2026-08-28'
is_stub: false
stub_reason: ''
---

This change modifies the Fortran coarray shared memory implementation to correctly handle `ERROR STOP` statements. Previously, an `ERROR STOP` on one image would cause other images to block indefinitely on subsequent synchronization operations. Now, `ERROR STOP` correctly initiates error termination across all images in the team, preventing deadlocks and ensuring consistent program termination behavior.
