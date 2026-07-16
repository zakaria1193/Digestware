---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- integer
- UB
commit_hash: 2fcbe075ec3b32f4a523ebae68a8a32381bb46a9
source_type: github
author: Richard Biener
headline: Fix SCEV handling of INT_MIN subtraction to avoid UB
tldr: Ensures correct scalar evolution calculation for subtractions involving the
  most negative integer, preventing undefined behavior.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `scev_dfs::add_to_evolution` and `follow_ssa_edge_binary` functions
  in `tree-scalar-evolution.cc` have been refactored to remove manual `MINUS_EXPR`
  handling. The `follow_ssa_edge_expr` now handles `MINUS_EXPR` by promoting the entire
  operation to unsigned, instead of just the negated operand. This corrects a wrong
  `scev_direction` that previously occurred when handling subtractions involving `INT_MIN`
  and prevented undefined behavior that could arise from negating `INT_MIN` directly.
primer_glossary:
- term: Scalar Evolution (SCEV)
  definition: A GCC analysis pass that determines how values change across loop iterations.
    It's used to find opportunities for optimizations like loop unrolling and vectorization
    by representing values as affine expressions.
- term: INT_MIN
  definition: The smallest representable value for a signed integer type. For a 32-bit
    integer, this is typically -2,147,483,648.
- term: Undefined Behavior (UB)
  definition: Behavior that results from an erroneous program construct or incorrect
    use of a standard API. The C and C++ standards do not specify what must happen
    in such cases, and compilers are free to assume UB does not occur, potentially
    leading to unexpected results or optimizations.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned a value exactly once. This simplifies many data-flow
    analyses.
- term: tree-optimization
  definition: GCC's middle-end optimizer that operates on the compiler's internal
    Abstract Syntax Tree (AST) or GIMPLE representation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2fcbe075ec3b32f4a523ebae68a8a32381bb46a9
date: '2026-07-15'
is_stub: false
stub_reason: ''
---

This commit resolves an issue in Scalar Evolution (SCEV) analysis where subtracting the most negative value of a signed integer type could lead to undefined behavior and incorrect analysis results. Previously, only the negation of INT_MIN was guarded, but this did not correct the resulting SCEV direction when the operation was flipped from subtraction to addition. The fix now promotes the entire operation to unsigned, ensuring correct analysis even in these edge cases. New test cases verify the fix.
