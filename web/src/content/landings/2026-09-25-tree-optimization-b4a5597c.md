---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- SLP
- loop analysis
commit_hash: b4a5597ccd6a38f5598c4c190f34162031ad6700
source_type: github
author: Richard Biener
headline: 'tree-optimization: Disable SLP vectorization with gaps for negative steps'
tldr: Disables SLP vectorization for negative step sizes when gaps are present, as
  the current implementation cannot handle them.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Disables VMAT_STRIDED_SLP vectorization when the loop step is negative
  and memory gaps are present (PR tree-optimization/127601). The current implementation
  of `VMAT_STRIDED_SLP` does not support the necessary logic to either use smaller
  vector loads to avoid touching a gap or to employ peeling to manage gaps that would
  be encountered by the first vector load. The changes in `get_load_store_type` adjust
  overrun flag handling and assert memory access types more correctly, explicitly
  disallowing `VMAT_STRIDED_SLP` for negative steps.
primer_glossary:
- term: SLP vectorization
  definition: Store-Load-Pair vectorization. A compiler optimization technique that
    groups consecutive memory stores and loads to create vector operations, even when
    the operations are not in a typical loop structure.
- term: Store-Load-Pair (SLP)
  definition: A compiler optimization technique that identifies and vectorizes sequences
    of memory store and load operations.
- term: vectorization
  definition: The process by which a compiler transforms code to use SIMD (Single
    Instruction, Multiple Data) instructions, enabling operations on multiple data
    elements simultaneously.
- term: memory gap
  definition: A region of memory that is not accessed by a loop or a sequence of operations,
    potentially disrupting contiguous vector loads or stores.
- term: peeling
  definition: A loop transformation technique where one or more initial iterations
    of a loop are separated and executed before the main loop body, often to align
    data or handle specific conditions.
- term: VMAT_STRIDED_SLP
  definition: A specific vectorization mode within GCC, likely referring to strided
    SLP vectorization, used for memory access patterns with a constant stride.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b4a5597ccd6a38f5598c4c190f34162031ad6700
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

This commit disables Store-Load-Pair (SLP) vectorization for loops with negative step sizes and memory gaps. The existing vectorization path for strided SLP does not support handling smaller vectors to avoid gaps or using peeling to manage gaps encountered with the first vector load, thus preventing incorrect code generation.
