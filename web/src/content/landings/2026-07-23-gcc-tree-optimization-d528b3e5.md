---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- vectorization
- optimization
- SLP
commit_hash: d528b3e5314fde594080406c95ac39c77881c770
source_type: github
author: Richard Biener
headline: Enhance SLP tree construction for better BB vectorization
tldr: Improved SLP tree construction allows for multiple isomorphic groups and distinguishes
  fatal failures from unvectorizable statements.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `vect_build_slp_tree_1` function now computes a `match_elt_t[]`
  instead of a simple `bool[]` for `matches[]`. This new type distinguishes between
  a lane not matching any other lane (`-1`), a lane not being vectorizable (`-2`),
  and a successful match (`0` or higher). This allows the SLP vectorizer to find multiple
  isomorphic groups and to better handle cases where specific lanes contain statements
  that cannot be vectorized, improving BB vectorization by enabling more effective
  operand swapping and group splitting.
primer_glossary:
- term: SLP (Superword-Level Parallelism)
  definition: A compiler optimization technique that identifies sequences of identical
    scalar instructions operating on different data elements and transforms them into
    a single vector instruction that operates on multiple data elements simultaneously.
    It's often used for loop-invariant code.
- term: isomorphic group
  definition: A set of instructions that have the same structure and can be executed
    as a single vector instruction. The SLP vectorizer looks for these groups to perform
    vectorization.
- term: BB unrolling
  definition: Basic Block (BB) unrolling is a transformation where a basic block is
    duplicated one or more times to enable further optimizations, such as loop vectorization.
    In this context, it refers to unrolling a BB to find vectorizable patterns.
- term: operand swapping
  definition: Rearranging the order of operands in an instruction. In the context
    of the SLP vectorizer, this can be used to move unvectorizable statements to a
    specific lane, making the rest of the group vectorizable.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d528b3e5314fde594080406c95ac39c77881c770
date: '2026-07-23'
is_stub: false
stub_reason: ''
---

This commit refactors `vect_build_slp_tree_1` in GCC's SLP (Superword-Level Parallelism) vectorizer to compute multiple sets of matching instructions. It changes the `matches[]` representation to distinguish between unvectorizable statements and fatal failures, and to retain knowledge about isomorphic tails even when BB unrolling fails. This allows for more robust BB vectorization by enabling operand swapping to isolate unvectorizable code.
