---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- parallel programming
- windows
- configure
commit_hash: 802eeb0ce083461a9f48e22c5d08ab862d88e0fd
source_type: github
author: LIU Hao
headline: 'libgfortran: Enable CAF shared memory for Cygwin and MinGW'
tldr: Enables shared memory support for Coarray Fortran (CAF) on Cygwin and MinGW
  by default.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `libgfortran/caf/shmem/thread_support.{h,c}` headers conditionally
  include `pthread.h` based on `!defined(WIN32) && !defined(__CYGWIN__)`. This commit
  modifies `configure.ac` to unconditionally set `enable_caf_shmem` to true for Cygwin
  and MinGW hosts, ensuring the shared memory backend is built even if a separate
  pthread library isn't linked, as these platforms use native mutexes/semaphores.
primer_glossary:
- term: libgfortran
  definition: The runtime library for the GNU Fortran compiler (gfortran).
- term: CAF
  definition: Coarray Fortran, a parallel programming extension to the Fortran language
    that simplifies data-parallel programming.
- term: shmem
  definition: Shared memory, a form of inter-process communication where multiple
    processes can access the same region of physical memory.
- term: Cygwin
  definition: A POSIX-compatible environment that runs on Windows, providing a Unix-like
    layer.
- term: MinGW
  definition: Minimalist GNU for Windows, a development environment that provides
    a GNU toolchain for creating Windows applications.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/802eeb0ce083461a9f48e22c5d08ab862d88e0fd
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

This commit ensures that the shared memory implementation for Coarray Fortran (CAF) is enabled by default for Cygwin and MinGW hosts. Previously, the build configuration excluded building the `libcaf_shmem` library on these platforms because they do not typically require the POSIX threads library. This change overrides that exclusion, allowing CAF shared memory to be used when available on these systems.
