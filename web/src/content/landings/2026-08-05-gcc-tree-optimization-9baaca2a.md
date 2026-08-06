---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- compiler
commit_hash: 9baaca2adeca178edf8c0816ef328dba1cf270bc
source_type: github
author: Richard Biener
headline: Fix bitfield rounding in get_inner_reference_aff.
tldr: Correctly handles bitfield precision offsets and sizes for affine transformations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `get_inner_reference_aff` function in `tree-affine.cc` computes
  affine transformations, which are crucial for loop optimizations. This patch fixes
  a bug in how it handles bitfields, specifically the rounding of their sizes and
  positions. The corrected logic ensures that the precise bit-level offsets and sizes
  are accurately incorporated into the affine representation, preventing potential
  miscalculations in optimizations that rely on bitfield layouts.
primer_glossary:
- term: affine transformation
  definition: A mathematical transformation that preserves lines and parallelism,
    often used in compiler optimizations to represent relationships between loop indices
    and memory accesses.
- term: bitfield
  definition: A data structure within a C or C++ struct that allows for storage of
    integral types in a specified number of bits, less than the natural size of the
    type. This can save space but introduces complexities in accessing and calculating
    sizes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9baaca2adeca178edf8c0816ef328dba1cf270bc
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

The get_inner_reference_aff function has been corrected to properly handle bit precision offsets and sizes when calculating affine transformations. Previously, it failed to round these values correctly. This change adjusts the rounding logic to ensure more accurate computations, accompanied by a new test case to verify the fix.
