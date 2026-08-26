---
project: gcc
subsystem: c++
patch_id: null
tags:
- c++
- initialization
commit_hash: bedbcdfd9ab9ff86de96a6338d8eec6bb31ccd22
source_type: github
author: Sebastian Miles
headline: 'c++: assignment from {} with array member NSDMI'
tldr: Fixes initialization of array members in nested structure assignments using
  initializer lists.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In C++, when an array member of a nested structure is initialized via
  an initializer list (e.g., in a nested structure designator init - NSDMI), the `can_convert_array`
  function in `cp/call.cc` previously only accepted `CONSTRUCTOR` or string literals.
  It incorrectly rejected `VEC_INIT_EXPR` which arises when array elements require
  complex initialization. This change ensures `VEC_INIT_EXPR` is handled, allowing
  assignment for such array members.
primer_glossary:
- term: NSDMI
  definition: Nested Structure Designator Initialization. Refers to the initialization
    of members within nested structures or classes, particularly when using initializer
    lists.
- term: VEC_INIT_EXPR
  definition: A GIMPLE intermediate representation construct representing an expression
    that initializes a vector or an array.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bedbcdfd9ab9ff86de96a6338d8eec6bb31ccd22
date: '2026-08-23'
is_stub: false
stub_reason: ''
---

The compiler previously failed to correctly initialize array members within nested structure assignments when using an empty initializer list. This commit updates the `can_convert_array` function to recognize `VEC_INIT_EXPR` as a valid initializer, resolving the issue and enabling proper implicit assignment operator generation for such cases. This fixes PR127016.
