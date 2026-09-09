---
project: gcc
subsystem: gcc
patch_id: null
tags:
- optimization
- cfg
discussion_id: ap9pjXUOhYGVixBO@bertguix
source_type: public_inbox
title: 'Re: [RISCV] redundant return-only BB not eliminated'
headline: Redundant return-only BB not eliminated
tldr: A patch to optimize CFG cleanup by removing redundant return-only basic blocks
  is discussed, with suggestions on implementation details.
proposer: Robert Guthrie <forkbombidable@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Reliance on `prev_bb`/`next_bb` vs. predecessor/successor lists for CFG manipulation.
exchanges:
- author: Robert Guthrie
  role: proposer
  position: Submitted a patch to optimize CFG cleanup by removing redundant consecutive
    return-only basic blocks and explained his debugging process.
  quote: 'Thanks -- I didn''t want to ask anyone to debug my stuff, and

    anyways it took a bit of time but was straightforward. Most of the debugging

    has just been me resolving my misunderstandings about what certain functions

    do or variables are for, which is helpful for me.'
- author: unknown
  role: reviewer
  position: Critiqued the patch's approach of using `prev_bb`/`next_bb`, suggesting
    that predecessor and successor lists are more relevant for block ordering in CFG
    cleanup.
  quote: "So in general you don't want to be looking at prev_bb/next_bb. Yes,\nblocks\
    \ are kept in a chain, but there's really no meaning to the order \nof the chain\
    \ until after block layout. What really matters are the \npred/succ lists."
primer_expert: This discussion concerns the `cfgcleanup.cc` pass in GCC's middle-end.
  The patch proposes to optimize the Control Flow Graph (CFG) by removing redundant
  basic blocks that contain only a return instruction and immediately follow another
  such block. The core of the discussion revolves around the correct way to identify
  and manipulate these blocks within the CFG data structures, specifically whether
  to rely on the block's immediate predecessor/successor pointers or the more general
  predecessor/successor lists.
primer_glossary:
- term: Basic Block (BB)
  definition: A sequence of instructions with exactly one entry point and one exit
    point. Control flow can only enter at the beginning and leave at the end.
- term: Control Flow Graph (CFG)
  definition: A representation of all possible execution paths through a program.
    Nodes are basic blocks, and edges represent control flow transfers.
- term: cfgcleanup.cc
  definition: A GCC source file containing functions for cleaning up and optimizing
    the control flow graph.
- term: return-only BB
  definition: A basic block that contains only a return instruction and no other executable
    code.
- term: Predecessor/Successor Lists
  definition: In a CFG, predecessor lists contain nodes that transfer control to the
    current node, while successor lists contain nodes that the current node transfers
    control to.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/ap9pjXUOhYGVixBO@bertguix
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

Robert Guthrie proposes a patch to eliminate redundant consecutive return-only basic blocks in the CFG cleanup pass. He initially struggled with debugging but found the solution straightforward after resolving misunderstandings. Another participant (implied by the quote) suggests a different approach, focusing on predecessor and successor lists rather than `prev_bb`/`next_bb` for block ordering.
