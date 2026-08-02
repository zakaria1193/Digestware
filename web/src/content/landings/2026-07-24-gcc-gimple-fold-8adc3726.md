---
project: gcc
subsystem: gcc/gimple-fold
patch_id: null
tags:
- optimization
- gcc
- gimple
commit_hash: 8adc3726fe0c256f4ad36ba1c7d978261118e2f5
source_type: github
author: Andrea Pinski
headline: 'gimple-fold: Fix undefined overflow handling in follow_outer_ssa_edges'
tldr: Fixes incorrect code generation for undefined overflow cases in gimple-fold's
  SSA edge following logic.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This commit modifies `gimple-fold.cc` to fix `follow_outer_ssa_edges`
  in handling SSA name ranges across conditional branches, specifically when undefined
  overflow is involved. Previously, the function returned early for types with undefined
  overflow *before* saving the current SSA name''s global range, leading to incorrect
  range propagation when `ifcombine` later used the stale global range. The fix swaps
  the order: save global range, then return early if necessary.'
primer_glossary:
- term: gimple-fold
  definition: A GCC optimization pass that performs various folding operations on
    GIMPLE (GCC's internal representation) code to simplify expressions and improve
    efficiency.
- term: SSA (Static Single Assignment)
  definition: An intermediate representation property where every variable is assigned
    exactly once. This simplifies many compiler analyses and optimizations.
- term: follow_outer_ssa_edges
  definition: A function within GCC that traces the boundaries of SSA values across
    conditional control flow edges to determine their valid ranges.
- term: undefined overflow
  definition: An arithmetic operation that results in a value outside the representable
    range for its data type, where the behavior is not defined by the language standard
    (e.g., signed integer overflow in C/C++).
- term: GIMPLE
  definition: GCC's Generic Intermediate Representation. It's a three-address, statement-based
    representation used after initial parsing and before optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8adc3726fe0c256f4ad36ba1c7d978261118e2f5
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in GCC's `gimple-fold` pass where the `follow_outer_ssa_edges` function could generate incorrect code when dealing with undefined integer overflows. The problem arose because the function would prematurely return without saving the global range of an SSA name, leading to incorrect range analysis and subsequent optimizations, as demonstrated in PR126313. The fix reorders operations to save the global range before the early return.
