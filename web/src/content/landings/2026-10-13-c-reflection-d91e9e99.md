---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- lto
- compiler bug
commit_hash: d91e9e992cf8edf7dfcbe5a2d1f4cb05a66d7640
source_type: github
author: Marek Polacek
headline: 'C++/reflection: Use OPAQUE_TYPE for std::meta::info to fix LTO.'
tldr: C++ reflection's std::meta::info type is now represented using OPAQUE_TYPE,
  resolving LTO issues and a related bug.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The C++ reflection implementation previously used `LANG_TYPE` for `std::meta::info`.
  This commit switches to `OPAQUE_TYPE` (introduced in GCC 11 for PowerPC MMA types)
  in `gcc/cp/reflect.cc` and related tree handling (`gcc/tree.cc`, `gcc/tree.def`).
  This resolves PR c++/126017 (LTO streaming crashes) and PR c++/127856 by correctly
  handling placeholder types and enabling proper type discrimination, while also updating
  DWARF output (`gcc/dwarf2out.cc`) and pretty-printing (`gcc/cp/cxx-pretty-print.cc`).
primer_glossary:
- term: LTO
  definition: Link-Time Optimization. A compiler optimization technique that performs
    optimizations on the entire program at link time, rather than on individual object
    files. This allows for more aggressive interprocedural optimizations.
- term: OPAQUE_TYPE
  definition: A GCC tree node type used to represent types whose internal structure
    is not fully known or relevant at a particular stage of compilation. It was introduced
    for specific target types and is now used for C++ reflection's `std::meta::info`.
- term: LANG_TYPE
  definition: A GCC tree node type historically used to represent language-specific
    types. Its use for `std::meta::info` proved problematic for LTO and type handling.
- term: std::meta::info
  definition: A C++ standard library type (part of C++26 reflection features) that
    provides runtime information about types, functions, and other program entities.
- term: TREE_TYPE
  definition: A fundamental data structure in GCC's internal representation (GIMPLE
    and GENERIC) used to represent various language constructs, including types.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d91e9e992cf8edf7dfcbe5a2d1f4cb05a66d7640
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

This change updates the representation of `std::meta::info` in C++ reflection from `LANG_TYPE` to `OPAQUE_TYPE`. The previous `LANG_TYPE` representation caused issues with Link-Time Optimization (LTO) and failed to be marked correctly, leading to crashes and bugs. Using `OPAQUE_TYPE`, which was introduced for other types, resolves these problems by providing a more suitable representation for this type.
