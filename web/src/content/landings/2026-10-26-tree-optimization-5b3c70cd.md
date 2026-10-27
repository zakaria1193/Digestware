---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- bugfix
- optimization
commit_hash: 5b3c70cdb8474a0a489ca7401a37ad18229eafda
source_type: github
author: Richard Biener
headline: Fix vectorized _BitInt loads to handle padding bits
tldr: Vectorized loads of `_BitInt` types now correctly handle padding bits, preventing
  incorrect values.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vectorizable_load` function within GCC's tree-optimization pipeline
  previously mishandled padding bits for `_BitInt` types during vectorization. This
  commit modifies the function to reject `_BitInt` loads where the requested precision
  does not exactly match the underlying mode's precision. This prevents incorrect
  data from being loaded due to the presence of unused bits in the `_BitInt` representation,
  particularly when vectorizing operations on these non-standard integer types.
primer_glossary:
- term: _BitInt
  definition: A non-standard integer type that allows specifying an arbitrary number
    of bits for its size, offering more flexibility than fixed-width types like `int`
    or `long`.
- term: vectorization
  definition: An optimization technique that allows a single instruction to operate
    on multiple data points simultaneously, often using SIMD (Single Instruction,
    Multiple Data) instructions. This can significantly speed up data-parallel computations.
- term: padding bits
  definition: Unused bits within a data type that are not part of the actual value
    being stored. These bits can exist due to alignment requirements or the nature
    of variable-width types.
- term: tree-optimization
  definition: A phase in the GCC compilation process where the code is represented
    in an intermediate form called GIMPLE (a three-address code) and subjected to
    various optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5b3c70cdb8474a0a489ca7401a37ad18229eafda
date: '2026-10-26'
is_stub: false
stub_reason: ''
---

This commit addresses an issue where vectorized loads of `_BitInt` types failed to correctly account for padding bits. The `vectorizable_load` function in `tree-vect-stmts.cc` has been updated to reject `_BitInt` loads that do not precisely match the type's precision. This ensures that padding bits do not interfere with the loaded value, fixing a bug in the vectorization of these types.
