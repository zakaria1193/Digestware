---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- loop optimization
- shifts
- ARM
commit_hash: 58bf8a355a73b7fbc6d7bfebcc7281b3cdadd4da
source_type: github
author: Dominic P
headline: Hoist shifts by in-range constants out of loops
tldr: Improves loop optimization by hoisting shifts with constant counts that are
  provably in range.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'The `movement_possibility_1` logic in GCC''s loop invariant code motion
  pass was inverted regarding shifts and rotates. It used `wi::ltu_p(count, precision)`
  to check if the shift count was within the valid range. The original code restricted
  shifts when `count < precision` (i.e., in-range) to `MOVE_PRESERVE_EXECUTION`, while
  out-of-range shifts (`count >= precision`) were incorrectly marked `MOVE_POSSIBLE`.
  This was due to a misunderstanding of the `PR111000` fix which aimed to prevent
  hoisting of *undefined* shifts (out-of-range counts). This commit corrects the condition:
  shifts with in-ran…'
primer_glossary:
- term: loop optimization
  definition: Compiler techniques to improve the performance of code within loops,
    such as reducing redundant computations or reordering operations.
- term: hoisting
  definition: Moving a computation from inside a loop to outside the loop, if the
    result of the computation is the same on every iteration.
- term: shift operation
  definition: A bitwise operation that shifts the bits of a number to the left or
    right.
- term: constant count
  definition: In a shift operation, the number of positions to shift is a fixed value
    known at compile time.
- term: loop invariant code motion
  definition: An optimization that moves computations that produce the same result
    in every loop iteration from inside the loop to outside.
- term: libcall
  definition: A call to a function in a shared or static library, often used when
    the compiler cannot generate inline code for an operation.
- term: register pressure
  definition: A measure of how many registers are needed by the program at a given
    point; high register pressure can lead to performance degradation as the compiler
    must spill values to memory.
discussion_id_link: null
bugzilla_pr: null
series_id: 'gcc:tree-optimization: hoist shifts by an in-range constant count'
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/58bf8a355a73b7fbc6d7bfebcc7281b3cdadd4da
date: '2026-08-23'
is_stub: false
stub_reason: ''
---

This commit corrects a bug in loop optimization where shifts with constant counts were incorrectly restricted from being hoisted out of loops. The `movement_possibility_1` logic mistakenly pinned shifts with in-range counts, while shifts with out-of-range counts were incorrectly marked as movable. The fix inverts this logic, allowing shifts with constant counts that are proven to be in range to be hoisted. This can lead to performance improvements by reducing redundant computations within loop bodies, as demonstrated by reductions in loop-invariant code and register pressure on ARM targets.
