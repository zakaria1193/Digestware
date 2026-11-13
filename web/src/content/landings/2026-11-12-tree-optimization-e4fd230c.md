---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-ssa
- bugfix
commit_hash: e4fd230c4f29761497652f49b1285916ff55f554
source_type: github
author: Richard Biener
headline: Fix incorrect handling of complex number parts in addressability checks
tldr: Fixes bug where complex number components were not checked, leading to incorrect
  memory access analysis.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `may_be_nonaddressable_p` function, used within the loop invariant
  code motion (IVOPTS) pass, determines if an expression can be safely used as a memory
  address. Previously, it failed to recurse into `REALPART_EXPR` and `IMAGPART_EXPR`
  nodes, which represent the real and imaginary parts of complex numbers. This commit
  adds recursion for these types, ensuring that the addressability of complex number
  components is correctly analyzed, preventing misoptimizations.
primer_glossary:
- term: IVOPTS
  definition: Loop Invariant Code Motion and Optimization. A compiler pass that identifies
    computations within loops that do not change with each iteration and moves them
    outside the loop to improve performance.
- term: reverse-storage-order accesses
  definition: Memory accesses where data is read or written in the opposite order
    of how it is stored in memory. This can occur in certain loop transformations
    or when dealing with complex data structures.
- term: REALPART_EXPR / IMAGPART_EXPR
  definition: Internal compiler representations for the real and imaginary parts of
    complex numbers, respectively. These are nodes in GCC's abstract syntax tree (or
    Gimple/Tree SSA) used during optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e4fd230c4f29761497652f49b1285916ff55f554
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

The `may_be_nonaddressable_p` function in `tree-ssa-loop-ivopts.cc` has been updated to correctly recurse for `REALPART_EXPR` and `IMAGPART_EXPR`. This resolves an issue where complex number components were not handled, causing incorrect rewrites of reverse-storage-order accesses by the IVOPTS pass.
