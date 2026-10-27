---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- compiler bug
- type system
commit_hash: d6d1dedff578726b9d0ed55d0ebc28a9dc5b543c
source_type: github
author: Jerry DeLisle
headline: 'fortran: [PR126968] Fix ICE for wrongly guessed inferred ASSOCIATE type'
tldr: Fixes a compiler crash (ICE) in Fortran when an ASSOCIATE type is inferred incorrectly.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch addresses PR126968 by correcting how inferred ASSOCIATE
  types are handled. Previously, when an ASSOCIATE selector was a function call that
  hadn't been parsed, `primary.cc` would guess the type. `gfc_fixup_inferred_type_refs`
  would then attempt to repair the reference chain, but only updated `ref->u.c.sym`,
  leaving `ref->u.c.component` pointing to the guessed type. This mismatch caused
  an ICE in `gfc_conv_component_ref` in the backend. The fix involves re-looking up
  each component reference by name within the corrected derived type, ensuring both
  `u.c.sym` and `u.c.component` are co…
primer_glossary:
- term: ASSOCIATE
  definition: A Fortran construct that allows defining local names for parts of a
    structure or for the results of expressions, simplifying code that accesses nested
    components or frequently uses certain values.
- term: ICE
  definition: Internal Compiler Error. A crash within the compiler itself, indicating
    a bug in the compiler's logic.
- term: derived type
  definition: A user-defined composite data type in Fortran, similar to a struct in
    C or a class in C++, which can contain components of various data types.
- term: component reference
  definition: Accessing a member (component) of a derived type, e.g., `my_struct%component_name`
    in Fortran.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned exactly once, which simplifies many optimization passes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d6d1dedff578726b9d0ed55d0ebc28a9dc5b543c
date: '2026-10-24'
is_stub: false
stub_reason: ''
---

This commit resolves an internal compiler error in GCC's Fortran front-end that occurred due to incorrectly inferred types for ASSOCIATE constructs. When an ASSOCIATE selector was a function not yet parsed, the compiler would guess the type, leading to a mismatch between component references and their types. The fix ensures that component references are re-validated against the corrected type, preventing the ICE and ensuring correct handling of derived types and array components.
