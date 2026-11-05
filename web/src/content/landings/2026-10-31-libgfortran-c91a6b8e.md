---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- gcc
- glibc
- Y2038
- build
commit_hash: c91a6b8ec7cedb8949675c6855f2f35cfe4100e5
source_type: github
author: Richard Biener
headline: 'libgfortran: Enable 64-bit time_t on 32-bit glibc targets'
tldr: Libgfortran now supports 64-bit time_t on 32-bit glibc to avoid Y2038 issues.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Libgfortran's build system has been updated to conditionally enable
  64-bit `time_t` by defining `_TIME_BITS=64` on 32-bit glibc targets. This is managed
  by a new `LIBGFOR_CHECK_TIME_BITS64` check in `acinclude.m4`, which runs after `AC_SYS_LARGEFILE`.
  It verifies if `time_t` can be widened to 64 bits, necessary to avoid `stat()` overflows
  and related build failures (PR114895). The change doesn't affect the ABI as no exported
  interfaces use `time_t` directly.
primer_glossary:
- term: time_t
  definition: A fundamental C type (usually an integer) that represents calendar time,
    typically as the number of seconds elapsed since the Epoch (January 1, 1970).
    Its size determines the range of dates that can be represented.
- term: Year 2038 problem (Y2038)
  definition: A problem similar to the Year 2000 problem, but specific to 32-bit signed
    integer representations of time. On January 19, 2038, a 32-bit `time_t` will overflow,
    causing systems to incorrectly interpret the date as being in 1901.
- term: stat()
  definition: A system call that retrieves status information about a file or file
    system, such as size, modification times, and permissions. It typically returns
    a `struct stat` containing this information.
- term: libgfortran
  definition: The runtime library for the GNU Fortran compiler (gfortran). It provides
    support for Fortran language features, including I/O operations and intrinsic
    functions.
- term: ABI
  definition: Application Binary Interface. Defines how binary code (compiled programs)
    interacts with the operating system and other libraries. Changes to the ABI can
    break compatibility between different versions of software.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c91a6b8ec7cedb8949675c6855f2f35cfe4100e5
date: '2026-10-31'
is_stub: false
stub_reason: ''
---

Libgfortran now correctly enables 64-bit time_t support on 32-bit glibc systems that can accommodate it, addressing the Year 2038 problem for file timestamp handling. Previously, builds could break due to `stat()` failures on 32-bit `time_t` past January 19, 2038. A new configure check, `LIBGFOR_CHECK_TIME_BITS64`, determines if `_TIME_BITS=64` can be defined, ensuring internal time-related functions remain robust past the Y2038 boundary.
