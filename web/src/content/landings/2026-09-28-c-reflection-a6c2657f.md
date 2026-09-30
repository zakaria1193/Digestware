---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- compiler
commit_hash: a6c2657fc6aa507315d4ca81573ebb026fae1142
source_type: github
author: Marek Polacek
headline: Skip templated clones in members_of for reflection
tldr: Reflection's `members_of` now correctly ignores templated constructor clones.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `gcc/cp/reflect.cc`, the `class_members_of` function's logic for
  skipping cloned declarations has been extended to also handle templated clones.
  The `DECL_CLONED_FUNCTION_P` check previously missed templated functions, leading
  to `members_of` including multiple instances of constructors generated from templates.
  This commit adds a check to exclude these templated clones, resolving PR127643.
primer_glossary:
- term: reflection
  definition: A programming technique that allows code to inspect and modify its own
    structure and behavior at runtime or compile time. In C++, this refers to compile-time
    reflection features.
- term: members_of
  definition: A function or operation within C++ reflection that returns a list of
    members belonging to a specified class.
- term: template clone
  definition: A copy or instantiation of a function or class template, often generated
    by the compiler.
- term: ctor
  definition: Abbreviation for constructor, a special member function that initializes
    an object of a class.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a6c2657fc6aa507315d4ca81573ebb026fae1142
date: '2026-09-28'
is_stub: false
stub_reason: ''
---

GCC's C++ reflection facility, specifically the `members_of` function, now correctly handles templated constructor clones. Previously, it would include duplicate entries for templated constructors and their clones, such as `__ct`, `__ct_comp`, and `__ct_base`. This change modifies `class_members_of` to skip templated clones, ensuring that the reflection API returns a clean list of members.
