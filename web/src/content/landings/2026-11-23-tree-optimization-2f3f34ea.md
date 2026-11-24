---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- intermediate representation
commit_hash: 2f3f34ea0945a3cd4eba05ec6c5d3c353e1fbe78
source_type: github
author: Richard Biener
headline: tree-optimization/128943 - Avoid leaking conditional value-numbering equivalences.
tldr: Fixes PRE to avoid hoisting operations with undefined overflow, preventing incorrect
  signed overflow by not leaking conditional equivalences.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-sccvn.cc`, `visit_nary_op` previously inserted equivalences
  into the global nary table even if they relied on a narrow operation with undefined
  overflow. This made the equivalence available in blocks not dominated by the narrow
  operation's guard. PRE could then hoist the operation, causing undefined signed
  overflow. The fix restricts inserting equivalences into the nary table when they
  are derived from narrow operations or negated operands with undefined overflow,
  unless the type guarantees no overflow. This prevents incorrect hoisting and resolves
  PR128943.
primer_glossary:
- term: tree-optimization
  definition: GCC's intermediate representation (Tree) optimization passes, which
    operate on a high-level representation of the code.
- term: value-numbering (VN)
  definition: An optimization technique that identifies and merges equivalent expressions
    to avoid redundant computations.
- term: Partial Redundancy Elimination (PRE)
  definition: An optimization pass that eliminates redundant computations by hoisting
    them to dominance points.
- term: undefined signed overflow
  definition: An arithmetic operation where the result exceeds the maximum or minimum
    value representable by a signed integer type, leading to unpredictable behavior.
- term: dominance
  definition: In control flow graphs, a block A dominates block B if every path from
    the entry node to B must go through A.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2f3f34ea0945a3cd4eba05ec6c5d3c353e1fbe78
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in GCC's value-numbering (VN) pass where equivalences derived from narrow operations with potential overflow were incorrectly made available globally. This could lead the Partial Redundancy Elimination (PRE) pass to hoist such operations across control flow paths where they were not valid, resulting in undefined signed overflow. The fix prevents these conditional equivalences from being recorded globally, ensuring they are only used within their valid execution contexts. This resolves PR tree-optimization/128943.
