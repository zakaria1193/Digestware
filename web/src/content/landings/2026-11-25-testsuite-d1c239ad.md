---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- float16
- compiler-options
commit_hash: d1c239ad86e7d62ad089c07b87a53b3b2e145280
source_type: github
author: Jakub Jelinek
headline: Fix up sso-22.c test
tldr: Corrects a test case that failed due to missing options for _Float16 support.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gcc.dg/sso-22.c` test case was failing because it relied on `_Float16`
  (likely a custom or experimental type, potentially related to IEEE 754-2008 or a
  future extension) without the compiler being instructed to enable the necessary
  target-specific options (e.g., `-msse2` or similar) that provide `_Float16` support.
  The `dg-add-options` directive is a testsuite mechanism to automatically add compiler
  flags to the test invocation based on specific features or types used in the test
  code. This commit adds `float16` to the `dg-add-options` directive, ensuring the
  test runs with the appropria…
primer_glossary:
- term: _Float16
  definition: A floating-point type with 16 bits of precision. It is part of proposals
    for future C/C++ standards and may require specific compiler flags to enable.
- term: i686-linux
  definition: A target triplet specifying the architecture (Intel Pentium Pro and
    later x86 processors), operating system (Linux), and vendor. In this case, it
    indicates a 32-bit x86 Linux system.
- term: dg-add-options
  definition: A directive used in GCC's testsuite to specify compiler options that
    should be added when compiling a particular test case.
- term: testsuite
  definition: A collection of programs and scripts used to verify the correctness
    of the compiler by testing various language features, optimizations, and target-specific
    behaviors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d1c239ad86e7d62ad089c07b87a53b3b2e145280
date: '2026-11-25'
is_stub: true
stub_reason: low_score
---

A GCC test case (`sso-22.c`) was failing on the i686-linux target because it used the `_Float16` type without the necessary compiler options. This commit adds the `dg-add-options float16` directive to the test file, ensuring that the required flags are enabled during test execution. This fixes the test and guarantees correct behavior for `_Float16` on platforms that support it.
