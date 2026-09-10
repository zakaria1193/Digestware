---
project: gcc
subsystem: tree-ssa-loop-im
patch_id: null
tags:
- optimization
- exception handling
commit_hash: 41596ef9be648c8488165c95be1aacb228ad6750
source_type: github
author: Kyrylo Tkachov
headline: 'tree-ssa-loop-im: Reject trapping store motion with non-call EH'
tldr: Disallows moving stores out of loops when non-call exceptions are enabled to
  prevent incorrect behavior.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-loop-im.cc` pass handles loop-invariant memory motion.
  The `can_sm_ref_p` function, which determines if a store motion reference is safe,
  previously did not adequately consider exception-throwing behavior. This commit
  corrects `can_sm_ref_p` to reject trapping stores when `tree_could_throw_p` indicates
  non-call exceptions are possible, ensuring EH correctness for loop transformations.
primer_glossary:
- term: LIM
  definition: Loop Invariant Motion, a compiler optimization that moves loop-independent
    computations outside a loop to reduce redundant work.
- term: EH
  definition: Exception Handling, the mechanism used by a program to handle runtime
    errors or exceptional conditions.
- term: tree-ssa
  definition: Static Single Assignment form, an intermediate representation used by
    GCC that makes many optimizations easier to implement by ensuring each variable
    is assigned only once.
- term: trap
  definition: An event where a program instruction causes an immediate, synchronous
    interruption due to an error, such as division by zero or accessing invalid memory.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/41596ef9be648c8488165c95be1aacb228ad6750
date: '2026-09-03'
is_stub: false
stub_reason: ''
---

The loop invariant motion (LIM) pass in GCC incorrectly handled exception information when moving stores out of loops. Previously, it treated bare memory references as loads, and a safe load didn't prove a store to the same address couldn't trap. This change ensures that trapping stores are rejected when exception handling is enabled and non-call exceptions can be thrown, preventing potential runtime errors. A new test case verifies this behavior.
