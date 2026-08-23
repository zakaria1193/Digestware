---
project: gcc
subsystem: match/forwprop
patch_id: null
tags:
- optimization
- compiler
commit_hash: dc16f9ae5101be400b63d2bea5cbdab3fe4becfe
source_type: github
author: Andrea Pinski
headline: 'match/forwprop: Consolidate `cond_carry_add` patterns for simplification.'
tldr: 'match/forwprop: Merges two conditional carry add patterns into one, reducing
  code and improving efficiency.'
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The `match.pd` and `tree-ssa-forwprop.cc` files previously handled
  conditional carry add operations using two distinct patterns/functions: `cond_carry_add_neg`
  and potentially another related one. This commit unifies them into a single `cond_carry_add`
  pattern. The `forwprop` pass itself is agnostic to which edge of the conditional
  (true or false) the addition occurs on. Merging these patterns reduces redundant
  code and ensures the `forwprop` pass processes the combined pattern only once, leading
  to minor performance and memory benefits.'
primer_glossary:
- term: match/forwprop
  definition: Indicates changes affecting both the pattern matching system and the
    forward propagation optimization pass in GCC.
- term: cond_carry_add
  definition: A pattern or operation representing an addition that includes a carry-out,
    conditional on the result of a preceding operation.
- term: tree traversal
  definition: The process of visiting each node in a tree data structure, often used
    by compilers to analyze or transform intermediate representations like GIMPLE
    or AST.
- term: GIMPLE
  definition: GCC's internal three-address code representation. It's an intermediate
    language used between parsing and machine code generation, optimized for analysis
    and transformation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dc16f9ae5101be400b63d2bea5cbdab3fe4becfe
date: '2026-08-22'
is_stub: false
stub_reason: ''
---

This commit simplifies the handling of conditional carry additions by merging two existing match patterns (`cond_carry_add_neg` and its counterpart) into a single pattern named `cond_carry_add`. Previously, separate patterns handled cases where the addition was on the true or false edge of a condition. The forward propagation code did not distinguish between these edges, making the consolidation logical. This change reduces compile time and memory usage by avoiding redundant traversals and tree creations.
