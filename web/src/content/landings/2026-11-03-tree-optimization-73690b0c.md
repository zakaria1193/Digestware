---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
commit_hash: 73690b0ce3749249c0791f22872c85ad37442c14
source_type: github
author: Richard Biener
headline: SLP vectorizer handles returns-twice calls on entry
tldr: SLP vectorizer now correctly handles cases where a vectorization region starts
  with a call that returns twice.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `vec_info::insert_seq_on_entry` function in the tree-vectorizer
  is responsible for setting up vectorization sequences. This commit addresses an
  issue where it would incorrectly attempt to insert a sequence before a block containing
  a returns-twice call. Such calls cannot be vectorized, so the iterator now advances
  past them, ensuring that the SLP (Superword Level Parallelism) vectorizer correctly
  identifies and processes vectorizable code following such calls.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/73690b0ce3749249c0791f22872c85ad37442c14
date: '2026-11-03'
is_stub: false
stub_reason: ''
---

The SLP vectorizer in GCC has been updated to correctly handle a specific edge case. Previously, if a vectorization candidate region began with a 'returns-twice' call (a call that can return to more than one instruction), the vectorizer would incorrectly attempt to insert code before it. This change modifies the `insert_seq_on_entry` function to advance past such calls, ensuring that vectorization occurs only when appropriate and preventing incorrect code generation.
