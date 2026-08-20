---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- bugfix
commit_hash: f678eab4f721ee3da1730e6c637b90a40aeb9d4d
source_type: github
author: Richard Biener
headline: Fix vectorization scheduling to exclude use statement from dominance check
tldr: Vectorization scheduling now correctly excludes the use statement from dominance
  checks to prevent incorrect scheduling.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The SLP (Straight-Line-Progression) vectorizer in `tree-vect-slp.cc`
  has a verification step that checks for dominance relationships between statements.
  For live lane extraction and reduction root scheduling, the `use_stmt` (the statement
  that consumes the vector being generated) was incorrectly allowed to be the same
  as the `placement_point` (where the vector definition is inserted). Since vector
  definitions (`vect_def`) are inserted *after* the `placement_point`, the `use_stmt`
  must not be dominated by it. This commit modifies `vect_bb_slp_mark_live_stmts`
  and `vect_schedule_slp` to exclude…
primer_glossary:
- term: SLP vectorization
  definition: A compiler optimization technique that identifies sequences of identical
    or similar instructions operating on different data elements and replaces them
    with a single vector instruction that operates on multiple data elements simultaneously.
- term: Live lanes
  definition: In the context of vectorization, 'live lanes' likely refers to vector
    elements that are actively being used or produced by instructions within a basic
    block.
- term: Dominance check
  definition: In control flow analysis, a check to determine if a block or statement
    in a program's execution path is guaranteed to be executed before another block
    or statement.
- term: Placement point
  definition: In the context of SLP vectorization, this likely refers to the instruction
    or location in the code where a newly generated vector instruction is to be inserted.
- term: Reduction root
  definition: In vectorization, a reduction operation (like sum, product, min, max)
    that combines multiple elements of a vector into a single scalar value. The 'root'
    may refer to the instruction that initiates or concludes this reduction.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f678eab4f721ee3da1730e6c637b90a40aeb9d4d
date: '2026-08-19'
is_stub: false
stub_reason: ''
---

This patch corrects an issue in GCC's vectorization scheduler where the `use_stmt` was incorrectly included in dominance checks for live lanes and reduction roots. The problem arises because vector definitions are inserted after the placement point, meaning the `use_stmt` should not be considered dominated by it. The fix modifies `vect_bb_slp_mark_live_stmts` and `vect_schedule_slp` to exclude the `use_stmt` from dominance checks, resolving a verification error. A new test case `bb-slp-pr126936.c` has been added to verify the fix.
