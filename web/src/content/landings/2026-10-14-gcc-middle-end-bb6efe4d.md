---
project: gcc
subsystem: gcc/middle-end
patch_id: null
tags:
- optimization
- aarch64
- vectorization
- bugfix
commit_hash: bb6efe4d690515e49c5da9167d9ca4836d1ab546
source_type: github
author: Igor Shevlyakov
headline: Fixes for merging VEC_PERM_EXPR with differing vector lengths
tldr: A bug causing miscompilation or ICEs when merging vector permutations with different
  element counts, particularly affecting SVE intrinsics on aarch64, has been…
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Fixes the `match.pd` patterns and `forwprop`'s identity check for `VEC_PERM_EXPR`
  merges when the permute or its inputs have differing element counts. Since GCC 14,
  `VEC_PERM_EXPR` can have inputs with different widths than its output. This leads
  to ICEs or miscompilation on targets like AArch64 with SVE intrinsics (e.g., `svld1rq`
  followed by `svrev`) when `match.pd` attempts to merge these operations, assuming
  uniform widths. The fix ensures selectors are built with the correct element counts,
  aligning with the input types and resulting vector lengths, resolving issues in
  both `<a, b>` into…
primer_glossary:
- term: VEC_PERM_EXPR
  definition: An expression in GCC's intermediate representation (GIMPLE) representing
    a vector permutation operation. It rearranges elements within vectors based on
    a selector.
- term: GIMPLE
  definition: GCC's Internal Representation (IR) used in the middle-end of the compiler.
    It's a three-address code form designed for optimization.
- term: ICE
  definition: Internal Compiler Error. An unrecoverable error within the compiler
    itself, typically indicating a bug in the compiler's logic.
- term: SVE
  definition: Scalable Vector Extension. An ARM architecture extension that provides
    vector processing capabilities with a vector length that can vary at runtime.
- term: aarch64
  definition: The 64-bit ARM architecture. Compilers often have specific backends
    to generate optimal code for this architecture.
- term: intrinsics
  definition: Special functions or instructions that provide direct access to hardware
    capabilities, often for performance-critical operations like vector processing.
- term: forwprop
  definition: Forward propagation, a compiler optimization technique where values
    or expressions are substituted earlier in the code to enable further optimizations.
- term: match.pd
  definition: A file containing patterns used by GCC's backend to match intermediate
    representation code to target-specific instructions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bb6efe4d690515e49c5da9167d9ca4836d1ab546
date: '2026-10-14'
is_stub: false
stub_reason: ''
---

This commit addresses a bug in GCC's middle-end where merging `VEC_PERM_EXPR` operations with inputs of different element counts led to incorrect GIMPLE, miscompilation, or Internal Compiler Errors (ICEs). The issue, present since GCC 14, particularly affected AArch64 SVE intrinsics when combining permutation operations. The fix ensures that each generated selector correctly uses the element count of its respective inputs, preventing invalid GIMPLE and silent code corruption.
