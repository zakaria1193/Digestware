---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- compiler bug
- optimization
commit_hash: 3e6ac9b8d87704323df1f12214c29725c4e5eb9d
source_type: github
author: Richard Biener
headline: Robustify reduction analysis by handling unsupported operations early
tldr: Prevents compiler crashes by performing early checks for vectorizable reduction
  operations.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vectorizable_reduction` function within `tree-vect-loop.cc` is
  responsible for determining if a reduction operation can be vectorized using the
  SLP (Shortest-Length Processing) peephole optimization. This commit adds a check
  to ensure that all operands of the GIMPLE statement correspond to children in the
  SLP tree. This robustification prevents an ICE when, for example, `.CLZ` is used
  with two operands, as the operand count mismatch previously would not be caught
  until later, by which point the GIMPLE statement's structure was already assumed
  to match the SLP tree.
primer_glossary:
- term: Vectorization
  definition: An optimization technique that allows a single instruction to operate
    on multiple data elements simultaneously. This is often achieved by leveraging
    SIMD (Single Instruction, Multiple Data) instructions.
- term: Reduction Operation
  definition: An operation that combines a sequence of values into a single result,
    such as sum, product, minimum, or maximum. In vectorization, these can often be
    parallelized.
- term: SLP (Shortest-Length Processing)
  definition: A compiler optimization technique that vectorizes sequences of identical,
    consecutive operations that have identical operands, even if they are not aligned
    in a straight vector.
- term: GIMPLE
  definition: A three-address intermediate representation used by GCC. It's designed
    to simplify many optimizations compared to RTL (Register Transfer Language).
- term: ICE (Internal Compiler Error)
  definition: An error that occurs within the compiler itself, indicating a bug in
    the compiler's internal logic or data structures. It typically results in the
    compilation process aborting.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3e6ac9b8d87704323df1f12214c29725c4e5eb9d
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

This commit improves the robustness of the vectorization reduction analysis by adding an early exit for unsupported reduction operations. The analysis previously assumed a direct correspondence between GIMPLE statement operands and SLP (Shortest-Length Processing) vectorization operands, which can break for operations like count-leading-zeros with multiple operands. By rejecting such cases upfront, the compiler avoids internal errors (ICEs) and provides better diagnostics.
