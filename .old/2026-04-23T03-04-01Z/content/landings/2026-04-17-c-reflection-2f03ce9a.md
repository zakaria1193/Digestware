---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- consteval
- templates
commit_hash: 2f03ce9a22d9338fb3de79ad0739f65a10d22f6a
source_type: github
author: Marek Polacek
headline: 'C++: Don''t treat dependent types as consteval-only in reflection.'
tldr: The C++ reflection implementation no longer incorrectly flags dependent types
  as `consteval-only`, preventing spurious errors.
why_it_matters: Prevents the compiler from incorrectly rejecting valid code that uses
  reflection with dependent types, improving usability.
impact_score: 6
impact_rationale: Bug fix that prevents false positive errors in reflection code.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `consteval_only_p` function in `reflect.cc` was incorrectly returning
  true for dependent types in the reflection implementation. This led to errors when
  the type would become non-`consteval-only` after substitution. The fix ensures that
  dependent types are not considered `consteval-only`.
primer_general: C++ reflection allows programs to inspect and manipulate their own
  structure at compile time. `consteval` functions must produce constant values at
  compile time. A 'dependent type' is a type that depends on template parameters,
  and its exact nature is only known after the template is instantiated. This commit
  fixes a bug where the compiler incorrectly assumed that dependent types were always
  `consteval`, leading to errors. Now, the compiler correctly handles dependent types
  during reflection.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2f03ce9a22d9338fb3de79ad0739f65a10d22f6a
date: '2026-04-17'
---

The compiler was incorrectly considering dependent types as `consteval-only` within the C++ reflection implementation. This led to false positive errors when a function's type would become non-`consteval-only` after template substitution. This commit modifies `consteval_only_p` in `reflect.cc` to return false if the type is dependent, resolving the issue.
