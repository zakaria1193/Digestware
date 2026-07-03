---
project: gcc
subsystem: gcc/c++/reflection
patch_id: null
tags:
- c++
- reflection
- compiler
commit_hash: 8ee8f2beab432c57a5b68b8816910c985c8e9356
source_type: github
author: Marek Polacek
headline: 'C++/reflection: members_of skips built-in functions.'
tldr: Reflection API now correctly excludes built-in functions from member listings.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: C++20 reflection `P0157R1` implementation, specifically `members_of`.
  This commit adds a check for `DECL_IS_UNDECLARED_BUILTIN` to `namespace_members_of`
  to prevent intrinsic functions like `__builtin_abs` from being exposed in reflection
  results, while still allowing user-defined functions like `abs`.
primer_glossary:
- term: C++ reflection
  definition: A C++ language feature that allows a program to inspect and manipulate
    its own structure, metadata, and behavior at runtime. Typically involves querying
    information about types, members, and functions.
- term: members_of
  definition: A function within the C++ reflection library that returns a list of
    members (fields, methods, etc.) belonging to a specified type or namespace.
- term: __builtin_fdimf32x
  definition: An example of a compiler built-in function, providing optimized, low-level
    functionality often not directly implemented by user code.
- term: DECL_IS_UNDECLARED_BUILTIN
  definition: An internal GCC compiler flag or attribute used to identify declarations
    that correspond to compiler-provided built-in functions, distinguishing them from
    standard library or user-defined functions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8ee8f2beab432c57a5b68b8816910c985c8e9356
date: '2026-06-18'
is_stub: false
stub_reason: ''
---

The C++ reflection API's `members_of` function no longer includes compiler built-ins, such as `__builtin_fdimf32x`. This change uses `DECL_IS_UNDECLARED_BUILTIN` to filter these out, significantly reducing the number of elements returned and producing more accurate results for reflection queries.
