---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- compiler error
- template
commit_hash: 8fb57eda04f88f4e0d1cbbcc209533fd9689dd9d
source_type: github
author: Marek Polacek
headline: Fix ICE with '&template [:members_of():]' in reflection
tldr: Resolves a compiler internal error when using C++ reflection with template members.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The C++ reflection implementation in GCC (`reflect.cc`, `parser.cc`,
  `semantics.cc`) handles complex syntax for compile-time introspection. This patch
  addresses an ICE (`PR124794`) occurring with expressions like `&template [:members_of():]`.
  The problem arises because `members_of` can return a set of overloads, including
  template declarations. The parsing logic in `cp_parser_splice_expression` was not
  correctly constructing the necessary `BASELINK` around an `OVERLOAD` set containing
  a `TEMPLATE_DECL` when `members_of` was involved. Additionally, the `baselink_for_fns`
  helper function was mo…
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. A serious error that occurs within the compiler
    itself, typically due to a bug in the compiler's logic or an unexpected program
    construct, causing the compilation to halt.
- term: reflection
  definition: A feature in some programming languages that allows code to inspect,
    introspect, and modify its own structure and behavior at runtime or compile time.
    In C++, this is an evolving area, allowing compile-time examination of types and
    entities.
- term: BASELINK
  definition: A data structure or concept within GCC's C++ front-end used to represent
    a link or relationship between a base class and a derived class in the context
    of name lookup or member access. It helps manage scope and inheritance.
- term: OVERLOAD
  definition: A set of functions or function templates that share the same name but
    have different parameter lists. The compiler must determine which specific overload
    is being called based on the arguments provided.
- term: TEMPLATE_DECL
  definition: Represents a template declaration (e.g., a function template or class
    template) within the compiler's internal representation.
- term: members_of
  definition: A C++ reflection expression operator that retrieves members of a given
    type or entity. It is used for compile-time introspection.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8fb57eda04f88f4e0d1cbbcc209533fd9689dd9d
date: '2026-07-31'
is_stub: false
stub_reason: ''
---

This commit fixes an internal compiler error (ICE) that occurred when using C++ reflection with expressions like `&template [:members_of():]`. The issue stemmed from incorrect handling of overloaded function templates within the reflection parsing logic. The compiler failed to correctly wrap template declarations in an `OVERLOAD` set and apply necessary context like `BASELINK`. This change ensures that both `OVERLOAD` and `BASELINK` are appropriately applied, resolving the ICE and improving the robustness of C++ reflection.
