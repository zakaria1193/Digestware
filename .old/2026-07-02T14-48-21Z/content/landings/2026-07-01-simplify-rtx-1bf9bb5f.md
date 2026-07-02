---
project: gcc
subsystem: simplify-rtx
patch_id: null
tags:
- optimization
- vectorization
- x86
commit_hash: 1bf9bb5f1c5bdaf8f96c64fbf2a081aaaa2b9b2f
source_type: github
author: Roger Sayle
headline: 'simplify-rtx: Simplify vec_merge with repeated operands.'
tldr: Optimization simplifies vector merge operations involving repeated operands,
  potentially improving code generation efficiency.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `simplify-rtx.cc` pass now canonicalizes `(vec_merge (vec_merge
  a b m) a n)` into `(vec_merge a b (m|~n))` for V4SI and similar SIMD types. This
  handles cases where the second operand of a `vec_merge` is itself a `vec_merge`
  whose first operand is identical to the first operand of the outer `vec_merge`.
  The analysis leverages the fact that `(vec_merge a b m)` is equivalent to `(vec_merge
  b a ~m)` and that two such operations can be combined. This is particularly relevant
  for x86_64 AVX2 code generation involving vector element updates.
primer_general: This commit enhances the GCC compiler's ability to optimize code that
  manipulates data stored in vectors, which are like arrays that the CPU can process
  in parallel. Specifically, it improves how the compiler handles a common operation
  called 'vector merge.' When code modifies multiple elements within a vector, especially
  if it modifies them with the same value, the compiler can now recognize a pattern
  where two sequential merge operations can be combined into a single, more efficient
  one. This optimization happens at an internal representation stage of the compiler
  (RTL) and can lead to simpler, faster machine code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1bf9bb5f1c5bdaf8f96c64fbf2a081aaaa2b9b2f
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

GCC's RTL (Register Transfer Language) optimizer now simplifies vector merge operations where one of the operands is a duplicated value and appears multiple times. This optimization addresses complex vector manipulation patterns that could arise from code modifying elements of a vector. By recognizing that merging a vector with itself, followed by another merge involving the same initial value, can be consolidated, the compiler can generate more efficient instructions.
