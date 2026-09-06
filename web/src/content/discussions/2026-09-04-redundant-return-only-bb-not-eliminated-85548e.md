---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- optimization
- cfg
- risc-v
discussion_id: df047a71-775f-4901-b717-aad0aa08a659@oss.qualcomm.com
source_type: public_inbox
title: 'Re: [RISCV] redundant return-only BB not eliminated'
headline: redundant return-only BB not eliminated
tldr: Discussion on the complexities of eliminating redundant return-only basic blocks
  in GCC, considering different optimization modes.
proposer: Jeff Law <jeffrey.law@oss.qualcomm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Complexity of CFG manipulation across different optimization modes.
- Ensuring correctness of edge redirection and fall-through handling.
exchanges:
- author: Jeff Law <jeffrey.law@oss.qualcomm.com>
  role: proposer
  position: Explains that eliminating a redundant return-only block is feasible after
    prologue/epilogue threading and can be done by modifying CFG edges to point to
    a new target block.
  quote: "Conceptually a block ending in a return can have its return removed and\
    \ the cfg altered so that it has a fallthru edge to a block that has a return\
    \ and nothing else.  This is true before and after cfg layout mode.\n\nThe refined\
    \ wrinkle is you have to be past threading the \nprologue/epilogue.  It's only\
    \ after that point that you know if you have a trivial return or not.\n\nSo conceptually\
    \ you could e…"
- author: Robert Guthrie
  role: contributor
  position: Acknowledges the complexity and describes encountering issues with infinite
    loops and differing behavior between CFGRTL and CFGLAYOUT modes when modifying
    `cleanup_cfg`.
  quote: "That is true: it has been a little harder than I expected!\nSince I am modifying\
    \ cleanup_cfg, and it is called so many times,\nI am getting a lot of weird interactions\
    \ leading to infinite loops or\nother errors. Or getting different behavior when\
    \ it is called in \nCFGRTL vs. CFGLAYOUT\nmode (I spent last evening trying to\
    \ grok the difference)."
primer_expert: This discussion pertains to optimizing the control flow graph (CFG)
  in GCC by eliminating redundant basic blocks that solely contain a return statement.
  It delves into the intricacies of when this optimization can be safely applied,
  particularly concerning the stages of CFG manipulation (CFGRTL vs. CFGLAYOUT) and
  the impact of prologue/epilogue threading, suggesting a strategy involving predecessor
  analysis and edge redirection.
primer_glossary:
- term: basic block
  definition: A sequence of instructions with a single entry point and a single exit
    point. Control flow enters at the beginning and exits at the end without halt
    or possibility of branching except at the exit.
- term: CFG
  definition: Control Flow Graph, a representation of all execution paths in a program,
    typically used by compilers for analysis and optimization.
- term: CFGRTL
  definition: A stage in GCC's compilation pipeline where the code is represented
    in RTL (Register Transfer Language), a low-level intermediate representation.
- term: CFGLAYOUT
  definition: Likely refers to a phase in GCC's CFG manipulation where basic blocks
    are laid out and fall-through edges are established.
- term: prologue/epilogue threading
  definition: A compiler optimization step that standardizes the entry (prologue)
    and exit (epilogue) code of functions, often simplifying subsequent analyses and
    optimizations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/df047a71-775f-4901-b717-aad0aa08a659@oss.qualcomm.com
bugzilla_url: null
date: '2026-09-04'
is_stub: false
stub_reason: ''
---

Jeff Law provides guidance on eliminating redundant return-only basic blocks in GCC, explaining that it can be done after prologue/epilogue threading. The discussion touches on the differences between CFGRTL and CFGLAYOUT modes and how the optimization should conceptually work by examining predecessors of the exit block.
