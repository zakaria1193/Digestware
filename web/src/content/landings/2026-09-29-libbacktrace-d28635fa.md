---
project: gcc
subsystem: libbacktrace
patch_id: null
tags:
- build
- zstd
- configure
- libbacktrace
commit_hash: d28635fae64a32c3f4859aa427960119ed29651c
source_type: github
author: Torbjörn SVENSSON
headline: 'libbacktrace: Use shared zstd detection'
tldr: libbacktrace now uses the shared AC_ZSTD macro for zstd detection.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: libbacktrace now uses AC_ZSTD from pkg.m4 and zstd.m4 instead of its
  own local zstd detection logic. This commit updates aclocal.m4, configure, configure.ac,
  Makefile.am, and Makefile.in to use the shared macro and pkg-config or compiler
  search fallbacks, simplifying zstd support and ensuring it aligns with the main
  GCC build system's approach.
primer_glossary:
- term: AC_ZSTD
  definition: An Autoconf macro used to detect zstd library presence and export compiler
    and linker flags.
- term: pkg-config
  definition: A helper tool used to provide information about installed libraries
    in the system, such as compiler and linker flags.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d28635fae64a32c3f4859aa427960119ed29651c
date: '2026-09-29'
is_stub: true
stub_reason: low_score
---

The libbacktrace component has replaced its local zstd library check with the shared AC_ZSTD macro. This change simplifies zstd detection within libbacktrace by leveraging the common configuration logic already present in the build system, ensuring consistency and maintainability.
