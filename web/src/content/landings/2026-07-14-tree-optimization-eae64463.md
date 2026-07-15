---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- memset
- performance
- bugfix
commit_hash: eae644638908427b11f8d791f718851e25bece01
source_type: github
author: Naveen
headline: 'tree-optimization: Fold length-one memset through arbitrary pointers.'
tldr: Optimizes length-one memset calls through arbitrary pointers into scalar stores.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `gimple_fold_builtin_memset` function now includes a dedicated
  folding path for length-one `memset` calls through arbitrary pointer destinations.
  It constructs a `MEM_REF` at offset zero, preserving the volatile qualifier and
  the call's result if used. This fold is deferred until after object-size analysis
  to keep the original `memset` available for diagnostics. This complements the existing
  folding for `ADDR_EXPR` destinations.
primer_glossary:
- term: tree-optimization
  definition: A phase in the GCC compilation pipeline where the code is represented
    in an intermediate form called 'tree' and optimized for efficiency.
- term: memset
  definition: A standard C library function used to fill a block of memory with a
    specified byte value.
- term: ADDR_EXPR
  definition: An expression in GCC's intermediate representation that represents the
    address of an object.
- term: Scalar store
  definition: An operation that writes a single value (like a byte, word, or dword)
    to a memory location.
- term: GIMPLE
  definition: GCC's low-level Intermediate Representation (IR) used for performing
    optimizations. It's a three-address-like code format.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/eae644638908427b11f8d791f718851e25bece01
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

The compiler can now optimize calls to `memset` with a length of one, even when the destination is an arbitrary pointer (e.g., a function parameter). Previously, such calls were not optimized into scalar stores unless the destination was a known `ADDR_EXPR`. This change allows folding these into a single byte store, preserving volatile qualification and supporting both constant and non-constant fill values, thereby improving performance and code generation efficiency.
