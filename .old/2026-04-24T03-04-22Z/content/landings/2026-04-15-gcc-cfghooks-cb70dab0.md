---
project: gcc
subsystem: gcc/cfghooks
patch_id: null
tags:
- refactor
- cfg
- parallel gcc
commit_hash: cb70dab0e4bfa94e009700086001a5b2dc17ea5d
source_type: github
author: Andrew Pinski
headline: 'Cfghooks: Pass data to callback function of make_forwarder_block'
tldr: Reduces global variables by passing data directly to the callback function in
  `make_forwarder_block`.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `cfghooks.cc`, `cfghooks.h`, `cfgloop.cc`, `cfgloopmanip.cc`,
  `cfgloopmanip.h`, `tree-cfgcleanup.cc`, and `tree-ssa-threadupdate.cc` to pass data
  directly to the `redirect_edge_p` callback within `make_forwarder_block`.  This
  eliminates the need for global/static variables, simplifying the code and reducing
  dependencies.  It touches the CFG loop manipulation code.
primer_general: This commit improves the internal structure of GCC's control flow
  graph (CFG) manipulation code. Specifically, it changes how data is passed to callback
  functions used when creating 'forwarder blocks' within the CFG. Instead of using
  global variables, the data is now passed directly as an argument. This makes the
  code cleaner and easier to maintain, and it also helps with the ongoing effort to
  parallelize GCC's compilation process.
discussion_id_link: github:gcc-mirror/gcc#123113
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cb70dab0e4bfa94e009700086001a5b2dc17ea5d
date: '2026-04-15'
---

This commit refactors the `make_forwarder_block` function to pass data directly to its callback, instead of relying on global variables. This reduces the number of global variables, which is beneficial for the Parallel GCC project, and simplifies code by reducing dependencies between files.
