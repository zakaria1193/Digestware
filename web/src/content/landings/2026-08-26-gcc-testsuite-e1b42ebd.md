---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- vectorization
- cleanup
commit_hash: e1b42ebd80dce9303994bb84a78931c7d9f4c6e2
source_type: github
author: Kyrylo Tkachov
headline: Use x86 effective target for vector MIN tests
tldr: Test suite cleanup consolidates x86 target patterns for vector MIN narrowing
  tests.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `g++.dg/tree-ssa/` test suite includes tests for vector narrowing
  operations. This patch targets `vec-narrow-1.C` and `vec-narrow-minmax-2.C`, which
  verify the compiler's ability to perform MIN/MAX operations on narrowed vector types.
  Previously, these tests used explicit target patterns for both `i?86` and `x86_64`.
  By adopting the `x86_64` effective target, which encompasses both, the test suite
  becomes more concise and easier to maintain, reflecting a suggestion from the bug
  tracking system (Bugzilla).
primer_glossary:
- term: vector narrowing
  definition: An operation where a vector of a larger element type is converted to
    a vector of a smaller element type, often involving truncation or saturation.
    This is common in SIMD operations.
- term: effective target
  definition: A representation of the target architecture and instruction set extensions
    that GCC uses during optimization to determine available features and constraints.
- term: x86
  definition: A family of instruction set architectures (ISAs) commonly used in desktop
    and server processors, including 32-bit (IA-32) and 64-bit (x86-64) variants.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e1b42ebd80dce9303994bb84a78931c7d9f4c6e2
date: '2026-08-26'
is_stub: true
stub_reason: low_score
---

This commit simplifies GCC's test suite by using the generic x86 effective target in vector MIN narrowing tests. Previously, tests for `vec-narrow-1.C` and `vec-narrow-minmax-2.C` explicitly listed both i?86 and x86_64 patterns. This change consolidates them under the x86 effective target, improving test maintainability without altering the configurations tested.
