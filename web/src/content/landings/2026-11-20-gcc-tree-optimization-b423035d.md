---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- gcc
- bugfix
commit_hash: b423035d75f742a7377185a195231a62f1e36e92
source_type: github
author: Richard Biener
headline: Fix overflow in bytes to bits conversion for large offsets
tldr: GCC's alias analysis prevents overflow when converting large byte offsets to
  bits.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-alias.cc`, the `ao_ref_init_from_ptr_and_range` function's
  calculation of bit offsets from byte offsets, used in alias set analysis, was susceptible
  to overflow. Specifically, when the input byte offset was large, multiplying by
  8 could exceed the capacity of `poly_int64`. This commit introduces a check to ensure
  the byte offset is within a range that, when multiplied by 8, will not overflow
  `poly_int64` before the multiplication occurs.
primer_glossary:
- term: alias analysis
  definition: A compiler analysis that determines which memory accesses might refer
    to the same memory location. This is crucial for optimizations that involve reordering
    or eliminating memory operations.
- term: tree-ssa
  definition: GCC's internal representation for performing optimizations. SSA stands
    for Static Single Assignment, a form where each variable is assigned a value only
    once.
- term: poly_int64
  definition: A GCC internal integer type that can represent values larger than a
    standard 64-bit integer, often used for symbolic constants or intermediate calculations
    in optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b423035d75f742a7377185a195231a62f1e36e92
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

A bug in GCC's alias analysis (PR90241) could lead to incorrect code generation when calculating large offsets in bits from byte offsets. The `ao_ref_init_from_ptr_and_range` function could overflow when converting a large byte offset by multiplying by 8. This change adds a missing range check before the multiplication to ensure the resulting bit offset fits within a `poly_int64`.
