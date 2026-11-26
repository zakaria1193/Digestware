---
project: gcc
subsystem: internal-fn
patch_id: null
tags:
- internal-fn
- clmul
- optimization
commit_hash: 1ebf5b5172007fe281e257df2cf1dc20f777e816
source_type: github
author: Jakub Jelinek
headline: 'internal-fn: Fix up __builtin_clmulg optimization'
tldr: Optimize __builtin_clmulg for constant counts by unrolling loops.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `expand_clmul` function in `internal-fn.cc` handles `__builtin_clmulg`.
  The previous implementation used a `do-while` loop that was incorrect for compile-time
  constants `cnt = 1` and `cnt = 2`. For `cnt == 1`, the intended operation `x <<
  N` was obscured by the loop. For `cnt == 2`, the loop performed `r ^= r << i; i
  = i + i;` which should result in `(x ^ (x << 1)) << N`. This patch corrects this
  by special-casing `cnt == 1` to emit `res << tz` directly, and for `cnt == 2`, it
  explicitly generates `(x ^ (x << 1)) << tz`. This avoids the need for RTL cleanup
  in these simple cases.
primer_glossary:
- term: __builtin_clmulg
  definition: A GCC intrinsic function that performs a carry-less multiplication,
    often used in cryptographic algorithms. It takes two arguments and a count parameter.
- term: RTL (Register Transfer Language)
  definition: An intermediate representation used within GCC to describe machine instructions
    before they are translated into final assembly code.
- term: unroll the loop
  definition: A compiler optimization technique where the body of a loop is duplicated
    one or more times to reduce loop overhead and potentially expose more instruction-level
    parallelism.
- term: compile-time constant
  definition: A value known at compile time, as opposed to a value determined at runtime.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1ebf5b5172007fe281e257df2cf1dc20f777e816
date: '2026-11-26'
is_stub: false
stub_reason: ''
---

This commit refines the optimization for the `__builtin_clmulg` intrinsic function within GCC. The original implementation of the fallback logic for `__builtin_clmulg` involved a loop that was not correctly handled when the `cnt` (count) parameter was a compile-time constant of 1 or 2. For `cnt == 1`, the function should simply perform a left shift. For `cnt == 2`, the loop performs one iteration. This patch corrects the implementation by directly emitting the shift for `cnt == 1` and manually unrolling the loop for `cnt == 2`. This avoids generating unnecessary RTL (Register Transfer Language) code and simplifies the emitted instructions, leading to cleaner and potentially more efficient code.
