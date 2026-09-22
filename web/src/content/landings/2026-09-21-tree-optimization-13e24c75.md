---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- bugfix
commit_hash: 13e24c75a812b4838242e8da7d6697d81534a30a
source_type: github
author: Richard Biener
headline: 'tree-optimization: Avoid get_same_sized_vectype in vectorizable_induction'
tldr: Improves vector type selection in induction variable optimization.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vectorizable_induction` function in `tree-vect-loop.cc` previously
  used `get_same_sized_vectype` to determine the vector type for induction variables.
  This function had problematic handling for scalar boolean types. This commit replaces
  `get_same_sized_vectype` with `signed_or_unsigned_type_for`, which directly provides
  signed or unsigned variants of a given type. This simplifies the type selection
  logic and avoids the problematic scalar boolean type handling.
primer_glossary:
- term: vectorizable_induction
  definition: A function within GCC's tree optimization framework that identifies
    and processes induction variables suitable for vectorization.
- term: induction variable
  definition: A variable in a loop that is updated by a constant amount in each iteration,
    often used as a loop counter.
- term: get_same_sized_vectype
  definition: An internal GCC function that attempts to find a vector type of the
    same size as a given type, sometimes exhibiting issues with specific type kinds.
- term: signed_or_unsigned_type_for
  definition: An internal GCC function that returns a signed or unsigned version of
    a given C type, used for type promotion and consistent handling.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/13e24c75a812b4838242e8da7d6697d81534a30a
date: '2026-09-21'
is_stub: false
stub_reason: ''
---

This commit refactors the `vectorizable_induction` function within the tree optimization passes to avoid using `get_same_sized_vectype`. Instead, it now uses `signed_or_unsigned_type_for` to obtain signed or unsigned variants of vector types. This change prevents issues related to the handling of oddball scalar boolean types within `get_same_sized_vectype`, leading to more robust vectorization of induction variables.
