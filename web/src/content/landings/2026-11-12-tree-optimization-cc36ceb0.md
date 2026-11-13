---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- CSE
- complex numbers
- floating-point
- GCC
commit_hash: cc36ceb085de6111d3e0f41290f872363d208d21
source_type: github
author: Richard Biener
headline: 'tree-optimization: Avoid CSE of negated complex division/multiplication'
tldr: Prevents incorrect Common Subexpression Elimination for negated complex floating-point
  operations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `visit_nary_op` function in `tree-ssa-sccvn.cc` previously performed
  a Common Subexpression Elimination (CSE) that transformed expressions like `a/b`
  into `-((-a)/b)`. This optimization is invalid for complex floating-point types
  due to potential issues with signed zeros and the behavior of negation with complex
  numbers. This change modifies the CSE logic to prevent this transformation for complex
  float types, addressing PR128628.
primer_glossary:
- term: Common Subexpression Elimination (CSE)
  definition: A compiler optimization that identifies and eliminates redundant computations
    of the same expression, replacing subsequent occurrences with the result of the
    first computation.
- term: complex floating-point
  definition: A data type representing complex numbers where both the real and imaginary
    parts are floating-point numbers.
- term: signed zero
  definition: A floating-point zero value that carries information about its sign
    (positive or negative), which can affect comparison and arithmetic operations
    in certain contexts.
- term: tree-ssa-sccvn.cc
  definition: A source file within GCC's tree- SSA (Static Single Assignment) optimization
    infrastructure, specifically dealing with value numbering and CSE.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cc36ceb085de6111d3e0f41290f872363d208d21
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This commit corrects an issue where the compiler incorrectly performed Common Subexpression Elimination (CSE) on negated complex floating-point divisions and multiplications. The optimization `a/b -> -((-a)/b)` is invalid for complex floating-point types, especially when signed zeros are involved. The compiler now avoids this specific CSE transformation for complex floats, ensuring correctness.
