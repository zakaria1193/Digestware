---
project: gcc
subsystem: compare-elim
patch_id: null
tags:
- optimization
- compiler
commit_hash: 6ddf635c9c694dcdf5a5e490592f71b65c7e278f
source_type: github
author: Kyrylo Tkachov
headline: 'compare-elim: Test successor''s live-in set for flags register'
tldr: Corrects compare-elim pass to accurately check flag register liveness across
  basic block boundaries.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `find_comparisons_in_bb` function in `compare-elim.cc` identifies
  comparisons whose flags are live-out of a basic block (BB) and live-in to a successor
  not part of the extended basic block. Previously, it queried `DF_LIVE_BB_INFO(BB)->in`
  instead of `DF_LIVE_BB_INFO(DEST)->in` (where DEST is the successor). This commit
  reverts to the correct check, ensuring that missing uses of flags in join blocks
  are correctly detected, particularly when flags are live across BB boundaries.
primer_glossary:
- term: compare-elim
  definition: A compiler optimization pass that eliminates redundant comparison instructions
    by analyzing program flow and data dependencies. It aims to simplify the control
    flow graph and reduce overhead.
- term: flags register
  definition: A special register (often part of the processor's status register) that
    holds the results of arithmetic and logical operations, such as zero, carry, or
    overflow flags, which are then used by conditional instructions.
- term: basic block
  definition: A contiguous sequence of instructions in a program in which control
    flow enters at the beginning and leaves at the end without halt or possibility
    of branching except at the end.
- term: live-in set
  definition: In liveness analysis, the set of variables or registers that hold values
    that are live (i.e., will be used later) upon entry to a particular basic block.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6ddf635c9c694dcdf5a5e490592f71b65c7e278f
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

The compare-elimination pass incorrectly checked the live-in set of the current basic block instead of its successor when determining if the flags register was used in a join block. This commit corrects the pass to query the successor's live-in set, ensuring that comparisons whose flags are live across block boundaries are properly identified and handled, preventing potential issues in join blocks.
