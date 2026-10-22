---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- bugfix
- aarch64
commit_hash: 8afde8eab36eb74ceecfbcc20322693358feba94
source_type: github
author: Roger Sayle
headline: Vectorizer avoids incorrect conversion of pow(x, 0.5) to sqrt(x)
tldr: Fixes vectorizer to not incorrectly transform pow(x, 0.5) into sqrt(x).
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch addresses PR tree-optimization/126562 by refining the vectorizer's
  pattern matching for `pow(x, 0.5)`. The previous `vect_recog_pow_pattern` in `tree-vect-patterns.cc`
  incorrectly recognized this as a square root operation. The correction ensures that
  the pattern only matches when the input `x` is non-negative, or specifically handles
  cases involving signed zero or negative infinity, preventing the incorrect transformation.
  Scalar aspects of this PR were addressed in a prior patch for PR tree-optimization/127544.
primer_glossary:
- term: vectorizer
  definition: A compiler component that transforms code to use SIMD (Single Instruction,
    Multiple Data) instructions, allowing a single operation to be performed on multiple
    data elements simultaneously.
- term: SIMD
  definition: Single Instruction, Multiple Data. A class of parallel computers in
    Flynn's taxonomy. It describes computers with individually specified memory for
    each processor. SIMD allows a single instruction to be executed on multiple data
    points at once.
- term: pattern matching
  definition: In compilers, the process of identifying specific code structures or
    sequences that correspond to known operations or optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8afde8eab36eb74ceecfbcc20322693358feba94
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

The GCC vectorizer previously misidentified `pow(x, 0.5)` as `sqrt(x)`, leading to incorrect transformations. This patch corrects the pattern recognition in `vect_recog_pow_pattern` to only convert to `sqrt` when appropriate, specifically excluding cases involving signed zero or negative infinity. The fix also required adjustments to two test cases that relied on the old, incorrect behavior.
