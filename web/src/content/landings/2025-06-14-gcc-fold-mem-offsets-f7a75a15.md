---
project: gcc
subsystem: gcc/fold-mem-offsets
patch_id: null
tags:
- optimization
- rtl-ssa
commit_hash: f7a75a1506d91fcc76890732a0f720952e01e8fa
source_type: github
author: Konstantinos Eleftheriou
headline: Convert fold-mem-offsets pass to use RTL-SSA
tldr: The fold-mem-offsets optimization pass is rewritten to use RTL-SSA, improving
  efficiency by processing instructions in a single pass.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The ``fold-mem-offsets`` pass, previously operating on DF, is now ported
  to RTL-SSA. It analyzes RTL instructions to identify memory references of the form
  `(*base_reg + offset)` where the offset is a constant. The pass now iterates once
  over non-debug INSNs, building a DEF-chain of these roots. It distinguishes between
  single-USE and multi-USE scenarios for transformations, impacting analysis cost
  and optimization opportunities. The pass's behavior is controlled by flags like
  ``-fno-fold-mem-offsets`` and ``-fexpensive-optimizations``.
primer_glossary:
- term: DF
  definition: Data Flow analysis, a technique used in compilers to gather information
    about the flow of data through a program. It typically involves iterating over
    program instructions multiple times to converge on a stable state.
- term: RTL-SSA
  definition: Register Transfer Language Static Single Assignment. RTL is GCC's intermediate
    representation for machine instructions. SSA is a program representation where
    every variable is assigned exactly once, simplifying many compiler analyses and
    optimizations.
- term: fold-mem-offsets
  definition: A compiler optimization pass that identifies and potentially simplifies
    memory accesses where the address is calculated as a base register plus a constant
    offset.
- term: DEF-chain
  definition: In the context of SSA, a chain tracing the definition of a value to
    its subsequent uses. Analyzing the DEF-chain helps determine if a value can be
    safely modified or eliminated.
- term: INSN
  definition: An 'instruction' in GCC's internal representation. INSNs represent low-level
    machine operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f7a75a1506d91fcc76890732a0f720952e01e8fa
date: '2025-06-14'
is_stub: false
stub_reason: ''
---

The fold-mem-offsets optimization pass has been converted from using DF (Data Flow) to RTL-SSA (Register Transfer Language Static Single Assignment). This rewrite significantly alters how the pass collects information, now processing each instruction only once. It introduces single-USE and multi-USE modes for identifying foldable memory offsets, with performance varying based on code complexity and optimization level.
