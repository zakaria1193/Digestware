---
project: gcc
subsystem: sched-deps
patch_id: null
tags:
- optimization
- scheduler
- memory management
commit_hash: ce720fc2b7e70fe284f5b6159e4088dc6e8844c0
source_type: github
author: Kyrylo Tkachov
headline: 'sched-deps: Release reg_last lists outside of reg_last_in_use'
tldr: Fixes memory leaks in sched-deps by ensuring lists are returned to the recycler.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `sched-deps` component tracks dependencies between instructions
  to aid in scheduling. Specifically, `reg_last_in_use` tracks which `reg_last` entries
  are currently in use. However, certain paths, like debug-insn and control-use analysis,
  add `INSN_LIST` nodes to `reg_last` without updating `reg_last_in_use`. These nodes
  were then leaked. This patch introduces `reg_last_dirty` to capture these lists
  temporarily and merges them into `reg_last_in_use` before freeing, ensuring all
  lists are returned to the recycler. This prevents potential memory leaks and ensures
  correct dependency analysis,…
primer_glossary:
- term: sched-deps
  definition: A component within the GCC compiler that analyzes and manages dependencies
    between instructions to optimize instruction scheduling.
- term: reg_last
  definition: A data structure within `sched-deps` that likely stores information
    about the last usage of registers.
- term: reg_last_in_use
  definition: A subset of `reg_last` that tracks which entries are currently actively
    in use, helping to manage register lifetimes and dependencies.
- term: INSN_LIST
  definition: A data structure representing a list of instructions, used in `sched-deps`
    for tracking grouped instruction dependencies.
- term: recycler
  definition: A memory management mechanism that reclaims and reuses objects (like
    `INSN_LIST` nodes) instead of deallocating them, improving performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ce720fc2b7e70fe284f5b6159e4088dc6e8844c0
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This commit addresses a memory leak in the sched-deps component where certain lists associated with register usage were not being properly released. Specifically, debug-insn and control-use paths added lists to `reg_last` that were not tracked by `reg_last_in_use`, preventing them from being returned to the recycler. A new `reg_last_dirty` set is introduced to track these lists, and they are now merged into `reg_last_in_use` during teardown to ensure proper deallocation. A selftest is added to verify this fix.
