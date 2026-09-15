---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- optimization
- SSA
- bugfix
commit_hash: 492fbdbf99dc9d8c4f13d8afe654f36d47811a2f
source_type: github
author: Richard Biener
headline: tree-optimization/127377 - Wrong pruning of non-constant partial defs
tldr: Fixes a bug in SSA SCCVN optimization where sub-byte padding was not correctly
  handled.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `tree-ssa-sccvn.cc` pass uses value numbering within strongly connected
  components to optimize SSA. This commit fixes a bug in `vn_walk_cb_data::push_partial_def`
  where the size pruning logic did not correctly account for sub-byte padding *before*
  the partial definition was created. This could lead to incorrect size calculations
  and value numberings for subsequent operations. The fix adjusts the size calculation
  to include this preceding padding, ensuring correct pruning and value propagation.
primer_glossary:
- term: SSA
  definition: Static Single Assignment form, an intermediate representation used in
    compilers where every variable is assigned a value only once.
- term: SCCVN
  definition: Strongly Connected Components for Value Numbering. A compiler optimization
    pass that identifies redundant computations within loops or cyclic code structures.
- term: partial definition
  definition: In SSA, a definition that only assigns a part of a larger value (e.g.,
    a sub-byte field within a larger integer).
- term: pruning
  definition: The process of reducing the size or scope of a variable or definition
    when its full range is not needed.
- term: sub-byte padding
  definition: Extra bits or bytes added within a larger data type to align a field
    or meet alignment requirements, where the padding itself is smaller than a byte.
- term: PR tree-optimization/127377
  definition: A specific bug report filed against the GCC tree-optimization component,
    tracking this particular issue.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/492fbdbf99dc9d8c4f13d8afe654f36d47811a2f
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

This commit addresses a bug in GCC's SSA SCCVN (Strongly Connected Components for Value Numbering) optimization pass, identified by PR tree-optimization/127377. The issue involved incorrect pruning of non-constant partial definitions. Specifically, the optimization failed to adjust for sub-byte padding before an object when pruning its size after the object. The fix ensures that the padding is properly considered, preventing incorrect value numberings and ensuring accurate optimization.
