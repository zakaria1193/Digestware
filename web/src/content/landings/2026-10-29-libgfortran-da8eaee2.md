---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- coarray
- parallel-programming
- error-handling
commit_hash: da8eaee295071ab2c24c837e0323a10463174a8e
source_type: github
author: Jerry DeLisle
headline: Handle coarray allocation pool exhaustion and size overflow
tldr: ' libgfortran now correctly reports errors for coarray allocation pool exhaustion
  and size overflows, preventing hangs and data corruption.'
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: These commits resolve two related issues in `libgfortran`'s `caf_shmem`
  implementation concerning coarray allocation and size management. The first (da8eaee295071ab2c24c837e0323a10463174a8e)
  fixes a deadlock scenario where `ALLOCATE` of a coarray component failed while holding
  the allocator lock, and the shared memory pool could not accommodate a larger table
  of coarray IDs. The fix ensures the table remains unchanged and the error is reported
  via STAT=/ERRMSG. It also corrects freeing logic for component tokens. The second
  commit (0235a09b822088b8bea3bc3fccbea3a8fc773d29) introduces `mul_siz…
primer_glossary:
- term: coarray
  definition: A Fortran language feature that allows for parallel programming by providing
    a syntax for declaring objects that are implicitly distributed across images (processes
    or threads).
- term: libgfortran
  definition: The runtime library for the GNU Fortran compiler (gfortran). It provides
    support for language features, intrinsic procedures, and I/O operations.
- term: caf_shmem
  definition: Coarray Fortran Shared Memory. A specific implementation within libgfortran
    for handling coarray communication and data distribution using shared memory on
    multi-node systems.
- term: STAT=
  definition: A Fortran specifier used with I/O statements and allocation operations
    to indicate the status of the operation. A value of 0 typically means success,
    while a non-zero value indicates an error.
- term: ERRMSG=
  definition: A Fortran specifier used with I/O statements and allocation operations
    to provide a descriptive error message when an error occurs (indicated by STAT=).
- term: SIZE_MAX
  definition: A C preprocessor macro defined in <stdint.h> representing the maximum
    value for an object of type size_t. Used here to detect and prevent integer overflow.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/da8eaee295071ab2c24c837e0323a10463174a8e
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This pair of commits addresses critical issues in libgfortran's coarray shared memory implementation related to allocation pool exhaustion and integer overflow. Previously, attempting to allocate a coarray that exceeded the shared memory pool size could lead to image hangs. Now, such failures are reported through STAT= and ERRMSG=, and the system remains stable. Additionally, calculations involving coarray sizes now saturate at SIZE_MAX to prevent overflow, ensuring that requests for excessively large coarrays are correctly rejected.
