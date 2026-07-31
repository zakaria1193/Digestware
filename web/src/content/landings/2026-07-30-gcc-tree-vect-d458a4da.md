---
project: gcc
subsystem: gcc/tree-vect
patch_id: null
tags:
- debugging
- vectorization
- SLP
commit_hash: d458a4daa68cdbaa869344ec1a75360a842ef19e
source_type: github
author: Richard Biener
headline: Dump SLP subgraph entries upon costing
tldr: Added debugging output to SLP vectorization to show subgraph entries during
  cost analysis.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: vect_bb_vectorization_profitable_p in tree-vect-slp.cc now dumps SLP
  graph entries when costing. This aids in debugging and understanding the cost model
  for SLP vectorization, particularly for complex intermediate representations.
primer_glossary:
- term: SLP
  definition: Superword-Level Parallelism, a compiler optimization technique that
    finds and exploits instruction-level parallelism by grouping independent instructions
    that operate on different data elements.
- term: vectorization
  definition: The process of transforming scalar code (operating on single data elements)
    into vector code (operating on multiple data elements simultaneously using SIMD
    instructions).
- term: costing
  definition: The process by which the compiler estimates the performance impact or
    benefit of applying an optimization, such as vectorization.
- term: basic block
  definition: A sequence of consecutive instructions in a program in which control
    enters at the beginning and leaves at the end without the possibility of branching
    except at the end.
- term: tree-vect-slp.cc
  definition: A source file within GCC that handles Superword-Level Parallelism (SLP)
    based vectorization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d458a4daa68cdbaa869344ec1a75360a842ef19e
date: '2026-07-30'
is_stub: true
stub_reason: low_score
---

To aid in debugging and understanding the cost analysis for SLP (Superword-Level Parallelism) vectorization, commit d458a4daa68cdbaa869344ec1a75360a842ef19e adds diagnostic dumping of SLP graph entries. This information is output when the vectorization profitability of a basic block is being calculated, providing developers with more insight into the internal workings of the vectorizer.
