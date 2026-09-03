---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- ICE
commit_hash: 439cd07b51676996889b1277afd46c1053d24ebc
source_type: github
author: Richard Biener
headline: ICE in vectorizable_lane_reducing fixed by handling analysis failure.
tldr: Fixes an internal compiler error by properly handling failures in vectorization
  analysis for lane-reducing operations.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vectorizable_lane_reducing` function in `tree-vect-loop.cc` is
  modified to handle the case where `vect_get_num_copies_for_invariant` fails. Previously,
  this helper function would assert if it could not determine the number of copies
  for a lane-reducing operation. Since `vectorizable_lane_reducing` uses this count
  for costing, the assertion led to an ICE. The change makes `vectorizable_lane_reducing`
  return failure when `vect_get_num_copies_for_invariant` does, addressing PR 127190.
primer_glossary:
- term: Internal Compiler Error (ICE)
  definition: An unrecoverable error that occurs within the compiler itself, indicating
    a bug in the compiler's logic or internal state. It typically halts the compilation
    process.
- term: vectorization
  definition: An optimization technique that allows the compiler to perform the same
    operation on multiple data elements simultaneously using special vector instructions
    (SIMD).
- term: lane-reducing reduction
  definition: A type of reduction operation within a vector loop where intermediate
    results are combined across different lanes (elements) of a vector register. For
    example, summing elements across lanes.
- term: vect_get_num_copies_for_invariant
  definition: A GCC internal function used during vectorization analysis to determine
    how many copies of an invariant value are needed for a specific operation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/439cd07b51676996889b1277afd46c1053d24ebc
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

This commit resolves an Internal Compiler Error (ICE) that occurred when analyzing lane-reducing reductions for vectorization. The issue arose because `vect_get_num_copies_for_invariant` would assert failure instead of returning an error code when it could not determine the number of copies. The analysis later relied on this information for costing, leading to the ICE. The fix ensures that the `vectorizable_lane_reducing` function fails early and gracefully when `vect_get_num_copies_for_invariant` encounters an issue, preventing the ICE and improving robustness for PR 127190.
