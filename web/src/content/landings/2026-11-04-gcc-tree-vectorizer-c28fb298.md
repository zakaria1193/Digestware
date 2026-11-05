---
project: gcc
subsystem: gcc/tree-vectorizer
patch_id: null
tags:
- gcc
- vectorization
- bugfix
commit_hash: c28fb298ab9abae7f7501411c2003e834ae568ef
source_type: github
author: Richard Biener
headline: Fill match[] on can_duplicate_and_interleave_p failure
tldr: Fixes a bug in SLP vectorization where a failed 'duplicate and interleave' check
  could corrupt internal match data.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: When the SLP vectorizer in `tree-vect-slp.cc` attempts to build an
  SLP tree (specifically in `vect_build_slp_tree_2`), it calls `can_duplicate_and_interleave_p`
  to check if operands can be combined. If this check fails, it may leave the `matches[]`
  array in an inconsistent state, potentially using a clobbered version from an earlier
  operand or failing to report all non-matching lanes. This patch ensures that upon
  failure of `can_duplicate_and_interleave_p`, a valid `matches[]` is constructed,
  preventing a false sense of success or further incorrect analysis.
primer_glossary:
- term: SLP
  definition: Slanted Line Processor. A compiler optimization technique that finds
    vectorization opportunities by identifying identical or similar sequences of scalar
    instructions that can be executed in parallel on vector hardware. It operates
    on the intermediate representation after loop optimizations.
- term: Vectorizer
  definition: A compiler component responsible for transforming scalar code into vector
    code, allowing multiple data elements to be processed simultaneously using SIMD
    (Single Instruction, Multiple Data) instructions. GCC has both loop vectorizers
    and SLP vectorizers.
- term: Intermediate Representation (IR)
  definition: A data structure or code format used internally by a compiler to represent
    the source code during various stages of translation. GCC uses multiple IRs, including
    GENERIC and GIMPLE.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c28fb298ab9abae7f7501411c2003e834ae568ef
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This commit addresses a defect in the SLP vectorizer where a failure in the `can_duplicate_and_interleave_p` check could lead to an improperly populated `matches[]` array. This condition could occur when trying to create a constant or invariant definition. The fix ensures that `matches[]` is correctly populated even when this check fails, preventing incorrect data from being used in subsequent operations.
