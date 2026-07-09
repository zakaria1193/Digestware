---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- bugfix
commit_hash: 210b4eca880c88e7f7ec970b68a93a2a28bad1be
source_type: github
author: Richard Biener
headline: tree-optimization/126150 - Fix ICE with replace_uses_by by deferring EH
  edge purging
tldr: Fixes a compiler internal error occurring during use replacement by deferring
  EH edge purging.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: PR tree-optimization/126150 revealed an ICE in `tree-cfg.cc`'s `replace_uses_by`.
  The problem arises because EH edge purging, which can remove basic blocks, is triggered
  within a `FOR_EACH_IMM_USE_STMT` loop. This loop iterates over uses that might be
  in basic blocks subsequently removed, leading to use-after-free or similar issues.
  The fix defers the EH edge purging to occur after the loop finishes, ensuring the
  integrity of the iteration.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error. A crash within the compiler itself, usually
    indicating a bug in the compiler's logic rather than the user's code.
- term: EH edge
  definition: An edge in the control flow graph (CFG) representing an exception handling
    path. These edges connect code blocks that might throw an exception to the corresponding
    exception handlers.
- term: basic block
  definition: A sequence of instructions with a single entry point and a single exit
    point. Control flow graphs are composed of basic blocks.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/210b4eca880c88e7f7ec970b68a93a2a28bad1be
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This commit resolves an internal compiler error (ICE) in the `replace_uses_by` function that occurred when removing basic blocks. The issue stemmed from attempting to purge EH (Exception Handling) edges while iterating over the statements that defined the uses. The fix defers the purging of EH edges until after the iteration is complete, preventing the invalidation of data structures during processing.
