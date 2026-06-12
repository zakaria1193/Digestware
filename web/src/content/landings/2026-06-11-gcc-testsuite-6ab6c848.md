---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- tls
- c++
- portability
commit_hash: 6ab6c84821e80c0d17e77f3a67a3a931b6fcde9d
source_type: github
author: Iain Sandoe
headline: Test suite now handles emulated Thread-Local Storage for C++ attribute tests.
tldr: The GCC testsuite now correctly accounts for differences in output when testing
  C++ thread-local storage attributes with emulated TLS.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Thread-Local Storage (TLS) provides a mechanism for static or global
  variables to have distinct values for each thread. When the target architecture
  does not natively support TLS, the compiler toolchain provides an emulated implementation.
  This change adjusts the C/C++ test suite's expected output patterns when emulated
  TLS is active, particularly in tests involving attributes like `__thread`. The specific
  files, `c-c++-common/tls-attr-common.c`, `tls-attr-le-pic.c`, and `tls-attr-le-pie.c`,
  are part of the GCC test infrastructure that verifies correct handling of TLS, especially
  in PIC/PIE c…
primer_general: In programs that use multiple threads (like a web browser with many
  tabs), sometimes a variable needs to have a unique value for each thread, even if
  it's declared globally. This is called Thread-Local Storage (TLS). Some computer
  processors have built-in support for TLS, while others don't. When there's no native
  support, the compiler and operating system have to \"emulate\" it using software
  tricks. This update to the GCC compiler's internal tests makes sure that when these
  software tricks are used for TLS, the compiler's output still matches what's expected.
  This helps ensure that programs using TLS work correctly on all kinds of computer
  systems.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6ab6c84821e80c0d17e77f3a67a3a931b6fcde9d
date: '2026-06-11'
is_stub: false
---

This commit updates GCC's testsuite to include specific match criteria for emulated Thread-Local Storage (TLS) in C and C++ attribute tests. Previously, tests for TLS attributes might have failed when using emulated TLS because the generated output differs from that of native TLS implementations. By adding these adjustments to `tls-attr-common.c`, `tls-attr-le-pic.c`, and `tls-attr-le-pie.c`, the test suite now provides more accurate results across various TLS configurations, improving the reliability of attribute testing.
