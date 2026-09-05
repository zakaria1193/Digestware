---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- tree-optimization
- slp
commit_hash: 19fae3c44356017e3f36626d9d57fe0081533fad
source_type: github
author: Richard Biener
headline: SLP schedule failure state caching improved.
tldr: GCC's SLP vectorization now correctly uses cached failure states for previously
  analyzed entries.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect_schedule_slp` function in `tree-vect-slp.cc` has been updated
  to properly leverage cached failure states. If `scc_info` (Scalar or Superword Code
  information) is already present for an entry, indicating a prior analysis, the function
  now consults its `failure` field. This prevents re-evaluation of code segments previously
  determined to be unsuitable for SLP vectorization, improving efficiency and consistency.
primer_glossary:
- term: SLP (Superword Level Parallelism)
  definition: A compiler optimization technique that identifies and vectorizes sequences
    of identical operations that operate on different data elements within a single
    instruction stream.
- term: vectorization
  definition: The process of transforming code to use SIMD (Single Instruction, Multiple
    Data) instructions, allowing a single instruction to operate on multiple data
    elements simultaneously.
- term: tree-optimization
  definition: A phase in GCC's compilation pipeline where optimizations are performed
    on the GCC's intermediate representation (GIMPLE).
- term: scc_info
  definition: Information related to Scalar or Superword Code, often used in vectorization
    passes to track analysis results.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/19fae3c44356017e3f36626d9d57fe0081533fad
date: '2026-09-04'
is_stub: false
stub_reason: ''
---

This commit ensures that GCC's SLP (Superword Level Parallelism) vectorization pass properly utilizes cached failure information. When an entry has already been analyzed and determined to be unvectorizable, its failure state is now correctly reused, preventing redundant analysis and ensuring that previously identified unvectorizable code patterns are consistently handled.
