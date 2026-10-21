---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- ICE
- bug fix
commit_hash: 04f26dfb261677b094602f3d6428de183ddebc5b
source_type: github
author: Richard Biener
headline: Insert live lane extracts at region boundary to prevent ICEs
tldr: Fixes an issue where live lane extracts were inserted incorrectly, causing ICEs,
  by ensuring they are placed at region boundaries.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `vectorizable_live_operation` in `tree-vect-loop.cc`
  to ensure that extracts from external vector definitions are inserted at the region
  boundary, specifically on region entry. This prevents incorrect placement after
  'returns-twice' calls, which previously caused an ICE due to the ordering of extract
  emission. A new test case (`bb-slp-pr128014.c`) is added to cover this scenario.
primer_glossary:
- term: Live Lane
  definition: In vector processing, a 'live lane' likely refers to a specific element
    or subset of elements within a vector that remains active or used after certain
    operations. Managing these live lanes is crucial for efficient vectorization.
- term: Extracts
  definition: Operations that retrieve specific elements or parts of a larger data
    structure, such as a vector or an array. In this context, it refers to extracting
    data from vector definitions.
- term: Region Boundary
  definition: A point in the code that delineates the start or end of a logical or
    structural unit, such as a loop, a basic block, or a vectorized region. Correctly
    placing operations at these boundaries is important for maintaining program correctness
    and enabling optimizations.
- term: ICE (Internal Compiler Error)
  definition: An unrecoverable error within the compiler itself, indicating a bug
    in the compiler's logic or data structures. ICEs halt the compilation process
    and typically require a fix in the compiler source code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/04f26dfb261677b094602f3d6428de183ddebc5b
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

A bug in the vectorization of 'live lanes' has been fixed. Previously, when dealing with extracts from external vector definitions, these extracts could be inserted at arbitrary external locations, including after 'returns-twice' calls. This incorrect placement led to internal compiler errors (ICEs). The fix ensures that such extracts are now inserted at region boundaries, specifically on region entry, resolving the ICEs and improving vectorization reliability.
