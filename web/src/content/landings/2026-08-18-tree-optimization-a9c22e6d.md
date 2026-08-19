---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- tree-optimization
- vectorization
- slp
commit_hash: a9c22e6d049bf10e44b6a76384a1eb00991c3eb8
source_type: github
author: Richard Biener
headline: Back-to-back SLP instance scheduling fix [PR126926]
tldr: Fixes SLP vectorization scheduling when instances interact, preventing incorrect
  transformations.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In `vectorize_slp_instance_root_stmt`, when two SLP instances interact
  such that one defines a vector CTOR root which is also a leaf in another (reduction)
  instance, the current transformation replaces the entire statement. This prematurely
  modifies the definition, causing the second SLP instance's scheduler to see the
  transformed value as external. This commit amends the function to only replace the
  RHS of the vector-constructing statement, ensuring that the SLP scheduling logic
  for subsequent instances remains correct. A new test case `bb-slp-pr126926.c` is
  added.
primer_glossary:
- term: SLP
  definition: Shortest Path, a compiler optimization technique used for vectorization
    that identifies straight-line code sequences that can be mapped to single vector
    instructions.
- term: vector CTOR
  definition: Constructor for a vector type, typically used to create or initialize
    vector data structures within the compiler's intermediate representation.
- term: reduction instance
  definition: In the context of SLP vectorization, a part of the code that aggregates
    values using an operation like sum, product, or minimum across a vector.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a9c22e6d049bf10e44b6a76384a1eb00991c3eb8
date: '2026-08-18'
is_stub: false
stub_reason: ''
---

This commit addresses a bug in the SLP (Shortest Path) vectorization scheduling where interacting SLP instances caused incorrect transformations. When one SLP instance transformed a vector constructor that was also a component of a second SLP instance, the scheduling process was disrupted. The fix ensures that only the right-hand side of the vector constructing statement is replaced, preserving the integrity of the SLP scheduling for both instances and resolving a PR for the tree-optimization component.
