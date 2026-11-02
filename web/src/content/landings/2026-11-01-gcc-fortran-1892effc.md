---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- compiler
- optimization
- array handling
commit_hash: 1892effc2f4b99665a3aa5d1d27aa093475a158d
source_type: github
author: Mikael Morin
headline: Fortran uses span indexing for polymorphic target dummies
tldr: Fortran's compiler now correctly uses span indexing for polymorphic target dummy
  arguments, improving array handling.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change affects the GCC Fortran frontend, specifically the handling
  of polymorphic dummy arguments with the TARGET attribute. It extends the infrastructure
  for span indexing, previously added for non-polymorphic arguments, to support polymorphic
  entities. The core modifications are in `gfc_dummy_requires_direct_arg` and `gfc_get_array_span`
  in `symbol.cc` and `trans-array.cc`, respectively. The challenge lies in the differing
  attribute storage and array specification for polymorphic entities compared to non-polymorphic
  ones, requiring a more complex update to correctly access the array de…
primer_glossary:
- term: span indexing
  definition: A compiler optimization technique in Fortran that allows efficient access
    to array elements by using information about the array's extents (its 'span').
    This can improve performance by enabling more direct memory access and reducing
    overhead.
- term: polymorphic
  definition: In Fortran, an entity that can assume different types at runtime. This
    is typically achieved through class types and derived types that can hold values
    of different underlying types.
- term: target dummy argument
  definition: A dummy argument (parameter) in a Fortran procedure that is declared
    with the TARGET attribute. This attribute indicates that the argument may be the
    target of a pointer.
- term: array descriptor
  definition: A data structure that holds metadata about an array, such as its bounds,
    type, and memory address. The compiler uses array descriptors to manage and access
    array elements efficiently.
- term: class container
  definition: In Fortran, a type that can hold values of different derived types,
    enabling polymorphism. When an object of a class type is passed as an argument,
    its actual type may vary at runtime.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1892effc2f4b99665a3aa5d1d27aa093475a158d
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This change enables span indexing for polymorphic target dummy arguments in Fortran by modifying how array descriptors are handled. Previously, span indexing was limited to non-polymorphic arguments. The compiler now correctly extracts array span information from class containers for polymorphic entities, ensuring consistent array handling. This fixes a bug where span indexing was not correctly applied to polymorphic dummy arrays, enhancing the compiler's robustness for complex array declarations.
