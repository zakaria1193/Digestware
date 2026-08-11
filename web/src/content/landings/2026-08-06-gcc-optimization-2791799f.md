---
project: gcc
subsystem: gcc/optimization
patch_id: null
tags:
- optimization
- correctness
- code generation
- gcc
commit_hash: 2791799fe11f886736869e3aff093e0c14fb10b8
source_type: github
author: Kyrylo Tkachov
headline: 'pair-fusion: Verify that a fused pair really is adjacent'
tldr: Fixes pair-fusion optimization to prevent incorrect code generation by ensuring
  fused memory accesses are truly adjacent.
impact_score: 8
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `fuse_pair` function in `pair-fusion.cc` was incorrectly merging
  `MEM_EXPR`s that shared a base register but had differing offsets, leading to invalid
  fusion. This was particularly problematic for stack slots. The fix ensures that
  the two memory accesses are exactly one access size apart when their base registers
  match, enforcing the adjacency invariant and preventing incorrect code generation
  by making violations an ICE.
primer_glossary:
- term: pair-fusion
  definition: An optimization pass that attempts to fuse adjacent memory access operations
    (reads or writes) into a single, more efficient instruction.
- term: MEM_EXPR
  definition: A GCC intermediate representation that denotes a memory reference, typically
    comprising a base address and an offset.
- term: out-of-SSA
  definition: Refers to transformations that occur after the Static Single Assignment
    (SSA) form has been established, potentially breaking SSA invariants. The pass
    in question must maintain these invariants.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2791799fe11f886736869e3aff093e0c14fb10b8
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

The `pair-fusion` optimization pass has been corrected to accurately verify that fused memory accesses are indeed adjacent. Previously, when using `MEM_EXPR` base offsets, the pass could incorrectly identify non-adjacent memory accesses as adjacent, leading to silent generation of wrong code. This fix adds a check to compare offsets relative to a common base register, preventing such misinterpretations and ensuring correctness.
