---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- compiler bugs
commit_hash: ae22dab993a717e8c7da11faac5c3f5d208cab85
source_type: github
author: Paul Thomas
headline: 'Fortran: Fix parameterized derived type errors'
tldr: Improves handling of parameterized derived types in Fortran by correcting how
  component initializers and lengths are simplified.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch in `gcc/fortran` addresses PR82173 concerning Parameterized
  Derived Types (PDTs). It modifies `expr.cc`'s `find_inquiry_ref` to use `gfc_simplify_len`
  after constructing a KIND expression, rather than directly calling `gfc_pdt_find_component_copy_initializer`.
  The `gfc_simplify_len` function is enhanced to better handle PDT string lengths
  that are variables, simplifying the logic by storing the variable name and inserting
  parameter expressions when necessary. This aims to resolve issues where the length
  simplification might not have produced a constant expression correctly.
primer_glossary:
- term: Parameterized Derived Type (PDT)
  definition: A derived type in Fortran whose components or other attributes can be
    specified by parameters at the time of type instantiation, similar to templates
    in C++ or generic types in other languages.
- term: Fortran gfc
  definition: The internal representation and processing framework used by the GNU
    Fortran compiler (gfortran) to manage Fortran source code during compilation.
- term: inquiry reference
  definition: In Fortran, an inquiry refers to a intrinsic function or a type attribute
    that returns information about a variable or type, such as its length or kind.
    An inquiry reference is an expression that invokes such an inquiry.
- term: KIND expression
  definition: In Fortran, KIND specifies the properties of intrinsic data types, such
    as precision or range. A KIND expression is used to determine the KIND value for
    a type.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ae22dab993a717e8c7da11faac5c3f5d208cab85
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

This commit refines the handling of parameterized derived types (PDTs) in the Fortran compiler by adjusting how component inquiries and string lengths are processed. It changes the approach for finding component initializers to use a KIND expression and `gfc_simplify_len`, which simplifies the logic for accessing original code and handling variable string lengths. This change improves robustness when dealing with PDTs that have lengths defined by variables.
