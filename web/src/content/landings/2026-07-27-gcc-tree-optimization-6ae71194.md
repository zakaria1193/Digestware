---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- gcc
- optimization
- vectorization
commit_hash: 6ae711942f345e3b6e149431e5ce4eff9162835b
source_type: github
author: Richard Biener
headline: Fix fold-left reduction check for vector types.
tldr: Correctly checks vector lane count for fold-left reduction, preventing incorrect
  checks.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The vectorization pass uses `fold-left` reduction for certain operations.
  This commit corrects `tree-vect-slp.cc` to compare the total number of lanes with
  a two-lane special case, rather than comparing the vector type itself. This ensures
  that reductions are correctly identified and handled, especially in edge cases.
primer_glossary:
- term: vectorization
  definition: The process of converting scalar operations into vector operations,
    which can process multiple data elements simultaneously. This is a common optimization
    technique.
- term: pass
  definition: A distinct, self-contained stage within the compiler's optimization
    pipeline. Each pass performs a specific transformation on the intermediate representation
    of the code.
- term: fold-left reduction
  definition: A type of parallel operation where a binary operation is repeatedly
    applied to elements of a sequence, accumulating a single result. In vectorization,
    this allows multiple operations to be performed in parallel.
- term: SLP (Superword Level Parallelism)
  definition: A compiler optimization technique that identifies and vectorizes sequences
    of identical scalar operations that operate on consecutive memory locations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6ae711942f345e3b6e149431e5ce4eff9162835b
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This commit corrects a bug in the vectorization pass where the code was checking the vector type instead of the number of lanes for fold-left reduction. This change ensures the correct number of lanes is considered, preventing unnecessary or incorrect reduction handling. A new test case has also been added to verify this fix.
