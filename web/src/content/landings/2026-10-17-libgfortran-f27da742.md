---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- cleanup
- concurrency
commit_hash: f27da74230644cda0b3391955a61781da7164988
source_type: github
author: Jerry DeLisle
headline: Remove unused robust mutex setup in libgfortran's caf_shmem
tldr: Unused and non-functional robust mutex setup code is removed from libgfortran's
  shared memory support.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `libgfortran/caf/shmem/thread_support.c` file had code attempting
  to initialize robust mutexes using `pthread_mutexattr_setrobust`. This was guarded
  by `#ifdef PTHREAD_MUTEX_ROBUST`. In glibc, `PTHREAD_MUTEX_ROBUST` is an enum, not
  a macro, so the `ifdef` always failed. Where it might be a macro, the `EOWNERDEAD`
  error state was not handled, leading to unusable mutexes. This commit removes the
  ineffective setup and the executable bit from the relevant files.
primer_glossary:
- term: robust mutex
  definition: A type of mutex in POSIX threads that allows recovery after the thread
    owning the mutex terminates unexpectedly. It helps prevent deadlocks in multithreaded
    applications.
- term: EOWNERDEAD
  definition: An error code returned by a thread attempting to acquire a robust mutex
    whose previous owner has terminated. Handling this error allows the new owner
    to clean up resources held by the previous owner.
- term: libgfortran
  definition: The runtime library for the GNU Fortran compiler (gfortran).
- term: caf_shmem
  definition: Refers to the shared memory implementation within libgfortran's Coarray
    Fortran (CAF) support.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f27da74230644cda0b3391955a61781da7164988
date: '2026-10-17'
is_stub: true
stub_reason: low_score
---

Code intended to set up robust mutexes in libgfortran's shared memory (caf_shmem) functionality has been removed. The `pthread_mutexattr_setrobust` calls were guarded by a preprocessor macro that was not defined by glibc, rendering them ineffective. Furthermore, even when it was a macro, the necessary error handling for `EOWNERDEAD` was missing, meaning mutexes would become unusable if their owner died. The removal cleans up dead code and avoids potential confusion.
