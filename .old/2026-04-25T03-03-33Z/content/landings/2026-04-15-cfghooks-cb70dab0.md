---
project: gcc
subsystem: cfghooks
patch_id: null
tags:
- cfghooks
- refactor
- parallelism
- cfg
commit_hash: cb70dab0e4bfa94e009700086001a5b2dc17ea5d
source_type: github
author: Andrew Pinski
headline: 'Cfghooks: Pass data to callback function of make_forwarder_block'
tldr: Refactors `make_forwarder_block` to pass data to its callback function, reducing
  global variable usage and improving code clarity.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors `make_forwarder_block` in `cfghooks.cc` to pass
  a `void* data` argument to the `redirect_edge_p` callback, replacing the use of
  global variables like `mfb_keep_just`. This simplifies the API and reduces global
  state, which is beneficial for parallel compilation efforts. `cfghooks` provides
  hooks into the control flow graph (CFG) manipulation routines. Interacts with `cfgloopmanip.cc`
  and `tree-ssa-threadupdate.cc`.
primer_general: This commit improves the internal structure of the GCC compiler by
  changing how data is passed between functions that manipulate the control flow graph
  (CFG). The CFG represents the flow of execution in a program. The `make_forwarder_block`
  function is used to create a block of code that forwards execution to another block.  Instead
  of using global variables to communicate data to the callback function, the data
  is now passed directly as an argument, making the code cleaner and easier to understand.
discussion_id_link: github:gcc-mirror/gcc#123113
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cb70dab0e4bfa94e009700086001a5b2dc17ea5d
date: '2026-04-15'
---

The `make_forwarder_block` function now passes data directly to its callback, eliminating the need for global/static variables. This reduces global variable usage, which helps with the Parallel GCC project, and simplifies the interface.  This change was motivated by the need for a new callback function in PR123113.
