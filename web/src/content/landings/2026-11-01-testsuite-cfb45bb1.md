---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- LTO
- binutils
commit_hash: cfb45bb1e58aedb8dc7d787dcdeda17c1e4b5a04
source_type: github
author: Torbjörn SVENSSON
headline: Use gcc-nm for symbol scans in testsuite
tldr: Testsuite symbol scans now use `gcc-nm` to ensure proper handling of LTO plugins
  and other build-time tool dependencies.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `scan-symbol-common` helper in `lib/gcc-dg.exp`
  to use `gcc-nm` instead of a generic `nm` found in the build tree. This is analogous
  to the earlier change for `gcc-ar` (r16-7327-gc9addbc79ac0f9). The primary motivation
  is to ensure that LTO-related tests, which depend on `liblto_plugin.so`, correctly
  locate the plugin by using the `nm` tool that is aware of the build environment,
  especially when LTO is configured. It also introduces `GCC_NM_UNDER_TEST` for explicit
  control.
primer_glossary:
- term: gcc-nm
  definition: A wrapper script or executable that invokes the GNU Binutils 'nm' utility,
    often configured to work within a specific GCC build environment. It helps ensure
    that the correct version of 'nm' is used, especially when dealing with complex
    build configurations like LTO.
- term: LTO
  definition: Link-Time Optimization. A compiler optimization technique where the
    optimization process is deferred until link time, allowing the linker to optimize
    across multiple object files.
- term: liblto_plugin.so
  definition: A shared library that implements the Link-Time Optimization (LTO) plugin
    interface for GCC. It enables GCC to perform LTO during the linking stage.
- term: testsuite
  definition: A collection of tests used to verify the correctness and functionality
    of the GCC compiler. It includes various test cases for different languages, features,
    and optimization levels.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cfb45bb1e58aedb8dc7d787dcdeda17c1e4b5a04
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

The GCC testsuite now uses `gcc-nm` for symbol scanning, ensuring it finds the correct `nm` tool associated with the compiler being tested. This resolves an issue where LTO tests failed due to `liblto_plugin.so` not being found. The change also allows overriding `gcc-nm` via the `GCC_NM_UNDER_TEST` environment variable, similar to how `gcc-ar` is handled.
