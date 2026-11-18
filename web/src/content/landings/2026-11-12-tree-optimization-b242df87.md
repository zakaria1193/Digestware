---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- correctness
- floating-point
commit_hash: b242df8741d2328e7fb2b8216dd96ad03b91c8b1
source_type: github
author: Kyrylo Tkachov
headline: GCC loop unswitching avoids trapping conditions
tldr: GCC's loop unswitching pass now avoids hoisting conditions that may trap (e.g.,
  floating-point exceptions) unless they are in the loop header.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refines the loop unswitching pass in `tree-ssa-loop-unswitch.cc`.
  The `find_unswitching_predicates_for_bb` function is updated to identify and reject
  loop-invariant conditions that carry a risk of trapping (e.g., due to `-ftrapping-math`).
  Such conditions are only safe to hoist if they reside within the loop's header,
  as this guarantees they are evaluated only once upon loop entry. Hoisting non-header
  trapping conditions can lead to unexpected exceptions. The patch also prevents unswitching
  outer loops based on trapping conditions within inner loops, ensuring that the trap
  behavio…
primer_glossary:
- term: loop unswitching
  definition: A GCC optimization that duplicates a loop and removes the loop-invariant
    condition from one copy, effectively evaluating the condition once before the
    loop starts.
- term: trapping conditions
  definition: Conditions or operations that, when evaluated, can cause a hardware
    exception or signal (trap) to be raised. Examples include floating-point exceptions
    or division by zero.
- term: -ftrapping-math
  definition: A GCC compiler flag that enables IEEE 754 standard behavior for floating-point
    operations, including raising exceptions on exceptional conditions like NaN or
    infinity.
- term: loop header
  definition: The basic block at the entry of a loop that contains the loop-controlling
    condition and branches.
- term: floating-point exceptions
  definition: Hardware-detected events that occur during floating-point arithmetic
    operations, such as overflow, underflow, or invalid operations (e.g., 0/0).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b242df8741d2328e7fb2b8216dd96ad03b91c8b1
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

GCC's loop unswitching optimization pass has been improved to prevent incorrect behavior with trapping conditions, such as floating-point operations that might raise exceptions. Previously, the pass could hoist such conditions outside the loop, causing exceptions on paths where the original code would not have evaluated them. The optimization now rejects conditions that may trap unless they are part of the loop's header. This ensures that trapping behavior aligns with the original code's execution, particularly for floating-point arithmetic with `-ftrapping-math` enabled.
