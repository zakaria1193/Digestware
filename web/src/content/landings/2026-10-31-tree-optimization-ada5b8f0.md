---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- bugfix
commit_hash: ada5b8f08739b26bf76558c9d5157cbbdd16c205
source_type: github
author: Richard Biener
headline: Tree SSA SCCVN pass now correctly handles padding for tail pruning.
tldr: Fixes a bug in tree-ssa-sccvn.cc where tail pruning did not account for head
  padding, potentially leading to incorrect size calculations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The Scalar and Value Numbering (SCCVN) optimization pass, specifically
  within `tree-ssa-sccvn.cc`, incorrectly calculates the new size of a data structure
  after pruning its tail. The issue arises because `vn_walk_cb_data::push_partial_def`
  fails to account for head padding when the tail is pruned, leading to incorrect
  sizing for non-constant definitions. This patch amends the logic to include head
  padding, fixing PR128322.
primer_glossary:
- term: tree-ssa-sccvn.cc
  definition: A source file within GCC's tree-ssa optimization pipeline that implements
    Scalar and Value Numbering (SCCVN) optimizations. It works on the Static Single
    Assignment (SSA) form of the intermediate representation.
- term: tail pruning
  definition: An optimization technique where the end portion of a data structure
    or computation is removed if it is not needed, potentially reducing memory usage
    or computation.
- term: head padding
  definition: Unused space at the beginning of a data structure or memory allocation,
    often used for alignment or other purposes. In this context, it refers to padding
    before the actual data begins.
- term: Scalar and Value Numbering (SCCVN)
  definition: An optimization technique used in compilers to identify and eliminate
    redundant computations by assigning unique numbers to scalar values and detecting
    when different expressions compute the same value.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ada5b8f08739b26bf76558c9d5157cbbdd16c205
date: '2026-10-31'
is_stub: false
stub_reason: ''
---

A bug in the tree-ssa-sccvn pass caused incorrect size calculations after pruning the tail of a data structure. This commit corrects the `push_partial_def` function to properly consider head padding when determining the new size, ensuring more accurate optimization. A new test case, pr128322.c, has been added to verify the fix.
