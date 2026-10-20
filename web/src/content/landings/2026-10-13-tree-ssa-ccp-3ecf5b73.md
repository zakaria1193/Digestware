---
project: gcc
subsystem: tree-ssa-ccp
patch_id: null
tags:
- optimization
- performance
commit_hash: 3ecf5b73c7f1104441dee2d591e1cb47785f3fa7
source_type: github
author: linden
headline: 'tree-ssa-ccp: avoid copying lattice values and shift counts'
tldr: Pass lattice values and shift counts by const reference to reduce copying.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit optimizes parameter passing in two functions within the
  Constant Propagation (CCP) pass. `valid_lattice_transition` now accepts its lattice
  value arguments (`ccp_prop_value_t`) by const reference to avoid copying these structures.
  `bit_value_binop` similarly avoids an unnecessary copy of a `widest_int` used as
  a shift count in one of its cases, directly using the parameter `r2val`.
primer_glossary:
- term: CCP
  definition: Abbreviation for Constant Propagation. A compiler optimization pass
    that determines which variables hold constant values and replaces their uses with
    those constants.
- term: lattice values
  definition: In dataflow analysis, lattice values represent the possible states or
    values a variable can hold at a particular point in the program. These can be
    complex structures used to track information across basic blocks.
- term: widest_int
  definition: An arbitrary-precision integer type used in GCC for representing values
    that exceed the standard machine integer types. It is crucial for intermediate
    calculations in various optimization passes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3ecf5b73c7f1104441dee2d591e1cb47785f3fa7
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

The valid_lattice_transition function in tree-ssa-ccp.cc now takes its lattice value arguments by const reference, avoiding unnecessary copies of potentially large data structures. Additionally, the bit_value_binop function avoids copying a shift count when it's not modified, directly using the input value instead. These changes improve efficiency without altering the compiler's behavior.
