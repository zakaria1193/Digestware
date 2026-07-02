---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- bugfix
- memory-management
commit_hash: bb873ada17b5cea56e7ac4c4156af2f07e8db2cf
source_type: github
author: Paul Thomas
headline: Fortran fixes memory leaks in PDT tests
tldr: GCC's Fortran frontend resolves memory leaks in parameterized derived type (PDT)
  tests by correctly converting the PDT template before building the class symbo…
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In GCC's Fortran frontend, parameterized derived types (PDTs) allow
  for compile-time parametric polymorphism. The `build_struct` function in `decl.cc`
  is responsible for constructing the internal representation of these types. The
  memory leaks arose because the PDT template conversion was delayed until after `gfc_build_class_symbol`
  was invoked. This meant that the symbol table entry was being created from an un-converted
  template, leading to resources being allocated without proper tracking. The fix
  ensures that the PDT template undergoes conversion *before* the call to `gfc_build_class_symb…
primer_general: In programming languages like Fortran, a 'derived type' is like a
  custom data structure you define. A 'parameterized derived type' (PDT) is an advanced
  version where you can specify some properties of the type using parameters at the
  time you declare it, much like templates in C++. When the GCC Fortran compiler processes
  these PDTs, it needs to perform several internal steps to set them up correctly.
  This update fixes a problem where the compiler was leaking memory during this setup.
  Essentially, it was allocating memory for the PDT but then losing track of it because
  it wasn't performing a necessary conversion step at the right time. By reordering
  these internal steps, the compiler now properly manages all the memory it uses when
  working with PDTs, preventing these leaks and making the compiler more robust.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bb873ada17b5cea56e7ac4c4156af2f07e8db2cf
date: '2026-06-23'
is_stub: false
---

This update fixes memory leaks occurring in GCC's Fortran frontend when testing parameterized derived types (PDT). The issue stemmed from an incorrect ordering of operations, specifically failing to convert the PDT template before calling `gfc_build_class_symbol`. By adjusting the sequence in `decl.cc`, the compiler now properly manages memory during PDT processing, preventing resource leaks and improving the stability of Fortran compilation.
