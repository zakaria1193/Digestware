---
project: gcc
subsystem: c++/contracts
patch_id: null
tags:
- c++
- contracts
- templates
commit_hash: d7a18fca936d64d8c6e7ef7c535e2cfc6665aa8d
source_type: github
author: Wang Jinghao
headline: C++ contracts handle parameter pack expansions correctly.
tldr: Fixes C++26 contract conditions with parameter pack expansions to correctly
  use local specializations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The C++20/26 contracts feature requires careful handling of scope and
  parameter substitution. In `pt.cc`, the `make_pack_expansion` function was using
  `at_function_scope_p()` to determine the context for substituting template parameters
  within parameter packs. However, contract conditions are parsed outside the immediate
  function scope, causing this check to fail. This change introduces `local_bindings_p`
  and adjusts the `enum scope_kind` in `name-lookup.h` so that parameter pack substitutions
  within contracts correctly identify and utilize local specializations, resolving
  PR125011.
primer_glossary:
- term: C++26 contracts
  definition: A C++ language feature (tentatively C++26) that allows developers to
    specify contract conditions (preconditions, postconditions, assertions) directly
    in the code. These contracts can be used for static analysis, runtime checking,
    and documentation.
- term: parameter pack expansion
  definition: A C++ feature that allows a template parameter pack (a pack of zero
    or more template arguments) to be expanded into individual arguments, for example,
    in a function call or a type list.
- term: local specialization
  definition: In C++ templates, a specialization that is defined within a specific
    scope, typically within a function or a class, allowing for context-specific template
    behavior.
- term: scope_kind
  definition: An enumeration in GCC that represents different types of scopes within
    the C++ code, such as function scope, class scope, or contract scope, used to
    manage symbol visibility and name lookup.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d7a18fca936d64d8c6e7ef7c535e2cfc6665aa8d
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in C++26 contract conditions where parameter pack expansions were not correctly using local specializations. Previously, the `at_function_scope_p()` check incorrectly returned false when parameter pack expansions were formed in contract conditions, leading to improper substitution. The fix involves using `local_bindings_p` and reordering scope kinds to ensure parameter packs are handled correctly within contract conditions, aligning their behavior with that inside a function body.
