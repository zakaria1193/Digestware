---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- analysis
commit_hash: 62214130b61f48cf7cdb37c69bb14c22aea6c65a
source_type: github
author: Andrew MacLeod
headline: Create relation immediately in value relation search
tldr: Improves value relation analysis by creating relations upfront and then computing
  ranges.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `dom_oracle::search_and_merge_relation` in `value-relation.cc`,
  the relation object is now created unconditionally at the start of the function.
  Previously, it was created conditionally. This change ensures that a relation object
  always exists, allowing for immediate range calculation and intersection, which
  may simplify the logic and potentially improve performance or correctness for certain
  relation merging scenarios.
primer_glossary:
- term: value relation
  definition: A compiler analysis that tracks relationships between values of variables.
    It's used to determine properties like whether one value is always greater than,
    equal to, or within a certain range of another.
- term: relation
  definition: In the context of value relation analysis, a data structure representing
    a specific relationship (e.g., inequality, range) between program variables or
    expressions.
- term: range
  definition: A set of possible values that a variable or expression can take. In
    compiler analysis, ranges are often used to infer properties about program execution.
- term: tree-optimization
  definition: A phase in the GCC compiler that operates on an intermediate representation
    (IR) called GENERIC/GIMPLE trees. It performs various optimizations by analyzing
    and transforming these tree structures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/62214130b61f48cf7cdb37c69bb14c22aea6c65a
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

This change modifies the value relation search to create a new relation immediately, rather than deferring it. After creation, any known range is calculated and intersected with the result. This adjustment aims to improve the efficiency and correctness of the value relation analysis by establishing the relation's context earlier in the process.
