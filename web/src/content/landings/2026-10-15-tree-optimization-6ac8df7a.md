---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- vectorization
commit_hash: 6ac8df7a4992dc7c5eec1217808bea31c085ec74
source_type: github
author: Kyrylo Tkachov
headline: Correct unsigned saturation add pattern for overflow type
tldr: Fixes incorrect saturation results for unsigned additions by checking the type
  of the overflow result.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `unsigned_integer_sat_add` forms in `match-sat-alu.pd`, particularly
  those selecting a separate `X + Y` and using `.ADD_OVERFLOW`, did not verify the
  type of the overflow result. The overflow flag can describe a different type than
  `X + Y`, causing incorrect saturation if the compiler selects the wrong type. This
  commit adds a check to ensure the `.ADD_OVERFLOW` result parts have the same type
  as the `X + Y` operation, resolving issues seen with the vectorizer and general
  incorrect saturations.
primer_glossary:
- term: unsigned saturating add
  definition: An arithmetic operation that adds two unsigned numbers. If the result
    exceeds the maximum representable value for the type, it is clamped to the maximum;
    if it falls below the minimum, it is clamped to the minimum. This is also known
    as saturation arithmetic.
- term: .ADD_OVERFLOW
  definition: A pattern in GCC's intermediate representation that computes an addition
    and an overflow flag simultaneously. It's often used as a building block for saturation
    arithmetic.
- term: vectorizer
  definition: A compiler component that transforms code to use SIMD (Single Instruction,
    Multiple Data) instructions, allowing a single operation to be performed on multiple
    data elements simultaneously for performance gains.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6ac8df7a4992dc7c5eec1217808bea31c085ec74
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

This commit corrects a bug in the unsigned saturating add (`SAT_U_ADD`) pattern within `match-sat-alu.pd`. Previously, when the `.ADD_OVERFLOW` sub-pattern was used to determine saturation, the type of its overflow flag was not checked against the expected result type. This led to incorrect saturation values, particularly when using vector types or when the overflow result type differed from the addition's type. The fix ensures that the `.ADD_OVERFLOW` result's type matches the addition's type, preventing incorrect saturation.
