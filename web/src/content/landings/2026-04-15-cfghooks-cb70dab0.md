---
project: gcc
subsystem: cfghooks
patch_id: null
tags:
- cfghooks
- refactor
- parallelism
commit_hash: cb70dab0e4bfa94e009700086001a5b2dc17ea5d
source_type: github
author: Andrew Pinski
headline: 'Cfghooks: Pass data to callback function of make_forwarder_block.'
tldr: The `make_forwarder_block` callback now receives data directly, reducing global
  variables and improving parallel compilation.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors the `make_forwarder_block` function in `cfghooks.cc`
  to pass data directly to the `redirect_edge_p` callback.  Previously, the callback
  relied on global/static variables like `mfb_reis_set` and `mfb_kj_edge`.  This change
  reduces global state, which is beneficial for parallel compilation efforts.  The
  commit touches `cfgloop.cc`, `cfgloopmanip.cc`, `tree-cfgcleanup.cc`, and `tree-ssa-threadupdate.cc`
  to update calls to `make_forwarder_block`.
primer_general: This commit improves the internal structure of the GCC compiler, specifically
  within the control flow graph (CFG) handling. The CFG represents how the program's
  execution flows. This change makes the code cleaner and easier to manage by passing
  data directly to functions that need it, rather than relying on global variables.
  This can help improve the reliability and performance of the compiler, especially
  when compiling code in parallel.
discussion_id_link: github:gcc-mirror/gcc#123113
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cb70dab0e4bfa94e009700086001a5b2dc17ea5d
date: '2026-04-15'
---

The `make_forwarder_block` function now passes data directly to its callback, rather than relying on global variables.  This reduces the number of global variables, which should help with the Parallel GCC project, and simplifies the interface. The `mfb_keep_just` variable is also no longer shared between files.
