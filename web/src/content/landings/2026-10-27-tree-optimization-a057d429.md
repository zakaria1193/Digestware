---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- tree-optimization
commit_hash: a057d429ba49a2ad991a3e5931e5508c3035e9af
source_type: github
author: Richard Biener
headline: tree-optimization/128187 - Vector reductions with single cycle
tldr: Fixes vector reduction code generation for operations with non-standard operand
  counts, like FMA.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The `tree-vect-loop.cc` function `vect_transform_reduction` is updated
  to correctly handle masked internal functions with varying operand counts, particularly
  for vector reductions forced to a single cycle. Previously, it assumed exactly two
  operands, causing incorrect code generation for operations like FMA (which has three
  operands: destination, operand1, operand2). This patch ensures that both two- and
  three-argument masked functions are handled properly, resolving PR tree-optimization/128187.'
primer_glossary:
- term: Vectorization
  definition: An optimization technique that transforms code to operate on multiple
    data elements simultaneously using special vector instructions.
- term: Reduction
  definition: A computation that combines elements of a sequence into a single value,
    such as summing all elements in an array.
- term: Single cycle
  definition: An optimization goal to complete a complex operation within a single
    clock cycle, often applicable to vector instructions.
- term: Fused Multiply-Add (FMA)
  definition: A single instruction that performs both a multiplication and an addition,
    often used in floating-point computations.
- term: Masked function
  definition: A function where operations are conditionally applied based on a mask,
    allowing selective updates to vector elements.
- term: tree-vect-loop.cc
  definition: A GCC source file containing code related to the vectorization of loops.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a057d429ba49a2ad991a3e5931e5508c3035e9af
date: '2026-10-27'
is_stub: false
stub_reason: ''
---

This commit resolves an issue in GCC's vectorization of reductions that are forced into a single cycle, specifically addressing code generation for operations with more or fewer than two operands, such as Fused Multiply-Add (FMA). The change updates the `vect_transform_reduction` function to correctly handle both two- and three-argument masked internal functions, ensuring accurate code generation for these cases.
