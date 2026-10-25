---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- compiler
commit_hash: d0f760ff309ab3a4a8cbe71b9971d08429ff2596
source_type: github
author: Richard Biener
headline: Use LOOPS_NORMAL for FRE to ensure simple latches.
tldr: Modify the FRE pass to use LOOPS_NORMAL for loop latches, improving efficiency
  by reducing iteration overhead.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The FRE pass is part of GCC's inter-procedural optimization. Loop structures
  with complex latches can lead to separate iteration computations. By switching to
  LOOPS_NORMAL, the pass ensures that loops have simple latches, reducing the number
  of iteration management edges and potentially improving overall loop performance.
primer_glossary:
- term: FRE
  definition: FRE stands for Function Reordering Engine, a compiler optimization pass
    that reorders functions to improve instruction cache behavior and overall program
    performance.
- term: loop latch
  definition: A loop latch is an edge in a control flow graph that goes from the last
    basic block of a loop back to the header block, signifying the loop's iteration
    condition.
- term: LOOPS_NORMAL
  definition: A compiler internal flag or setting that indicates a loop has a normal,
    simple latch structure, as opposed to more complex or irreducible loop constructs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d0f760ff309ab3a4a8cbe71b9971d08429ff2596
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

The FRE (Function Reordering Engine) pass in GCC previously did not guarantee simple loop latches. This commit changes the FRE pass to use LOOPS_NORMAL, which enforces simpler latch structures. This is beneficial because fewer latch edges generally lead to more efficient iteration, reducing overhead for the compiler.
