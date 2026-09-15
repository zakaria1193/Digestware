---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler bug
- aarch64
commit_hash: b3527d9b213fcbe2f4550709d25220ab6ba43184
source_type: github
author: Dominic P
headline: 'match.pd: Restrict range test to scalars [PR127379]'
tldr: Fixes a bug where vector types were incorrectly processed by a scalar range
  test, preventing potential regressions.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `ior_range_test_0` pattern in `match.pd` previously lacked a constant
  operand check, allowing vector types to reach it. The `X | -X` expression, when
  applied to vectors, resulted in a scalar comparison being promoted to a vector type.
  This commit restricts the pattern to `INTEGER_CST` operands, mirroring other scalar-focused
  matchers in the range-test patterns and addressing PR127379.
primer_glossary:
- term: match.pd
  definition: A file within GCC that defines patterns used for instruction matching
    and optimization.
- term: scalar
  definition: A data type representing a single value, as opposed to an array or structure.
- term: vector type
  definition: A data type that holds multiple values of the same base type, typically
    processed in parallel by a single instruction.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b3527d9b213fcbe2f4550709d25220ab6ba43184
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

A pattern in `match.pd` used for range tests, `X | -X`, was incorrectly applied to vector types. This led to a scalar comparison being converted to a vector type, potentially causing issues. The fix restricts this pattern to integral types, aligning with other scalar-only matchers and preventing regressions. A new test case has been added to verify the fix.
