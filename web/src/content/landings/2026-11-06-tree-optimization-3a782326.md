---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- gcc
- optimization
- complex numbers
- lattice analysis
commit_hash: 3a782326a3927032b5fafcebbb7fcd2f9842ee33
source_type: github
author: Richard Biener
headline: Fix complex number propagation to handle abnormal definitions correctly
tldr: Correctly propagates lattice values for complex numbers, including handling
  abnormal definitions.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch addresses PR tree-optimization/128464 by correcting the
  handling of abnormal definitions within the `complex_propagate` pass. Previously,
  abnormal definitions were ignored during the analysis phase, meaning their lattice
  values were not propagated. The fix modifies `complex_propagate::visit_stmt` and
  `complex_propagate::visit_phi` to set the lattice value of abnormal definitions
  to `VARYING`, ensuring that the analysis correctly accounts for potential variations
  in complex number values.
primer_glossary:
- term: Complex number propagation
  definition: A compiler optimization technique that tracks the possible values of
    complex numbers throughout the program to enable further optimizations.
- term: lattice value
  definition: A value within a lattice data structure used in compiler analysis to
    represent the possible states or properties of a program element (e.g., a variable's
    value).
- term: VARYING
  definition: A lattice value indicating that a variable can take on multiple possible
    values, making its exact state uncertain for optimization purposes.
- term: abnormal definition
  definition: In the context of compiler analysis, a definition that cannot be precisely
    determined or tracked, possibly due to complex control flow or external influences.
- term: visit_stmt
  definition: A method within a compiler's analysis pass that is called to process
    a specific statement in the intermediate representation.
- term: visit_phi
  definition: A method within a compiler's analysis pass that is called to process
    a PHI node, which represents control flow merging in SSA form.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3a782326a3927032b5fafcebbb7fcd2f9842ee33
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This commit fixes an issue in GCC's complex number optimization pass where abnormal definitions were ignored during analysis, leading to incorrect lattice value propagation. The fix ensures that abnormal definitions are properly handled by setting their lattice value to `VARYING`. This correction improves the accuracy of complex number propagation, allowing for more effective optimizations related to complex types.
