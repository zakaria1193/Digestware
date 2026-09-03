---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- gcc
- libstdc++
- C++26
- compile time
- type safety
commit_hash: eccc490c21fc7c9dadf8d13566963bce151c902d
source_type: github
author: Jakub Jelinek
headline: Implement C++26 P2641R4 - Checking if a union alternative is active
tldr: Implements C++26 P2641R4 in libstdc++ for checking union active members at compile
  time using `__builtin_is_within_lifetime`.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Implements C++26 P2641R4 (`std::is_within_lifetime`) using GCC's `__builtin_is_within_lifetime`.
  The builtin checks if a pointer `__p` points into the lifetime of an object. For
  unions, this specifically verifies if `__p` refers to the currently active member.
  This patch defers implementation of P3450R1 and correct `std::allocator` constant
  evaluation, which depend on further changes (e.g., `CONSTRUCTOR` bit). The test
  case `within-lifetime3.C` is included but partially guarded.
primer_glossary:
- term: libstdc++
  definition: The standard C++ library implementation used by GCC.
- term: union
  definition: A user-defined data type that can store different data types in the
    same memory location, but only one at a time.
- term: P2641R4
  definition: A C++ standard proposal (Revision 4) that introduces a mechanism to
    check which alternative in a union is active at compile time.
- term: compile-time evaluation
  definition: The process of evaluating expressions or functions during the compilation
    phase, rather than at runtime. This is often referred to as 'constexpr' or 'consteval'
    evaluation in C++.
- term: __builtin_is_within_lifetime
  definition: A GCC-specific intrinsic function that checks if a given pointer points
    within the allocated lifetime of an object.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/eccc490c21fc7c9dadf8d13566963bce151c902d
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

This patch implements the C++26 feature P2641R4, allowing compile-time checks for which member of a union is currently active. It introduces a builtin function that returns true if a given pointer points to an active union member, with specific handling for constant expressions and lifetime rules. This aligns GCC's libstdc++ with Clang's implementation of the paper, enhancing type safety and enabling more robust compile-time evaluations.
