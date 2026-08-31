---
project: gcc
subsystem: gcc
patch_id: null
tags:
- riscv
- optimization
- compiler-internals
- cfg
discussion_id: apSEEAiw9CP262re@bertguix
source_type: public_inbox
title: '[RISCV] redundant return-only BB not eliminated'
headline: 'RISCV: redundant return-only BB not eliminated'
tldr: A factorial function compiled for RISCV produces an unnecessary return instruction,
  and the contributor seeks guidance on optimization passes.
proposer: Robert Guthrie <forkbombidable@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 8
technical_tradeoffs:
- The author's custom fix is overly specific and might not generalize.
- Incorrectly modifying CFG passes like `try_optimize_cfg` can lead to infinite loops
  or break other optimizations.
exchanges:
- author: Robert Guthrie <forkbombidable@gmail.com>
  role: proposer
  position: Reports a redundant return instruction in RISC-V compiled code and seeks
    guidance on compiler optimization passes.
  quote: 'The below basic recursive factorial function generates two `ret` insns when
    only one is necessary: the BB labeled with .L12 can be eliminated (by just re-targeting
    to .L1).'
- author: Jeff Law <jeffreyalaw@gmail.com>
  role: other
  position: Acknowledges the report and provides initial context.
  quote: "On 8/30/26 1:34 PM, Robert Guthrie via Gcc wrote:\n> Hello, I have been\
    \ exploring RISCV, compiling simple programs and \n> looking at the output.\n\
    > The below basic recursive factorial function generates two `ret` insns \n> when\
    \ only one is necessary: ..."
primer_expert: The reporter observed that a simple recursive factorial function compiled
  for RISC-V generates two return instructions. This is caused by loop unrolling creating
  an early exit, and subsequent passes like 'bbro' arranging these returns such that
  one is redundant. The issue lies in the control flow graph (CFG) optimization passes
  failing to eliminate this redundant basic block, possibly due to conditions in `cleanup_cfg`
  or related functions.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on RISC principles,
    known for its modularity and extensibility.
- term: return instruction
  definition: A machine code instruction that signals the end of a function's execution
    and transfers control back to the caller.
- term: basic block (BB)
  definition: A sequence of instructions with a single entry point and a single exit
    point, typically used in compiler intermediate representations for optimization.
- term: loop unrolling
  definition: An optimization technique where loop iterations are duplicated to reduce
    loop overhead and enable further optimizations.
- term: fall-through
  definition: In control flow, when execution proceeds to the next instruction or
    basic block without an explicit jump or branch.
- term: bbro
  definition: Likely refers to the 'Branch and Block Reordering' optimization pass
    in GCC, which aims to improve instruction cache performance.
- term: cleanup_cfg
  definition: A function or pass within GCC's compiler infrastructure that cleans
    up and optimizes the Control Flow Graph (CFG) after other transformations.
- term: CROSSJUMP
  definition: A specific optimization within GCC's CFG cleanup that identifies and
    merges basic blocks that are direct jumps to each other.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/apSEEAiw9CP262re@bertguix
bugzilla_url: null
date: '2026-08-30'
is_stub: false
stub_reason: ''
---

The author reports an unnecessary return instruction generated for a RISC-V factorial function due to loop unrolling and fall-through. They investigated optimization passes like 'bbro' and 'cleanup_cfg' but couldn't pinpoint the exact pass responsible for not eliminating the redundant basic block. The contributor, new to compiler development, added a custom fix and seeks advice on the correct approach.
