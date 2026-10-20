---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- correctness
- optimization
commit_hash: a793e66d706e04e0600b852cd8818bde21ae3599
source_type: github
author: Richard Biener
headline: tree-optimization/127958 - avoid building invalid BIT_FIELD_REF
tldr: Fix redundant store elimination to avoid creating invalid bitfield references.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `eliminate_dom_walker::eliminate_stmt` function in `tree-ssa-sccvn.cc`,
  used for redundant store elimination, could construct a `BIT_FIELD_REF` with an
  offset that exceeded the representable range of `poly_uint64`. This would cause
  an ICE later when `bit_field_offset` was called on this invalid reference. This
  commit adds a check to ensure the offset is valid before the `BIT_FIELD_REF` is
  used for lookup, addressing PR tree-optimization/127958.
primer_glossary:
- term: redundant store elimination
  definition: An optimization pass that removes store operations to memory locations
    if the value being stored is the same as a previous store to the same location
    and the location has not been modified in between.
- term: BIT_FIELD_REF
  definition: A GCC Intermediate Representation (IR) node that accesses a bitfield
    within a larger value. It specifies an offset and a length for the bitfield.
- term: poly_uint64
  definition: A type used in GCC for representing unsigned 64-bit integers that can
    also handle symbolic or unknown values, typically used in optimization contexts.
- term: ICE
  definition: Internal Compiler Error. A crash within the compiler itself, usually
    indicating a bug in the compiler's logic or an unexpected input state.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a793e66d706e04e0600b852cd8818bde21ae3599
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

A bug in GCC's redundant store elimination (within tree-ssa-sccvn.cc) could lead to the creation of invalid BIT_FIELD_REF expressions. This occurred because the offset for the temporary BIT_FIELD_REF was not constrained, causing subsequent operations that assumed a valid offset to fail. The fix ensures the offset fits within a poly_uint64 before it's used, preventing an ICE (Internal Compiler Error).
