---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- C++98
- compiler warnings
- diagnostics
commit_hash: b624ebefa3a6a591924c0d680772ba89c5cd08d2
source_type: github
author: Jonathan Wakely
headline: 'libstdc++: Use deleted functions in C++98 mode'
tldr: Enables use of deleted functions in C++98 mode for better diagnostics and robustness.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies libstdc++ headers to use C++98-compatible syntax
  for deleted functions, suppressing C++11 extension warnings via pragmas. This allows
  types that should not be copyable to be explicitly declared as deleted for C++98,
  improving diagnostics and preventing accidental copies that would have previously
  been defined as private or not defined at all. This impacts internal implementation
  details of containers and their allocators, providing clearer error messages when
  unsupported operations are attempted.
primer_glossary:
- term: deleted function
  definition: A function explicitly marked as deleted in C++11 and later. Attempting
    to call a deleted function results in a compile-time error. This is used to prevent
    certain operations, like copying, from being performed.
- term: C++98
  definition: The 1998 standard for the C++ programming language. It is an older version
    of the language with fewer features than modern C++ standards.
- term: libstdc++
  definition: The standard C++ library implementation used by GCC. It provides fundamental
    classes and functions for C++ programming, such as containers, algorithms, and
    I/O streams.
- term: pragma
  definition: A preprocessor directive that allows for implementation-defined behavior.
    In this case, it's used to control compiler warnings.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b624ebefa3a6a591924c0d680772ba89c5cd08d2
date: '2026-09-17'
is_stub: false
stub_reason: ''
---

This change allows the use of deleted functions in C++98 mode within libstdc++, by suppressing C++11 extension warnings with pragmas. Previously, some types were not made copyable at all, relying on C++11 and later testing. Now, deleted copy constructors and assignment operators provide better diagnostics and robustness, preventing accidental use of these functions in C++98 code. Several areas in the STL, including vector<bool> and tree nodes, are updated.
