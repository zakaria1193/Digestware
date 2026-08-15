---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- ICE
commit_hash: d42b8b15aa9f246293c976f141df1c1936d93dc6
source_type: github
author: Richard Biener
headline: Fix ICE with SLP schedule at explicit region start
tldr: Correctly handles SLP scheduling at region starts to prevent ICEs.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The SLP vectorizer in `tree-vect-slp.cc` used a statement as a marker
  for scheduling at a region start. If this statement was a control flow statement,
  it could lead to an ICE. The fix ensures that only NULL is used as a marker for
  region starts, as per the documented interface, preventing invalid states and compiler
  crashes.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d42b8b15aa9f246293c976f141df1c1936d93dc6
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This commit addresses an ICE (Internal Compiler Error) that occurred during SLP (Sliding Window Parallelization) scheduling at the start of explicit regions. The issue stemmed from using a random statement as a marker, which could be a control statement. The fix replaces this with NULL, adhering to documentation and resolving the ICE. A new test case is included.
