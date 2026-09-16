---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- optimization
- _BitInt
- bugfix
commit_hash: faf5c056ca1826cffb5673fa3b445eb61a6bb7eb
source_type: github
author: Richard Biener
headline: Vectorization rejects bit-precision integer comparisons
tldr: Vectorizer now correctly rejects comparisons of _BitInt types, requiring bitfield
  lowering.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `tree-vect-stmts.cc` function `vectorizable_comparison_1` previously
  allowed vectorization of comparisons on types like `_BitInt(N)` where N is not a
  standard machine mode. This commit adds a check to reject such types, forcing them
  to be handled by bitfield lowering or specific pattern matching, aligning with the
  requirements of PR tree-optimization/127390.
primer_glossary:
- term: vectorization
  definition: An optimization technique that allows a single instruction to operate
    on multiple data elements simultaneously, significantly improving performance
    for data-parallel operations.
- term: _BitInt
  definition: A C++ integer type that allows arbitrary bit widths, introduced to support
    specific hardware or algorithms that require non-standard integer sizes.
- term: ifcvt
  definition: Instruction-level if-conversion, a technique used by compilers to replace
    conditional branches with predicated instructions, often enabling better instruction-level
    parallelism.
- term: pattern recognition
  definition: A compiler technique where sequences of intermediate representation
    (IR) or instructions are matched against predefined patterns to identify opportunities
    for optimization or code generation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/faf5c056ca1826cffb5673fa3b445eb61a6bb7eb
date: '2026-09-15'
is_stub: false
stub_reason: ''
---

The GCC vectorizer previously failed to reject attempts to vectorize comparisons involving non-mode precision integer types, such as _BitInt. This commit modifies `vectorizable_comparison_1` to reject such comparisons, ensuring they are handled by bitfield lowering in `ifcvt` or through pattern recognition, addressing PR tree-optimization/127390.
