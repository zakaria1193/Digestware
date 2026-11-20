---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop interchange
- bitfield
commit_hash: 5e3007f353e16c7d3e641aeb0770a7976f009eda
source_type: github
author: Richard Biener
headline: Handle BIT_FIELD_REF in compute_access_stride
tldr: Loop interchange optimization now correctly analyzes bit-field references by
  using their base address.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gimple-loop-interchange.cc` pass `compute_access_stride` is used
  to analyze memory access patterns for loop transformations. This patch extends its
  analysis to handle `BIT_FIELD_REF` by dropping to the base address of the bitfield,
  similar to how other bitfield accesses are treated, ensuring more accurate stride
  analysis for loop interchange.
primer_glossary:
- term: Loop Interchange
  definition: Loop interchange is an optimization technique that swaps the order of
    nested loops. This can improve data locality and enable other optimizations by
    restructuring array accesses to be more contiguous in memory.
- term: BIT_FIELD_REF
  definition: A BIT_FIELD_REF refers to a specific bit field within a larger data
    structure. In GCC's GIMPLE intermediate representation, it represents an access
    to a part of a larger integer or structure member.
- term: compute_access_stride
  definition: A function within GCC's loop optimization passes that calculates the
    stride of memory accesses within a loop. This information is crucial for determining
    if loop transformations like interchange or fusion are beneficial and safe.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5e3007f353e16c7d3e641aeb0770a7976f009eda
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This commit improves the `compute_access_stride` function within the loop interchange optimization. Previously, bit-field references (`BIT_FIELD_REF`) were not fully handled. The change ensures that for `BIT_FIELD_REF`s, the analysis now uses the address of its base for stride calculation, aligning its behavior with how loop interchange handles other bitfield accesses. A new test case is added.
