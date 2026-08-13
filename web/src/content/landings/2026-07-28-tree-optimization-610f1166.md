---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- integer overflow
- pattern matching
commit_hash: 610f1166538ad2e637c913be78b074100270cc5c
source_type: github
author: Andrea Pinski
headline: 'match: Fix signed integer overflow in pattern for `cmp + (-cmp ^ x)`'
tldr: Corrects a GCC pattern that introduced unintended signed integer overflow with
  INT_MIN.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `match.pd` file contains patterns for optimizations. A recent pattern
  for `(A ^ -cmp) + cmp` was intended to simplify expressions but introduced a signed
  integer overflow when `x` was `INT_MIN` and `cmp` was 0 (the expression `0 + (-0
  ^ INT_MIN)` would overflow). This commit corrects the pattern by casting to an unsigned
  type before negating, preventing the overflow and aligning with PR tree-optimization/126418.
primer_glossary:
- term: Pattern matching
  definition: A technique used by compilers to recognize specific sequences of operations
    or data structures (patterns) in the intermediate representation, which can then
    be transformed into more efficient code.
- term: Signed integer overflow
  definition: Occurs when the result of an arithmetic operation on signed integers
    is outside the range that can be represented by the data type. In C and C++, this
    results in undefined behavior.
- term: INT_MIN
  definition: The smallest representable value for a signed integer type (e.g., -2147483648
    for a 32-bit int).
- term: Intermediate Representation (IR)
  definition: A data structure or code format used internally by a compiler to represent
    the program being compiled, between the source code and the target machine code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/610f1166538ad2e637c913be78b074100270cc5c
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

A recent addition to GCC's pattern matching system inadvertently introduced signed integer overflow for specific inputs, particularly when dealing with `INT_MIN`. The pattern `cmp + (-cmp ^ x)` was incorrectly translated, causing overflow when `x` was `INT_MIN` and `cmp` was 0. This commit fixes the issue by using an unsigned type for the negation, preventing the overflow.
