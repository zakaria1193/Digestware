---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- constexpr
- c++
commit_hash: 77cb5aed66c500758bde3a9edc4f4bff5bfce6ba
source_type: github
author: Tomasz Kamiński
headline: 'libstdc++: Make std::stack constexpr.'
tldr: std::stack and its formatting capabilities are now constexpr.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch enables `constexpr` evaluation for `std::stack` and its
  relational operators and `swap` function, along with its formatter, aligning with
  proposals P3372 and P3391R2. The changes involve marking member functions and operators
  with `_GLIBCXX26_CONSTEXPR` and updating version definitions (`constexpr_stack`,
  `__cpp_lib_constexpr_stack`) to allow compile-time instantiation and manipulation
  of stack objects.
primer_glossary:
- term: constexpr
  definition: A keyword in C++ that indicates a variable or function can be evaluated
    at compile time. This can lead to performance improvements and allows for compile-time
    computations.
- term: std::stack
  definition: A C++ Standard Library container adaptor that provides a LIFO (Last-In,
    First-Out) stack data structure. It is typically implemented using other containers
    like `std::deque` or `std::vector`.
- term: P3372
  definition: A C++ proposal aiming to introduce `constexpr` capabilities for containers
    and adaptors, allowing them to be used in compile-time contexts.
- term: P3391R2
  definition: A C++ proposal, likely related to formatting or I/O, that introduces
    `constexpr` support for formatters.
- term: libstdc++
  definition: The standard C++ library implementation used by GCC.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/77cb5aed66c500758bde3a9edc4f4bff5bfce6ba
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

The `std::stack` container adaptor and its associated formatting functions have been made `constexpr`, implementing parts of the P3372 and P3391R2 proposals. This allows `std::stack` to be used in compile-time contexts, enhancing its utility for constant evaluation and improving compile-time performance for certain applications.
