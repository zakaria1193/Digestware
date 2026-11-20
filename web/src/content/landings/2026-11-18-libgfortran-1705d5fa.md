---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- bugfix
- memory management
commit_hash: 1705d5fa6e08dd75f479de1bdf820b56e7727aa9
source_type: github
author: Jerry DeLisle
headline: libgfortran checks mmap results against MAP_FAILED.
tldr: Fixed libgfortran's shared memory initialization to correctly detect mmap failures,
  preventing segfaults and misleading error messages.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `shared_memory_init` function in `libgfortran/caf/shmem/shared_memory.c`
  incorrectly checked the return value of `mmap` for failure. POSIX systems signal
  `mmap` failure by returning `MAP_FAILED` (typically `(void*)-1`), not `NULL`. This
  commit corrects the check to `MAP_FAILED`, ensuring that `mmap` failures are detected
  and handled properly, preventing subsequent memory access errors.
primer_glossary:
- term: mmap
  definition: Memory map. A system call that maps files or devices into memory. It's
    used here to establish shared memory segments for inter-process communication.
- term: MAP_FAILED
  definition: A special return value from `mmap` indicating that the memory mapping
    failed. It's typically defined as `(void*)-1`.
- term: libgfortran
  definition: The GNU Fortran runtime library, providing support for Fortran programs
    compiled by GCC.
- term: CAF
  definition: Coarray Fortran. A Fortran language feature for parallel programming,
    allowing explicit parallel data structures (corays) and synchronization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1705d5fa6e08dd75f479de1bdf820b56e7727aa9
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

The libgfortran library's shared memory initialization now correctly checks the result of `mmap` against `MAP_FAILED`. Previously, it incorrectly compared the result to `NULL`, leading to unnoticed `mmap` failures. This could cause segfaults on first access or confusing 'no common state' errors, as observed in the supervisor restarting images.
