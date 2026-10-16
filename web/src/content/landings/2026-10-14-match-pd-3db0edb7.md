---
project: gcc
subsystem: match.pd
patch_id: null
tags:
- vectorization
- optimization
- gcc
commit_hash: 3db0edb7331f01233dc3b4d1e32b094c7b4ba678
source_type: github
author: Igor Shevlyakov
headline: 'match.pd: Fix mode queries for VEC_PERM merge with view-convert'
tldr: Improves vector permute instruction generation when view-conversions are involved.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `match.pd` pattern for merging `VEC_PERM_EXPR` instances, particularly
  when one is nested within a `VIEW_CONVERT_EXPR`, was incorrectly querying modes.
  It used the output mode for the inner permute and the input mode for the outer.
  This commit corrects the queries to use the modes of the original operands (`a`
  and `b`) for the inner permute and the intermediate type (`c`) for the outer, resolving
  failures when element types differ due to view conversion and preventing performance
  degradation.
primer_glossary:
- term: VEC_PERM_EXPR
  definition: A GCC intermediate representation (tree) representing a vector permute
    operation, which rearranges elements within vectors.
- term: view-convert
  definition: A GCC operation that casts a vector to a different type without changing
    the underlying data, effectively changing the interpretation of its elements.
- term: match.pd
  definition: A file within GCC's middle-end that contains patterns used for matching
    and optimizing code, particularly for vector operations.
- term: vector lowering
  definition: The process in GCC where high-level vector operations are transformed
    into target-specific machine instructions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3db0edb7331f01233dc3b4d1e32b094c7b4ba678
date: '2026-10-14'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in `match.pd` where merging vector permute operations (`VEC_PERM_EXPR`) through view conversions was causing incorrect mode queries. Previously, when a conversion changed the element type (e.g., from `short` to `_Float16`), the pattern incorrectly assumed it could handle the permute, leading to suboptimal code generation. The fix ensures that each permute is queried with its correct modes, preventing unnecessary expansion and instruction bloat.
