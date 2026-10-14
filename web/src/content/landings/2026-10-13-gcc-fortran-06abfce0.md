---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- compiler bugs
commit_hash: 06abfce015976234a25e24a72d858b94414a7c87
source_type: github
author: Paul Thomas
headline: 'Fortran: Fix parameterized derived type instance handling'
tldr: Correctly handles parameterization for derived types in Fortran, fixing issues
  with instance creation and referencing.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In the Fortran frontend, handling of Parameterized Derived Types (PDTs)
  involves managing instances and their associated parameters. This series of commits
  fixes several bugs in `decl.cc` and `trans-decl.cc` related to the lifecycle of
  PDT instances. Specifically, it ensures `gfc_get_pdt_instance` correctly increments
  references for imported instances and provides a default initializer. It also guards
  calls to `gfc_allocate_pdt_comp` and `gfc_trans_deallocate` to ensure they are only
  invoked when the symbol has a valid `param_list` or for valid PDTs, respectively,
  preventing crashes and incor…
primer_glossary:
- term: Parameterized Derived Type (PDT)
  definition: A derived type in Fortran whose components or other attributes can be
    specified by parameters at the time of type instantiation, similar to templates
    in C++ or generic types in other languages.
- term: Fortran gfc
  definition: The internal representation and processing framework used by the GNU
    Fortran compiler (gfortran) to manage Fortran source code during compilation.
- term: instance
  definition: A specific occurrence or realization of a type. For a parameterized
    derived type, an instance is created with specific values for its parameters.
- term: references
  definition: In this context, it refers to a count of how many parts of the program
    are using a particular type or instance. This is important for memory management
    and ensuring a type is not deallocated while still in use.
- term: allocatable
  definition: A Fortran keyword used to declare arrays or derived type components
    that can be dynamically allocated and deallocated during program execution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/06abfce015976234a25e24a72d858b94414a7c87
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

This commit addresses several issues related to parameterized derived types (PDTs) in the Fortran compiler. It ensures that new PDT instances are properly initialized and their references are incremented. Additionally, it corrects the conditions under which PDT allocation and deallocation routines can be called, improving the compiler's ability to handle complex type definitions.
