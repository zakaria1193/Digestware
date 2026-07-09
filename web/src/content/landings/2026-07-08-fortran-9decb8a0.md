---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- compiler
- allocation
commit_hash: 9decb8a07ac764f2a39885b2a5905515f188da06
source_type: github
author: Jerry DeLisle
headline: 'Fortran: Fix derived type rank for array allocation with mold'
tldr: Corrects an issue where the rank of an array within a derived type was not set
  when using the `mold` keyword during allocation.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `gcc/fortran/trans-array.cc`, `gfc_array_init_size` now correctly
  sets the `rank` field of the `dtype` for arrays allocated using `ALLOCATE(derived_type_var%array_member,
  mold = source_array)`. Previously, the `rank` was omitted, leading to incorrect
  type information for such arrays.
primer_glossary:
- term: derived type
  definition: A user-defined data type in Fortran that can aggregate variables of
    different types and kinds, including arrays and other derived types.
- term: rank
  definition: The number of dimensions of an array. A scalar has rank 0, a vector
    has rank 1, a matrix has rank 2, and so on.
- term: mold
  definition: An optional keyword in Fortran's `ALLOCATE` statement that specifies
    the type, kind, rank, and shape of the array to be allocated, based on an existing
    array or variable.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9decb8a07ac764f2a39885b2a5905515f188da06
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This change fixes a bug in Fortran's array allocation where the rank of an array inside a derived type was not correctly determined when the `mold` keyword was used. The `gfc_array_init_size` function in `trans-array.cc` has been updated to ensure the rank is properly set, preventing potential errors in derived type initialization. New test cases have been added to verify the fix.
