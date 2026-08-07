---
project: gcc
subsystem: phiopt/cselim
patch_id: null
tags:
- optimization
- phiopt
- cselim
- conditional store
commit_hash: cd65161b78ececc629183d210b56142c6653c092
source_type: github
author: Andrea Pinski
headline: 'phiopt/cselim: Allow load between conditional store replacement.'
tldr: Enables conditional store replacement even with a load between the store and
  the condition.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In tree-ssa-phiopt.cc, cond_store_replacement_limited now permits a
  load instruction after the conditional store to be replaced. Previously, any load
  after the store would cause the replacement to be rejected. This change allows more
  general conditional stores to be converted into unconditional stores, relying on
  DSE to remove redundant stores, thereby improving optimization effectiveness.
primer_glossary:
- term: phiopt/cselim
  definition: A GCC optimization pass that performs conditional select elimination
    and related optimizations, aiming to simplify code by removing conditional branches
    or stores where possible.
- term: load
  definition: An instruction that reads data from memory into a processor register.
- term: store
  definition: An instruction that writes data from a processor register to memory.
- term: Dead Store Elimination (DSE)
  definition: An optimization pass that removes stores to memory locations whose values
    are never subsequently read.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cd65161b78ececc629183d210b56142c6653c092
date: '2026-08-02'
is_stub: false
stub_reason: ''
---

This commit enhances the `cond_store_replacement_limited` pass in GCC's `phiopt/cselim` optimization. It now allows a load instruction to exist between a conditional store and the condition that guards it. Previously, such loads were rejected, preventing the optimization. The change enables more aggressive conditional store elimination, potentially reducing code size by replacing conditional stores with unconditional ones, with Dead Store Elimination (DSE) handling further cleanup.
