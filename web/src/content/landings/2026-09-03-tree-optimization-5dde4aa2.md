---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- bugfix
- vectorization
- optimization
- compiler-error
commit_hash: 5dde4aa27ecfefcebc0a0d7dfbf336e321ec6ea1
source_type: github
author: Richard Biener
headline: tree-optimization/127195 - Fix ICE with vect_create_constant_vectors
tldr: Fixes an ICE in vectorization when creating constant vectors with excess lanes.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect_create_constant_vectors` function in `tree-vect-slp.cc` suffered
  from an ICE (PR tree-optimization/127195) when processing vectorized constants with
  excess lanes. The issue stemmed from a miscalculation of `number_of_copies`, leading
  to `ctor_seq` statements not being emitted correctly. This patch corrects the `number_of_copies`
  calculation and adds an assertion to verify that the operation completes on a vector
  boundary, ensuring correct constant vector generation.
primer_glossary:
- term: Internal Compiler Error (ICE)
  definition: An unrecoverable error within the compiler itself, indicating a bug
    in the compiler's logic or internal data structures. The build process is halted.
- term: vectorization
  definition: The process of transforming a loop or algorithm to operate on multiple
    data elements simultaneously using SIMD instructions, often leading to significant
    performance improvements.
- term: tree-optimization
  definition: A phase in the GCC compiler pipeline where optimizations are performed
    on an intermediate representation called GENERIC/GIMPLE trees.
- term: ctor_seq
  definition: Constructor sequence. In GCC's intermediate representation, this likely
    refers to a sequence of operations used to construct a vector or aggregate data
    type.
- term: excess lanes
  definition: In the context of vectorization, this refers to a situation where the
    available vector width is larger than required by the data elements, potentially
    leading to miscalculations if not handled properly.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5dde4aa27ecfefcebc0a0d7dfbf336e321ec6ea1
date: '2026-09-03'
is_stub: false
stub_reason: ''
---

An Internal Compiler Error (ICE) in GCC's vectorization pass, specifically within `vect_create_constant_vectors`, has been resolved. The bug occurred when code had excess vector lanes, causing an incorrect count of element copies. This led to `ctor_seq` statements not being emitted properly. The fix corrects the calculation of the number of copies and ensures the operation aligns with vector boundaries.
