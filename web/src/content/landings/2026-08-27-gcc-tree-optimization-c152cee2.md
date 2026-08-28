---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- gcc
- range analysis
commit_hash: c152cee29654b3008f20e2247251a980b40114e9
source_type: github
author: Andrew MacLeod
headline: Handle differing signs in MOD range operations.
tldr: Range analysis now correctly handles MOD operations with differing signs.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `operator_trunc_mod::wi_fold` function in `range-op.cc` now correctly
  handles modulo operations where the operands might have different signs. This is
  achieved by introducing a new helper function, `operator_trunc_mod::same_quotient`,
  which likely determines if the quotient of two numbers is the same regardless of
  their signs. This improves the accuracy of range analysis for modulo operations.
primer_glossary:
- term: range analysis
  definition: An optimization technique that determines the possible range of values
    a variable can take during program execution. This information is used to eliminate
    redundant checks or simplify computations.
- term: MOD
  definition: The modulo operator, which returns the remainder of a division operation.
- term: WI-fold
  definition: A function likely related to 'Widening Integer' folding, a compiler
    optimization technique that simplifies expressions involving integer operations
    by propagating range information.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c152cee29654b3008f20e2247251a980b40114e9
date: '2026-08-27'
is_stub: false
stub_reason: ''
---

The range analysis optimization pass has been improved to correctly handle modulo operations involving operands with different signs. A new helper function, `same_quotient`, was introduced to manage this, and it's now used within the `wi_fold` function.
