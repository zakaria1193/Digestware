---
project: gcc
subsystem: tree-ssa-threadbackward
patch_id: null
tags:
- refactor
- backthreader
commit_hash: 801ce7c8c122c251b76f1fe478069cfb8b4bfb0b
source_type: github
author: Aldy Hernandez
headline: 'backthreader: group the per-path stats into a struct'
tldr: Backthreader's per-path statistics are now grouped into a struct for cleaner
  management.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors the `back_threader_profitability` class in `tree-ssa-threadbackward.cc`
  by introducing a `path_stats` struct. This struct encapsulates fields like `m_threaded_through_latch`,
  `m_multiway_branch_in_path`, `m_contains_hot_bb`, and `m_unprofitable_bb`, which
  were previously members of the class. Grouping these into a struct facilitates easier
  data management, such as moving and clearing the stats as a single unit, making
  the code cleaner and less error-prone.
primer_glossary:
- term: backthreader
  definition: A GCC optimization pass that reorders instructions to improve parallelism.
    It analyzes execution paths to determine the most profitable reordering strategies.
- term: struct
  definition: A composite data type in C/C++ that groups together variables of different
    data types under a single name. It helps in organizing related data.
- term: multiway branch
  definition: A control flow instruction that can transfer execution to one of several
    different locations based on a condition or value.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/801ce7c8c122c251b76f1fe478069cfb8b4bfb0b
date: '2026-09-09'
is_stub: false
stub_reason: ''
---

To improve code clarity and manageability, the backthreader pass now groups its per-path statistics into a dedicated `path_stats` struct. This change consolidates related fields, allowing them to be moved and cleared as a unit, simplifying the `tree-ssa-threadbackward.cc` implementation.
