---
project: gcc
subsystem: build-system
patch_id: null
tags:
- build
- lto
- bootstrap
- gmp
- mpfr
commit_hash: 84bba23575590b0fcd51094af3a38dd410d0cf69
source_type: github
author: Tamar Christina
headline: Strip checking flags when compiling GMP to fix LTO bootstrap
tldr: LTO bootstrap failures due to compiler flag mismatches in GMP are fixed by stripping
  flags.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses an issue in the GCC build system, specifically
  related to LTO (Link-Time Optimization) bootstrapping. The problem arises because
  compile-time flags (`-fno-checking` and `-fchecking=1`) used for MPFR and GMP during
  bootstrapping are being incorrectly included in the LTO metadata (`.gnu.lto.*` sections)
  via generated headers. The `compare-lto` tool then fails due to these flag discrepancies.
  The solution introduces autogen macros and Scheme functions to strip these flags
  only for MPFR and GMP compilation, preventing them from polluting the LTO metadata.
primer_glossary:
- term: LTO
  definition: Link-Time Optimization. A compiler optimization technique where the
    compiler performs whole-program optimization at link time, after all source files
    have been compiled.
- term: bootstrap
  definition: The process of building a compiler using an earlier version of itself.
    A 'clean' bootstrap means building from source with no pre-built components. An
    LTO bootstrap involves using LTO during the compiler's own build.
- term: GMP
  definition: GNU Multiple Precision Arithmetic Library. A free library for arbitrary-precision
    arithmetic. GCC uses it internally for certain calculations.
- term: MPFR
  definition: Multiple Precision Floating-Point Reliable Library. A C library that
    extends the IEEE 754 standard to an arbitrary number of correctly rounded binary
    floating-point formats. GCC uses it for floating-point emulation.
- term: Makefile.tpl
  definition: A template file used by GCC's build system to generate the final Makefile.
    It contains build rules and variables that are processed by 'configure' and 'make'.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/84bba23575590b0fcd51094af3a38dd410d0cf69
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This commit resolves failures in the LTO bootstrap process that occurred because compiler checking flags like `-fno-checking` and `-fchecking=1` were incorrectly embedded in GMP's generated header files. These flags leaked into LTO metadata, causing miscompares between build stages. The fix modifies the build system to strip these flags specifically when compiling GMP and MPFR, preventing the issue and ensuring a successful LTO bootstrap across various configurations and architectures.
