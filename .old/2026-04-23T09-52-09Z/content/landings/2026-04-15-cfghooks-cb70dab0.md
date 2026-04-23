---
project: gcc
subsystem: cfghooks
patch_id: null
tags:
- cfghooks
- refactoring
- code cleanup
- parallelization
commit_hash: cb70dab0e4bfa94e009700086001a5b2dc17ea5d
source_type: github
author: Andrew Pinski
headline: 'Cfghooks: Pass data to callback function of make_forwarder_block'
tldr: This commit refactors the `make_forwarder_block` function to pass data to its
  callback, reducing global variables and improving code maintainability.
why_it_matters: Reduces reliance on global/static variables, improving code reusability
  and making the compiler more amenable to parallelization.
impact_score: 6
impact_rationale: Refactors code to reduce global variables, improving modularity
  and potential for parallelization.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `make_forwarder_block` function is used to create basic blocks
  that forward control flow. Previously, global variables like `mfb_keep_just` were
  used to communicate data to the callback function. This commit replaces that pattern
  by directly passing a `void*` data argument, facilitating more flexible and maintainable
  code. This affects files like `cfgloopmanip.cc` and `tree-ssa-threadupdate.cc`.
primer_general: In GCC, control flow graph (CFG) hooks allow modification of the program's
  structure during compilation. This commit refactors a function responsible for creating
  'forwarder blocks' in the CFG. Instead of relying on global variables to pass data
  to a callback function, the data is now passed directly as an argument. This makes
  the code cleaner, easier to understand, and prepares GCC for potential parallel
  compilation efforts.
discussion_id_link: github:gcc-mirror/gcc#123113
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cb70dab0e4bfa94e009700086001a5b2dc17ea5d
date: '2026-04-15'
---

The `make_forwarder_block` function in `cfghooks.cc` is updated to accept a data argument which is then passed to the `redirect_edge_p` callback. This change eliminates the need for global/static variables that were previously used to share data with the callback function. Consequently, this refactoring reduces the number of global variables and improves code modularity.
