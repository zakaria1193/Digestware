---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- bugfix
commit_hash: e86951e831b893ee8fdc3f87d77dd469b8ec8500
source_type: github
author: Richard Biener
headline: Clear LOOP_C_FINITE for scalar prologue/epilogue after vectorization
tldr: Ensures scalar loop assumptions are correctly handled after vectorization, preventing
  confusion for subsequent passes.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change in `tree-vect-loop-manip.cc` clears the `LOOP_C_FINITE`
  flag on scalar prologue and epilogue loops when early-break vectorization is performed.
  Early-break vectorization, when combined with assumptions, might not record all
  non-main exit conditions in the versioning loop's condition. This can lead subsequent
  scalar passes to incorrectly assume loop finiteness. Clearing `LOOP_C_FINITE` ensures
  these scalar loops are treated appropriately after vectorization, preventing incorrect
  analysis.
primer_glossary:
- term: tree-optimization
  definition: An intermediate representation (IR) used by GCC for performing optimizations.
    'Tree' refers to the structure of the IR, which resembles an abstract syntax tree.
- term: vectorization
  definition: An optimization technique that transforms scalar operations (processing
    one data item at a time) into vector operations (processing multiple data items
    simultaneously using SIMD instructions).
- term: scalar prologue/epilogue
  definition: Code segments that are executed before (prologue) and after (epilogue)
    the main vectorized loop. These handle initialization, cleanup, or iterations
    that cannot be vectorized.
- term: LOOP_C_FINITE
  definition: A compiler internal flag or attribute associated with a loop, indicating
    that the loop is guaranteed to terminate (i.e., it is finite).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e86951e831b893ee8fdc3f87d77dd469b8ec8500
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This commit addresses an issue where scalar passes could be confused by loop flags after vectorization, particularly for scalar prologue and epilogue loops. When early-break vectorization occurs, assumptions might not be fully recorded in the versioning condition, leading to alternate loop exits. The change clears the `LOOP_C_FINITE` flag for these scalar loops to ensure correct behavior and accurate assumption propagation for subsequent optimization passes.
