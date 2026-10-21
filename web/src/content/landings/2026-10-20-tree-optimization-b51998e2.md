---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- points-to analysis
- optimization
- restrict
- C++
commit_hash: b51998e2208b36fef6a1f68a18fdd6e562f910a4
source_type: github
author: Richard Biener
headline: Add PTA constraints for restrict-qualified parameter fields
tldr: Fixes Points-To Analysis (PTA) for restrict-qualified parameters with fields
  to avoid empty points-to sets.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit enhances `create_variable_info_for_1` in `gimple-ssa-pta-constraints.cc`
  to correctly handle restrict-qualified parameters with fields. When recursion is
  detected for the same structure type and a fake pointed-to variable is not created,
  a `NONLOCAL` constraint is now added. This prevents the points-to set of the restrict-qualified
  variable/field from being empty. Additionally, it rectifies a latent issue where
  pointed-to types containing placeholders would never acquire constraints. This is
  crucial for PTA accuracy, especially in complex C++ code with `restrict` qualifiers
  and ne…
primer_glossary:
- term: Points-To Analysis (PTA)
  definition: A static analysis technique used by compilers to determine, for each
    pointer in a program, the set of memory locations that the pointer might possibly
    refer to.
- term: SSA
  definition: Static Single Assignment. An intermediate representation where every
    variable is assigned exactly once, simplifying many dataflow analyses and optimizations.
- term: restrict
  definition: A C99 keyword that provides a promise to the compiler that a pointer
    is the sole initial means of accessing a particular object. This can enable more
    aggressive optimizations.
- term: NONLOCAL
  definition: A concept in Points-To Analysis representing memory locations that are
    not necessarily constrained within the current scope, often associated with global
    or external variables.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b51998e2208b36fef6a1f68a18fdd6e562f910a4
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

This change addresses an issue in Points-To Analysis (PTA) concerning restrict-qualified parameters that have fields. When a fake pointed-to variable is not generated for such parameters, a constraint from `NONLOCAL` is now added. This ensures that the points-to set for these restrict-qualified variables or fields is not empty, which was a latent issue. It also fixes a related problem where pointed-to types with placeholders never received any constraints, improving the accuracy and robustness of PTA.
