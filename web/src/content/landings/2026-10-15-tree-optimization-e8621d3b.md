---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- vectorization
commit_hash: e8621d3bdaf022078b98614a003ea2f5bf95e7b4
source_type: github
author: Kyrylo Tkachov
headline: Add operand type checks to signed saturation add patterns
tldr: Fixes incorrect saturation results by ensuring operand types match the expected
  result type.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Several forms of `signed_integer_sat_add` in `match-sat-alu.pd` were
  found to be incorrect. The `.ADD_OVERFLOW` form lacked a `types_match` check, and
  other forms allowed operands that, after implicit or explicit conversion, did not
  match the result type. This commit adds checks to ensure that the primary operand
  `X` matches the result type and that the immediate operand `IMM` either matches
  or is a constant that fits the result type. This resolves incorrect saturation behavior,
  especially when operations are widened or narrowed.
primer_glossary:
- term: .SAT_ADD
  definition: A pattern in GCC's intermediate representation (PD - Pattern Description)
    representing a signed saturating addition operation.
- term: .ADD_OVERFLOW
  definition: A pattern in GCC's intermediate representation that computes an addition
    and an overflow flag simultaneously. It's often used as a building block for saturation
    arithmetic.
- term: vectorizer
  definition: A compiler component that transforms code to use SIMD (Single Instruction,
    Multiple Data) instructions, allowing a single operation to be performed on multiple
    data elements simultaneously for performance gains.
- term: widening_mul
  definition: A compiler pass or optimization stage that handles arithmetic operations
    involving operands of different sizes, potentially widening them to a larger type
    before performing the operation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e8621d3bdaf022078b98614a003ea2f5bf95e7b4
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

This commit addresses issues in `match-sat-alu.pd` where signed saturation add operations (`.SAT_ADD`) did not properly check operand types, leading to incorrect results, particularly when used by the vectorizer. The patterns now enforce that the operands' types are consistent with the result type of the saturation operation, preventing cases where intermediate conversions cause unexpected behavior, such as saturation to the wrong value range.
