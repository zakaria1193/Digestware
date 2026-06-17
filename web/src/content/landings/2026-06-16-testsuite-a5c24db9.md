---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- fortran
- resource management
commit_hash: a5c24db958b97c6f804636a1c8d0b25b4b167702
source_type: github
author: Rainer Orth
headline: Limits shared memory use in coarray Fortran tests to prevent excessive resource
  consumption.
tldr: The GCC testsuite now defaults coarray Fortran tests to use 2MB of shared memory,
  avoiding excessive resource use during parallel testing.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `caf.exp` script in the gfortran testsuite manages the execution
  of coarray Fortran tests. Specifically, it configures the `GFORTRAN_SHARED_MEMORY_SIZE`
  environment variable, which dictates the size of the shared memory image for coarray
  programs. The issue arose because the default size was too large for parallel test
  runs on some architectures, leading to resource contention. This commit introduces
  a default of 2MB to mitigate this, with an override mechanism via `GCC_TEST_RUN_EXPENSIVE`
  to allow for more extensive testing when needed.
primer_general: Compilers like GCC include a 'testsuite', which is a collection of
  programs and expected outputs used to verify that the compiler is working correctly
  across various features and architectures. Coarray Fortran is a Fortran language
  feature that enables parallel programming by allowing different instances of a program
  to access shared memory. On some operating systems, the way this shared memory was
  handled during testing could lead to the system running out of resources, especially
  when many tests were run at the same time. This update reduces the default amount
  of shared memory these tests use, preventing resource exhaustion and ensuring the
  testsuite can run reliably on all supported platforms.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a5c24db958b97c6f804636a1c8d0b25b4b167702
date: '2026-06-16'
is_stub: false
---

This change modifies the GCC testsuite to limit the shared memory allocated by coarray Fortran tests using the `-lcaf_shmem` option. Previously, these tests could consume up to 4GB of shared memory per test, causing issues like excessive virtual memory usage, especially on systems like Solaris that don't employ lazy allocation. The new default of 2MB per test prevents these resource exhaustion problems, while still allowing for larger allocations if `GCC_TEST_RUN_EXPENSIVE` is set.
