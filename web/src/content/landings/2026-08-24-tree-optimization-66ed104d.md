---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loops
- vectorization
commit_hash: 66ed104db50c639c79e7ba2826ccd6df41cb37c1
source_type: github
author: Richard Biener
headline: Loop unswitching now hoists loop invariants
tldr: Loop unswitching optimization now also hoists loop-invariant statements, improving
  vectorization opportunities.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `tree_ssa_unswitch_loops` function in `tree-ssa-loop-unswitch.cc`
  now performs invariant motion after unswitching a loop. Previously, invariant statements
  within a loop might not have been moved out if they couldn't be if-converted. This
  change ensures that such invariants are hoisted, similar to the established behavior
  in loop interchange and unroll-and-jam, thereby improving the effectiveness of subsequent
  optimizations like vectorization.
primer_glossary:
- term: loop unswitching
  definition: 'A compiler optimization that transforms a loop with a conditional branch
    at the loop header into two separate loops: one for the case where the condition
    is initially true, and one for when it''s false. This can expose more optimization
    opportunities.'
- term: loop invariant motion
  definition: An optimization that identifies computations within a loop that produce
    the same result in every iteration and moves them outside the loop to be computed
    only once.
- term: if-conversion
  definition: An optimization technique that replaces conditional branches with conditional
    move instructions, allowing code to be executed speculatively and potentially
    improving instruction-level parallelism.
- term: vectorization
  definition: An optimization process that transforms code to operate on multiple
    data elements simultaneously using special CPU instructions (SIMD), often improving
    performance for data-parallel tasks.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/66ed104db50c639c79e7ba2826ccd6df41cb37c1
date: '2026-08-24'
is_stub: false
stub_reason: ''
---

GCC's loop unswitching optimization has been enhanced to also perform loop invariant motion. This means that statements whose values do not change within the loop are now moved out of the loop, even if they cannot be if-converted. This behavior aligns with other loop optimizations like interchange and unroll-and-jam, and prevents invariant statements from hindering vectorization.
