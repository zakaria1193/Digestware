---
project: gcc
subsystem: tree-ssa-threadbackward
patch_id: null
tags:
- refactor
- backthreader
commit_hash: 610ea2e119f9eda59d889bf8309555cb0e962782
source_type: github
author: Aldy Hernandez
headline: 'backthreader: split out back_threader_profitability::account_bb'
tldr: Backthreader's block accounting logic is extracted into a new function for clarity.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors `tree-ssa-threadbackward.cc` by extracting the
  loop body responsible for accumulating statistics for a single basic block into
  a new member function, `back_threader_profitability::account_bb`. The previous mechanism
  for handling unthreadable blocks, which involved a bailout within the loop, is replaced
  by setting an `m_unprofitable_bb` flag. This flag persists after the call, simplifying
  the control flow for determining path profitability.
primer_glossary:
- term: backthreader
  definition: A GCC optimization pass that reorders instructions to improve parallelism.
    It analyzes execution paths to determine the most profitable reordering strategies.
- term: basic block
  definition: A contiguous sequence of zero or more three-address instructions in
    which control enters at the beginning and leaves at the end without halt or possibility
    of branching except at the end.
- term: function extraction
  definition: The process of taking a block of code from within one function and creating
    a new, separate function for it. This improves modularity and readability.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/610ea2e119f9eda59d889bf8309555cb0e962782
date: '2026-09-09'
is_stub: false
stub_reason: ''
---

The logic for accounting a basic block's statistics within the backthreader's profitability analysis has been extracted into a new `account_bb` function. This change improves code organization by isolating the block-specific processing, and introduces an `m_unprofitable_bb` flag to signal unthreadable blocks.
