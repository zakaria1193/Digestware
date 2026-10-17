---
project: gcc
subsystem: genattrtab
patch_id: null
tags:
- optimization
- genattrtab
- build system
- performance
commit_hash: be1fb4e87de02b8c865d0335d01bec3204c68220
source_type: github
author: Kyrylo Tkachov
headline: 'genattrtab: Efficiently build IOR trees for attribute value lists'
tldr: Optimizes the construction of boolean logic trees for attribute values, reducing
  build times for complex configurations.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `check_attr_test` function in `genattrtab.cc` is responsible for
  converting attribute tests like `(eq_attr "type" "a,b,c")` into IOR trees. The previous
  implementation using `insert_right_side` led to O(N^4) complexity for lists of N
  values. This patch directly builds the tree, preserving the first occurrence of
  each value and nesting, resulting in O(N) construction. This is crucial for complex
  scheduling descriptions with long value lists.
primer_glossary:
- term: genattrtab
  definition: A GCC internal tool that generates attribute tables used by various
    backends for instruction selection and scheduling.
- term: IOR tree
  definition: An internal representation of a boolean expression, specifically representing
    the logical OR operation between different conditions or tests.
- term: eq_attr
  definition: An internal GCC construct representing an equality test for a specific
    attribute.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/be1fb4e87de02b8c865d0335d01bec3204c68220
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

This commit refactors `genattrtab`'s `check_attr_test` function to build the disjunctive normal form (IOR tree) for attribute value lists more efficiently. Instead of iteratively adding values to a tree, which previously had a quartic cost, it now directly constructs the tree by keeping unique values and nesting. This significantly speeds up `genattrtab` for targets with long attribute value lists, such as s390x and ARM.
