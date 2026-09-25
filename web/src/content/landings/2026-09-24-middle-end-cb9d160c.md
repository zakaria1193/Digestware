---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- c++
- middle-end
- optimization
- standard conformance
- uninitialized reads
commit_hash: cb9d160c4dab693a3fc214736db2441ebbee6c35
source_type: github
author: Jakub Jelinek
headline: Fix C++26 uninitialized read behavior for P2795R5
tldr: Corrects C++26 handling of uninitialized reads to ensure consistent values and
  diagnostics.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The implementation of C++26 P2795R5 ('Erroneous behavior for uninitialized
  reads') had a flaw in the middle-end passes. While the front-end and initial gimplification
  handled the new `AUTO_INIT_CXX26` mode, subsequent optimizations were treating `.DEFERRED_INIT`
  for C++26 as something that could be optimized away or treated as `UNDEFINED` too
  aggressively. This violated the standard's requirement for consistent, albeit unspecified,
  values from multiple reads and for diagnostics. This patch adjusts the middle-end's
  understanding of `AUTO_INIT_CXX26` to prevent such aggressive optimizations.
primer_glossary:
- term: C++26
  definition: The 2026 revision of the C++ programming language standard.
- term: P2795R5
  definition: A revision of a C++ standardization proposal (likely related to uninitialized
    variables) that has been incorporated into the C++26 standard.
- term: uninitialized read
  definition: Accessing the value of a variable that has not been explicitly assigned
    a value. In C++, this can lead to undefined or unspecified behavior.
- term: middle-end
  definition: The part of a compiler that performs optimizations and transformations
    on an intermediate representation (IR) of the code, after the front-end has parsed
    the source code and before the back-end generates machine code.
- term: gimplification
  definition: The process in GCC where the high-level intermediate representation
    (like GENERIC or GIMPLE) is transformed into a lower-level, simpler form (GIMPLE)
    suitable for optimization passes.
- term: PHI node
  definition: In compiler theory, a PHI node is used in control flow graphs to represent
    a value that may have come from multiple different control flow paths. It's analogous
    to a merge point.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cb9d160c4dab693a3fc214736db2441ebbee6c35
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

This commit fixes an incorrect implementation of the C++26 P2795R5 standard concerning uninitialized reads. The standard requires that multiple reads of the same uninitialized variable yield a consistent (though unspecified) value and that such uses are diagnosed. The previous implementation incorrectly optimized these reads in the middle-end passes, violating the standard's requirements. This fix ensures that uninitialized reads are treated more conservatively, preserving their value consistency and allowing for diagnostics.
