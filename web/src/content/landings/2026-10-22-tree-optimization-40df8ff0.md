---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- debugging
- CRC
- loop optimization
commit_hash: 40df8ff06970e783b424299be509115b574d9f13
source_type: github
author: Yongqiang Tian
headline: 'tree-optimization: Preserve debug correctness in CRC loop replacement [PR127716]'
tldr: Ensures debug information remains correct when optimizing CRC loops.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch addresses PR127716 by ensuring debug correctness during
  CRC loop replacement. The `crc_symbolic_execution::is_used_outside_the_loop` function
  now ignores debug statements, preventing them from interfering with loop recognition.
  More importantly, `crc_optimization::optimize_crc_loop` now calls `reset_debug_uses_outside_loop`
  before replacing the loop. This function, factored from `vect_do_peeling`, resets
  outside-loop debug binds that use SSA values originating from within the loop. This
  prevents the debugger from displaying stale values after the loop transformation.
  Debug binds wi…
primer_glossary:
- term: CRC loop
  definition: A loop in the code that repeatedly calculates a Cyclic Redundancy Check
    (CRC) on a sequence of data.
- term: debug bind
  definition: A statement or mechanism that associates a debugger variable name with
    a specific program variable or memory location, allowing a developer to inspect
    its value during a debugging session.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation where
    every variable is assigned exactly once, simplifying many optimization passes.
- term: vectorizer
  definition: A compiler component that attempts to replace scalar operations with
    equivalent vector (SIMD) operations, potentially improving performance on suitable
    hardware.
- term: peeling
  definition: A loop transformation technique where one or more iterations of a loop
    are extracted and executed separately before or after the main loop body, often
    to simplify loop control or enable vectorization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/40df8ff06970e783b424299be509115b574d9f13
date: '2026-10-22'
is_stub: false
stub_reason: ''
---

This commit preserves debug information correctness when optimizing loops that perform CRC (Cyclic Redundancy Check) calculations. Previously, debug statements referencing variables within the loop could lead to incorrect values being displayed by debuggers after loop transformation. The fix ignores debug statements when identifying loop-internal definitions used outside the loop and, crucially, resets any outside-loop debug binds that refer to values defined inside the loop before loop replacement. This ensures that debuggers show the correct state, even after the loop is optimized or vectorized.
