---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- compiler
commit_hash: 8d32122f1a692e841ee3c2d27f3200a712f9f145
source_type: github
author: Richard Biener
headline: Zero-pad vectors in constant creation to fix ICE.
tldr: Fixes an ICE related to vector constant creation by ensuring proper zero-padding.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch corrects an issue in `tree-vect-slp.cc` where `vect_create_constant_vectors`
  failed to zero-pad elements when vector types were no longer restricted for externs/constants.
  This was causing an ICE, particularly in scenarios involving multiple output vectors
  derived from partial input vectors. It also adjusts `vect_create_vectorized_demotion_stmts`
  in `tree-vect-stmts.cc` to handle a variable number of output vectors.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. An unrecoverable error that occurs within the
    compiler itself, usually due to a bug in the compiler's logic.
- term: vectorization
  definition: An optimization technique that enables a single instruction to operate
    on multiple data elements simultaneously, often improving performance for array
    processing and similar tasks.
- term: SLP
  definition: Superword Level Parallelism. A type of instruction-level parallelism
    where multiple independent data elements within a vector are processed in parallel
    by a single instruction.
- term: zero-pad
  definition: To fill the unused elements of a data structure, such as a vector, with
    zero values. This is important for maintaining correct behavior and avoiding undefined
    values.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8d32122f1a692e841ee3c2d27f3200a712f9f145
date: '2026-08-25'
is_stub: false
stub_reason: ''
---

This commit resolves an ICE (Internal Compiler Error) that occurred when creating partly populated vectors. The issue stemmed from a failure to zero-pad excess elements in `vect_create_constant_vectors`. This change ensures that all elements in the vector are properly initialized, preventing the ICE and addressing related bugs in vectorizable conversions and demotions.
