---
project: gcc
subsystem: gcc/middle-end
patch_id: null
tags:
- gcc
- vectorization
- refactor
commit_hash: 1bedb5ac23801c6639387e53b544157f2f51cd34
source_type: github
author: Tamar Christina
headline: Rename vector extract internal function for clarity.
tldr: The GCC internal function `extract_last` is renamed to `extract_last_active`
  to clarify that it operates based on the last active bit in a mask.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `EXTRACT_LAST` internal function (and its associated optab/patterns)
  selects a vector element corresponding to the highest-set bit in a given mask. This
  commit renames it to `EXTRACT_LAST_ACTIVE` to better convey that the selection is
  based on an 'active' lane indicated by the mask. This renaming is part of a series
  to introduce `extract_first_active` and improve the clarity of vector manipulation
  primitives within GCC's middle-end and target-specific code generation.
primer_glossary:
- term: vector extract
  definition: An operation that retrieves a specific element from a vector data type.
- term: mask
  definition: In vector processing, a bitmask used to control which elements of a
    vector are operated on or to select specific elements.
- term: active lane
  definition: A lane (element) within a vector that is enabled or selected by a mask
    for processing.
- term: optab
  definition: Optimization table; a data structure in GCC that maps generic operations
    to specific machine instructions or patterns.
- term: middle-end
  definition: The part of a compiler (between the front-end and back-end) that performs
    machine-independent optimizations on an intermediate representation of the code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1bedb5ac23801c6639387e53b544157f2f51cd34
date: '2026-10-24'
is_stub: true
stub_reason: low_score
---

The GCC internal function responsible for extracting a vector element based on the last set bit in a mask has been renamed from `extract_last` to `extract_last_active`. This change makes the function's behavior more explicit, as it selects an element from the 'last active lane' specified by the mask, rather than just the 'last' element. The corresponding `optab` and target patterns have also been updated.
