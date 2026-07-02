---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- bugfix
commit_hash: ea80d5b13dd9c4fdf979234ae24d5d9559402135
source_type: github
author: Marek Polacek
headline: Fixes crash in `can_substitute` with function returning reference.
tldr: GCC's C++ reflection feature no longer crashes when calling `can_substitute`
  on a function type that returns a reference.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's C++ reflection implementation, specifically within `reflect.cc`,
  deals with querying properties of types at compile time. The `eval_can_substitute`
  function determines if one type can substitute another. The bug involved `convert_from_reference`
  being called with a `FUNCTION_TYPE` (e.g., `int&()`) whose return type was a reference.
  While `convert_from_reference` typically handles expressions, calling it on a type
  led to an assertion failure. The fix avoids this call when dealing with types, preventing
  the crash.
primer_general: C++ reflection is a cutting-edge feature that allows programs to examine
  and manipulate their own structure at compile time. Think of it like a program being
  able to "look at its own blueprints." In GCC, a part of the compiler called `reflect.cc`
  handles these reflection queries. This fix resolves a rare bug where the compiler
  would crash when trying to use reflection to check if one type could be substituted
  for another, specifically when dealing with functions that return a reference (like
  `int&`). The compiler was trying to apply an operation meant for actual values to
  a type definition, causing it to crash. The fix simply prevents this incorrect operation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ea80d5b13dd9c4fdf979234ae24d5d9559402135
date: '2026-06-12'
is_stub: false
---

This commit addresses a crash in the C++ reflection mechanism when `eval_can_substitute` was called with a function type returning a reference. Previously, `convert_from_reference` was incorrectly invoked on a function type, leading to a crash. The fix prevents this erroneous call, ensuring the reflection system handles such types correctly.
