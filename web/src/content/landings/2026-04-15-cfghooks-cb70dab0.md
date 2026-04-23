---
project: gcc
subsystem: cfghooks
patch_id: null
tags:
- cfg
- refactor
- parallelism
commit_hash: cb70dab0e4bfa94e009700086001a5b2dc17ea5d
source_type: github
author: Andrew Pinski
headline: 'Cfghooks: Pass data to callback function of make_forwarder_block'
tldr: The data argument is now passed to the callback function of 'make_forwarder_block',
  which removes global variables and simplifies the code.
why_it_matters: Reducing reliance on global variables makes the code more thread-safe
  and easier to reason about, which is important for projects like Parallel GCC.
impact_score: 5
impact_rationale: Refactoring to remove global variables and improve code maintainability.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The patch modifies `cfghooks.cc`, `cfghooks.h`, `cfgloop.cc`, `cfgloopmanip.cc`,
  `cfgloopmanip.h`, `tree-cfgcleanup.cc`, and `tree-ssa-threadupdate.cc`. The `make_forwarder_block`
  function signature is updated to include a `void* data` argument, which is then
  passed to the `redirect_edge_p` callback. This eliminates the need for the global
  variables `mfb_reis_set` and `mfb_kj_edge`.
primer_general: Control flow graph (CFG) hooks allow GCC to insert custom actions
  during the compilation process, particularly during control flow graph construction
  and manipulation. The control flow graph represents how execution flows through
  a program. This commit improves the design of a callback mechanism related to these
  hooks by passing data directly to the callback function, avoiding the use of global
  variables. This makes the system more flexible and easier to maintain, and prepares
  the ground for parallel compilation.
discussion_id_link: github:gcc-mirror/gcc#123113
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cb70dab0e4bfa94e009700086001a5b2dc17ea5d
date: '2026-04-15'
---

This commit refactors the `make_forwarder_block` function in `cfghooks.cc` to pass data directly to its callback function, `redirect_edge_p`, rather than using global/static variables. This change reduces the number of global variables, which should benefit the Parallel GCC project. It also simplifies the code and makes it easier to maintain.
