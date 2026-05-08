---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- bugfix
commit_hash: 6d035aa99c3d1197167e085302d8ce015b950b35
source_type: github
author: Marek Polacek
headline: 'c++/reflection: Fix error with ODR-used inline consteval variables.'
tldr: The compiler now correctly handles ODR-used inline variables of consteval-only
  types by checking for DECL_INITIAL.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The issue stemmed from `wrapup_namespace_globals` incorrectly flagging
  ODR-used `inline` variables of `consteval-only` types as errors. This happened because
  such variables are marked `DECL_EXTERNAL`. The fix refines the check to include
  `!DECL_INITIAL` which identifies explicitly initialized variables.  This is in `gcc/cp/decl.cc`.
primer_general: In C++, the One Definition Rule (ODR) requires that an object or function
  has only one definition in a program. Inline variables can be defined in multiple
  translation units, but they must have the same definition. Consteval functions and
  variables are evaluated at compile time. This commit fixes a bug in the C++ reflection
  implementation where the compiler incorrectly flagged inline variables that are
  only used in compile-time contexts as violating the ODR.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6d035aa99c3d1197167e085302d8ce015b950b35
date: '2026-04-21'
---

The compiler was incorrectly issuing an error for ODR-used inline variables of consteval-only types.  The fix strengthens the check in `wrapup_namespace_globals` to also verify that `!DECL_INITIAL` is true before issuing the error. This ensures that variables with definitions are not erroneously flagged as missing definitions.
