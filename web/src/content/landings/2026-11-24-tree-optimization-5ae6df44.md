---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- slp
commit_hash: 5ae6df447e12cbdfca0c65fa6341e161046df6b7
source_type: github
author: Richard Biener
headline: Improve BB SLP discovery for split graphs
tldr: Block SLP discovery is delayed to improve split-point identification and optimize
  vectorization of complex code.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect_build_slp_tree_2` function in `tree-vect-slp.cc` previously
  had a premature soft-fail mechanism for SLP discovery. This commit delays that soft-fail
  until leaf nodes are reached, allowing for better discovery of vectorizable instruction
  sequences, especially in graphs that are intended to be split. It also avoids operand
  swapping on nodes that are likely to soft-fail and prevents building SLP trees from
  scalars if a soft-fail is imminent. This change aims to improve the effectiveness
  of SLP for complex control flow and data dependency scenarios, addressing issues
  like those in PR128…
primer_glossary:
- term: BB SLP
  definition: Basic Block Superword Level Parallelism. An optimization technique that
    identifies and vectorizes sequences of identical instructions within a basic block.
- term: Basic Block (BB)
  definition: A sequence of consecutive three-address statements which has only one
    entry point and one exit point.
- term: Superword Level Parallelism (SLP)
  definition: A compiler optimization technique that finds redundant instructions
    operating on independent data elements (shuffles) and replaces them with vector
    instructions.
- term: split-points
  definition: Points in the code where a larger instruction sequence or basic block
    might be divided for further processing or optimization.
- term: soft-fail
  definition: A condition where an optimization attempt is not immediately abandoned
    but is deferred or has less impact, allowing for further analysis or alternative
    strategies.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5ae6df447e12cbdfca0c65fa6341e161046df6b7
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This commit enhances the Basic Block (BB) Superword Level Parallelism (SLP) discovery mechanism to improve the identification of optimal split-points for code that will be further processed. By delaying the 'soft-fail' condition of SLP discovery until it's absolutely necessary, the compiler can find better groupings of instructions for vectorization, particularly in cases that were previously problematic. This change avoids unnecessary overhead from operand swapping and ensures that SLP is only attempted when truly beneficial.
