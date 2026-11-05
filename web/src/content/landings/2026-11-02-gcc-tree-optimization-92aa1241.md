---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- ssa
- optimization
- pointers
- bugfix
commit_hash: 92aa1241492529300f3cc3953f35524f31196119
source_type: github
author: Andrew MacLeod
headline: Known non-zero bits for pointers as well.
tldr: Fixes calculation of known non-zero bits for pointers in SSA names.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `get_known_nonzero_bits_1` function in `tree-ssanames.cc` is part
  of GCC's SSA (Static Single Assignment) infrastructure, used to compute properties
  of values, such as which bits are known to be non-zero. This function was incorrectly
  returning 0 for pointer types, failing to utilize the `bitmask` and `alignment`
  information stored in the `prange_storage` that represents the value's properties.
  This patch updates the function to correctly process pointers, ensuring that `known_nonzero_bits`
  accurately reflects pointer characteristics, which can benefit optimizations that
  rely on such info…
primer_glossary:
- term: Static Single Assignment (SSA)
  definition: An intermediate representation form where every variable is assigned
    exactly once. This simplifies many compiler analyses and optimizations, including
    data flow analysis and constant propagation.
- term: Known non-zero bits
  definition: Information within the compiler indicating which specific bits of a
    variable or expression are guaranteed to be set to 1. This can help optimize operations
    that depend on bit patterns.
- term: Pointer
  definition: A variable that stores a memory address. In C/C++, pointers are fundamental
    for dynamic memory management and low-level data manipulation.
- term: Tree optimization
  definition: A phase in GCC's compilation pipeline that operates on the 'tree' intermediate
    representation (specifically GIMPLE). This is where many high-level optimizations,
    like constant folding and dead code elimination, are performed.
- term: SSA names
  definition: In the SSA form, each variable assignment creates a new version, or
    'name', for that variable. SSA names are used to track value flow through the
    program.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/92aa1241492529300f3cc3953f35524f31196119
date: '2026-11-02'
is_stub: false
stub_reason: ''
---

This commit corrects the calculation of `known_nonzero_bits` for pointer types within GCC's Static Single Assignment (SSA) naming infrastructure. Previously, this calculation incorrectly returned 0 for pointers, ignoring available bitmask and alignment information. The fix modifies `get_known_nonzero_bits_1` in `tree-ssanames.cc` to correctly handle pointers, ensuring more accurate information is available for subsequent optimizations.
