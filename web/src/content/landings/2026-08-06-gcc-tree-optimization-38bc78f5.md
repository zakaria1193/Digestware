---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- cleanup
- ssa
commit_hash: 38bc78f593488bb1a28ca6b20e538f378113392d
source_type: github
author: Kael Andrew Alonzo Franco
headline: Remove dead code in tree-ssa-strlen.cc
tldr: Cleans up dead code related to conditional expressions in strlen optimization.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Removes dead code in `gcc/tree-ssa-strlen.cc` related to the `use_in_zero_equality`
  function. The condition `COND_EXPR` is guaranteed to be either an `SSA_NAME` or
  a constant in this pass, rendering the prior check for `SSA_NAME` redundant. This
  cleanup simplifies the SSA-based strlen optimization.
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC where the compiler operates on an intermediate representation
    (the 'tree' form) to perform high-level optimizations before generating code.
- term: tree-ssa-strlen.cc
  definition: A GCC source file likely containing optimizations for the strlen function,
    utilizing the Static Single Assignment (SSA) form of the intermediate representation.
- term: COND_EXPR
  definition: An intermediate representation node in GCC representing a conditional
    expression (like C's ternary operator ?:).
- term: SSA_NAME
  definition: In Static Single Assignment (SSA) form, a variable that is assigned
    exactly once. This simplifies many program analysis and optimization tasks.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/38bc78f593488bb1a28ca6b20e538f378113392d
date: '2026-08-06'
is_stub: true
stub_reason: low_score
---

This commit removes a section of dead code from `tree-ssa-strlen.cc`. The removed code was associated with handling `COND_EXPR` which, in this context, is always either an `SSA_NAME` or a constant, making the original conditional logic unnecessary. This simplifies the optimization pass.
