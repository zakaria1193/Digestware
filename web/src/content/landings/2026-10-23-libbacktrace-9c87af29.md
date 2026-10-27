---
project: gcc
subsystem: libbacktrace
patch_id: null
tags:
- libbacktrace
- build
- cross-compilation
- zstd
commit_hash: 9c87af29325acc2b7c41c88c3d24a30930743111
source_type: github
author: Torbjörn SVENSSON
headline: 'libbacktrace: zstd detection failures are nonfatal for cross-target builds'
tldr: Configuration of libbacktrace for cross-target builds now tolerates missing
  zstd library.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The AC_ZSTD macro, used in libbacktrace's configure.ac, forwards zstd
  detection flags to the target build. This commit adds a new `FAILURE_IS_FATAL` argument
  to AC_ZSTD. For cross-target libbacktrace builds, this argument is set to false,
  preventing configuration failures when the host's zstd library is unavailable on
  the target, as external zstd is not a hard requirement for libbacktrace itself on
  the target.
primer_glossary:
- term: libbacktrace
  definition: A library used by GCC to generate stack traces, typically for debugging
    purposes.
- term: cross-target build
  definition: A build process where the compiler runs on one architecture (the host)
    but generates code for a different architecture (the target). For example, building
    an ARM executable on an x86-64 machine.
- term: zstd
  definition: A fast lossless compression algorithm. GCC may use it for host tools
    or forward its configuration to target libraries.
- term: AC_ZSTD
  definition: An Autoconf macro used to detect the zstd compression library and its
    availability. This commit modifies it to optionally control whether a failure
    to find zstd is considered a fatal error.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9c73440b6f8b81040379de62dc040aa8d2fd0803
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

GCC's zstd configuration options were being forwarded to target libraries, causing build failures for libbacktrace when zstd was not installed on the target. This change modifies the AC_ZSTD macro to accept an optional argument that makes zstd detection failures nonfatal. This allows cross-target builds of libbacktrace to succeed even without an external libzstd installation, while preserving the requirement for host and native builds.
