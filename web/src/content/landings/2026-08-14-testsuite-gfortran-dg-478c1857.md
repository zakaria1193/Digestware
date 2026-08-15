---
project: gcc
subsystem: testsuite/gfortran.dg
patch_id: null
tags:
- gfortran
- testsuite
- fortran
- regression
commit_hash: 478c1857b4afb88d7f69a4c79158350908fa8eed
source_type: github
author: Hans-Peter Nilsson
headline: 'Gfortran tests: Gate on fd_truncate capability'
tldr: Ensures Fortran tests requiring file truncation only run on systems that support
  it.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit gates several `gfortran.dg` test cases on the `effective_target`
  for `fd_truncate`. This capability corresponds to the availability of `chsize` or
  `ftruncate` system calls, which are used by libgfortran's I/O routines (e.g., `unix.c:raw_truncate`).
  Without this gate, tests that implicitly or explicitly trigger file truncation might
  fail on platforms lacking these system calls, even if the Fortran code is valid.
  Similar gating has been applied in previous years to maintain test stability across
  diverse target environments.
primer_glossary:
- term: gfortran.dg
  definition: The directory within the GCC testsuite that contains regression tests
    specifically for the Gfortran compiler.
- term: fd_truncate
  definition: A target capability indicating that the system supports file truncation
    operations, typically via system calls like `ftruncate()` or `chsize()`. These
    are essential for resizing files.
- term: effective_target
  definition: In the context of GCC test suites, this refers to the specific capabilities
    and features of the target architecture and operating system that are available
    and relevant for a particular test case.
- term: chsize
  definition: A system call, often found on older Unix-like systems, used to change
    the size of a file. It is functionally similar to `ftruncate`.
- term: ftruncate
  definition: A POSIX system call that truncates (or extends) a file specified by
    a file descriptor to a specified length. It is commonly used for file size manipulation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/478c1857b4afb88d7f69a4c79158350908fa8eed
date: '2026-08-14'
is_stub: true
stub_reason: low_score
---

Several Gfortran test cases are now gated on the `fd_truncate` capability. This change prevents these tests from running on targets that do not support file truncation operations like `chsize` or `ftruncate`. Previously, tests that involved file truncation could fail unexpectedly on such systems, even if the code itself was correct. Gating these tests ensures they only execute in environments where the underlying functionality is available, improving test reliability.
