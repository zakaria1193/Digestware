---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- c++20
- chrono
- standards
commit_hash: e1ddbb6f6f2a1230c0d7832228d75a00eaf5a280
source_type: github
author: Jonathan Wakely
headline: 'libstdc++: Use specific feature test macros in <chrono>'
tldr: Switches <chrono> header in libstdc++ to use feature test macros instead of
  __cplusplus checks.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch replaces most `__cplusplus` preprocessor checks in `<bits/chrono.h>`
  with feature test macros. For standard C++20 chrono features, it uses compiler-provided
  macros or `__glibcxx_chrono_cxx20`. The primary motivation is to correctly signal
  the availability of C++20 chrono features, especially for C++20 conformance. A known
  limitation is the continued use of `__cplusplus` for functions like `chrono::abs`
  and `chrono::floor` in freestanding environments, as `__cpp_lib_chrono` is not defined
  there; this is noted as a follow-up task.
primer_glossary:
- term: __cplusplus
  definition: A predefined macro that indicates the C++ language standard version
    being used. For C++20, it is typically defined as 202002L or a higher value.
- term: feature test macro
  definition: A macro used in C++ to conditionally compile code based on the availability
    of specific language or library features, as defined by C++ standards.
- term: <chrono>
  definition: A C++ standard library header that provides types and functions for
    measuring, tracking, and manipulating time.
- term: freestanding environment
  definition: A minimal C++ execution environment where only a subset of the standard
    library is available. This is common in embedded systems or operating system kernels.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e1ddbb6f6f2a1230c0d7832228d75a00eaf5a280
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

The `<chrono>` header in libstdc++ has been updated to use specific C++ feature test macros, such as compiler-defined macros for Core C++ features and `__glibcxx_chrono_cxx20` for C++20 chrono features, rather than relying solely on the `__cplusplus` macro. This provides a more precise way to control feature availability, although `chrono::abs`, `chrono::floor`, etc., still use `__cplusplus` for freestanding environments due to the `__cpp_lib_chrono` macro not being defined in that context.
