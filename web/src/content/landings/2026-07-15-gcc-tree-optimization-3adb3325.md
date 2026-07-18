---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- optimization
- vectorization
commit_hash: 3adb3325954177939d59031055fc08a81ae21be3
source_type: github
author: Richard Biener
headline: Improve BB vectorization of reductions
tldr: Enhances loop vectorization for reductions by improving SLP discovery and handling
  of non-uniform operation chains.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `vect_slp_check_for_roots` and `vect_build_slp_instance` functions
  in GCC's SLP vectorizer were modified to better handle reduction operations. The
  change removes the artificial constraint of forcing BB reduction roots to have an
  even number of lanes. Instead, it allows SLP to re-attempt discovery on either the
  matching or non-matching portion of a non-uniform operation chain when an initial
  BB reduction attempt fails, improving robustness for cases like PR126028.
primer_glossary:
- term: vectorization
  definition: A compiler optimization technique that allows a single instruction to
    operate on multiple data elements simultaneously, often improving performance
    for numerical computations.
- term: SLP (Super Low-Power) vectorization
  definition: A compiler technique used to find straight-line code patterns that can
    be vectorized, even if they are not part of a loop. It works by identifying sequences
    of identical operations that can be mapped to SIMD instructions.
- term: Reduction operation
  definition: An operation that combines a sequence of values into a single result,
    such as summing, multiplying, or finding the maximum/minimum.
- term: Basic Block (BB)
  definition: A sequence of instructions with a single entry point and a single exit
    point. Vectorization is often applied to instructions within basic blocks.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3adb3325954177939d59031055fc08a81ae21be3
date: '2026-07-15'
is_stub: false
stub_reason: ''
---

This commit improves the vectorization of reduction operations in basic blocks (BBs) by refining the use of Super Low-Power (SLP) vectorization. Previously, uneven operation chains led to premature stripping of operations to achieve an even number of lanes, which was suboptimal. The change removes this early stripping, allowing SLP to discover the full pattern and re-analyze larger matching or non-matching parts, increasing successful vectorization.
