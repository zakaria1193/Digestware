---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- pdt
- gfortran
commit_hash: 40c4b9dcd9be3e63f8e4f6e4e49cdcd341764082
source_type: github
author: Paul Thomas
headline: 'Fortran: Fix errors related to parameterized derived types'
tldr: Resolves multiple issues in gfortran's handling of parameterized derived types.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This series of changes for GCC's Fortran front-end (gfortran) targets
  Parameterized Derived Types (PDTs). It touches `match.cc` and `resolve.cc`, focusing
  on correcting state corruption in `gfc_match_class_is` by clearing `type_param_spec_list`
  and ensuring correct hash value computation. It also refines `resolve_allocate_expr`
  to properly instantiate PDTs from allocate-typespec parameters and introduces helper
  functions in `trans-stmt.cc` for PDT parameter handling during allocation and initialization.
  New tests `pdt_bug9.f90` and `pdt_bug10.f90` are added.
primer_glossary:
- term: Parameterized Derived Type (PDT)
  definition: A derived type in Fortran whose components or type parameters depend
    on other type parameters. This allows for more flexible and generic type definitions.
- term: gfortran
  definition: The GNU Fortran compiler, part of the GCC suite.
- term: CLASS IS matching
  definition: A Fortran construct used for dynamic type checking and assignment, where
    an object of a dynamic type is compared against a specific static type.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/40c4b9dcd9be3e63f8e4f6e4e49cdcd341764082
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

This commit addresses several bugs in the Fortran compiler's support for parameterized derived types (PDTs). It refactors internal structures, corrects type parameter handling during allocation and matching, and adds new test cases to cover the fixed scenarios. These changes improve the robustness of PDT instantiation and class IS matching.
