---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler
commit_hash: 097cd0ceee61aa4b5100931341e9c8642f060c0a
source_type: github
author: Kyrylo Tkachov
headline: Tighten matching for unsigned narrow clip patterns.
tldr: Refines pattern matching for unsigned integer narrow clips to correctly handle
  signed comparisons and unsigned right shifts.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Tightens the `unsigned_integer_narrow_clip` pattern in `match-sat-alu.pd`.
  It now explicitly requires the comparison operand to be unsigned and the right shift
  operand to be signed. This addresses cases where `nop_convert?` might not enforce
  an unsigned conversion and where signed comparisons could lead to negative inputs
  or where an unsigned right shift would yield `0` or `1` instead of the expected
  clip value.
primer_glossary:
- term: pattern matching
  definition: In compilers, a technique used in optimization passes to recognize specific
    code structures (patterns) in the intermediate representation and replace them
    with more efficient equivalents.
- term: unsigned integer narrow clip
  definition: An operation that takes a wider unsigned integer and converts it to
    a narrower unsigned integer, clamping the value to the maximum of the narrower
    type if it exceeds that limit.
- term: intermediate representation
  definition: A data structure or code format used internally by a compiler to represent
    the source code during various stages of translation. Examples include Gimple
    and RTL in GCC.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/097cd0ceee61aa4b5100931341e9c8642f060c0a
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This commit improves the `unsigned_integer_narrow_clip` pattern matching by requiring the comparison to be unsigned and the right shift to be signed. Previously, the pattern incorrectly assumed these conditions, potentially leading to incorrect transformations when a signed comparison preserved negative inputs or an unsigned right shift produced an incorrect result. The change captures both expressions and checks their result types before applying the transform, with new tests covering rejected forms.
