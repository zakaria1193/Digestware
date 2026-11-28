---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- ssa
- tree-optimization
- compiler-bug
commit_hash: a0627765c5626f320f26f80ea6aba3c6fb7f19d1
source_type: github
author: Richard Biener
headline: tree-optimization/129064 - value-number PHIs of a block in parallel
tldr: Improves value-numbering termination for complex PHI cycles in GCC's SSA form.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `process_bb` function in `tree-ssa-sccvn.cc` previously iterated
  and committed value-numbering results for PHIs sequentially within a basic block.
  This approach could lead to non-termination for PHI cycles, especially when multiple
  equivalent cycles existed. A PHI argument coming from a backedge, if it was the
  result of a PHI already processed in the same block, would see an updated value,
  while a later PHI might see an old value. This commit changes `process_bb` to value-number
  all PHIs in a block based on the previous values of their arguments, and then commit
  the new values collectivel…
primer_glossary:
- term: PHI node
  definition: In Static Single Assignment (SSA) form, a PHI node is an instruction
    that denotes the selection of one of several values based on the control flow
    path taken to reach the instruction. It's used to merge values from different
    preceding basic blocks.
- term: value-numbering
  definition: An optimization technique that assigns unique numbers to equivalent
    expressions or values within a program's intermediate representation, allowing
    the compiler to identify and eliminate redundant computations.
- term: SSA form
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned exactly once. PHI nodes are used to handle control
    flow merging.
- term: basic block
  definition: A sequence of instructions with a single entry point and a single exit
    point, where control flow does not branch except at the very end.
- term: CSE
  definition: Common Subexpression Elimination. An optimization that identifies and
    removes redundant occurrences of the same expression in code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a0627765c5626f320f26f80ea6aba3c6fb7f19d1
date: '2026-11-26'
is_stub: false
stub_reason: ''
---

This commit fixes a non-termination issue in GCC's SSA value-numbering pass when encountering PHI cycles. Previously, PHIs were processed sequentially, allowing one cycle to advance ahead of an equivalent one, leading to oscillations and failure to converge. The fix modifies the process to value-number all PHIs in a block based on their prior values, committing the results only after all PHIs are visited. This change aligns with the parallel execution semantics of PHIs and ensures correct termination.
