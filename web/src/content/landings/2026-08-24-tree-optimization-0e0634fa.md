---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- bugfix
commit_hash: 0e0634fa16871672beef1187da0d43cb10dd3182
source_type: github
author: Richard Biener
headline: SLP scheduling respects trapping statements
tldr: SLP vectorization now correctly handles statements that might trap, preventing
  incorrect scheduling and ICEs.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `vect_schedule_slp_node` function in `tree-vect-slp.cc` has been
  updated to maintain scheduling when the target schedule point is dominated by a
  trapping statement. This addresses a bug (PR126995) where SLP scheduling could lead
  to an ICE by incorrectly reordering instructions around statements that might raise
  exceptions.
primer_glossary:
- term: SLP
  definition: Superword-Level Parallelism, a compiler optimization technique that
    identifies and vectorizes consecutive instructions with identical operations on
    different data elements.
- term: ICE
  definition: Internal Compiler Error, a fatal error encountered by the compiler during
    translation, typically indicating a bug in the compiler itself.
- term: vectorization
  definition: An optimization process that transforms code to operate on multiple
    data elements simultaneously using special CPU instructions (SIMD), often improving
    performance for data-parallel tasks.
- term: trapping statement
  definition: A statement or instruction that, if executed, may cause an exception
    or trap, interrupting normal program flow. Examples include division by zero or
    accessing invalid memory.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0e0634fa16871672beef1187da0d43cb10dd3182
date: '2026-08-24'
is_stub: false
stub_reason: ''
---

The SLP (Superword-Level Parallelism) scheduler in GCC now correctly respects constraints imposed by potentially trapping statements. This prevents SLP from scheduling instructions after a trapping statement if that statement dominates the schedule point, fixing an ICE and improving the robustness of vectorization.
