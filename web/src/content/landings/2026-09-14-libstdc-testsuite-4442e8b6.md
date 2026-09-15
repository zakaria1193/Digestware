---
project: gcc
subsystem: libstdc++,testsuite
patch_id: null
tags:
- libstdc++
- c++26
- compiler
- type traits
- UB
commit_hash: 4442e8b6cbffd113ec7bd25f449cc18f104f7150
source_type: github
author: Jakub Jelinek
headline: Implement C++26 std::is_within_lifetime extension.
tldr: C++26 `std::is_within_lifetime` is now implemented in libstdc++ using compiler
  built-ins.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit implements the C++26 P3450R1 paper in `libstdc++`'s `<type_traits>`.
  The `std::is_within_lifetime` type trait now accepts an optional `_Up` template
  parameter, defaulting to `void`. It leverages `__builtin_constant_p` to check if
  the `static_cast<const volatile _Up*>(__p)` expression, which is part of the standard's
  UB diagnosis for pointer conversions, is a compile-time constant. This follows up
  on an earlier change that enabled constexpr evaluation of such downcasts.
primer_glossary:
- term: std::is_within_lifetime
  definition: A C++ type trait that checks if a given pointer is within the lifetime
    of a specified object. The C++26 extension adds flexibility for specific pointer
    conversions.
- term: P3450R1
  definition: A C++ standardization proposal document (Revision 1) titled 'Extend
    std::is_within_lifetime'.
- term: __builtin_constant_p
  definition: A GCC built-in function that returns non-zero if its argument is a compile-time
    constant, and zero otherwise. Used to enable compile-time optimizations and checks.
- term: constexpr evaluation
  definition: The process by which the compiler evaluates expressions or function
    calls at compile time, rather than at runtime. This can enable optimizations and
    is required for certain language features.
- term: UB
  definition: Undefined Behavior. In C++, this means the program's behavior is unpredictable
    and can lead to crashes, incorrect results, or security vulnerabilities. Compilers
    often try to detect and diagnose UB.
- term: static_cast
  definition: A C++ casting operator used for explicit conversions between related
    types, such as converting a base class pointer to a derived class pointer (downcasting).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4442e8b6cbffd113ec7bd25f449cc18f104f7150
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

GCC's libstdc++ now implements the C++26 proposal P3450R1, which extends `std::is_within_lifetime`. This implementation uses `__builtin_constant_p` to determine if a `static_cast` mandated by the standard can be evaluated as a constant expression. New test cases verify this functionality.
