---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler internals
commit_hash: bb64fe84ede31ebeb1ef1c57f5eda4c3827e9c53
source_type: github
author: Richard Biener
headline: Refactor match-op to nary-op initialization for VN lookup.
tldr: Simplifies initialization of VN lookup structures by factoring out common logic
  for match-op.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-sccvn.cc`, this commit introduces helper functions `match_op_generic_constructor_p`,
  `vn_nary_length_from_match_op`, and `init_vn_nary_op_from_match_op`. These helpers
  streamline the process of creating `vn_nary_op` structures from `gimple_match_op`
  inputs, specifically within the context of SCCVN (Strongly Connected Components
  based Value Numbering). The `vn_lookup_simplify_result` function is updated to use
  these new helpers, improving the initialization logic for lookup nary ops. This
  addresses PR tree-optimization/128651.
primer_glossary:
- term: VN lookup
  definition: Value Numbering lookup is a compiler optimization technique used to
    identify and eliminate redundant computations by assigning a unique number (value
    number) to each distinct expression. A VN lookup helps in finding existing value
    numbers for newly encountered expressions.
- term: n-ary operation
  definition: An n-ary operation is a computational operation that takes 'n' operands.
    In the context of compilers, it often refers to operations with multiple arguments
    or components, such as function calls or complex expressions.
- term: gimple_match_op
  definition: A GIMPLE construct representing a match operation. GIMPLE is an intermediate
    representation used by GCC. `gimple_match_op` likely pertains to pattern matching
    within the GIMPLE representation for optimization purposes.
- term: tree-optimization
  definition: A phase in the GCC compiler that operates on the 'tree' intermediate
    representation. It performs various optimizations like constant folding, dead
    code elimination, and loop optimizations before code generation.
- term: SCCVN
  definition: Strongly Connected Components based Value Numbering. A value numbering
    technique that leverages graph theory, specifically strongly connected components,
    to analyze and optimize code, often used for detecting and eliminating redundant
    computations within loops or mutually recursive code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bb64fe84ede31ebeb1ef1c57f5eda4c3827e9c53
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This change refactors the initialization of VN lookup structures in the tree-optimization subsystem. It factors out helper functions for initializing `vn_nary_op` from `gimple_match_op` structures. This simplifies the `vn_lookup_simplify_result` function by using these new helpers, making the code cleaner and easier to maintain. The change is motivated by PR tree-optimization/128651.
