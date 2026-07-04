---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- memset
- simplification
commit_hash: a8072f31bc90000b3b8a2c0c7819710cf924727a
source_type: github
author: Naveen
headline: 'tree-optimization: fold memset with length in [0, 1] to conditional store
  [PR102202]'
tldr: Optimizes small `memset` calls to simple conditional stores.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch enhances the `tree-call-cdce` pass to optimize `memset`
  calls where the length is proven to be in the range [0, 1]. It introduces `len_has_boolean_range_p`
  and `can_shrink_wrap_len_p` to identify eligible `memset` calls. For length 0, it
  uses `shrink_wrap_len_call` to replace the call with a conditional check. For length
  1, it directly generates a store instruction, extending `gimple_fold_builtin_memset`
  to handle singleton lengths proven by Ranger analysis, not just constant lengths.
  This refines the shrink-wrapping logic to prioritize these small `memset` optimizations.
primer_glossary:
- term: memset
  definition: A standard C library function used to fill a block of memory with a
    particular byte value. It takes a pointer to the memory, the value to set, and
    the number of bytes to fill.
- term: Ranger Analysis
  definition: A static analysis technique used by compilers to determine the possible
    range of values for variables or expressions throughout the program's execution.
    This information can be used to prove properties about code, such as bounds on
    loop counters or array indices.
- term: Shrink Wrapping
  definition: An optimization technique where a condition or check is moved closer
    to the code it guards, potentially reducing the number of paths a check needs
    to be performed on. In this case, a zero-length `memset` call might be replaced
    by a conditional check that effectively does nothing if the length is zero.
- term: GIMPLE
  definition: GCC's internal three-address intermediate representation (IR). It's
    a low-level, simplified representation of the program used by the middle-end optimization
    passes.
- term: Conditional Store
  definition: A memory write operation that is only performed if a certain condition
    is met. This can be used to optimize code by avoiding unnecessary writes or to
    ensure data integrity based on program state.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a8072f31bc90000b3b8a2c0c7819710cf924727a
date: '2026-07-03'
is_stub: false
stub_reason: ''
---

The compiler now optimizes `memset` calls with lengths of 0 or 1 more effectively. For a zero-length `memset`, the call is shrink-wrapped. For a one-length `memset`, it's replaced with a direct byte store. This optimization leverages Ranger analysis to identify these cases, even when the length is determined by runtime values within a provable range, not just constants. This improves performance by eliminating function call overhead and simplifying the generated code.
