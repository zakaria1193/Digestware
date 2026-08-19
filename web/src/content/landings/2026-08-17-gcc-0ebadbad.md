---
project: gcc
subsystem: gcc
patch_id: null
tags:
- optimization
- path analysis
- compiler
commit_hash: 0ebadbad7c92133c467f7aed6f3c16a9e3b55774
source_type: github
author: Aldy Hernandez
headline: 'Path solver: Compute ranges only at current path position'
tldr: Fixes a path solver issue by restricting range computations to the current block
  in the control flow graph.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gimple-range-path.cc` changes restrict `path_range_query::internal_range_of_expr`
  to call `range_defined_in_block` only at the current path position (`m_path[m_pos]`).
  This resolves issues where optimizations like `match.pd` could query ranges with
  contexts from unrelated blocks, violating the positional invariant. An assertion
  is added in `range_defined_in_block` to enforce this invariant, ensuring positional
  correctness.
primer_glossary:
- term: Path Solver
  definition: A component within the compiler's optimization passes that analyzes
    different execution paths (control flow) through a program to determine properties
    of variables or expressions along those paths.
- term: Control Flow Graph (CFG)
  definition: A representation of all execution paths through a function or program.
    It consists of basic blocks (sequences of code with one entry and one exit) and
    edges representing possible transfers of control between blocks.
- term: GIMPLE
  definition: GCC's internal representation (IR) used for optimization after the initial
    parsing and before the final machine code generation. It's a three-address code
    form.
- term: SSA
  definition: Static Single Assignment. An intermediate representation property where
    every variable is assigned a value exactly once. This simplifies many compiler
    optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0ebadbad7c92133c467f7aed6f3c16a9e3b55774
date: '2026-08-17'
is_stub: false
stub_reason: ''
---

This commit corrects the path solver's range computation logic to only consider the current block's position in the control flow graph. Previously, range queries could occur with contexts from arbitrary blocks, leading to incorrect results when folding statements. The fix ensures that range calculations are confined to the relevant path position, falling back to global ranges otherwise, and adds an assertion to maintain this invariant.
