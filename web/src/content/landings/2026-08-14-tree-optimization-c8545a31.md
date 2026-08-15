---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- SLP
- tree-optimization
commit_hash: c8545a3143330983e51d913f0a01187258b14510
source_type: github
author: Richard Biener
headline: 'SLP optimization: Fix basic block constraint for trapping statements'
tldr: Improves SIMD Local Search (SLP) optimization by correctly handling trapping
  statements within basic blocks.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The SLP vectorizer in `tree-vect-slp.cc` must ensure that all statements
  forming a potential vector are in the same basic block (BB) to guarantee correct
  execution and avoid issues with control flow or trapping instructions. This patch
  corrects `vect_build_slp_tree_1` by introducing logic to track the common BB and
  a flag for any trapping statement encountered within a candidate set. After scanning
  all statements for a potential vector, it verifies the common BB constraint. This
  resolves PR tree-optimization/126865, where the absence of this check allowed SLP
  to create vectors from statements…
primer_glossary:
- term: SLP (SIMD Local Search)
  definition: An optimization technique in GCC that identifies sequences of identical
    operations in the code that can be combined into a single instruction operating
    on multiple data elements (SIMD - Single Instruction, Multiple Data). It operates
    on the tree-IR.
- term: trapping statement
  definition: An operation or instruction that, if it occurs, causes a program exception
    or interrupt (a trap). Examples include division by zero, null pointer dereference,
    or integer overflow in some contexts.
- term: basic block (BB)
  definition: A sequence of consecutive instructions in a program for which flow of
    control enters at the beginning and leaves at the end without halt or possibility
    of branching except at the end. Basic blocks are fundamental units for compiler
    analysis and optimization.
- term: tree-optimization
  definition: The phase in GCC where optimizations are applied to the intermediate
    representation, known as the GCC Tree. This pass focuses on vectorization using
    SLP.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c8545a3143330983e51d913f0a01187258b14510
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in the SLP (SIMD Local Search) optimization pass where the compiler failed to ensure that all statements within a node belonged to the same basic block when a trapping statement was present. The fix modifies `vect_build_slp_tree_1` to track the common basic block and detect trapping statements. It then verifies that all statements in a potential SLP vectorization candidate reside in the same basic block after all statements have been processed, preventing incorrect vectorization that could lead to runtime errors.
